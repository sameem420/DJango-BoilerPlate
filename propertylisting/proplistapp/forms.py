from django import forms
from .models import *

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