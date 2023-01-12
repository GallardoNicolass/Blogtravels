from django.urls import path
from .views import *


urlpatterns = [
    path("posts/", posts, name="posts"),
    path("inicio/", inicio, name="inicio"),
    path("perfil/", perfil, name="perfil"),
    path("about/", about, name="about"),
    
    path("postFormulario/", postFormulario, name="postFormulario"),
    path("busquedaAutor/", busquedaAutor, name="busquedaAutor"),
    path("buscar/", buscar, name="buscar"),
    
    
    path("leerPosts/", leerPosts, name="leerPosts"),
    path("eliminarPost/<id>", eliminarPost, name="eliminarPost"),
    path("editarPost/<id>", editarPost, name="editarPost"),


]