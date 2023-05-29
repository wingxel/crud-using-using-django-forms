from django.db import models


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
