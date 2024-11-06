from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Formulario

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = [
            'ejidoAnterior',
            'chacraAnterior',   'fraccionAnterior', 'quinta', 
            'lote',
            'macizoAnterior', 'manzanaAnterior', 'unidad_funcionalAnterior',
            'ejidoActual', 'circunscripcion', 
            'sector',
            'chacraActual', 'fraccionActual', 'macizoActual', 'manzanaActual', 
            'parcela', 'unidad_funcionalActual',
            'expediente', 
            'plano', 
            'TomoCatastral', 'folioCatastral', 'apellido',
            'calle', 
            'numero', 
            'cuit',
            'tomoJuridicos', 'FolioJuridicos', 'matricula', 'fecha_juridicos', 'fecha_matricula'
        ]

    # Ejemplo de validaciones personalizadas
    def clean_cuit(self):
        cuit = self.cleaned_data.get('cuit')
        if len(str(cuit)) != 11:  
            raise ValidationError('El CUIT debe tener 11 dígitos.')
        return cuit

    def clean_fecha_juridicos(self):
        fecha_juridicos = self.cleaned_data.get('fecha_juridicos')
        if fecha_juridicos and fecha_juridicos > timezone.now().date():
            raise ValidationError('La fecha no puede ser mayor a la actual.')
        return fecha_juridicos
    
    def clean_fecha_matricula(self):
        fecha_matricula = self.cleaned_data.get('fecha_matricula')
        if fecha_matricula and fecha_matricula > timezone.now().date():
            raise ValidationError('La fecha no puede ser mayor a la actual.')
        return fecha_matricula
    
    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        if numero < 0:
            raise ValidationError('El número debe ser mayor o igual a cero.')
        return numero
