from django.utils import timezone
from django.forms import ValidationError
from django.contrib import messages
from .constants import ICON_CHECK, ICON_ERROR, ICON_TRIANGLE

# ------------- FUNCIONES PARA MENSAJES ------------------
def mensaje_error(request, message):
    messages.error(request, f'{ICON_ERROR} {message}')

def mensaje_exito(request, message):
    messages.success(request, f'{ICON_CHECK} {message}')

def mensaje_advertencia(request, message):
    messages.warning(request, f'{ICON_TRIANGLE} {message}')

# ------------- FUNCIONES PARA VALIDACION ------------------
def validate_no_mayor_actual(value):
    if value > timezone.now().date():
        raise ValidationError('La fecha no puede ser en el futuro.')

