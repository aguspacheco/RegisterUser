# Importancion de modulos y funciones.
import json
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from .models import Ejido, Formulario
from .forms import FormularioForm
from .utils.funciones import mensaje_exito, mensaje_error
from django.utils import timezone



# Función para validaciones de campos vacios
def validarCampos(request, *fields):
    if not all(fields):
        mensaje_error(request, 'Por favor, completa todos los campos.')
        return False
    return True

# Función para validaciones de contraseñas
def validarPass(request, password1, password2):
    if password1 != password2:
        mensaje_error(request, 'Las contraseñas no coinciden.')
        return False
    return True

# Vista para el registro de usuarios
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm()})
    
    username, email, password1, password2 = (request.POST.get(field) for field in ['username', 'email', 'password1', 'password2']) 

    if not validarCampos(request, username, email, password1, password2):
        return render(request, 'signup.html', {'form': UserCreationForm()})
    
    if not validarPass(request, password1, password2):
        return render(request, 'signup.html', {'form': UserCreationForm()})

    if User.objects.filter(email=email).exists():
            mensaje_error(request, 'El correo electrónico ya está registrado.')
            return render(request, 'signup.html', {'form': UserCreationForm()})

    try:
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        login(request, user)
        return redirect('index')
    except IntegrityError:
            mensaje_error(request, 'El nombre de usuario ya existe.')
            return render(request, 'signup.html', {'form': UserCreationForm()})

#Vistas para cerrar seccion
@login_required 
def salir(request):
    logout(request)
    return redirect('signin')

#Vista para iniciar seccion
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm()})
    
    # Obtén el nombre de usuario y la contraseña del formulario
    username = request.POST.get('username')
    password = request.POST.get('password')

    # Verifica que ambos campos estén llenos
    if not validarCampos(request, username, password):
        return render(request, 'signin.html', {'form': AuthenticationForm()})

    # Autentica al usuario por el nombre de usuario y contraseña
    user = authenticate(request, username=username, password=password)

    # Si la autenticación falla, muestra un mensaje de error
    if user is None:
        mensaje_error(request, 'El usuario o la contraseña es incorrecta.')
        return render(request, 'signin.html', {'form': AuthenticationForm()})
    
    # Si la autenticación es exitosa, inicia sesión y redirige
    login(request, user)
    return redirect('index')


# Vista para mostrar datos del usuario autenticado
@login_required
def datos_usuario(request):
    user = request.user 
    return render(request, 'datos_usuario.html', {'username': user.username,'email': user.email})

# Vista para actualizar los datos del usuario
@csrf_exempt
@login_required
def update_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = request.user
            user.username = data.get('username', user.username)
            user.email = data.get('email', user.email)
            user.save()
            return JsonResponse({'success': True})
        except Exception as e:
            messages.error(request, f'Ocurrió un error al actualizar los datos: {str(e)}')
            return JsonResponse({'success': False, 'error': 'Error en la actualización.'}, status=500)
    
    return JsonResponse({'success': False, 'error': 'Solicitud inválida.'}, status=400)

def render_template(request, template_name):
    return render(request, template_name)

def password_reset_complete(request):
    return render_template(request, 'password_reset_complete.html')

@login_required
def tramiteUser(request):   
    formularios = Formulario.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    tiene_formularios = formularios.exists()
    return render(request, 'tramiteUser.html', {
        'formularios': formularios,
        'tiene_formularios': tiene_formularios
    })

def completarformulario(request):
    fecha_actual = timezone.now().date().strftime()
    return render(request,'formulario.html', {'fecha_actual': fecha_actual})

def formulario_exito(request):
    return render(request, 'formulario_exito.html')

def index(request):
    return render(request, 'index.html')

def ejidos_view(request):
    ejidos = Ejido.objects.all()
    return render(request, 'formulario.html', {'ejidos': ejidos})

def date_form(request):
    if request.method == "POST":
        selected_date = request.POST.get("date")
        if selected_date:
            selected_date = timezone.datetime.strptime(selected_date, "%Y-%m-%d").date()
            today = timezone.now().date()

            # Validación de fecha en el servidor
            if selected_date > today:
                messages.error(request, "No puedes elegir una fecha futura.")
                return redirect("date_form")
            else:
                # Procesa la fecha (guarda en base de datos o lo que necesites hacer)
                messages.success(request, "Fecha válida seleccionada.")
                return redirect("date_form")
    return render(request, "date_form.html")

class CrearFormulario(CreateView):
    model = Formulario
    form_class = FormularioForm
    template_name = 'crear_formulario.html'

    def form_valid(self, form):
        fecha_actual = timezone.now().date()
        fecha_juridicos = form.cleaned_data.get('fechaJuridicos')
        fecha_matricula = form.cleaned_data.get("fechaMatricula")

        if fecha_juridicos and fecha_juridicos > fecha_actual:
            form.add_error('fechaJuridicos', 'La fecha no puede ser en el futuro')
            return self.form_invalid(form)
        
        if fecha_matricula and fecha_matricula > fecha_actual:
            form.add_error('fechaMatricula', 'La fecha no puede ser en el futuro')
            return self.form_invalid(form)

        form.instance.usuario = self.request.user
        form.save()
        mensaje_exito(self.request, 'El formulario se guardo correctamente.')
        return redirect('formulario_exito')
