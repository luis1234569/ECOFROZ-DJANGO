from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms.models import inlineformset_factory

from .models import OrdenesTrabajos, DetalleTrabajo, CotizaTrabajo, PedidosMba, TrabajosPago, TipoPedido, PreCotiza, SolicitudesAdqui
from apps.activos.models import activo_ubica, activo_areas
from apps.usuarios.models import User

# ordenes = OrdenesTrabajos.objects.all()
# orden_data = []
# for ord in ordenes:
#     d=(
#         ord.numtrabajo, ord.numtrabajo
#     )
#     orden_data.append(d)

class selectAsignadoa(forms.Form):
    asignacion = forms.ModelMultipleChoiceField(required=False,queryset= User.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    def __init__(self, *args, **kwargs):
        super(selectAsignadoa, self).__init__(*args, **kwargs)
        self.fields['asignacion'].queryset = User.objects.filter(consulta_experta=True).order_by('last_name')
        self.fields['asignacion'].label_from_instance = lambda obj: "%s" % (obj.last_name + ' ' + obj.first_name)
        


medidas={
    ('unidad','Unidad'),
    ('m','Metro'),
    ('cm','Centimetro'),
    ('mm','Milimetro'),
    ('lt','Litros'),
    ('gl','Galones'),
    ('gr','Gramos'),
    ('kg','Kilos'),
    ('lb','Libras'),
}

orden_ref={
    (True, 'SI'),
    (False, 'NO'),
}

tipo_ped={
    ('PR', 'Proyecto'),
    ('MP', 'Mantenimiento Preventivo'),
    ('MC', 'Mantenimiento Correctivo'),
    ('OT', 'Otros Insumos'),
    ('OS', 'Orden de Servicio'),    
}

# class MyModelChoiceField(forms.ModelChoiceField):
#     def label_from_instance(self, obj):
#         return "N° de Orden %i" % obj.numtrabajo

class TrabajoForm(forms.ModelForm):

    # orden_referencial = forms.ModelChoiceField(queryset = OrdenesTrabajos.objects.none(), to_field_name='numtrabajo', widget = forms.Select(attrs={'class':'form-control', 'id':'orden_referencial', 'required':'False'}))
    # tipo_pedi = forms.ModelChoiceField(queryset = TipoPedido.objects.all())

    def __init__(self, *args, **kwargs):
        super(TrabajoForm, self).__init__(*args, **kwargs)
        self.fields['tipo_pedi'].queryset = TipoPedido.objects.filter(estado=True).filter(tipo='N')
        self.fields['ubica'].queryset = activo_ubica.objects.filter(ubica_estado=1)
        # self.fields['orden_referencial'].label_from_instance = lambda obj: "N° de Orden %s" % (obj.numtrabajo)


    class Meta:
        model = OrdenesTrabajos
        fields = [
            'tipo_trabajo',
            'tipo_pedi',
            'departamento',
            'area',
            'usuario_solicita',
            # 'numproyecto',
            'justificacion_compra',
            'refer_orden',
            'orden_referencial',
            'fchsolicitatxt',
            'salida_activo',
            'ubica',
            'grupo',
        ]

        labels = {
            'tipo_trabajo': 'Tipo de Trabajo',
            'tipo_pedi': 'Tipo de Pedido',
            'departamento': 'Departamento',
            'area': 'Sector (En donde se realizará el trabajo)',
            # 'numproyecto': 'Seleccione el Proyecto',
            'justificacion_compra': 'Justificación de Compra',
            'refer_orden': 'Esta Asociado a una Orden Anterior?',
            'salida_activo': 'El Activo Sale de la Empresa?',
            'ubica': 'Ubicación',
            'grupo': 'Grupo',
        }

        widgets = {
            
            'tipo_trabajo': forms.RadioSelect(
                attrs={
                    'class': 'form-check-input',
                    'id': 'tipo_trabajo',
                }
            ),

            'tipo_pedi': forms.Select(
                attrs={
                    'class': 'form-control in col-md-6',
                    'id': 'tipo_pedido',
                    'required':'required',
                }
            ),

            'departamento': forms.Select(
                attrs={
                    'class':'form-control in',
                    'id':'departamento',
                    'required':'required',
                }
            ),

            'area': forms.Select(
                attrs={
                    'class': 'form-control in',
                    'id': 'area',
                    'required':'required',
                }
            ),

            # 'numproyecto': forms.TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         'id': 'numproyecto',
            #         'placeholder': 'Proyecto',
            #     }
            # ),

            'justificacion_compra': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'justificacion_compra',
                    'maxlength':2000,
                    'rows':4,
                }
            ),

            'refer_orden': forms.RadioSelect(
                attrs={
                    # 'class': 'form-check-input',
                    'id': 'refer_orden',
                    # 'type': 'radio',
                }
            ),

            'salida_activo': forms.RadioSelect(
                attrs={
                    'class': 'radio-inline',
                    # 'list-style': 'none',
                    # 'display': 'inline-blo',
                    'id': 'salida_activo',
                }
            ),
            # 'orden_referencial': forms.Select(
            #     choices=medidas
            #     attrs={
            #         'class': 'form-control',
            #         'id': 'orden_referencial'
            #     }
            # ),
        }

