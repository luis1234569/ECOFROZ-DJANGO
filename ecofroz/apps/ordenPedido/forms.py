from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms.models import inlineformset_factory

from .models import OrdenesPedidos, DetallePedido, CotizaPedido, OrdenesPago, PreCotiza
from apps.activos.models import activo_areas, desc_activo, detalle_desc_activo
from apps.parametrosGlobales.models import proyectos_contabilidad
from apps.usuarios.models import User

class selectAsignadoa(forms.Form):
    asignacion = forms.ModelMultipleChoiceField(required=False,queryset= User.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    def __init__(self, *args, **kwargs):
        super(selectAsignadoa, self).__init__(*args, **kwargs)
        self.fields['asignacion'].queryset = User.objects.filter(consulta_experta=True).order_by('last_name')
        self.fields['asignacion'].label_from_instance = lambda obj: "%s" % (obj.last_name + ' ' + obj.first_name)
        


class nombreProyectoForm(forms.Form):
    nombre_proyecto = forms.ModelChoiceField(queryset = proyectos_contabilidad.objects.all(), widget = forms.Select(attrs={ 'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(nombreProyectoForm, self).__init__(*args, **kwargs)
        self.fields['nombre_proyecto'].queryset = proyectos_contabilidad.objects.filter(activo=True).order_by('nombre_proyecto')
        self.fields['nombre_proyecto'].label_from_instance = lambda obj: "%s" % (obj.nombre_proyecto)
        self.fields['nombre_proyecto'].required = False



class OrdenForm(forms.ModelForm):
    class Meta:
        model = OrdenesPedidos
        fields = [
            'usuario_solicita',
            'departamento',
            'area',
            'tipoactivo',
            'tiempo_vida',
            'tiempo_tipo',
            # 'numproyecto',
            'regimenespecial',
            'motivo_compra',
            'justificacion_compra',
            'reemplazo_accion',
            'reemplazo_observa',
            'ubica',
            'grupo',
            'parte_activo',
        
        ]

        labels = {
            'departamento': 'Departamento (Departamento de la persona que solicita)',
            'area': 'Sector (Escoger la ubicación en donde se colocará el activo)',
            'tipoactivo': 'Tipo',
            'tiempo_vida': 'Tiempo de vida',
            'tiempo_tipo': 'Unidad',
            # 'numproyecto': 'Cuenta Contable (Para Proyectos únicamente)',
            'regimenespecial': 'Regimen Especial',
            'motivo_compra': 'Motivo de Compra',
            'justificacion_compra': 'Justificación de Compra',
            'reemplazo_accion': 'Acción de Equipo Reemplazado',
            'reemplazo_observa': 'Observación de Reemplazo',
            'ubica': 'Ubicación',
            'grupo': 'Grupo',
            'parte_activo': 'Marque si el activo es parte de otro activo madre',
            
        }

        widgets = {
            
            'departamento': forms.Select(
                attrs={
                    'class':'form-control in',
                    'id':'departamento',
                    'required':'required'
                }
            ),

            'area': forms.Select(
                attrs={
                    'class': 'form-control in',
                    'id': 'area',
                    'required':'required',
                }
            ),

            'tipoactivo': forms.Select(
                attrs={
                    'class': 'form-control in',
                    'id': 'tipoactivo',
                    'required':'required',
                }
            ),

            'tiempo_vida': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'tiempo_vida',
                    'placeholder': 'Tiempo de vida',
                    'required':'required',
                }
            ),

            'tiempo_tipo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'tiempo_tipo',
                    'required':'required',
                }
            ),

            # 'numproyecto': forms.TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         'id': 'numproyecto',
            #         'placeholder': 'Cuenta Contable',
            #     }
            # ),

            'regimenespecial': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'id': 'regimenespecial',
                    'type': 'checkbox',
                }
            ),

            'motivo_compra': forms.Select(
                attrs={
                    'class': 'form-control in',
                    'id': 'motivo_compra',
                    'required':'required',
                }
            ),

            'justificacion_compra': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'justificacion_compra',
                    'rows':5,
                }
            ),

            'reemplazo_accion':forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'reemplazo_accion',
                }
            ),

            'reemplazo_observa':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'reemplazo_accion',
                    'placeholder': 'Observación del reemplazado, Referencia de ubicación o custodio del equipo a ser reemplazado',
                    'rows':5,
                }
            ),

            'parte_activo':forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'id': 'regimenespecial',
                    'type': 'checkbox',
                }
            ),

            # 'ubica':forms.Select(
            #     attrs={
            #         'class': 'form-control',
            #         'id': 'ubica',
            #     }
            # ),
        }

class DetForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
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
            'otros_doc':'Otros Documentos',
        }

        widgets = {
            'descripcion': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'id':'descripcion',
                    'required':'required',
                    'rows':5,
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

class EditaForm(forms.ModelForm):
    class Meta:
        model = OrdenesPedidos
        fields = [
            'departamento',
            'area',
            'tipoactivo',
            'tiempo_vida',
            'tiempo_tipo',
            # 'numproyecto',
            'regimenespecial',
            'motivo_compra',
            'justificacion_compra',
            'reemplazo_accion',
            'reemplazo_observa',
            'ubica',
            'grupo',
            'parte_activo',
            'codigo_activo_reemplazado',
        ]

        labels = {
            'departamento': 'Departamento (Departamento de la persona solicitante)',
            'area': 'Sector (Escoger la ubicación en donde se colocará el activo)',
            'tipoactivo': 'Tipo',
            'tiempo_vida': 'Tiempo de vida',
            'tiempo_tipo': 'Unidad',
            # 'numproyecto': 'Proyecto',
            'regimenespecial': 'Regimen Especial',
            'motivo_compra': 'Motivo de Compra',
            'justificacion_compra': 'Justificación de Compra',
            'reemplazo_accion': 'Acción de Equipo Reemplazado',
            'reemplazo_observa': 'Observación de Reemplazo',
            'ubica': 'Ubicación',
            'grupo': 'Grupo',
            'parte_activo': 'Marque si el activo es parte de otro activo madre',
            'codigo_activo_reemplazado':'Código de Activo a ser reemplazado'
        }

        widgets = {
            'departamento': forms.Select(
                attrs={
                    'class':'form-control in',
                    'id':'departamento',
                    'required':'required'
                }
            ),

            'area': forms.Select(
                attrs={
                    'class': 'form-control in',
                    'id': 'area',
                    'required':'required'
                }
            ),

            'tipoactivo': forms.Select(
                attrs={
                    'class': 'form-control in',
                    'id': 'tipoactivo',
                    'required':'required',
                    
                }
            ),

            'tiempo_vida': forms.TextInput(
                attrs={
                    'class': 'form-control in',
                    'id': 'tiempo_vida',
                    'placeholder': 'Tiempo de vida',
                    'required':'required',
                }
            ),

            'tiempo_tipo': forms.Select(
                attrs={
                    'class': 'form-control in',
                    'id': 'tiempo_tipo',
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

            'regimenespecial': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'id': 'regimenespecial',
                    'type': 'checkbox',
                }
            ),

            'motivo_compra': forms.Select(
                attrs={
                    'class': 'form-control in',
                    'id': 'motivo_compra',
                    'required':'required',
                }
            ),

            'codigo_activo_reemplazado': forms.TextInput(
                attrs={
                    'class': 'form-control in',
                    'id': 'activo_reemplazado',
                    
                }
            ),

            'justificacion_compra': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'id':'justificacion_compra',
                    'rows':5,
                
                }
            ),

            'reemplazo_accion':forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'reemplazo_accion',
                }
            ),

            'reemplazo_observa':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'reemplazo_accion',
                    'placeholder': 'Observación del reemplazado, Referencia de ubicación o custodio del equipo a ser reemplazado',
                    'rows':5,
                }
            ),

            'parte_activo':forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'id': 'regimenespecial',
                    'type': 'checkbox',
                }
            ),
        }

class DetEditaForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = [
            'descripcion',
            'cantidad',
            'unimedida',
            'img_1',
            'img_2',
            'cotiza_Ref',
        ]

        labels = {
            'descripcion': 'Descripción',
            'cantidad': 'Cantidad',
            'img_1': 'Imagen 1',
            'img_2': 'Imagen 2',
            'cotiza_Ref': 'Cotización Referencial'
        }

        widgets = {
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control in',
                    'id': 'descripcion',
                    'placeholder': 'Ingrese el producto',
                    'required':'required',
                    'rows':5,
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

            'unimedida': forms.Select(
                attrs={

                    'class': 'form-control',
                    'id': 'unimedida',
                    'value': 'unidad',
                    'readonly': True
                }
            ),

            # 'img_1': forms.FileInput(
            #     attrs={
            #         'class': 'form-control-file',
            #         'accept': 'image/png, .jpeg, .jpg, image/gif',
            #     }
            # ),

            # 'img_2': forms.FileInput(
            #     attrs={
            #         'class': 'form-control-file',
            #         'accept': 'image/png, .jpeg, .jpg, image/gif',
            #     }
            # ),

            # 'cotiza_Ref': forms.FileInput(
            #     attrs={
            #         'class': 'form-control-file',
            #     }
            # ),
        }
    
