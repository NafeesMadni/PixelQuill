from django.contrib.auth import logout as Logout
from django.shortcuts import render, redirect
from .forms import LogInForm, SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


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