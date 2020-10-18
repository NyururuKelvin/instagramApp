from django.shortcuts import render
from django.http  import HttpResponse, Http404,HttpResponseRedirect
from .models import Post, Comment, Profile
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