class ApruebaForm(forms.ModelForm):
    class Meta:
        model = OrdenesPedidos
        fields = [
            'usuario_solicita',
            'departamento',
            'area',
            'tipoactivo',
            'tiempo_vida',
            'tiempo_tipo',
            'numproyecto',
            'regimenespecial',
            'aprobado',
        ]

        labels = {
            'departamento': 'Departamento (Escoger el departamento de la persona solicitante)',
            'area': 'Sector (Escoger la ubicación en donde se colocará el activo)',
            'tipoactivo': 'Categoría',
            'tiempo_vida': 'Tiempo de vida',
            'tiempo_tipo': 'Unidad',
            'numproyecto': 'Proyecto',
            'regimenespecial': 'Regimen Especial',
            'aprobado': 'Aprobado'
        }

        widgets = {
            'departamento': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'departamento',
                    'disabled':'disabled',
                }
            ),

            'area': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'area',
                    'disabled':'disabled',
                }
            ),

            'tipoactivo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'tipoactivo',
                    'disabled':'disabled',
                }
            ),

            'tiempo_vida': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'tiempo_vida',
                    'placeholder': 'Tiempo de vida',
                    'disabled':'disabled',
                }
            ),

            'tiempo_tipo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'tiempo_tipo',
                    'disabled':'disabled',
                }
            ),

            'numproyecto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'numproyecto',
                    'placeholder': 'Proyecto',
                    'disabled':'disabled',
                }
            ),

            'regimenespecial': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'id': 'regimenespecial',
                    'type': 'checkbox',
                    'disabled':'disabled',
                }
            ),

            'aprobado': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'aprobado',
                }
            )
        }

class DetApruebaForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = [
            'descripcion',
            'cantidad',
            'unimedida',
            'img_1',
            'img_2',
            'cotiza_Ref',
        ]

        labels = {
            'descripcion': 'Descripción',
            'cantidad': 'Cantidad',
            'img_1': 'Imagen 1',
            'img_2': 'Imagen 2',
            'cotiza_Ref': 'Cotización Referencial',
        }

        widgets = {
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'descripcion',
                    'placeholder': 'Ingrese el producto',
                    'disabled':'disabled',
                }
            ),

            'cantidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'cantidad',
                    'placeholder': 'Cantidad',
                    'disabled':'disabled',
                }
            ),

            'unimedida': forms.Select(
                attrs={

                    'class': 'form-control',
                    'id': 'unimedida',
                    'disabled':'disabled',
                }
            ),

            # 'img_1': forms.FileInput(
            #     attrs={
            #         'class': 'form-control-file',
            #         'accept': 'image/png, .jpeg, .jpg, image/gif',
            #     }
            # ),

            # 'img_2': forms.FileInput(
            #     attrs={
            #         'class': 'form-control-file',
            #         'accept': 'image/png, .jpeg, .jpg, image/gif',
            #     }
            # ),

            # 'cotiza_Ref': forms.FileInput(
            #     attrs={
            #         'class': 'form-control-file',
            #     }
            # ),
        }

class CotizaForm(forms.ModelForm):
    class Meta:
        model = OrdenesPedidos
        fields = [
            'usuario_solicita',
            'departamento',
            'area',
            'tipoactivo',
            'tiempo_vida',
            'tiempo_tipo',
            'numproyecto',
            'regimenespecial',
        ]

        labels = {
            'departamento': 'Departamento Solicitante',
            'area': 'Sector',
            'tipoactivo': 'Categoría',
            'tiempo_vida': 'Tiempo de vida',
            'tiempo_tipo': 'Unidad',
            'numproyecto': 'Proyecto',
            'regimenespecial': 'Regimen Especial',
        }

        widgets = {
            'departamento': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'departamento',
                }
            ),

            'area': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'area',
                }
            ),

            'tipoactivo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'tipoactivo',
                }
            ),

            'tiempo_vida': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'tiempo_vida',
                    'placeholder': 'Tiempo de vida',
                }
            ),

            'tiempo_tipo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'tiempo_tipo',
                }
            ),

            'numproyecto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'numproyecto',
                    'placeholder': 'Proyecto',
                }
            ),

            'regimenespecial': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'id': 'regimenespecial',
                    'type': 'checkbox',
                }
            )
        }

