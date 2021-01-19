from django import forms
from .models import *

class PostAdForm(forms.ModelForm):
    class Meta: 
        model = PostAd
        fields = '__all__'