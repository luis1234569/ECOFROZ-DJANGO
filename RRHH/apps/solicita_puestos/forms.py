from .views import solicita_puesto
from django import forms


class SolicitaPuestoForm(forms.ModelForm):
    class Meta:
        model = solicita_puesto
        fields = ['ubicacion',
                  'departamento',
                  'area',
                  'motivo',
                  'puesto',
                  'descripcion',
                  'justificacion',
                  'solicitante',
                  'estado_aprobacion']
        # O puedes usar '__all__' para incluir todos los campos
        # fields = '__all__'

        # Opcional: Agregar widgets personalizados, etiquetas, etc.
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
            'puesto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'puesto',
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
