from django.shortcuts import render
from django.template import RequestContext
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from calendar import calendar
from blog.models import *
from django.core.paginator import  Paginator , EmptyPage , PageNotAnInteger

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    calendar
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def editor(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'post_edit.html', {'form': form})


def post_new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

def home(request):

    return render(request, 'post_list.html',locals())

def home2(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('is_active')
    calendar
    return render(request, 'home2.html', {'posts': posts})



def category(reguest, slug):
    category = Category.objects.get(slug=slug)
    post = Post.objects.filter(category=category)
    paginator = Paginator(post,1)
    page = reguest.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(reguest, 'category.html', {

        'page': page,
        'posts': post,
        'post': post,})

def ind(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('is_active')
    calendar
    return render(request, 'index.html', {'posts': posts})


def winter(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    calendar
    return render(request, 'winter.html', {'posts': posts})

def carusel(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    calendar
    return render(request, 'carusel.html', {'posts': posts})
	
	
def dz1(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    calendar
    return render(request, 'dz/dz1.html', {'posts': posts})

def dz2(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    calendar
    return render(request, 'dz/landing2.html', {'posts': posts})



def circle(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    calendar
    return render(request, 'circle.html', {'posts': posts})



def grid(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    calendar
    return render(request, '13.html', {'posts': posts})

	




