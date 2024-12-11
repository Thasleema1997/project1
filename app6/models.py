from django.db import models
from django.contrib.auth.hashers import make_password

class mytable(models.Model):
    Name=models.CharField(max_length=100)
    Age=models.IntegerField()
    Email=models.EmailField()
    Phoneno=models.IntegerField()
    Dob=models.DateField()
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)

# Create your models here.

class CustomUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # Hashed password

    def save(self, *args, **kwargs):
        if not self.pk:  # Ensure password is hashed only on initial save
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


