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
                    'placeholder': 'Enter Address here ...'
                    }
                ),
            'profile_picture': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Rooms here ...'
                    }
                ),
            'city': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Bathrooms here ...'
                    }
                ),
            'country': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),        
            }
        

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password', 'first_name', 'last_name']

    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
        # 'username', 'email', 'password', 'password_repeat', 'first_name', 'last_name' ,
        # fields = ['phone_number', 'profile_picture']
        # widgets = {
        #     'phone_number': forms.NumberInput(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': 'Enter phone number here ...'
        #             }
        #         ),
        #     'profile_picture': forms.ClearableFileInput(
        #         attrs={
        #             'class': 'form-control'
        #             }
        #         ),        
        #     }

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