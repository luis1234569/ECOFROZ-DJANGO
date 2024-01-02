from django import forms

from .models import TicketsIt
from apps.usuarios.models import User

class Tickets(forms.ModelForm):
    class Meta:
        model = TicketsIt
        fields = [
            'solicita_nombre',
            'solicita_apellido',
            'solicita_codigo',
            'ubicacion',
            'departamento',
            'area',
            'tipo_problema',
            'descripcion_problema',
            
        ]

        labels = {
            'solicita_nombre':'Nombre',
            'solicita_apellido':'Apellido',
            'solicita_codigo':'Código',
            'ubicacion':'Ubicación',
            'departamento':'Departamento',
            'area':'Area',
            'tipo_problema':'Tipo de Soporte',
            'descripcion_problema':'Descripción del Problema',
            
        }

        widgets = {
           
            'solicita_nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':'solicita_nombre',
                    'required':'required'
                }
            ), 

            'solicita_apellido': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':'solicita_apellido',
                    'required':'required'
                }
            ),

            'solicita_codigo': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':'solicita_codigo',
                    'required':'required'
                }
            ),

            'ubicacion': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'ubicacion',
                    'required':'required'
                }
            ),

            'departamento': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'departamento',
                    'required':'required'
                }
            ), 

            'area': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'area',
                    'required':'required'
                }
            ),

            'tipo_problema': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'tipo_problema',
                    'required':'required'
                }
            ),

            'descripcion_problema': forms.Textarea(
                attrs={
                    'class': 'form-control in',
                    'id': 'descripcion',
                    'placeholder': 'Ingrese el producto',
                    'required': 'required',
                    'rows': 5,
                }
            ),
        }

class IngresoSoporte(forms.ModelForm):
    def __init__(self,*args,**kwargs):
           super (IngresoSoporte,self ).__init__(*args,**kwargs) # populates the post
           self.fields['usuario_responsabe'].queryset = User.objects.filter(soporte=True)
        #    self.fields['client'].queryset = Client.objects.filter(company=company)

    class Meta:
        model = TicketsIt
        fields = [
            'solicita_nombre',
            'solicita_apellido',
            'solicita_codigo',
            'ubicacion',
            'departamento',
            'area',
            'tipo_problema',
            'descripcion_problema',
            'area_responsable',
            'usuario_responsabe',
        ]

        labels = {
            'solicita_nombre':'Nombre',
            'solicita_apellido':'Apellido',
            'solicita_codigo':'Código',
            'ubicacion':'Ubicación',
            'departamento':'Departamento',
            'area':'Area',
            'tipo_problema':'Tipo de Soporte',
            'descripcion_problema':'Descripción del Problema, Actividad o Soporte',
            'area_responsable':'Area Responsable',
            'usuario_responsabe':'Usuario Responsable',
        }

        widgets = {
            'solicita_nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':'solicita_nombre',
                    'required':'required'
                }
            ), 

            'solicita_apellido': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':'solicita_apellido',
                    'required':'required'
                }
            ),

            'solicita_codigo': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':'solicita_codigo',
                    # 'required':'required'
                }
            ),

            'ubicacion': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'ubicacion',
                    'required':'required'
                }
            ),

            'departamento': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'departamento',
                    'required':'required'
                }
            ), 

            'area': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'area',
                    # 'required':'required'
                }
            ),

            'tipo_problema': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'tipo_problema',
                    'required':'required'
                }
            ),

            'descripcion_problema': forms.Textarea(
                attrs={
                    'class': 'form-control in',
                    'id': 'descripcion',
                    'placeholder': 'Ingrese el producto',
                    'required': 'required',
                }
            ),

            'area_responsable': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'area_responsable',
                    'required':'required'
                }
            ),

            'usuario_responsabe': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'usuario_responsabe',
                    'required':'required'
                }
            ),
        }

