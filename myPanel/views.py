from .forms import BlogPostForm, MessagesPostForm
from django.contrib.auth.decorators import login_required
from myPanel.forms import RegistrationForm
from django.shortcuts import  get_object_or_404
from .models import BlogPost, Messages
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
@login_required(login_url="/panel/login/")
def addPost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # Set any additional fields on the post object here
            post.save()
            return redirect('posts')

    else:
        form = BlogPostForm()
    return render(request, 'addPost.html', {'form': form})


@login_required(login_url="/panel/login/")
def updatePost(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('posts')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'updatePost.html', {'form': form})


@login_required(login_url="/panel/login/")
def showPosts(request):
    posts = BlogPost.objects.all()
    return render(request, 'posts.html', {'posts': posts})

@login_required(login_url="/panel/login/")
def message(request):
    messages = Messages.objects.all()
    return render(request, 'messages.html', {'messages': messages})


@login_required(login_url="/panel/login/")
def deletePost(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    post.delete()
    return redirect('posts')

@login_required(login_url="/panel/login/")
def deleteMessage(request, pk):
    message = get_object_or_404(Messages, pk=pk)
    message.delete()
    return redirect('message')

@login_required(login_url="/panel/login/")
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'regist.html', {'form': form})

def loginOperation(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('posts')

        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logoutOperation(request):
    logout(request)
    return redirect('login')