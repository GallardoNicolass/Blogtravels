from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from AppBlog.forms import *

def posts(request):
    return render(request, "AppBlogg/posts.html")



def inicio(request):
    return render(request, "AppBlogg/inicio.html")

def perfil(request):
    return render(request, "AppBlogg/perfil.html")

def about(request):
    return render(request, "AppBlogg/about.html")


def postFormulario(request):
    if request.method=="POST":
        form= postFormulario(request.POST)

        if form.is_valid():
            informacion=form.changed_data
            titulo= informacion["titulo"]
            subtitulo= informacion["subtitulo"]
            cuerpo= informacion["cuerpo"]
            autor= informacion["autor"]
            fecha= informacion["fecha"]
            imagen= informacion["imagen"]
            post= Post(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha, imagen=imagen)
            post.save()
            posts=Post.objects.all()
            return render(request, "AppBlogg/posts.html" ,{"posts":posts, "mensaje": "Post subido correctamente"})
        else:
            return render(request, "AppBlogg/PostFormulario.html" ,{"form": form, "mensaje": "Algo salio mal, vuelve a intentar"})

    else:
        formulario= PostForm()
        return render (request, "AppBlogg/PostFormulario.html", {"form": formulario})


def busquedaAutor(request):
    return render(request, "AppBlogg/busquedaAutor.html")

def buscar(request):
    autor= request.GET["autor"]
    if autor!="":
        posts= Post.objects.get()
        return render(request, "AppBlogg/resultadosBusqueda.html", {"posts": posts})
    else:
        return render(request, "AppBlogg/busquedaAutor.html", {"mensaje": "Ingresa un autor para busacar"})
        


def leerPosts(request):
    posts=Post.objects.all()

    return render(request, "AppBlogg/posts.html", {"posts": posts})

def eliminarPost(request, id):
    post=Post.objects.get(id=id)
    post.delete()
    posts=Post.objects.all()
    return render(request, "AppBlogg/Posts.html", {"posts": posts, "mensaje": "Post eliminado correctamente"})

def editarPost(request, id):
    post=Post.objects.get(id=id)
    if request.method=="POST":
        form= PostForm(request.POST)
        if form.is_valid():
            info=form.changed_data
            post.titulo=info["titulo"]
            post.subtitulo=info["subtitulo"]
            post.cuerpo=info["cuerpo"]
            post.autor=info["autor"]
            post.fecha=info["fecha"]
            post.imagen=info["imagen"]
            post.save()
            posts=Post.objects.all()
            return render(request, "AppBlogg/posts.html", {"posts":posts, "mensaje": "post editado correctamente"})
        pass
    else:
        formulario=PostForm(initial={"titulo":post.titulo, "subtitulo":post.subtitulo, "cuerpo":post.cuerpo, "autor":post.autor, "fecha":post.fecha, "imagen":post.imagen})
        return render(request, "AppBlogg/editarPost.html", {"form":formulario, "post":post})