class EditaSoporte(forms.ModelForm):
    def __init__(self,*args,**kwargs):
           super (EditaSoporte,self ).__init__(*args,**kwargs) # populates the post
           self.fields['usuario_responsabe'].queryset = User.objects.filter(soporte=True)
           self.fields['reasignado_a'].queryset = User.objects.filter(soporte=True)
        
        #    self.fields['client'].queryset = Client.objects.filter(company=company)

    class Meta:
        model = TicketsIt
        fields = [
            'solicita_nombre',
            'solicita_apellido',
            'solicita_codigo',
            'ubicacion',
            'departamento',
            'area',
            'tipo_problema',
            'descripcion_problema',
            'area_responsable',
            'usuario_responsabe',
            'fch_soluciona',
            'hr_soluciona_txt',
            'observa_solucion',
            'estado_solicitud',
            'hr_solicita',
            'fch_solicita',
            'reasignado_a',
        ]

        labels = {
            'solicita_nombre':'Nombre',
            'solicita_apellido':'Apellido',
            'solicita_codigo':'Código',
            'ubicacion':'Ubicación',
            'departamento':'Departamento',
            'area':'Area',
            'tipo_problema':'Tipo de Soporte',
            'descripcion_problema':'Descripción del Problema',
            'area_responsable':'Area Responsable',
            'usuario_responsabe':'Usuario Registra',
            'fch_soluciona':'Fecha de solución',
            'hr_soluciona_txt':'Hora de Solución',
            'observa_solucion':'Observación de Solución',
            'estado_solicitud':'Estado',
            'hr_solicita':'Hora solicitud',
            'fch_solicita':'Fecha solicitud',
            'reasignado_a':'Reasignado a:'
        }

        widgets = {
             'reasignado_a': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'reasignado',
                }
            ), 
            'solicita_nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':'solicita_nombre',
                    'required':'required',
                    'readonly':'readonly',
                }
            ), 

            'solicita_apellido': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':'solicita_apellido',
                    'required':'required',
                    'readonly':'readonly',
                }
            ),

            'solicita_codigo': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':'solicita_codigo',
                    # 'required':'required',
                    'readonly':'readonly',
                }
            ),

            'ubicacion': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'ubicacion',
                    'required':'required',
                    'readonly':'readonly',
                }
            ),

            'departamento': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'departamento',
                    'required':'required',
                    'readonly':'readonly',
                }
            ), 

            'area': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'area',
                    # 'required':'required',
                    'readonly':'readonly',
                }
            ),

            'tipo_problema': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'tipo_problema',
                    'required':'required',
                    'readonly':'readonly',
                }
            ),

            'descripcion_problema': forms.Textarea(
                attrs={
                    'class': 'form-control in',
                    'id': 'descripcion',
                    'placeholder': 'Ingrese el producto',
                    'required': 'required',
                    'readonly':'readonly',
                }
            ),

            'area_responsable': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'area_responsable',
                    'required':'required',
                    'readonly':'readonly',
                }
            ),

            'usuario_responsabe': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'usuario_responsabe',
                    'required':'required',
                    'readonly':'readonly',
                }
            ),

            'fch_solicita': forms.DateInput(
                attrs={
                    'class':'form-control',
                    'id':'fch_solicita',
                    'required':'required',
                    'type':'date',
                }
            ),

            'hr_solicita': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':'hr_solicita',
                    'required':'required',
                    'data-mask':"99:99"
                }
            ),

            'fch_soluciona': forms.DateInput(
                attrs={
                    'class':'form-control',
                    'id':'fch_soluciona',
                    'required':'required',
                    'type':'date',
                }
            ),

            'hr_soluciona_txt': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':'hr_soluciona_txt',
                    'required':'required',
                    'data-mask':"99:99"
                }
            ),

            'observa_solucion': forms.Textarea(
                attrs={
                    'class': 'form-control in',
                    'id': 'observa_solucion',
                    'placeholder': 'Ingrese la solución',
                    'required': 'required',
                }
            ),

            'estado_solicitud': forms.Select(
                attrs={
                    'class': 'form-control in',
                    'id': 'estado_solicitud',
                    'required': 'required',
                }
            ),
        }