from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from authentication.models import Profile


INPUT_CLASS = 'w-full my-2 px-4 py-1 rounded-md '

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

class ProfileForm(forms.ModelForm):
     class Meta:
          model = Profile
          fields = ('profile_img', 'f_name','l_name', 'job_role', 'bio',)
          widgets = {
               'l_name': forms.TextInput(attrs={
                    'class': INPUT_CLASS,
               }),
               'f_name': forms.TextInput(attrs={
                    'class': INPUT_CLASS,
               }),
               'job_role': forms.TextInput(attrs={
                    'class': INPUT_CLASS,
               }),
               'bio': forms.Textarea(attrs={
                    'class': INPUT_CLASS,
               }),
               'profile_img': forms.FileInput(attrs={
                    'class': INPUT_CLASS,
               }),
          }