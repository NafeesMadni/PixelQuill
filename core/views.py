from django.shortcuts import render, get_object_or_404
from .models import Blog, Category
from django.utils import timezone
from django.templatetags.static import static
from django.contrib.auth.models import User
from authentication.models import Profile
from pixelquill.utils import btn_cols, category_imgs, categories, getUserProfile



def home(request):
     profile = getUserProfile(request=request)
     profiles = Profile.objects.select_related('user').all()
     
     # Fetch all blogs, prefetched with their related User and Category
     blogs = Blog.objects.select_related('created_by').prefetch_related('category').all()

     return render(request, 'core/home.html', 
     {
          'blogs': blogs, 
          'categories': categories, 
          'btn_cols': btn_cols,
          'profile': profile,
          'profiles': profiles,
     }) # indirectly passing the list of category to layout.html


def details(request, pk):
     profile = getUserProfile(request=request)
     
     blog = get_object_or_404(Blog, pk=pk)
     btn_col = btn_cols[str(blog.category)]
     user = User.objects.prefetch_related('profile').get(pk=blog.created_by.id)
     blogger_data = user.profile
     
     return render(request, 'core/details.html',
     {
          'blog': blog,
          'categories': categories,
          'btn_col': btn_col,
          'profile': profile,
          'blogger_data': blogger_data,
     })

def category(request, pk):
     profile = getUserProfile(request=request)
     profiles = Profile.objects.select_related('user').all()
     
     category = Category.objects.prefetch_related('category_blogs').get(id=pk)
     related_blogs = category.category_blogs.all()  
     btn_col = btn_cols[str(category)]
     
     image = category_imgs[str(category)]
     image_url = static(f"{image}")  # Path to the image
     
     return render(request, 'core/category.html', 
     {
          'related_blogs': related_blogs,
          'categories': categories, # pass to layout.html
          'btn_col':btn_col,
          'category': category,
          'image_url': image_url,
          'profile': profile,
          'profiles': profiles,
     })

def author(request, pk):
     profile = getUserProfile(request=request)
     
     author = User.objects.prefetch_related('profile').prefetch_related('author_blogs').get(id=pk)
     related_blogs = author.author_blogs.all()
     author_data = author.profile
     
     return render(request, 'core/author.html', 
     {
          'related_blogs': related_blogs,
          'categories': categories, # pass to layout.html
          'btn_cols': btn_cols,
          'author': author,
          'profile': profile,
          'author_data': author_data,
     })