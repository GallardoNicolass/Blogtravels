from django.db import models


class Usuari(models.Model):
    name= models.CharField(max_length=50)
    email= models.EmailField()


    def __str__(self):
        return self.name



class Post(models.Model):
    titulo= models.CharField(max_length=100)
    subtitulo=models.CharField(max_length=150)
    cuerpo=models.TextField(blank=True, null=True)
    autor= models.CharField(max_length=50)
    fecha= models.DateField()
    imagen = models.URLField(max_length=700)

    def __str__(self):
        return self.titulo
    
