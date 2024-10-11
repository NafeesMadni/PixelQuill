from django.shortcuts import render, get_object_or_404
from .models import Blog, Category
from django.utils import timezone
from django.templatetags.static import static
from django.contrib.auth.models import User
from authentication.models import Profile

btn_text_cols = {
     "Fashion": " bg-rose-100/95 text-rose-500 ",
     "Technology": " bg-blue-100/95 text-blue-500 ",
     "Economy": " bg-green-100/95 text-green-500 ",
     "Business": " bg-indigo-100/95 text-indigo-500 ",
     "Travel": " bg-teal-100/95 text-teal-600 ",
     "Lifestyle": " bg-yellow-100/95 text-yellow-500 ",
     "Sports": " bg-cyan-100/95 text-cyan-500 ", 
}

category_imgs = {
     "Fashion": "img/categories/fashion.jpg",
     "Technology": "img/categories/technology.jpg",
     "Economy": "img/categories/economy.jpg",
     "Business": "img/categories/business.jpg",
     "Travel": "img/categories/travel.jpg",
     "Lifestyle": "img/categories/lifestyle.jpg",
     "Sports": "img/categories/sports.jpg", 
}

btn_cols = {
     "Fashion": " bg-rose-500 ",
     "Technology": " bg-blue-500 ",
     "Economy": " bg-green-500 ",
     "Business": " bg-indigo-500 ",
     "Travel": " bg-teal-500 ",
     "Lifestyle": " bg-yellow-500 ",
     "Sports": " bg-cyan-500 ", 
}

def home(request):
     if not request.user.is_superuser:
          profile = request.user.user_data
     
     categories = Category.objects.all()
     blogs = Blog.objects.all()
     
     return render(request, 'core/home.html', 
     {
          'blogs': blogs, 
          'categories': categories, 
          'btn_cols': btn_cols,
          'profile': profile,
     }) # indirectly passing the list of category to layout.html


def details(request, pk):
     # profile = Profile.objects.get(user=request.user.id)
     categories = Category.objects.all()
     blog = get_object_or_404(Blog, pk=pk)
     btn_col = btn_cols[str(blog.category)]

     return render(request, 'core/details.html',
     {
          'blog': blog,
          'categories': categories,
          'btn_col': btn_col,
          # 'profile': profile,
     })

def category(request, pk):
     # profile = Profile.objects.get(user=request.user.id)
     
     categories = Category.objects.all()
     category = Category.objects.get(id=pk)
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
          # 'profile': profile,
     })



def author(request, pk):
     # profile = profile.objects.get(user=request.user.id)
     categories = Category.objects.all()
     author = User.objects.get(id=pk)
     related_blogs = author.author_blogs.all()
     
     return render(request, 'core/author.html', 
     {
          'related_blogs': related_blogs,
          'categories': categories, # pass to layout.html
          'btn_cols': btn_cols,
          'author': author,
          # 'profile': profile,
     })


