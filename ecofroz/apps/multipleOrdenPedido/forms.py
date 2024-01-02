from django import forms
from django.forms.models import inlineformset_factory
from django.forms import modelformset_factory

from .models import OrdenesPedidosMulti, DetallePedidoMulti, CotizaPedidoMulti
from apps.activos.models import activo_areas, desc_activo, detalle_desc_activo

class OrdenMultiForm(forms.ModelForm):
    class Meta:
        model = OrdenesPedidosMulti
        fields = [
            'usuario_solicita',
            'departamento',
            'area',
            'numproyecto',
            'motivo_compra',
            'justificacion_compra',
            'reemplazo_accion',
            'reemplazo_observa',
            'cotiza_ref',
        ]

        labels = {
            'departamento': 'Departamento Solicitante',
            'area': 'Area Solicitante',
            'numproyecto': 'Proyecto',
            'motivo_compra': 'Motivo de Compra',
            'justificacion_compra': 'Justificación de Compra',
            'reemplazo_accion': 'Acción de Equipo Reemplazado',
            'reemplazo_observa': 'Observación de Reemplazo',
            'cotiza_ref': 'Cotización Referencial'
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

            'numproyecto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'numproyecto',
                    'placeholder': 'Proyecto',
                }
            ),

            'motivo_compra': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'motivo_compra',
                }
            ),

            'justificacion_compra': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'justificacion_compra',
                    'rows': 4,
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
                    'rows': 4,
                }
            ),

            'cotiza_ref':forms.FileInput(
                attrs={
                    'class': 'form-control-file',
                    'id': 'cotiza_ref',
                }
            ),
        }

class DetMultiForm(forms.ModelForm):
    class Meta:
        model = DetallePedidoMulti
        fields = [
            'tipoactivo',
            'descripcion',
            'cantidad',
            'unimedida',
            'tiempo_vida',
            'tiempo_tipo',
            'img_1',
        ]

        labels = {
            'tipoactivo': 'Tipo',
            'descripcion': 'Descripción',
            'cantidad': 'Cantidad',
            'tiempo_vida': 'Tiempo de Vida',
            'tiempo_tipo': 'Unidad',
            'img_1': 'Imagen 1',
        }

        widgets = {
            'tipoactivo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'tipoactivo',
                }
            ),

            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'descripcion',
                    'placeholder': 'Ingrese el producto',
                }
            ),

            'cantidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'cantidad',
                }
            ),

            'tiempo_vida': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'tiempo_vida',
                }
            ),

            'tiempo_tipo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'tiempo_tipo',
                }
            ),

            'img_1': forms.FileInput(
                attrs={
                    'class': 'form-control-file',
                    'accept': 'image/png, .jpeg, .jpg, image/gif',
                }
            ),
        }

DetMultiFormSet = modelformset_factory(DetallePedidoMulti, form=DetMultiForm, extra=1)

# class EditaForm(forms.ModelForm):
#     class Meta:
#         model = OrdenesPedidos
#         fields = [
#             'usuario_solicita',
#             'departamento',
#             'area',
#             'tipoactivo',
#             'tiempo_vida',
#             'tiempo_tipo',
#             'numproyecto',
#             'regimenespecial',
#             'motivo_compra',
#             'justificacion_compra',
#             'reemplazo_accion',
#             'reemplazo_observa',
#         ]

#         labels = {
#             'departamento': 'Departamento Solicitante',
#             'area': 'Area Solicitante',
#             'tipoactivo': 'Tipo',
#             'tiempo_vida': 'Tiempo de vida',
#             'tiempo_tipo': 'Unidad',
#             'numproyecto': 'Proyecto',
#             'regimenespecial': 'Regimen Especial',
#             'motivo_compra': 'Motivo de Compra',
#             'justificacion_compra': 'Justificación de Compra',
#             'reemplazo_accion': 'Acción de Equipo Reemplazado',
#             'reemplazo_observa': 'Observación de Reemplazo',
#         }

