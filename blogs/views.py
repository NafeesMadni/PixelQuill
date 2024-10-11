from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm
from django.contrib.auth.models import User
from core.models import Blog, Category
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def post(request):
     categories = Category.objects.all() # passing to layout.html
     if request.method == 'POST':
          form = BlogForm(request.POST, request.FILES) # request.FILES to get the files (images) user upload 
          if form.is_valid():
               post = form.save(commit=False)
               post.created_by = request.user
               post.save()
               return redirect('details', pk=post.id)
     else :
          form = BlogForm()
     return render(request, 'blogs/post.html', {'form':form, 'title': 'Create a new blog', 'categories': categories,})

@login_required
def edit(request, pk):
     categories = Category.objects.all() 
     blog = get_object_or_404(Blog, pk=pk, created_by=request.user)
     
     if request.method == 'POST':
          form = BlogForm(request.POST, request.FILES, instance=blog)
          if form.is_valid():
               form.save()
               return redirect('details', pk=blog.id)
     else:
          form = BlogForm(instance=blog)
     return render(request, 'blogs/post.html', {'form':form, 'title': 'Edit blog', 'categories': categories,})


@login_required
def delete(request, pk):
     blog = get_object_or_404(Blog, pk=pk, created_by=request.user)
     author = blog.created_by 
     blog.delete()
     
     return redirect('author', pk=author.id)