from django.urls import path
from .views import inicio, desafios, exit, puntos, register, perfil


urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('desafios/', desafios, name= 'desafios'),
    path('logout/', exit, name= 'exit'),
    path('puntos/', puntos, name= 'puntos'),
    path('register/', register, name= 'register'),
    path('perfil/', perfil, name= 'perfil'),
]