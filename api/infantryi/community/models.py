from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

class Project(models.Model):
    VISIBILITY_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='public')
    posted_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title} by {self.created_by.username}'