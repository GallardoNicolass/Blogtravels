from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.Form):
    titulo= forms.CharField(label="Titulo Post", max_length=100)
    subtitulo= forms.CharField(label="Subtitulo Post", max_length=150)
    cuerpo= forms.CharField(label="Cuerpo Post", max_length=5000)
    autor= forms.CharField(label="Autor Post", max_length=50)
    fecha= forms.DateField(label="Fecha Post")
    imagen= forms.URLField(label="imagen", max_length=700)


class RegistroUsuarioForm(UserCreationForm):

    email= forms.EmailField(label="Email")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}
        
