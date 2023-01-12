from django.db import models

class Usuari(models.Model):
    username= models.CharField(max_length=50)
    email= models.EmailField()


    def __str__(self):
        return self.username



class Post(models.Model):
    titulo= models.CharField(max_length=100)
    subtitulo=models.CharField(max_length=150)
    cuerpo= models.TextField(max_length=5000)
    autor= models.CharField(max_length=50)
    fecha= models.DateField()
    imagen = models.ImageField(null=True, blank=True, upload_to="post")

    def __str__(self):
        return self.titulo
    
