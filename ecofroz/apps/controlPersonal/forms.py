from django import forms
from .models import PersonaRegistro, VehiculoRegistro, Chofer, Cabezales, ReporteNovedades, DetReporteNovedades
from apps.usuarios.models import User
from django.forms.models import inlineformset_factory
from django.forms import modelformset_factory

carnet={
    (True, 'SI'),
    (False,'NO'),
}

class PersonaRegistroForm(forms.ModelForm):
    class Meta:
        model = PersonaRegistro
        fields = [
            'persona',
            'fch_ingreso',
            'fch_ingreso_txt',
            'hr_ingreso',
            'hr_ingreso_txt',
            'usuario_registra',
        ]
         
        labels = {
            'persona': '# Cédula',
            'hr_ingreso_txt': 'Hora Ingreso',
        }

        widgets = {
            'persona': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autofocus': True,
                }
            ),

            'fch_ingreso': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'hidden': True,
                }
            ),

            'fch_ingreso_txt': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'hidden': True,
                }
            ),

            'hr_ingreso': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'hidden': True,
                }
            ),

            'hr_ingreso_txt': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),

            'usuario_registra': forms.TextInput(
                attrs={
                    'hidden': True,
                }
            )
        }

class VehiculoRegistroForm(forms.ModelForm):
    class Meta:
        model = VehiculoRegistro
        fields = [
            'vehiculo',
            'fch_ingreso',
            'fch_ingreso_txt',
            'hr_ingreso',
            'hr_ingreso_txt',
            'usuario_registra',
        ]

        labels = {
            'vehiculo': 'N° Placa',
            'hr_ingreso_txt': 'Hora Ingreso',
        }

        widgets = {
            'vehiculo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autofocus': True,
                }
            ),

            'fch_ingreso': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'hidden': True,
                }
            ),

            'fch_ingreso_txt': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'hidden': True,
                }
            ),

            'hr_ingreso': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'hidden': True,
                }
            ),

            'hr_ingreso_txt': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),

            'usuario_registra': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }

class PersonaRegistroSForm(forms.ModelForm):
    class Meta:
        model = PersonaRegistro
        fields = [
            'persona',
            'hr_salida',
            'hr_salida_txt',
        ]
         
        labels = {
            'persona': '# Cédula',
            'hr_salida_txt': 'Hora Ingreso',
        }

        widgets = {
            'persona': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autofocus': True,
                }
            ),

            'hr_salida': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'hidden': True,
                }
            ),

            'hr_salida_txt': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }

class VehiculoRegistroSForm(forms.ModelForm):
    class Meta:
        model = VehiculoRegistro
        fields = [
            'vehiculo',
            'hr_salida',
            'hr_salida_txt',
        ]

        labels = {
            'vehiculo': 'N° Placa',
            'hr_salida_txt': 'Hora Salida',
        }

        widgets = {
            'vehiculo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autofocus': True,
                }
            ),

            'hr_salida': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'hidden': False,
                }
            ),

            'hr_salida_txt': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class RegistroPlacaCabezal(forms.ModelForm):
    class Meta:
        model = Cabezales
        fields = [
            'placa',
            'estado',
            'transportista',
        ]

        labels = {
            'placa': 'Nueva Placa',
            'estado': 'Estado',
            'transportista': 'Transportista',
        
        }

        widgets = {
            'placa':forms.TextInput(attrs={'class':'form-control'}),
			'estado':forms.TextInput(attrs={'class':'form-control'}),
			'transportista':forms.Select(attrs={'class':'form-control'}),
        }



class RegistroChoferForm(forms.ModelForm):
    class Meta:
        model = Chofer
        fields = [
            'cedula',
            'nombres',
            'telefono',
            'transportista',
            'estado',
            'placa',
            'observaciones',

        ]
         
        labels = {
            'cedula': '# Cédula',
            'nombres': 'Nombres',
            'telefono': 'Celular',
            'transportista': 'Transportista',
            'placa':'Placa',
            'observaciones':'Observaciones',
        }

        widgets = {
            'cedula':forms.TextInput(attrs={'class':'form-control'}),
			'nombres':forms.TextInput(attrs={'class':'form-control'}),
			'telefono':forms.TextInput(attrs={'class':'form-control'}),
			'transportista':forms.Select(attrs={'class':'form-control'}),
            'placa':forms.Select(attrs={'class':'form-control'}),
			'observaciones':forms.Textarea(attrs={'class':'form-control'}),

        }


