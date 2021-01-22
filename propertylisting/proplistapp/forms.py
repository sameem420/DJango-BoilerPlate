from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostAdForm(forms.ModelForm):
    class Meta: 
        model = PostAd
        fields = ['address', 'rooms', 'bathrooms', 'house_images']
        widgets = {
            'address': forms.TextInput(
				attrs={
					'class': 'form-control',
                    'placeholder': 'Enter Address here ...'
					}
				),
            'rooms': forms.NumberInput(
				attrs={
					'class': 'form-control',
                    'placeholder': 'Enter Rooms here ...'
					}
				),
            'bathrooms': forms.NumberInput(
				attrs={
					'class': 'form-control',
                    'placeholder': 'Enter Bathrooms here ...'
					}
				),
            'house_images': forms.ClearableFileInput(
				attrs={
					'class': 'form-control'
					}
				),        
			}