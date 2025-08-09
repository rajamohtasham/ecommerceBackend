from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'block w-full px-3 py-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300'}),
            'email': forms.EmailInput(attrs={'class': 'block w-full px-3 py-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300'}),
            'password1': forms.PasswordInput(attrs={'class': 'block w-full px-3 py-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300'}),
            'password2': forms.PasswordInput(attrs={'class': 'block w-full px-3 py-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            field.name: forms.TextInput(attrs={'class': 'block w-full px-3 py-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300'})
            for field in Product._meta.fields
        }