#         widgets = {
#             'departamento': forms.Select(
#                 attrs={
#                     'class':'form-control',
#                     'id':'departamento',
#                 }
#             ),

#             'area': forms.Select(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'area',
#                 }
#             ),

#             'tipoactivo': forms.Select(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'tipoactivo',
#                 }
#             ),

#             'tiempo_vida': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'tiempo_vida',
#                     'placeholder': 'Tiempo de vida',
#                 }
#             ),

#             'tiempo_tipo': forms.Select(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'tiempo_tipo',
#                 }
#             ),

#             'numproyecto': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'numproyecto',
#                     'placeholder': 'Proyecto',
#                 }
#             ),

#             'regimenespecial': forms.CheckboxInput(
#                 attrs={
#                     'class': 'form-check-input',
#                     'id': 'regimenespecial',
#                     'type': 'checkbox',
#                 }
#             ),

#             'motivo_compra': forms.Select(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'motivo_compra',
#                 }
#             ),

#             'justificacion_compra': forms.Textarea(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'justificacion_compra',
#                 }
#             ),

#             'reemplazo_accion':forms.Select(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'reemplazo_accion',
#                 }
#             ),

#             'reemplazo_observa':forms.Textarea(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'reemplazo_accion',
#                     'placeholder': 'Observación del reemplazado, Referencia de ubicación o custodio del equipo a ser reemplazado',
#                 }
#             ),
#         }

# class DetEditaForm(forms.ModelForm):
#     class Meta:
#         model = DetallePedido
#         fields = [
#             'descripcion',
#             'cantidad',
#             'unimedida',
#             'img_1',
#             'img_2',
#         ]

#         labels = {
#             'descripcion': 'Descripción',
#             'cantidad': 'Cantidad',
#             'img_1': 'Imagen 1',
#             'img_2': 'Imagen 2',
#         }

#         widgets = {
#             'descripcion': forms.Textarea(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'descripcion',
#                     'placeholder': 'Ingrese el producto',
#                 }
#             ),

#             'cantidad': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'cantidad',
#                     'placeholder': 'Cantidad',
#                     'value': 1,
#                     'readonly':True,
#                 }
#             ),

#             'unimedida': forms.Select(
#                 attrs={

#                     'class': 'form-control',
#                     'id': 'unimedida',
#                     'value': 'unidad',
#                     'readonly': True
#                 }
#             ),
#         }
    
# class ApruebaForm(forms.ModelForm):
#     class Meta:
#         model = OrdenesPedidos
#         fields = [
#             'usuario_solicita',
#             'departamento',
#             'area',
#             'tipoactivo',
#             'tiempo_vida',
#             'tiempo_tipo',
#             'numproyecto',
#             'regimenespecial',
#             'aprobado',
#         ]

#         labels = {
#             'departamento': 'Departamento Solicitante',
#             'area': 'Area Solicitante',
#             'tipoactivo': 'Categoría',
#             'tiempo_vida': 'Tiempo de vida',
#             'tiempo_tipo': 'Unidad',
#             'numproyecto': 'Proyecto',
#             'regimenespecial': 'Regimen Especial',
#             'aprobado': 'Aprobado'
#         }

#         widgets = {
#             'departamento': forms.Select(
#                 attrs={
#                     'class':'form-control',
#                     'id':'departamento',
#                     'disabled':'disabled',
#                 }
#             ),

#             'area': forms.Select(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'area',
#                     'disabled':'disabled',
#                 }
#             ),

#             'tipoactivo': forms.Select(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'tipoactivo',
#                     'disabled':'disabled',
#                 }
#             ),

#             'tiempo_vida': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'tiempo_vida',
#                     'placeholder': 'Tiempo de vida',
#                     'disabled':'disabled',
#                 }
#             ),

#             'tiempo_tipo': forms.Select(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'tiempo_tipo',
#                     'disabled':'disabled',
#                 }
#             ),

#             'numproyecto': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'numproyecto',
#                     'placeholder': 'Proyecto',
#                     'disabled':'disabled',
#                 }
#             ),

