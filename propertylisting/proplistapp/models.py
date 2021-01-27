from django.db import models

# Create your models here.
class PostAd(models.Model):
    address = models.CharField(max_length=50)
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    house_images = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True) 

class UsersAccount(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    password_repeat = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    profile_picture = models.ImageField()