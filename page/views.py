# Importancion de modulos y funciones.
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Ejido

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if not username or not password1 or not password2:
            error = 'Por favor, completa todos los campos para poder registrarse'
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': error
            })

        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya se encuentra registrado'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Las contraseñas no coinciden'
        })

@login_required 
def salir(request):
    logout(request)
    return redirect('signin')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            error = 'Por favor, completa todos los campos'
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': error
            })

        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            error = 'El usuario o la constraseña es incorrecta'
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': error
            })
        else:
            login(request, user)
            return redirect('index')
        
def password_reset_complete(request):
    return render(request, 'password_reset_complete')

def index(request):
    return render(request, 'index.html')

def vertramite(request):   
    return render(request, 'vertramite.html')

def completarformulario(request):
    return render(request,'formulario.html')
        
def formulario(request):
    title = "Formulario VeSEP" 
    return render(request, "formulario.html", {"title": title}) 

