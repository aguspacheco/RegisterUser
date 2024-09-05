# Importancion de modulos y funciones.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Ejido

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if not username or not email or not password1 or not password2:
            error = 'Por favor, completa todos los campos para poder registrarse'
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': error
            })

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El correo electrónico ya está registrado'
                })
            try:
                user = User.objects.create_user(username=username,
                                                password=password1,
                                                email=email)
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya se encuentra registrado'
                })
        else:
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

@login_required
def datos_usuario(request):
    user = request.user 
    return render(request, 'datos.html', {
        'username': user.username,
        'email': user.email, 
    })

@csrf_exempt
def update_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = request.user

        nuevo_nombre = data.get('username', user.username)
        nuevo_email = data.get('email', user.email)

        user.username = nuevo_nombre
        user.email = nuevo_email
        user.save()

        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)
        
def password_reset_complete(request):
    return render(request, 'password_reset_complete')

def index(request):
    return render(request, 'index.html')

def vertramite(request):   
    return render(request, 'vertramite.html')

def datos(request):
    return render(request, 'datos.html')

def completarformulario(request):
    return render(request,'formulario.html')
        
def formulario(request):
    title = "Formulario VeSEP" 
    return render(request, "formulario.html", {"title": title}) 

def ejidos_view(request):
    ejidos = Ejido.objects.all()
    return render(request, 'formulario.html', {'ejidos': ejidos})