#             'regimenespecial': forms.CheckboxInput(
#                 attrs={
#                     'class': 'form-check-input',
#                     'id': 'regimenespecial',
#                     'type': 'checkbox',
#                     'disabled':'disabled',
#                 }
#             ),

#             'aprobado': forms.Select(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'aprobado',
#                 }
#             )
#         }

# class DetApruebaForm(forms.ModelForm):
#     class Meta:
#         model = DetallePedido
#         fields = [
#             'descripcion',
#             'cantidad',
#             'unimedida',
#             'img_1',
#             'img_2',
#         ]

#         labels = {
#             'descripcion': 'Descripción',
#             'cantidad': 'Cantidad',
#             'img_1': 'Imagen 1',
#             'img_2': 'Imagen 2',
#         }

#         widgets = {
#             'descripcion': forms.Textarea(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'descripcion',
#                     'placeholder': 'Ingrese el producto',
#                     'disabled':'disabled',
#                 }
#             ),

#             'cantidad': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'cantidad',
#                     'placeholder': 'Cantidad',
#                     'disabled':'disabled',
#                 }
#             ),

#             'unimedida': forms.Select(
#                 attrs={

#                     'class': 'form-control',
#                     'id': 'unimedida',
#                     'disabled':'disabled',
#                 }
#             ),

#             'img_1': forms.FileInput(
#                 attrs={
#                     'class': 'form-control-file',
#                     'accept': 'image/png, .jpeg, .jpg, image/gif',
#                 }
#             ),

#             'img_2': forms.FileInput(
#                 attrs={
#                     'class': 'form-control-file',
#                     'accept': 'image/png, .jpeg, .jpg, image/gif',
#                 }
#             ),
#         }

# class CotizaForm(forms.ModelForm):
#     class Meta:
#         model = OrdenesPedidos
#         fields = [
#             'usuario_solicita',
#             'departamento',
#             'area',
#             'tipoactivo',
#             'tiempo_vida',
#             'tiempo_tipo',
#             'numproyecto',
#             'regimenespecial',
#         ]

#         labels = {
#             'departamento': 'Departamento Solicitante',
#             'area': 'Area Solicitante',
#             'tipoactivo': 'Categoría',
#             'tiempo_vida': 'Tiempo de vida',
#             'tiempo_tipo': 'Unidad',
#             'numproyecto': 'Proyecto',
#             'regimenespecial': 'Regimen Especial',
#         }

#         widgets = {
#             'departamento': forms.Select(
#                 attrs={
#                     'class':'form-control',
#                     'id':'departamento',
#                 }
#             ),

#             'area': forms.Select(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'area',
#                 }
#             ),

#             'tipoactivo': forms.Select(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'tipoactivo',
#                 }
#             ),

#             'tiempo_vida': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'tiempo_vida',
#                     'placeholder': 'Tiempo de vida',
#                 }
#             ),

#             'tiempo_tipo': forms.Select(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'tiempo_tipo',
#                 }
#             ),

#             'numproyecto': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'numproyecto',
#                     'placeholder': 'Proyecto',
#                 }
#             ),

#             'regimenespecial': forms.CheckboxInput(
#                 attrs={
#                     'class': 'form-check-input',
#                     'id': 'regimenespecial',
#                     'type': 'checkbox',
#                 }
#             )
#         }

# class DetCotizaForm(forms.ModelForm):
#     class Meta:
#         model = CotizaPedido
#         fields = [
#             'id',
#             'valor',
#             'empresa_cotiza',
#             'pdf_cotiza',
#             'cotiza_seleccion',
#         ]

#         labels = {
#             'id': 'Id',
#             'valor': 'Valor',
#             'empresa_cotiza': 'Proveedor',
#             'pdf_cotiza': 'Cotización',
#         }

#         widgets = {
#             'id': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             ),

#             'valor': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             ),

#             'empresa_cotiza': forms.Select(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'proveedor',
#                 }
#             ),

