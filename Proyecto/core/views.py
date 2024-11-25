import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
# Create your views here.

@login_required
def inicio(request):
    return render(request, 'core/inicio.html')

@login_required
def desafios(request):
    puntos_acumulados = request.user.score
    return render(request, 'core/desafios.html', {'puntos_acumulados': puntos_acumulados})

@login_required
def puntos(request):
    return render(request, 'core/puntos.html')

@login_required
def perfil(request):
    puntos_acumulados = request.user.score
    articles = obtener_articulos()
    return render(request, 'core/perfil.html', {'puntos_acumulados': puntos_acumulados, 'articles': articles})

def obtener_articulos():
    api_key = 'f338fb6b35f54c33a8431e0ff673b780'
    url = f'https://newsapi.org/v2/everything?q=calentamiento%20global&language=es&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['articles']
    return []

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('inicio')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)

def exit(request):
    logout(request)
    return redirect('inicio')

@login_required
@require_POST
def guardar_puntos(request):
    puntos = request.POST.get('puntos')
    if puntos is not None:
        try:
            puntos = int(puntos)
            request.user.score += puntos
            request.user.save()
            return JsonResponse({'mensaje': 'Puntos guardados correctamente', 'puntos': request.user.score})
        except ValueError:
            return JsonResponse({'error': 'Puntos inválidos'}, status=400)
    return JsonResponse({'error': 'Puntos no proporcionados'}, status=400)

@login_required
@require_GET
def obtener_puntos(request):
    return JsonResponse({'puntos': request.user.score})