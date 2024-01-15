from .views import SolicitaPuesto
from django import forms


class SolicitaPuestoForm(forms.ModelForm):
    class Meta:
        model = SolicitaPuesto
        fields = ['ubicacion',
                  'departamento',
                  'area',
                  'motivo',
                  'cargo',
                  'justificacion',
                  'solicitante',
                  'usuario_aprueba',
                  'estado_aprobacion']
        # fields = '__all__'
        widgets = {
            'ubicacion': forms.Select(
                attrs={
                    'class': 'form-control in',
                    'id': 'departamento',
                    'required': 'required'
                }
            ),
            'departamento': forms.Select(
                attrs={
                    'class': 'form-control in',
                    'id': 'departamento',
                    'required': 'required'
                }
            ),
            'area': forms.Select(
                attrs={
                    'class': 'form-control in',
                    'id': 'area',
                    'required': 'required',
                }
            ),
            'motivo': forms.Select(
                attrs={
                    'class': 'form-control in',
                    'id': 'motivo',
                    'required': 'required',
                }
            ),
            'cargo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'cargo',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'justificacion_compra',
                    'rows':5,
                }
            ),
            'justificacion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'justificacion_compra',
                    'rows':5,
                }
            ),
            # Agrega más widgets si lo necesitas
        }
