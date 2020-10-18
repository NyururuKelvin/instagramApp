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