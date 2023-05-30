from django.db import models
from django.urls import reverse

class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    location = models.CharField(max_length=150)
    MALE = "M"
    FEMALE = "F"
    NONE_OF_YOUR_BS = "NS"
    CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (NONE_OF_YOUR_BS, "--")
    ]
    gender = models.CharField(max_length=2, choices=CHOICES, default=NONE_OF_YOUR_BS)
    
    def __str__(self) -> str:
        return self.username
    
    def get_absolute_url(self):
        return reverse("details-page", kwargs={"pk": self.pk})
    