class TrabajoFormLab(forms.ModelForm):
 
    def __init__(self, *args, **kwargs):
        super(TrabajoFormLab, self).__init__(*args, **kwargs)
        self.fields['tipo_pedi'].queryset = TipoPedido.objects.filter(estado=True).filter(tipo='L')
        self.fields['ubica'].queryset = activo_ubica.objects.filter(ubica_estado=1)
        # self.fields['orden_referencial'].label_from_instance = lambda obj: "N° de Orden %s" % (obj.numtrabajo)

    class Meta:
        model = OrdenesTrabajos
        fields = [
            'tipo_trabajo',
            'tipo_pedi',
            'departamento',
            'area',
            'usuario_solicita',
            # 'numproyecto',
            'justificacion_compra',
            'refer_orden',
            'orden_referencial',
            'fchsolicitatxt',
            'salida_activo',
            'ubica',
            'grupo',
        ]

        labels = {
            'tipo_trabajo': 'Tipo de Trabajo',
            'tipo_pedi': 'Tipo de Pedido',
            'departamento': 'Departamento',
            'area': 'Sector (En donde se realizará el trabajo)',
            # 'numproyecto': 'Seleccione el Proyecto',
            'justificacion_compra': 'Justificación de Compra',
            'refer_orden': 'Esta Asociado a una Orden Anterior?',
            'salida_activo': 'El Activo Sale de la Empresa?',
            'ubica': 'Ubicación',
            'grupo': 'Grupo',
        }

        widgets = {
            
            'tipo_trabajo': forms.RadioSelect(
                attrs={
                    'class': 'form-check-input',
                    'id': 'tipo_trabajo',
                }
            ),

            'tipo_pedi': forms.Select(
                attrs={
                    'class': 'form-control in col-md-6',
                    'id': 'tipo_pedido',
                    'required':'required',
                }
            ),

            'departamento': forms.Select(
                attrs={
                    'class':'form-control in',
                    'id':'departamento',
                    'required':'required',
                }
            ),

            'area': forms.Select(
                attrs={
                    'class': 'form-control in',
                    'id': 'area',
                    'required':'required',
                }
            ),

          
            'justificacion_compra': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'justificacion_compra',
                    'maxlength':2000,
                    'rows':4,
                }
            ),

            'refer_orden': forms.RadioSelect(
                attrs={
                    # 'class': 'form-check-input',
                    'id': 'refer_orden',
                    # 'type': 'radio',
                }
            ),

            'salida_activo': forms.RadioSelect(
                attrs={
                    'class': 'radio-inline',
                    # 'list-style': 'none',
                    # 'display': 'inline-blo',
                    'id': 'salida_activo',
                }
            ),
           
        }


class TrabajoAutoriForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrabajoAutoriForm, self).__init__(*args, **kwargs)
        self.fields['tipo_pedi'].queryset = TipoPedido.objects.filter(estado=True)
        # self.fields['ubica'].queryset = activo_ubica.objects.filter(ubica_estado=1)

    class Meta:
        model = OrdenesTrabajos
        fields = [
            'tipo_trabajo',
            'tipo_pedi',
            'departamento',
            'area',
            # 'numproyecto',
            'justificacion_compra',
            'refer_orden',
            'orden_referencial',
            'ubica',
            'grupo',
        ]

        labels = {
            'tipo_trabajo': 'Tipo de Trabajo',
            'tipo_pedi': 'Tipo de Pedido',
            'departamento': 'Departamento (Departamento de la persona solicitante)',
            'area': 'Sector (Escoger la ubicación en donde se colocará el insumo o se realizará el trabajo)',
            # 'numproyecto': 'Ingrese el Nombre de la Cuenta Contable (Proyecto)',
            'justificacion_compra': 'Justificación de Compra',
            'refer_orden': 'Esta Asociado a una Orden Anterior?',
            'ubica': 'Ubicación',
            'grupo': 'Grupo',
        }

        widgets = {
            
            'tipo_trabajo': forms.RadioSelect(
                attrs={
                    'class': 'form-check-input',
                    'id': 'tipo_trabajo',
                }
            ),

            'tipo_pedi': forms.Select(
                attrs={
                    'class': 'form-control in',
                    'id': 'tipo_pedido',
                    'required':'required',
                }
            ),

            'departamento': forms.Select(
                attrs={
                    'class':'form-control in',
                    'id':'departamento',
                    'required':'required',
                }
            ),

            'area': forms.Select(
                attrs={
                    'class': 'form-control in',
                    'id': 'area',
                    'required':'required',
                }
            ),

            # 'numproyecto': forms.TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         'id': 'numproyecto',
            #         'placeholder': 'Proyecto',
            #     }
            # ),

            'justificacion_compra': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'justificacion_compra',
                    'rows':4,
                }
            ),

            'refer_orden': forms.RadioSelect(
                attrs={
                    # 'class': 'form-check-input',
                    'id': 'refer_orden',
                }
            ),
        }


class TrabajoAutoriForm2(forms.ModelForm):
    class Meta:
        model = OrdenesTrabajos
        fields = [
             'tipo_pedi',
            # 'departamento',
            'area',
            # 'numproyecto',
            # 'justificacion_compra',
            # 'ubica',
        ]

        widgets = {
             'tipo_pedi': forms.TextInput(
                attrs={
                     'required': False,
                        'class':"form-control"
                 }
            )}



class DetTrForm(forms.ModelForm):
    class Meta:
        model = DetalleTrabajo
        fields = [
            'descripcion',
            'cantidad',
            'unimedida',
            'img_1',
            'img_2',
            'cotiza_Ref',
            'otros_doc',
        ]

        labels = {
            'descripcion': 'Descripción',
            'cantidad': 'Cantidad',
            'unimedida': 'Medida',
            'img_1': 'Imagen 1',
            'img_2': 'Imagen 2',
            'cotiza_Ref': 'Cotización Referencial',
            'otros_doc': 'Ingrese Otro Documento Que Necesite Adjuntar',
        }

        widgets = {
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control in',
                    'id': 'descripcion',
                    # 'placeholder': 'Ingrese el producto',
                    'required': 'required',
                    'rows':4,
                }
            ),

            'cantidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'cantidad',
                    'placeholder': 'Cantidad',
                    'value': 1,
                    'readonly':True,
                }
            ),

            'unimedida': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'unimedida',
                    'value': 'unidad',
                    'readonly': True
                }
            ),

            'img_1': forms.FileInput(
                attrs={
                    'class': 'form-control-file',
                    'accept': 'image/png, .jpeg, .jpg, image/gif',
                }
            ),

            'img_2': forms.FileInput(
                attrs={
                    'class': 'form-control-file',
                    'accept': 'image/png, .jpeg, .jpg, image/gif',
                }
            ),

            'cotiza_Ref': forms.FileInput(
                attrs={
                    'class': 'form-control-file',
                }
            ),

            'otros_doc': forms.FileInput(
                attrs={
                    'class': 'form-control-file',
                }
            ),
        }

