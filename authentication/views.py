from django.contrib.auth import logout as Logout
from django.shortcuts import render, redirect
from .forms import LogInForm, SignUpForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from pixelquill.utils import getUserProfile

# Create your views here.

def signup(request):
     if request.method == 'POST':
          form = SignUpForm(request.POST)

          if form.is_valid():
               user = form.save()
               login(request, user)  # Logs the user in after successful signup
               return redirect('/')
     else:
          form = SignUpForm()
          
     return render(request, 'authentication/signup.html', {'form': form, 'title': 'Registration'})

@login_required
def logout(request):
    Logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('/')

@login_required
def user_profile(request):
     profile = getUserProfile(request=request)
     
     if request.method == 'POST':
          form = ProfileForm(request.POST, request.FILES, instance=profile)
          if form.is_valid():
               form.save()
               return redirect('author', pk=profile.user.id)
     else:
          form = ProfileForm(instance=profile)
     return render(request, 'authentication/profile.html', 
     {
          'form':form,
          'profile': profile,
     })