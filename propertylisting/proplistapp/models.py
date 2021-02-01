from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, default='')
    profile_picture = models.ImageField(upload_to="profile_images/", blank=True, default='profile_images//default.png')
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

class PostAd(models.Model):
    address = models.CharField(max_length=50)
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    house_images = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True) 
