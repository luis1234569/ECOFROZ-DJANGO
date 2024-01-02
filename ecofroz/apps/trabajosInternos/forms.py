from django import forms
from apps.activos.models import activo_areas,activo_depar, activo_ubica
from .models import SolicitudTrabajoInterno, DetSolicitudTrabajoInterno, RecibeEncargo
from apps.usuarios.models import User
from apps.ordenTrabajo.models import TipoPedido


class cabIngresoTrabajos(forms.ModelForm):
    class Meta:
        model = SolicitudTrabajoInterno

        fields = [
            'ubica',
            'departamento', 
            'tipo',
            'area',
            # 'usuario_solicita',
            'fchsolicita',
            'descripcion',
            'justificacion',

        ]

        labels = {
            'ubica':'Ubicación',
            'departamento':'Departamento',
            'tipo':'Tipo',
            'descripcion':'Descripción (Este campo es obligatorio)',
            'justificacion':'Justificacion (Este campo es obligatorio)'
        }

        widgets = {
            'ubica': forms.Select(
                attrs={
                    'class':'form-control',
                    'required':'required',
                }
            ),
        
            'departamento':forms.Select(
                attrs={
                    'class':'form-control',
                    'required':'required',
                }
            ),

            'tipo':forms.Select(
                attrs={
                    'class':'form-control',
                    'required':'required',
                }
            ),

            'area':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'hidden':True,
                }
            ),


            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'required':'required',
                    'rows': 8,
                }
            ),

            'justificacion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'required':'required',
                    'rows': 3,
                }
            ),

            'usuario_solicita':forms.TextInput(
                attrs={
                    'class':'form-control',
                    
                }
            )
        
        }

    
class detIngresoTrabajos(forms.ModelForm):
    class Meta:

        model = DetSolicitudTrabajoInterno

        fields = [
            'img_1',
            'img_2',
        ]

        labels = {
            'img_1':'Imágen #1',
            'img_2':'Imágen #2',
        }

        widgets = {
            'img_1':forms.FileInput(
                attrs={
                    'class':'form-control-file',
                    'accept':'image/png, .jpeg, .jpg, image/gif',
                }
            ),

            'img_2':forms.FileInput(
                attrs={
                    'class':'form-control-file',
                    'accept':'image/png, .jpeg, .jpg, image/gif',
                }
            ),

        }

class cabVerTrabajos(forms.ModelForm):
    class Meta:
        model = SolicitudTrabajoInterno

        fields = [
            'ubica',
            'departamento', 
            'tipo',
            'area',
            # 'usuario_solicita',
            'fchsolicita',
            'descripcion',
            'justificacion',

        ]

        labels = {
            'ubica':'Ubicación',
            'departamento':'Departamento',
            'tipo':'Tipo',
            'descripcion':'Descripción',
            'justificacion':'Justificacion'
        }

        widgets = {
            'ubica': forms.Select(
                attrs={
                    'class':'form-control',
                    'readonly': True,
                    'disabled': True,
                }
            ),
        
            'departamento':forms.Select(
                attrs={
                    'class':'form-control',
                    'readonly': True,
                    'disabled': True,
                }
            ),

            'tipo':forms.Select(
                attrs={
                    'class':'form-control',
                    'required':'required',
                    'readonly': True,
                    'disabled': True,
                }
            ),

            'area':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'hidden':True,
                    
                }
            ),


            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'required':'required',
                    'rows': 8,
                    'readonly': True,
                }
            ),

            'justificacion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'required':'required',
                    'rows': 3,
                    'readonly': True,
                }
            ),

            'usuario_solicita':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'readonly': True,
                    
                }
            )
        
        }

class detVerTrabajos(forms.ModelForm):
    class Meta:

        model = DetSolicitudTrabajoInterno

        fields = [
            'img_1',
            'img_2',
        ]

        labels = {
            'img_1':'Imágen #1',
            'img_2':'Imágen #2',
        }

       

class detIngresoTrab(forms.ModelForm):
    class Meta:

        model = DetSolicitudTrabajoInterno

        fields = [
            'img_1',
            'img_2',
        ]

        labels = {
            'img_1':'Imágen #1',
            'img_2':'Imágen #2',
        }

       

        

class selectAsignadoa(forms.Form):
    asignacion = forms.ModelMultipleChoiceField(required=False,queryset= User.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    def __init__(self, *args, **kwargs):
        super(selectAsignadoa, self).__init__(*args, **kwargs)
        self.fields['asignacion'].queryset = User.objects.filter(asignado_mantenimiento=True).order_by('last_name')
        self.fields['asignacion'].label_from_instance = lambda obj: "%s" % (obj.last_name + ' ' + obj.first_name)
        

class TipoTrab(forms.Form):
    tipo_trabajo = forms.ModelChoiceField(queryset = TipoPedido.objects.all(), widget = forms.Select(attrs={'class':'form-control', 'name':'tipo_trabajo', 'required': 'true'}))

    def __init__(self, *args, **kwargs):
        super(TipoTrab, self).__init__(*args, **kwargs)
        self.fields['tipo_trabajo'].queryset = TipoPedido.objects.filter(cod__in=['PR','MP','MC','OS']).order_by('nombre')
        self.fields['tipo_trabajo'].label_from_instance = lambda obj: "%s" % (obj.nombre)
        