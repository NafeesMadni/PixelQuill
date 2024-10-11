from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
     user =  models.OneToOneField(User, on_delete=models.CASCADE)
     f_name = models.CharField(max_length=10, default='James')
     l_name = models.CharField(max_length=10, default='Joe')
     job_role = models.CharField(max_length=10, default='_job')
     profile_img = models.ImageField(upload_to='profiles/', default="img/dp.jpg")
     bio = models.TextField(max_length=400, blank=True)
     acc_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
     
     def __str__(self):
          return f"{self.user.username}'s Profile"