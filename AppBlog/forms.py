from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.Form):
    titulo= forms.CharField(label="Titulo Post", max_length=100)
    subtitulo= forms.CharField(label="Subtitulo Post", max_length=150)
    cuerpo= forms.CharField(label="Cuerpo Post", max_length=5000)
    autor= forms.CharField(label="Autor Post", max_length=50)
    fecha= forms.DateField(label="Fecha Post")
    
