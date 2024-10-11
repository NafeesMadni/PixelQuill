from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

# Using django's LogIn View
class LogInForm(AuthenticationForm):
     username = forms.CharField(widget=forms.TextInput(attrs={
          'placeholder': 'Enter username',
          'class': 'w-full px-5 py-2 rounded-lg text-gray-600'
     }))
     password = forms.CharField(widget=forms.PasswordInput(attrs={
          'placeholder': 'Enter your password',
          'class': 'w-full px-5 py-2 rounded-lg text-gray-600'
     }))

class SignUpForm(UserCreationForm):
     class Meta:
          model = User
          fields = ('username', 'email', 'password1', 'password2')

     username = forms.CharField(widget=forms.TextInput(attrs={
          'placeholder': 'Enter your name',
          'class': 'w-full px-5 py-2 rounded-lg text-gray-600'
     }))
     
     email = forms.CharField(widget=forms.EmailInput(attrs={
          'placeholder': 'Enter your email address',
          'class': 'w-full px-5 py-2 rounded-lg text-gray-600'
     }))
     
     password1 = forms.CharField(widget=forms.PasswordInput(attrs={
          'placeholder': 'Enter your password',
          'class': 'w-full px-5 py-2 rounded-lg text-gray-600'
     }))
     
     password2 = forms.CharField(widget=forms.PasswordInput(attrs={
          'placeholder': 'Confirm your password',
          'class': 'w-full px-5 py-2 rounded-lg text-gray-600'
     }))
