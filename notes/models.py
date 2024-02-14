from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio=models.CharField(max_length=255, blank=True)
    # cover_photo=models.ImageField(upload_to='covers/', null=True, blank=True)

class Note(models.Model):
    title=models.TextField(null=True, blank=True)
    body=models.TextField(null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='notes')

    def __str__(self):
        return self.tiltle
