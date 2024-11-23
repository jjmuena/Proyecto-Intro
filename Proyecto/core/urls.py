from django.urls import path
from .views import inicio, desafios, exit, puntos, register, perfil, guardar_puntos, obtener_puntos
from . import views

urlpatterns = [
    path('', inicio, name='inicio'),
    path('desafios/', desafios, name='desafios'),
    path('logout/', exit, name='exit'),
    path('puntos/', puntos, name='puntos'),
    path('register/', register, name='register'),
    path('perfil/', perfil, name='perfil'),
    path('guardar-puntos/', views.guardar_puntos, name='guardar_puntos'),
    path('obtener-puntos/', obtener_puntos, name='obtener_puntos'),
]