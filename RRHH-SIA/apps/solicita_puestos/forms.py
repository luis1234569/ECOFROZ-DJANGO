from .views import SolicitaPuesto
from django import forms


class SolicitaPuestoForm(forms.ModelForm):
    class Meta:
        model = SolicitaPuesto
        fields = ['ubicacion',
                  'departamento',
                  'motivo',
                  'cargo',
                  'justificacion',
                  'solicitante',
                  'usuario_aprueba',
                  'observacion_aprueba',
                  'estado_aprobacion',
                  'estado_ingreso',
                  'notasges',
                  'motRechaza'
                  ]
        # fields = '__all__'
        labels = {
            'observacion_aprueba':'Observación',
            'justificacion':'Justificación'
        }
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
                    'required': 'required',
                }
            ),
            # 'descripcion': forms.Textarea(
            #     attrs={
            #         'class': 'form-control',
            #         'id': 'justificacion_compra',
            #         'rows':5,
            #     }
            # ),
            'justificacion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'justificacion',
                    'rows':5,
                    'required': 'required',
                }
            ),
            'observacion_aprueba': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'observacion_aprueba',
                    'rows':5,
                    'required': 'required',
                }
            ),
        }


