from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
     name = models.CharField(max_length=255,  unique=True)
     
     class Meta:
          verbose_name_plural = 'Categories'
          ordering  = ('name',)
     
     def __str__(self): 
          return self.name

class Blog(models.Model):
     
     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_blogs')
     heading = models.CharField(max_length=255, blank=False, null=True)
     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_blogs")
     description = models.TextField(max_length=3000, null=True)
     image = models.ImageField(upload_to= 'blog/', null=True) 
     added_date = models.DateTimeField(auto_now_add=True, null=True)
     
     def __str__(self):
          return f"'{self.heading}' created by {self.created_by}."
     