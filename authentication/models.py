import os
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

def get_default_image_path():
    return os.path.join('dp_img', 'default.png')

class Profile(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    f_name = models.CharField(max_length=10, default='James')
    l_name = models.CharField(max_length=10, default='Joe')
    job_role = models.CharField(max_length=10, default='_job')
    profile_img = models.ImageField(upload_to='dp_img/', default=get_default_image_path, )
    bio = models.TextField(max_length=400, blank=True)
    acc_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"