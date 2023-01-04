from django.urls import path
from .views import *


urlpatterns = [
    path("posts/", posts, name="posts"),
    path("inicio/", inicio, name="inicio"),
]  