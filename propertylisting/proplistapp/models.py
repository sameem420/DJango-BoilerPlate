from django.db import models

# Create your models here.
class PostAd(models.Model):
    address = models.CharField(max_length=50)
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    house_images = models.ImageField(upload_to='images/')
    # uploaded_at = models.DateTimeField(auto_now_add=True) 
