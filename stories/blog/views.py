from django.shortcuts import render,HttpResponse
from .models import Post
from .forms import CreatePostFrom

# Create your views here.

def index(request):
    allposts = Post.objects.all()
    context = {'allposts':allposts}
    return render(request,'blog/home.html',context)

def SearchPost(request):
    query = request.GET['query']
    posts = Post.objects.filter(title__icontains=query)
    context = {'allposts':posts}
    return render(request,'blog/search.html',context)

def ViewPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request,'blog/viewPost.html',context)

def CreatePost(request):
    if request.method == 'POST':
        form = CreatePostFrom(request.POST)
        if form.is_valid():
            messages = ''
        else:
            form = CreatePostFrom()
    return render(request,'blog/createPost.html',{'form':form})
    