from django.contrib.auth.forms import UserCreationForm

from .models import User
from django import forms

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Nombre de Usuario', 'name':'name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Correo Electrónico', 'name':'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Ingresar Contraseña'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Confirmar Contraseña'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']