from django.shortcuts import render, redirect

from myPanel.forms import MessagesPostForm
from myPanel.models import BlogPost, Messages
from django.shortcuts import render, get_object_or_404
# Create your views here.
def displayAll(request) :
    posts = BlogPost.objects.all()
    return render(request, 'index.html', {'posts': posts})

def displayPost(request, pk) :
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'postDetails.html', {'post': post})


def about(request) :
    return render(request, 'about.html')

def contact(request) :
    if request.method == 'POST':
        form = MessagesPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # Set any additional fields on the post object here
            post.save()
            return redirect('contact')
    else:
        form = MessagesPostForm()
    return render(request, 'contact.html',{'form': form})

def team(request) :
    return render(request, 'team.html')