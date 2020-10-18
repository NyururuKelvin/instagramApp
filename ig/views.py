from django.shortcuts import render
from django.http  import HttpResponse, Http404,HttpResponseRedirect
from .models import Post, Comment, Profile

# Create your views here.
def index(request):

    # Default view
    posts=Post.objects.all()
    comments = Comment.get_comments()
    profiles = Profile.objects.all()
    return render(request, 'temps/index.html', {'posts':posts, 'comments':comments,'profiles':profiles})