class DetCotizaForm(forms.ModelForm):
    class Meta:
        model = CotizaPedido
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
        }

DetCotizaFormSet = inlineformset_factory(OrdenesPedidos, CotizaPedido, form=DetCotizaForm, extra=3)

class CodificaForm(forms.ModelForm):
    class Meta:
        model = desc_activo
        fields = [
			'activo_codigo',
			'activo_grupo',
			'activo_tipo',
			'activo_descripcion',
			'activo_ubica',
			'activo_depar',
			'activo_area',
            'activo_valor',
            'orden_de_pedido',
			'numero_factura',
			'cod_activo_padre',
            'activo_valor_compra',
            'grabado',
		]
		
        labels = {
			'activo_codigo':'Código Activo',
			'activo_grupo':'Grupo',
			'activo_tipo':'Tipo Activo',
			'activo_descripcion':'Descripcion',
			'activo_ubica':'Ubicación',
			'activo_depar':'Departamento',
			'activo_area':'Sector',
            'activo_valor':'Valor',
            'orden_de_pedido':'No Orden de Pedido',
			'numero_factura':'Numero Factura',
			'cod_activo_padre':'Codigo de Activo Padre',
            'activo_valor_compra':'Valor de Compra',
            'grabado':'Identificado',
						
		}
#Son los que se van a pintar como etiquetas de HTML

        widgets = {
			'activo_codigo':forms.TextInput(attrs={'class':'form-control', 'hidden':False, 'readonly':True}),
			'activo_grupo':forms.Select(attrs={'class':'form-control', 'hidden':False, 'readonly':True}),
			'activo_tipo':forms.Select(attrs={'class':'form-control', 'hidden':False, 'readonly':True}),
			'activo_descripcion':forms.Textarea(attrs={'class':'form-control', 'hidden':False, 'readonly':True}),
			#'activo_ubica':forms.CheckboxSelectMultiple(),
			#'activo_ubica':forms.RadioSelect(),
			'activo_ubica':forms.Select(attrs={'class':'form-control', 'hidden':False, 'readonly':True}),
			'activo_depar':forms.Select(attrs={'class':'form-control', 'hidden':False, 'readonly':True}),
			'activo_area':forms.Select(attrs={'class':'form-control', 'hidden':False, 'readonly':True}),
			'activo_valor':forms.TextInput(attrs={'class':'form-control', 'hidden':False, 'readonly':True}),
    		'orden_de_pedido':forms.TextInput(attrs={'class':'form-control', 'hidden':False, 'readonly':True}),
   	  		'numero_factura':forms.TextInput(attrs={'class':'form-control', 'hidden':False, 'readonly':True}),
   			'cod_activo_padre':forms.Select(attrs={'class':'form-control', 'hidden':False, 'readonly':True}),
            'activo_valor_compra':forms.TextInput(attrs={'class':'form-control', 'hidden':False, 'readonly':True}),
            'grabado':forms.Select(attrs={'class':'form-control', 'hidden':False}),
			}
        
class CodificaFormDet(forms.ModelForm):
	class Meta:
		model = detalle_desc_activo

		fields = [
			'desc_activo_marca',
            'desc_activo_num_serie',
            'desc_activo_modelo',
            'desc_activo_proveedor',
			'desc_activo_usuario_registra',
            'desc_activo_fecha_ingre',
            'desc_activo_codigo_mba',
		]

		labels = {
			'desc_activo_marca':'Marca',
            'desc_activo_num_serie':'Número de Serie',
            'desc_activo_modelo':'Modelo',
            'desc_activo_proveedor':'Proveedor',
			'desc_activo_usuario_registra':'Ingresado por',
            'desc_activo_fecha_ingre':'Fecha de Compra',
            'desc_activo_codigo_mba':'Código MBA',
		}
		widgets = {
			'desc_activo_marca':forms.TextInput(attrs={'class':'form-control', 'hidden':False}),
            'desc_activo_num_serie':forms.TextInput(attrs={'class':'form-control', 'hidden':False}),
            'desc_activo_modelo':forms.TextInput(attrs={'class':'form-control', 'hidden':False}),
            'desc_activo_proveedor':forms.TextInput(attrs={'class':'form-control', 'hidden':False}),
			'desc_activo_usuario_registra':forms.TextInput(attrs={'class':'form-control', 'hidden':False}),
            'desc_activo_fecha_ingre':forms.TextInput(attrs={'class':'form-control'}),
            'desc_activo_codigo_mba':forms.TextInput(attrs={'class':'form-control'}),
		}


