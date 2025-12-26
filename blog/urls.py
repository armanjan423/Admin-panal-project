
from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('', views.home, name='home'),
    path('blog/<str:blog_id>/', views.blog_detail, name='blog_detail'),
    path('search/', views.search, name='search'),
    
    # Hidden Admin
    path('secure-panel-9090/', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.admin_logout, name='admin_logout'),
    
    # Dashboard Actions
    path('dashboard/add/', views.add_blog, name='add_blog'),
    path('dashboard/edit/<str:blog_id>/', views.edit_blog, name='edit_blog'),
    path('dashboard/delete/<str:blog_id>/', views.delete_blog, name='delete_blog'),
]
