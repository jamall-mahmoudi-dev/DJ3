from django.urls import path
from blog.views import blog_home, blog_single

app_name = 'blog'

urlpatterns = [
    path('blog-home/', blog_home, name='blog-home'),
    path('blog-single/', blog_single, name='blog-single')
]