class EditaCodificaForm(forms.ModelForm):
    class Meta:
        model = desc_activo
        fields = [
			'activo_nomenclatura',
			'activo_codigo',
			'activo_grupo',
			'activo_tipo',
			'activo_descripcion',
			'activo_ubica',
			'activo_depar',
			'activo_area',
            'activo_valor',
            'orden_de_pedido',
			'numero_factura',
			'cod_activo_padre',
		]
		
        labels = {
			'activo_nomenclatura':'Nomenclatura',
			'activo_codigo':'Código Activo',
			'activo_grupo':'Grupo',
			'activo_tipo':'Tipo Activo',
			'activo_descripcion':'Descripcion',
			'activo_ubica':'Ubicación',
			'activo_depar':'Departamento',
			'activo_area':'Sector',
            'activo_valor':'Valor',
            'orden_de_pedido':'No Orden de Pedido',
			'numero_factura':'Numero Factura',
			'cod_activo_padre':'Codigo de Activo Padre',
						
		}
#Son los que se van a pintar como etiquetas de HTML

        widgets = {
			'activo_nomenclatura':forms.Select(attrs={'class':'form-control', 'hidden':True}),
			'activo_codigo':forms.TextInput(attrs={'class':'form-control', 'disabled':True}),
			'activo_grupo':forms.Select(attrs={'class':'form-control', 'disabled':True}),
			'activo_tipo':forms.Select(attrs={'class':'form-control', 'disabled':True}),
			'activo_descripcion':forms.Textarea(attrs={'class':'form-control', 'disabled':True}),
			#'activo_ubica':forms.CheckboxSelectMultiple(),
			#'activo_ubica':forms.RadioSelect(),
			'activo_ubica':forms.Select(attrs={'class':'form-control', 'disabled':True}),
			'activo_depar':forms.Select(attrs={'class':'form-control', 'disabled':True}),
			'activo_area':forms.Select(attrs={'class':'form-control', 'disabled':True}),
			'activo_valor':forms.TextInput(attrs={'class':'form-control', 'disabled':True}),
    		'orden_de_pedido':forms.TextInput(attrs={'class':'form-control', 'disabled':True}),
   	  		'numero_factura':forms.TextInput(attrs={'class':'form-control', 'disabled':True}),
   			'cod_activo_padre':forms.Select(attrs={'class':'form-control', 'disabled':True}),

			}

class EditaCodificaFormDet(forms.ModelForm):
	class Meta:
		model = detalle_desc_activo

		fields = [
			'desc_activo_marca',
            'desc_activo_num_serie',
            'desc_activo_modelo',
            'desc_activo_proveedor',
			'desc_activo_usuario_registra',
		]

		labels = {
			'desc_activo_marca':'Marca',
            'desc_activo_num_serie':'Número de Serie',
            'desc_activo_modelo':'Modelo',
            'desc_activo_proveedor':'Proveedor',
			'desc_activo_usuario_registra':'Ingresado por',
		}
		widgets = {
			'desc_activo_marca':forms.TextInput(attrs={'class':'form-control'}),
            'desc_activo_num_serie':forms.TextInput(attrs={'class':'form-control'}),
            'desc_activo_modelo':forms.TextInput(attrs={'class':'form-control'}),
            'desc_activo_proveedor':forms.TextInput(attrs={'class':'form-control', 'disabled':True}),
			'desc_activo_usuario_registra':forms.TextInput(attrs={'class':'form-control', 'hidden':True}),
		}

class IngresoPagosForm(forms.ModelForm):
	class Meta:
		model = OrdenesPago

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
            'observaciones_adqui':forms.Textarea(attrs={'class':'form-control'}),
		}

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