class EditaDetTrForm(forms.ModelForm):
    class Meta:
        model = DetalleTrabajo
        fields = [
            'descripcion',
            'cantidad',
            'unimedida',
            'img_1',
            'img_2',
            'cotiza_Ref',
            'otros_doc',
        ]

        labels = {
            'descripcion': 'Descripción',
            'cantidad': 'Cantidad',
            'unimedida': 'Medida',
            'img_1': 'Imagen 1',
            'img_2': 'Imagen 2',
            'cotiza_Ref': 'Cotización Referencial',
            'otros_doc': 'Ingrese Otro Documento Que Necesite Adjuntar',
        }

        widgets = {
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control in',
                    'id': 'descripcion',
                    'placeholder': 'Ingrese el producto',
                    'required': 'required',
                    'rows':4,
                }
            ),

            'cantidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'cantidad',
                    'placeholder': 'Cantidad',
                    'value': 1,
                    'readonly':True,
                }
            ),

            'unimedida': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'unimedida',
                    'value': 'unidad',
                    'readonly': True
                }
            ),

            # 'otros_doc': forms.FileInput(
            #     attrs={
            #         'class': 'form-control-file',
            #     }
            # ),
        }

class EditaDetTrForm2(forms.ModelForm):
    class Meta:
        model = DetalleTrabajo
        fields = [
            'img_1',
            'img_2',
            'cotiza_Ref',
            'otros_doc',
        ]

class DetCotizaForm(forms.ModelForm):
    class Meta:
        model = CotizaTrabajo
        fields = [
            'id',
            'valor',
            'empresa_cotiza',
            'pdf_cotiza',
            'cotiza_seleccion',
        ]

        labels = {
            'id': 'Id',
            'valor': 'Valor',
            'empresa_cotiza': 'Proveedor',
            'pdf_cotiza': 'Cotización',
        }

        widgets = {
            'id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),

            'valor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),

            'empresa_cotiza': forms.Select(
                attrs={
                    'class': 'form-control',
                    # 'id': 'proveedor',
                }
            ),

            'cotiza_seleccion': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'type': 'checkbox',
                    'name': 'cotizacion'
                }
            ),

            'pdf_cotiza': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class DetCotizaForm2(forms.ModelForm):
    class Meta:
        model = CotizaTrabajo
        fields = [
            'id',
            'valor',
            'empresa_cotiza',
            'pdf_cotiza',
            'cotiza_seleccion',
        ]

        labels = {
            'id': 'Id',
            'valor': 'Valor',
            'empresa_cotiza': 'Proveedor',
            'pdf_cotiza': 'Cotización',
        }

        widgets = {
            'id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),

            'valor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),

            'empresa_cotiza': forms.Select(
                attrs={
                    'class': 'form-control',
                    # 'id': 'proveedor',
                }
            ),

            'cotiza_seleccion': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'type': 'checkbox',
                    'name': 'cotizacion'
                }
            ),

            'pdf_cotiza': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }

DetCotizaFormSet = inlineformset_factory(OrdenesTrabajos, CotizaTrabajo, form=DetCotizaForm, extra=3)

DetCotizaFormSet_LabCa = inlineformset_factory(OrdenesTrabajos, CotizaTrabajo, form=DetCotizaForm2, extra=1)


