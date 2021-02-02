from django import forms
from .models import *
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone_number', 'profile_picture', 'city', 'country')
        widgets = {
            'phone_number': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your mobile number ...'
                    }
                ),
            'profile_picture': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    }
                ),
            'city': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your city ...'
                    }
                ),
            'country': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your country ...'
                    }
                ),        
            }
        

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your username ...'
                    }
                ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    }
                ),
            'password': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'readonly': True
                    }
                ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your First Name ...'
                    }
                ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your Last Name ...'
                    }
                ),             
            }

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