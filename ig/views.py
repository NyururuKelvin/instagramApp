from django.shortcuts import render
from django.http  import HttpResponse, Http404,HttpResponseRedirect
from .models import Post, Comment, Profile
from django.contrib.auth.models import User
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, NewPostForm, CommentForm, ProfileForm

# Create your views here.
def index(request):

    # Default view
    images=Post.objects.all()
    comments = Comment.get_comments()
    profiles = Profile.objects.all()
    return render(request, 'temps/index.html', {'images':images, 'comments':comments,'profiles':profiles})

def signup(request):
    name = "Sign Up"
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('username')
            send_mail(
            'Welcome to Instagram App.',
            f'Hello {name},\n '
            'Welcome to Instagram App and have fun.',
            'nyururukelvin99@gmail.com@gmail.com',
            [email],
            fail_silently=False,
            )
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form, 'name':name})


def new_post(request):
    current_user = request.user
   
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user= current_user
            post.save()
        return redirect('home')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {'current_user':current_user, 'form':form})

def update_profile(request):
    """
    Function that enables one to edit their profile information
    """
    current_user = request.user
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=Profile.objects.get(user_id=current_user))
        if form.is_valid():
                profile = form.save(commit=False)
                profile.user = current_user
                profile.save()
        return redirect('home')

    
    else:
        if Profile.objects.filter(user_id=current_user).exists():
            form = ProfileForm(instance = Profile.objects.get(user_id=current_user))
        else:
            form = ProfileForm()
    return render(request, 'profile/edit-profile.html', {'current_user':current_user, 'form':form})