
import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password
from django.core.files.storage import FileSystemStorage
from django.http import Http404
from .models import BlogPost, AdminUser
import datetime

# --- Decorator for Admin Security ---
def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('admin_id'):
            return redirect('admin_login')
        return view_func(request, *args, **kwargs)
    return wrapper

# --- Public Views ---

def home(request):
    blogs = BlogPost.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    try:
        blog = BlogPost.objects.get(id=blog_id)
        # Increment View Count
        blog.view_count += 1
        blog.save()
        return render(request, 'blog_detail.html', {'blog': blog})
    except BlogPost.DoesNotExist:
        raise Http404("Blog not found")

def search(request):
    query = request.GET.get('q')
    if query:
        blogs = BlogPost.objects.filter(title__icontains=query)
    else:
        blogs = []
    return render(request, 'home.html', {'blogs': blogs, 'search_query': query})

# --- Admin Views ---

def admin_login(request):
    if AdminUser.objects.count() == 0:
        AdminUser.objects.create(username='admin', password=make_password('admin123'))
        print("Default admin created: admin/admin123")

    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        try:
            user = AdminUser.objects.get(username=u)
            if check_password(p, user.password):
                 request.session['admin_id'] = str(user.id)
                 return redirect('dashboard')
            else:
                return render(request, 'admin_login.html', {'error': 'Invalid credentials'})
        except AdminUser.DoesNotExist:
            return render(request, 'admin_login.html', {'error': 'Invalid credentials'})
            
    return render(request, 'admin_login.html')

def admin_logout(request):
    request.session.flush()
    return redirect('home')

@admin_required
def dashboard(request):
    blogs = BlogPost.objects.all()
    total_blogs = blogs.count()
    total_views = sum(b.view_count for b in blogs)
    return render(request, 'dashboard.html', {
        'blogs': blogs,
        'total_blogs': total_blogs,
        'total_views': total_views
    })

@admin_required
def add_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        image_path = ''
        if image:
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            image_path = fs.url(filename)
            
        blog = BlogPost.objects.create(
            title=title,
            content=content,
            image=image_path
        )
        return redirect('dashboard')
    return render(request, 'blog_form.html', {'action': 'Add'})

@admin_required
def edit_blog(request, blog_id):
    try:
        blog = BlogPost.objects.get(id=blog_id)
    except BlogPost.DoesNotExist:
         return redirect('dashboard')
         
    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.content = request.POST.get('content')
        
        if request.FILES.get('image'):
            image = request.FILES.get('image')
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            blog.image = fs.url(filename)
            
        blog.save()
        return redirect('dashboard')
        
    return render(request, 'blog_form.html', {'blog': blog, 'action': 'Edit'})

@admin_required
def delete_blog(request, blog_id):
    try:
        blog = BlogPost.objects.get(id=blog_id)
        blog.delete()
    except BlogPost.DoesNotExist:
        pass
    return redirect('dashboard')