### FORMUYLARIOS DE REPORTES DIARIOS DE NOVEDADES GUARDIANIA

class selectGuardia(forms.Form):
    guardia1 = forms.ModelChoiceField(queryset = User.objects.all(), widget = forms.Select(attrs={'class':'form-control', 'value':'persona_registra', 'required': 'true'}))
    
    guardia2 = forms.ModelChoiceField(queryset = User.objects.all(), widget = forms.Select(attrs={'class':'form-control'}))

    def __init__(self, *args, **kwargs):
        super(selectGuardia, self).__init__(*args, **kwargs)
        self.fields['guardia1'].queryset = User.objects.all().filter(guardia=True).order_by('last_name')
        self.fields['guardia1'].label_from_instance = lambda obj: "%s" % (obj.last_name + ' ' + obj.first_name)
        self.fields['guardia2'].queryset = User.objects.all().filter(guardia=True).order_by('last_name')
        self.fields['guardia2'].label_from_instance = lambda obj: "%s" % (obj.last_name + ' ' + obj.first_name)
        self.fields['guardia2'].required = False


class cabIngresoReportes(forms.ModelForm):
    
    
    class Meta:
        model = ReporteNovedades

        fields = [
            # 'guardia1',
            # 'guardia2',
            'asunto',
            'observaciones_guardias',
            'observaciones_seg',
            'fchregistro'


        ]

        labels = {
            # 'guardia1':'Guardia N° 1:',
            # 'guardia2':'Guardia N° 2:',
            'asunto':'Asunto:',
            'observaciones_guardias':'Observaciones:',
            'observaciones_seg':'Observaciones Administrativas:',
            'fchregistro':'Fecha y Hora Reporte:'
        }

        widgets = {
            # 'guardia1': forms.Select(
            #     attrs={
            #         'class':'form-control',
            #         'required':'required',
            #     }
            # ),
        
            # 'guardia2':forms.Select(
            #     attrs={
            #         'class':'form-control',
                    
            #     }
            # ),

            'asunto':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'required':'required',
                }
            ),

            'observaciones_guardias':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'required':'required',
                    'rows': 15,
                }
            ),

            'observaciones_seg':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows': 3,
                }
            ),

            'fchregistro':forms.TextInput(
                attrs= {
                    'class':'form-control',
                    # 'type':'date',
                    'readonly':True
                }
            )

        
        }

    
class detIngresoReportes(forms.ModelForm):
    class Meta:

        model = DetReporteNovedades

        fields = [
            'img_1',
            # 'img_2',
        ]

        labels = {
            'img_1':'Imágen #1',
            # 'img_2':'Imágen #2',
        }

        widgets = {
            'img_1':forms.ClearableFileInput(
                attrs={
                    'class':'form-control-file',
                    'accept':'image/png, .jpeg, .jpg, image/gif',
                    # 'multiple':True
                }
            ),

            # 'img_2':forms.FileInput(
            #     attrs={
            #         'class':'form-control-file',
            #         'accept':'image/png, .jpeg, .jpg, image/gif',
            #     }
            # ),

        }

class det_solicitudMultiForm(forms.ModelForm):
    
    class Meta:
        model = DetReporteNovedades
        fields = [
            'img_1',
            
        ]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['item'].queryset = items.objects.all()

        labels = {
            'img_1':'Foto',
            
        }

        widgets = {
            'img_1':forms.ClearableFileInput(
                attrs={
                    'class':'form-control-file',
                    'accept':'image/png, .jpeg, .jpg, image/gif',
                
                }
            ),

        }
    

DetMultiFormSet = modelformset_factory(DetReporteNovedades, form=det_solicitudMultiForm, extra=1)