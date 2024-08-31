from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .models import Post, Contact, CommentPost, Category
from django.contrib.auth.models import User
from django.core.paginator import Paginator

def HomePage(request):
    posts = Post.published.all()  
    paginator = Paginator(posts, 6) 

    page_number = request.GET.get("page")  
    page_obj = paginator.get_page(page_number)  
    
    return render(request, 'index.html', {'posts': page_obj})


def ContactPage(request):
    contact = Contact()
    if request.method == "POST":
        contact.username = request.POST.get('username')
        contact.email = request.POST.get('email')
        contact.phone_number = request.POST.get('phone')
        contact.message = request.POST.get('message')
        contact.save()
        return redirect('home')
    return render(request, 'contact.html')


def PostDetail(request, year, month, day, slug):
    usercomment = CommentPost()
    post = get_object_or_404(Post, slug=slug, status="published", publish__year=year, publish__month=month, publish__day=day)
    if request.method == 'POST':
        comment = request.POST.get('commentInput')
        user = request.user
        if comment:
            usercomment.author = user
            usercomment.post = post
            usercomment.comment = comment
            usercomment.save()
    comments = CommentPost.objects.filter(post=post).select_related('author')
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})


def SingupPage(request):
    if request.method == "POST":
        username = request.POST.get('name')
        useremail = request.POST.get('email')
        if request.POST.get('password1') == request.POST.get('password2'):
            password = request.POST.get('password1')
            user = User.objects.create_user(username=username, email=useremail, password=password)
            login(request, user)
            return redirect('home')
    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
            username = request.POST.get('name')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    return render(request, 'login.html')



def LogoutUser(request):
    logout(request)
    return redirect('home')

def AboutPage(request):
    return render(request, 'about.html')

def CategoryPost(request, slug):
    object_list = Post.published.filter(category__slug = slug)
    category = get_object_or_404(Category, slug=slug)

    paginator = Paginator(object_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'post_list.html', {'posts': page_obj, 'category': category})
