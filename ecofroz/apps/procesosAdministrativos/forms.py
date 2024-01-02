from django import forms
from apps.activos.models import activo_areas,activo_depar, activo_ubica
from .models import *
from apps.usuarios.models import User
from django.forms.models import inlineformset_factory
from django.forms import modelformset_factory


class cargaDoc(forms.ModelForm):
    class Meta:
        model = Eventos

        fields = [
            'docs',
        ]


class cabIngresoSolicitudTransporte(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(cabIngresoSolicitudTransporte, self).__init__(*args, **kwargs)
        self.fields['ubica'].queryset = activo_ubica.objects.exclude(id=9) # EXCLUYE DE LA LISTA A REPARACION EXTERNA

    class Meta:
        model = SolicitudTransporte

        fields = [
            'ubica',
            'departamento', 
            'tipo',
            'area',
            'ruta',
            'fchsolicita',
            'justificacion',
            'pasajero',
            'retorno',

        ]

        labels = {
            'ubica':'Ubicación',
            'departamento':'Departamento',
            'tipo':'Tipo',
            'justificacion':'Justificación / Observaciones / Instrucciones para la encomienda',
            'ruta':'Seleccione la ruta  (Este campo es obligatorio)',
            'pasajero':'Ingrese el nombre del pasajero',
            # 'fchevento':'Seleccione la fecha y hora para la que se requiere el transporte',
            'retorno':'Requiero transporte de retorno',
        }

        widgets = {
            'retorno': forms.TextInput(
                attrs={
                    'id':'retornoc',
                    'type':'checkbox',
                }
            ),
        
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

            'ruta': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'name':'ruta',
                    'id':'ruta',
                    'placeholder':'Digite una letra',
                    'hidden':True,
                }
            ),

            'justificacion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'required':'required',
                    'rows': 3,
                }
            ),

            'pasajero': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'name':'nombre_pasajero',
                    'id':'nombre_pasajero',
                    'placeholder':'Digite una letra'
                }
            ),

            

            'usuario_solicita':forms.TextInput(
                attrs={
                    'class':'form-control',
                    
                }
            ),

            # 'fchevento':forms.DateInput(
            #     attrs={
            #         'class':'form-control',
            #         'type':'datetime-local'
            #     }
            # ),

            #  'fchevento':forms.TextInput(
            #     attrs={
            #         'class':'form-control',
            #     }
            # ),

        }


    def clean_fchevento(self):
        val = self.cleaned_data['fchevento']
        fecha_r = val.replace("T"," ")
            
        return fecha_r


    
class detIngresoSolicitudTransporte(forms.ModelForm):
    class Meta:

        model = DetSolicitudTransporte

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

class solicitudMultiForm(forms.ModelForm):
    class Meta:
        model = Egresos
        fields = [
            'bodega',
            'proyecto',
            'fecha',
            'lote',
            'usuario_registra',
            'fecha_registra',
            'observaciones',
        ]

        labels = {
            'bodega':'Bodega',
            'proyecto':'Proyecto',
            'fecha':'Fecha',
            'lote':'Lote',
            'usuario_registra':'Usuario Registra',
            'fecha_registro':'Fecha Registro',
            'empresa':'Empresa o Gestor',
            'observaciones':'Observaciones',
        }

        widgets = {
            'bodega':forms.Select(
                attrs={
                    # 'class': 'select-tipo',
                    'class': 'form-select',
                }
            ),
            
            'proyecto':forms.Select(
                attrs={
                    # 'class': 'select-tipo',
                    'class': 'form-select',
                
                }
            ),
            'fecha':forms.DateInput(
                attrs={
                    # 'class': 'select-tipo',
                    'class': 'form-select',
                    'type': 'date',
                }
            ),
            'lote':forms.TextInput(
                attrs={
                    # 'class': 'select-tipo',
                    'class': 'form-control',
                }
            ),

            'observaciones':forms.Textarea(
                attrs={
                    # 'class': 'textarea',
                    'class': 'form-control',
                    'rows': 4,
                }
            ),

            'registra':forms.TextInput(
                attrs={
                    # 'class': 'textinput',
                    'class': 'form-control',
                    'readonly':'True',
                }
            ),


        }


class det_solicitudMultiForm(forms.ModelForm):
    
    class Meta:
        model = InventarioConsolidado
        fields = [
            'producto',
            'peso',
            'unimed',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['producto'].queryset = InventarioConsolidado.objects.all()

        labels = {
            'producto':'Producto',
            'peso':'Cantidad',
            'unimed':'Unidad de Medida',
        }

        widgets = {
            'producto':forms.Select(
                 attrs={
                    'class': 'select-tipo-item',
                    'id': 'item',
                    'required':'required',
                }
            ),
            'unimed':forms.Select(
                 attrs={
                    # 'class': 'select-tipo',
                    'class': 'form-select',
                    'required':'required',
                }
            ),

            'peso':forms.TextInput(
                 attrs={
                    # 'class': 'textinput',
                    'class': 'form-control',
                    'required':'required',
                }
            ),
        }
    

DetMultiFormSet = modelformset_factory(InventarioConsolidado, form=det_solicitudMultiForm, extra=1)