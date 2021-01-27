from django import forms
from .models import *


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))

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