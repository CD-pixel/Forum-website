from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# from .forms import UserForm
from .models import Post, Reply


# Create your views here.
def forum(request,):
    posts = Post.objects.all()
    reply = Reply.objects.all()

 
    context={'posts':posts}
    return render(request, 'forum.html', context)


def registerUser(request):

    user = User()        

    
    context={'user':user}
    return render(request, 'register.html', context)


def loginUser(request):
    user_data = User()        
    
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password'] 

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("forum")
    
    context={'user':user_data}
    return render(request, 'login.html', context)


def thread(request, id):
    post = get_object_or_404(Post, pk=id)
    replies = post.reply_set.all()

    context={'post':post, 'replies':replies}
    return render(request, 'forum-thread.html', context)


def newThread(request):
    user = User()
    
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']

        if request.user.is_authenticated:

            post = Post(title=title, body=body, author=request.user)
            post.save()

            return redirect('forum')

    return render(request, 'add-thread.html')

