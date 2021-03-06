from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User


class  Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="no  bio .....")
    avatar = models.ImageField(default='default.png', upload_to='avatars')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"Profile of {self.user.username}"