class IngresoTrabajos(forms.Form):
    ubica_nombre = forms.ModelChoiceField(
        label = 'Ubicación',
        queryset = activo_ubica.objects.all(),
        widget = forms.Select(
            attrs={
                'class': 'form-control',
                'onchange' : 'this.form.submit()', 
                'id':'ubica_nombre', 
                'required': 'true'
            }
        ),
    )

    departamento = forms.IntegerField(
        label = 'Departamento Solicitante',
        widget = forms.Select(
            attrs={
                'class':'form-control',
                'id':'departamento',
            }
        ),
    )
    
    area_nombre = forms.ModelChoiceField(
        label = 'Sector',
        queryset = activo_areas.objects.all(),
        widget = forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'area',
            }
        ),
    )

    tipo_pedi = forms.ChoiceField(
        label = 'Tipo de Pedido',
        choices = tipo_ped,
        widget = forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'tipo_pedido',
            }
        ),
    )

    numproyecto = forms.CharField(
        label = 'Ingrese el Nombre de la Cuena Contable (Proyecto)',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'numproyecto',
                'placeholder': 'Proyecto',
            }
        )
    )

    refer_orden = forms.ChoiceField(
        label = 'Esta Asociado a una Orden Anterior?',
        choices = orden_ref,
        widget = forms.RadioSelect(
            attrs={
                'class': 'radio-inline',
                'id': 'salida_activo',
            }
        ),
    )

    justificacion_compra = forms.CharField(
        label = 'Justificación de Compra',
        widget = forms.Textarea(
            attrs={
                'class': 'form-control',
                'id': 'justificacion_compra',
            }
        )
    )

    

    def __init__(self, *args, **kwargs):
        self._ubica_nombre = kwargs.pop('ubica_nombre', None)
        self._area_nombre = kwargs.pop('area_nombre', None)
        super(IngresoTrabajos, self).__init__(*args, **kwargs)
        # without the next line label_from_instance does NOT work
        self.fields['ubica_nombre'].queryset = activo_ubica.objects.all().order_by('id')
        self.fields['ubica_nombre'].label_from_instance = lambda obj: "%s" % (obj.ubica_nombre)
        # self.fields['proveedor1'].queryset= proveedor.objects.all()
        # self.fields['proveedor1'].label_from_instance = lambda obj: "%s" % (obj.nombre_empresa)
        self.fields['area_nombre'].queryset= activo_areas.objects.filter(area_ubica=self._ubica_nombre).order_by('area_nombre')
        self.fields['area_nombre'].label_from_instance = lambda obj: "%s" % (obj.area_nombre)

class PedidosMbaForm(forms.ModelForm):
    class Meta:
        model = PedidosMba
        fields = [
            'documentos',       
        ]

class Predocumentos(forms.ModelForm):
    class Meta:
        model = PreCotiza
        fields = [
            'archivos', 
            'seleccion',    
        ]
        widgets = {
            'seleccion':forms.CheckboxInput(attrs={}),
            
		}

class IngresoPagosForm(forms.ModelForm):
	class Meta:
		model = TrabajosPago

		fields = [
			'fch_genera',
            'fch_genera_txt',
            'origen',
            'numero',
			'documento',
            'usuario_solicita',
            'observaciones_adqui',
		]

		labels = {
			'origen':'Origen',
            'numero':'Numero de Pedido / Orden',
            'documento':'Seleccione el Archivo',
			'usuario_solicita':'Ingresado por',
            'observaciones_adqui':'Observaciones',
		}
		widgets = {
            'origen':forms.Select(attrs={'class':'form-control'}),
            'numero':forms.TextInput(attrs={'class':'form-control'}),
			'documento':forms.FileInput(attrs={'class':'form-control'}),
            'usuario_solicita':forms.TextInput(attrs={'class':'form-control'}),
            'observaciones_adqui':forms.Textarea(attrs={'class':'form-control', 'rows':4}),
		}

class cargaDoc(forms.ModelForm):
    class Meta:
        model = SolicitudesAdqui

        fields = [
            'docs',
        ]

class cargaComprobante(forms.ModelForm):
    class Meta:
        model = SolicitudesAdqui

        fields = [
            'comprobante',
        ]