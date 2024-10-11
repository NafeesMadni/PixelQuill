from django import forms

from core.models import Blog


INPUT_CLASS = 'w-full my-2 px-4 py-1 rounded-md '

class BlogForm(forms.ModelForm):
     class Meta:
          model = Blog
          fields = ('heading', 'category', 'image', 'description',)
          widgets = {
               'category': forms.Select(attrs={
                    'class': INPUT_CLASS,
               }),
               'heading': forms.TextInput(attrs={
                    'class': INPUT_CLASS,
               }),
               'description': forms.Textarea(attrs={
                    'class': INPUT_CLASS,
               }),
               'image': forms.FileInput(attrs={
                    'class': INPUT_CLASS,
               }),
          }
          