#             'cotiza_seleccion': forms.CheckboxInput(
#                 attrs={
#                     'class': 'form-control',
#                     'type': 'checkbox',
#                     'name': 'cotizacion'
#                 }
#             ),
#         }

# DetCotizaFormSet = inlineformset_factory(OrdenesPedidos, CotizaPedido, form=DetCotizaForm, extra=3)

# class CodificaForm(forms.ModelForm):
#     class Meta:
#         model = desc_activo
#         fields = [
# 			'activo_nomenclatura',
# 			'activo_codigo',
# 			'activo_grupo',
# 			'activo_tipo',
# 			'activo_descripcion',
# 			'activo_ubica',
# 			'activo_depar',
# 			'activo_area',
#             'activo_valor',
#             'orden_de_pedido',
# 			'numero_factura',
# 			'cod_activo_padre',
# 		]
		
#         labels = {
# 			'activo_nomenclatura':'Nomenclatura',
# 			'activo_codigo':'Código Activo',
# 			'activo_grupo':'Grupo',
# 			'activo_tipo':'Tipo Activo',
# 			'activo_descripcion':'Descripcion',
# 			'activo_ubica':'Ubicación',
# 			'activo_depar':'Departamento',
# 			'activo_area':'Area',
#             'activo_valor':'Valor',
#             'orden_de_pedido':'No Orden de Pedido',
# 			'numero_factura':'Numero Factura',
# 			'cod_activo_padre':'Codigo de Activo Padre',
						
# 		}
# #Son los que se van a pintar como etiquetas de HTML

#         widgets = {
# 			'activo_nomenclatura':forms.Select(attrs={'class':'form-control', 'hidden':True}),
# 			'activo_codigo':forms.TextInput(attrs={'class':'form-control'}),
# 			'activo_grupo':forms.Select(attrs={'class':'form-control', 'disabled':True}),
# 			'activo_tipo':forms.Select(attrs={'class':'form-control', 'disabled':True}),
# 			'activo_descripcion':forms.Textarea(attrs={'class':'form-control', 'readonly':True}),
# 			#'activo_ubica':forms.CheckboxSelectMultiple(),
# 			#'activo_ubica':forms.RadioSelect(),
# 			'activo_ubica':forms.Select(attrs={'class':'form-control'}),
# 			'activo_depar':forms.Select(attrs={'class':'form-control', 'disabled':True}),
# 			'activo_area':forms.Select(attrs={'class':'form-control', 'disabled':True}),
# 			'activo_valor':forms.TextInput(attrs={'class':'form-control'}),
#     		'orden_de_pedido':forms.TextInput(attrs={'class':'form-control'}),
#    	  		'numero_factura':forms.TextInput(attrs={'class':'form-control'}),
#    			'cod_activo_padre':forms.Select(attrs={'class':'form-control'}),
# 			}
        
# class CodificaFormDet(forms.ModelForm):
# 	class Meta:
# 		model = detalle_desc_activo

# 		fields = [
# 			'desc_activo_marca',
#             'desc_activo_num_serie',
#             'desc_activo_modelo',
#             'desc_activo_proveedor',
# 			'desc_activo_usuario_registra',
# 		]

# 		labels = {
# 			'desc_activo_marca':'Marca',
#             'desc_activo_num_serie':'Número de Serie',
#             'desc_activo_modelo':'Modelo',
#             'desc_activo_proveedor':'Proveedor',
# 			'desc_activo_usuario_registra':'Ingresado por',
# 		}
# 		widgets = {
# 			'desc_activo_marca':forms.TextInput(attrs={'class':'form-control'}),
#             'desc_activo_num_serie':forms.TextInput(attrs={'class':'form-control'}),
#             'desc_activo_modelo':forms.TextInput(attrs={'class':'form-control'}),
#             'desc_activo_proveedor':forms.TextInput(attrs={'class':'form-control'}),
# 			'desc_activo_usuario_registra':forms.TextInput(attrs={'class':'form-control', 'hidden':True}),
# 		}
