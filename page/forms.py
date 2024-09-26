from django import forms
from .models import Formulario
from django.utils import timezone

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
            raise forms.ValidationError('El CUIT debe tener 11 dígitos.')
        return cuit

    def clean_fecha_juridicos(self):
        fecha_juridicos = self.cleaned_data.get('fecha_juridicos')
        if fecha_juridicos and fecha_juridicos > timezone.now().date():
            raise forms.ValidationError('La fecha no puede ser futura.')
        return fecha_juridicos

    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        if numero < 0:
            raise forms.ValidationError('El número debe ser mayor o igual a cero.')
        return numero
