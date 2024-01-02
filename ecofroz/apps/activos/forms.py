from django import forms
from .models import desc_activo,detalle_desc_activo, activo_nomenclatura, salida_activos,activo_tipo, \
activo_ubica,activo_areas,Imagenes
from django.db.models import Q

BOOL_CHOICE = [
    (False, 'NO'),
	(True,'SI'),
]

class ActivoForm(forms.ModelForm):
	class Meta:
		model = desc_activo
		fields = ('id',)

class ImageForm(forms.ModelForm):
	class Meta:
		model = Imagenes
		fields = ('imagen_activo',)
		


class NoEncontradosForm(forms.Form):
	descripcion = forms.CharField(label='Observaciones', max_length=2000,widget=forms.Textarea)
	grabado = forms.BooleanField(label='El Activo se encuentra grabado?',required=True,widget = forms.Select(attrs={'class':'form-control', 'id':'grabado', 'required': 'true'},choices=BOOL_CHOICE))
	usuario_registra = forms.CharField(label='Usuario Registra',max_length=150)
	
	

class UbicacionesBodegaForm(forms.Form):
	ubicacion = forms.ModelChoiceField(label='Por Ubicación',queryset = activo_ubica.objects.all(),widget = forms.Select(attrs={'onchange' : 'this.form.submit()','class':'select-box', 'id':'ubicacion', 'required': 'false'}))

	def __init__(self,*args,**kwargs):
		super(UbicacionesBodegaForm, self).__init__(*args,**kwargs)
		self.fields['ubicacion'].queryset = activo_ubica.objects.filter(Q(id=9) | Q(id=4)).order_by('ubica_nombre')
		self.fields['ubicacion'].label_from_instance = lambda obj: "%s" % (obj.ubica_nombre)


class RegistroForm(forms.ModelForm):
	
	class Meta:
		model = desc_activo

#Campos del modelo que vamos a utilizar en el formulario
		fields = [
			'activo_nomenclatura',
			'activo_codigo',
			'activo_grupo',
			'activo_tipo',
			'activo_descripcion',
			'activo_ubica',
			'activo_depar',
			'activo_area',
			'activo_subsec',
            'activo_valor',
			'activo_valor_compra',
            'orden_de_pedido',
			'numero_factura',
			'cod_activo_padre',
			'pestanias_seguros',
			'poliza_seguros',
			'incendios',
			'grabado',
		]
		
#Etiquetas que van a aparecer a la hora de mostrar el formulario

		labels = {
			'activo_nomenclatura':'Nomenclatura para Codificación',
			'activo_tipo':'Tipo Activo',
			'activo_descripcion':'Descripcion',
			'activo_ubica':'Ubicación',
			'activo_depar':'Departamento',
			'activo_area':'Sector',
			'activo_subsec':'Sub Sector',
            'activo_valor':'Valor Reposición',
			'activo_valor_compra':'Valor Compra',
            'orden_de_pedido':'No Orden de Pedido',
			'numero_factura':'Numero Factura',
			'cod_activo_padre':'Codigo de Activo Padre',
			'pestanias_seguros':'Ubicacion en base de datos de seguros',
			'poliza_seguros':'Póliza de Seguros',
			'incendios':'Póliza de Incendios',
			'grabado':'Identificado',
						
		}
#Son los que se van a pintar como etiquetas de HTML

		widgets = {
			'activo_nomenclatura':forms.Select(attrs={'class':'form-control'}),
			'activo_codigo':forms.TextInput(attrs={'class':'form-control'}),
			'activo_grupo':forms.Select(attrs={'class':'form-control'}),
			'activo_tipo':forms.Select(attrs={'class':'form-control'}),
			'activo_descripcion':forms.Textarea(attrs={'class':'form-control','rows':5}),
			#'activo_ubica':forms.CheckboxSelectMultiple(),
			#'activo_ubica':forms.RadioSelect(),
			'activo_ubica':forms.Select(attrs={'class':'form-control'}),
			'activo_depar':forms.Select(attrs={'class':'form-control'}),
			'activo_area':forms.Select(attrs={'class':'form-control'}),
			'activo_subsec':forms.Select(attrs={'class':'form-control'}),
			'activo_valor':forms.TextInput(attrs={'class':'form-control'}),
			'activo_valor_compra':forms.TextInput(attrs={'class':'form-control'}),
    		'orden_de_pedido':forms.TextInput(attrs={'class':'form-control'}),
   	  		'numero_factura':forms.TextInput(attrs={'class':'form-control'}),
   			'cod_activo_padre':forms.Select(attrs={'class':'form-control'}),
			'pestanias_seguros':forms.Select(attrs={'class':'form-control'}),
			'poliza_seguros':forms.Select(attrs={'class':'form-control'}),
			'incendios':forms.Select(attrs={'class':'form-control'}),
			'grabado':forms.Select(attrs={'class':'form-control'})
			}

class RegistroSalida(forms.ModelForm):
	
	class Meta:
		model = salida_activos

#Campos del modelo que vamos a utilizar en el formulario
		fields = [
			'activo_codigo',
			'activo_tipo',
			'activo_num_serie',
			'marca',
			'retorno',
			'detalle_activo',
			'sale_por',
			'num_orden_trabajo',
            'solicitado_por',
            'motivo',
			'empresa_mantenimiento',
			'fecha_estimada_retorno',
			'hora_salida',
			'codigo',
			'orden_mantenimiento',
			'departamento',
			'grupo',
		]
		
#Etiquetas que van a aparecer a la hora de mostrar el formulario

		labels = {
			'activo_codigo':'Codigo Activo',
			'activo_tipo':'Tipo',
			'activo_num_serie':'Serie',
			'marca':'Marca',
			'retorno':'Debe retornar? ',
			'detalle_activo':'Detalle del activo a movilizar',
			'sale_por':'Salida por',
			'num_orden_trabajo':'N° de Requisición',
            'solicitado_por':'Ingresado por',
            'motivo':'Justificación',
			'empresa_mantenimiento':'Empresa Mantenimiento',
			'fecha_estimada_retorno':'Fecha estimada de retorno',
			'hora_salida':'Hora de salida',						
		}
#Son los que se van a pintar como etiquetas de HTML

		widgets = {
			'codigo':forms.TextInput(attrs={'class':'form-control'}),
			'activo_tipo':forms.TextInput(attrs={'class':'form-control'}),
			'activo_num_serie':forms.TextInput(attrs={'class':'form-control'}),
			'marca':forms.TextInput(attrs={'class':'form-control'}),
			# 'retorno':forms.RadioSelect(attrs={'id': 'value'}),
			'retorno':forms.Select(attrs={'class':'form-control'}),
			'detalle_activo':forms.Textarea(attrs={'class':'form-control','rows':2}),
			# 'activo_ubica':forms.CheckboxSelectMultiple(),
			'sale_por':forms.Select(attrs={'class':'form-control','required':'required'}),
			'num_orden_trabajo':forms.TextInput(attrs={'class':'form-control'}),
			'solicitado_por':forms.TextInput(attrs={'class':'form-control'}),
			'motivo':forms.Textarea(attrs={'class':'form-control', 'required':'required','rows':2}),
			'empresa_mantenimiento':forms.TextInput(attrs={'class':'form-control'}),
    		'fecha_estimada_retorno':forms.DateInput(attrs={'class':'form-control','type':'date'}),
   	  		'hora_salida':forms.TextInput(attrs={'class':'form-control', 'data-mask':"00:00", 'required':'required', 'placeholder':'24:00'}),
			# 'activo_codigo':forms.TextInput(attrs={'hidden':'hidden'}),
			'activo_codigo':forms.TextInput(attrs={'class':'form-control'}), #'hidden':'hidden'}),
			'departamento':forms.TextInput(attrs={'class':'form-control'}),#'hidden':'hidden'}),
			'grupo':forms.TextInput(attrs={'class':'form-control'}),#'hidden':'hidden'}),
			}


class RegistroSalidaAgri(forms.ModelForm):
	
	class Meta:
		model = salida_activos

#Campos del modelo que vamos a utilizar en el formulario
		fields = [
			'activo_codigo',
			'activo_tipo',
			'activo_num_serie',
			'marca',
			'detalle_activo',
			'sale_por',
			'num_orden_trabajo',
            'solicitado_por',
            'motivo',
			'empresa_mantenimiento',
			'fecha_estimada_retorno',
			'hora_salida',
			'codigo',
			'departamento',
			'grupo',
			'ubica_area',
			'ubica_ubica',
			'persona_autoriza_dep'
		]
		
#Etiquetas que van a aparecer a la hora de mostrar el formulario

		labels = {
			'activo_codigo':'Codigo Activo',
			'activo_tipo':'Tipo',
			'activo_num_serie':'Serie',
			'marca':'Marca',
			'detalle_activo':'Detalle del activo a movilizar',
			'sale_por':'Motivo Salida/Movimiento',
            'solicitado_por':'Solicitado por',
            'motivo':'Justificación',
			'empresa_mantenimiento':'Empresa Mantenimiento',
			'fecha_estimada_retorno':'Fecha estimada de retorno',
			'hora_salida':'Hora de salida',
			'ubica_area':'Sector Actual',
			'ubica_ubica':'Ubicación Actual',
			'persona_autoriza_dep':'Persona Autoriza',
			'persona_registra_en_proyecto':'Persona Registra',						
		}
#Son los que se van a pintar como etiquetas de HTML

		widgets = {
			'ubica_ubica':forms.TextInput(attrs={'class':'form-control'}),
			'ubica_area':forms.TextInput(attrs={'class':'form-control'}),
			'codigo':forms.TextInput(attrs={'class':'form-control'}),
			'activo_tipo':forms.TextInput(attrs={'class':'form-control'}),
			'activo_num_serie':forms.TextInput(attrs={'class':'form-control'}),
			'marca':forms.TextInput(attrs={'class':'form-control'}),
			# 'retorno':forms.RadioSelect(attrs={'id': 'value'}),
			#'retorno':forms.Select(attrs={'class':'form-control'}),
			'detalle_activo':forms.Textarea(attrs={'class':'form-control','rows':3}),
			# 'activo_ubica':forms.CheckboxSelectMultiple(),
			'sale_por':forms.Select(attrs={'class':'form-control','required':'required'}),
			#'num_orden_trabajo':forms.TextInput(attrs={'class':'form-control'}),
			'solicitado_por':forms.TextInput(attrs={'class':'form-control','required':'required'}),
			'motivo':forms.Textarea(attrs={'class':'form-control', 'required':'required','rows':4}),
			'empresa_mantenimiento':forms.TextInput(attrs={'class':'form-control'}),
    		'fecha_estimada_retorno':forms.DateInput(attrs={'class':'form-control','type':'date'}),
   	  		'hora_salida':forms.TextInput(attrs={'class':'form-control', 'data-mask':"00:00", 'required':'required', 'placeholder':'24:00'}),
			# 'activo_codigo':forms.TextInput(attrs={'hidden':'hidden'}),
			'activo_codigo':forms.TextInput(attrs={'class':'form-control'}), #'hidden':'hidden'}),
			'departamento':forms.TextInput(attrs={'class':'form-control'}),#'hidden':'hidden'}),
			'grupo':forms.TextInput(attrs={'class':'form-control'}),#'hidden':'hidden'}),
			'persona_autoriza_dep':forms.TextInput(attrs={'class':'form-control','required':'required'}),
			'persona_registra_en_proyecto':forms.TextInput(attrs={'class':'form-control'}),
			}





	

class FiltrarForm(forms.ModelForm):
	
	class Meta:
		model = desc_activo

#Campos del modelo que vamos a utilizar en el formulario
		fields = [
			'activo_codigo',
			'activo_grupo',
			'activo_tipo',
			'activo_ubica',
			'activo_depar',
			'activo_area',
			'pestanias_seguros',
			'poliza_seguros',
		]
		
#Etiquetas que van a aparecer a la hora de mostrar el formulario

		labels = {
			'activo_codigo':'Código Activo',
			'activo_grupo':'Grupo',
			'activo_tipo':'Tipo',
			'activo_ubica':'Ubicación',
			'activo_depar':'Departamento',
			'activo_area':'Sector',
			'pestanias_seguros':'Ubicación en pestañas de Archivo de Seguros',
			'poliza_seguros':'Póliza de Seguros asignada',
            			
		}
#Son los que se van a pintar como etiquetas de HTML

		widgets = {
			# 'activo_codigo':forms.TextInput(attrs={'class':'form-control','style':'max-width: 12em'}),
			# 'activo_grupo':forms.Select(attrs={'class':'form-control','style':'max-width: 20em'}),
			# 'activo_tipo':forms.Select(attrs={'class':'form-control','style':'max-width: 20em'}),
			# 'activo_ubica':forms.Select(attrs={'class':'form-control','style':'max-width: 20em'}),
			# #'activo_ubica':forms.RadioSelect(),
			# 'activo_depar':forms.Select(attrs={'class':'form-control','style':'max-width: 20em'}),
			# 'activo_area':forms.Select(attrs={'class':'form-control','style':'max-width: 20em'}),
			# 'pestanias_seguros':forms.Select(attrs={'class':'form-control','style':'max-width: 20em'}),
			
			}

class FiltrarMarca(forms.ModelForm):

	class Meta:
		model = detalle_desc_activo

		fields = [
			
			'desc_activo_marca',
		]

		labels = {
			
			'desc_activo_marca':'Marca',
		}

class FiltrarSerie(forms.ModelForm):

	class Meta:
		model = detalle_desc_activo

		fields = [
			
			'desc_activo_num_serie',
		]

		labels = {
			
			'desc_activo_num_serie':'Serie',
		}

		# widgets = {
			
		# 	'desc_activo_marca':forms.TextInput(attrs={'class':'form-control'}),
		# }


class RegistroFormDet(forms.ModelForm):

	class Meta:
		model = detalle_desc_activo

		fields = [
			
			'desc_activo_usuario_registra',
		]

		labels = {
			
			'desc_activo_usuario_registra':'Ingresado por',
		}
		widgets = {
			
			'desc_activo_usuario_registra':forms.Select(attrs={'class':'form-control'}),
		}

class CambiaEstadoForm(forms.ModelForm):

	class Meta:
		model = desc_activo

		fields = [
			'activo_estado',
		]


class MoverActivosForm(forms.ModelForm):

	class Meta:
		model = desc_activo

		fields = [
			'id',
			'activo_ubica',
			'activo_depar',
			'activo_area',
			'activo_subsec',
			'usuario_modifica',
			'justificacion_modifica',
			
		
		]

		labels = {
			'activo_ubica':'Ubicación',
			'activo_depar':'Departamento',
			'activo_area':'Sector',
			'activo_subsec':'Sub Sector',
			'justificacion_modifica':'Justificación',
			'usuario_modifica':'Usuario registra',
		
		
		}
		
		widgets = {
			'activo_ubica':forms.Select(attrs={'class':'form-control'}),
			'activo_depar':forms.Select(attrs={'class':'form-control','required':'required'}),
			'activo_area':forms.Select(attrs={'class':'form-control','required':'required'}),
			'activo_subsec':forms.Select(attrs={'class':'form-control'}),
			'justificacion_modifica':forms.Textarea(attrs={'class':'form-control','required':'required'}),
			'usuario_modifica':forms.TextInput(attrs={'class':'form-control'}),
		

		}

class MoverActivosFormDet(forms.ModelForm):

	class Meta:
		model = detalle_desc_activo

		fields = [
			'desc_activo_usuario_modifica',
			
		]

class EditaActivo(forms.ModelForm):
	
	class Meta:
		model = detalle_desc_activo

#Campos del modelo que vamos a utilizar en el formulario
		fields = [
			'desc_activo_codigo_mba',
			'desc_activo_fecha_ingre',
			'desc_activo_custodio',
			'desc_activo_cod_responsable',
			'desc_activo_num_serie',
			'desc_activo_modelo',
			'desc_activo_marca',
			'desc_activo_num_motor',
			'desc_activo_num_placa_vehiculo',
			'desc_activo_anio_fabrica',
			'desc_activo_usuario_modifica',
			'desc_activo_motivo_modifica',	
			'desc_activo_pc_procesador',
			'desc_activo_pc_memoria',
			'desc_activo_pc_disco',
			'desc_activo_proveedor',
			'motivo_no_se_puede_identificar',				
		]

#Etiquetas que van a aparecer a la hora de mostrar el formulario

		labels = {
			'desc_activo_codigo_mba':'Código MBA',
			'desc_activo_fecha_ingre':'Fecha de Compra',
			'desc_activo_custodio':'Nombre Custodio',
			'desc_activo_cod_responsable':'Código Empleado Custodio',
			'desc_activo_num_serie':'Número de Serie',
			'desc_activo_modelo':'Modelo',
			'desc_activo_marca':'Marca/Fabricante',
			'desc_activo_num_motor':'Número de  Motor',
			'desc_activo_num_placa_vehiculo':'Número de Placa Vehículo',
			'desc_activo_anio_fabrica':'Año de Fabricación',
			'desc_activo_usuario_modifica':'Usuario modifica',
			'desc_activo_motivo_modifica':'Motivo de la Modificación',
			'desc_activo_pc_procesador':'CPU Arquitectura Procesador',
			'desc_activo_pc_memoria':'CPU Memoria RAM',
			'desc_activo_pc_disco':'CPU Tamaño Disco',
			'desc_activo_proveedor':'Proveedor',
			'motivo_no_se_puede_identificar': 'Motivo no se puede Identificar',
	
			}
#Son los que se van a pintar como etiquetas de HTML

		widgets = {
			'desc_activo_codigo_mba':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_custodio':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_cod_responsable':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_num_serie':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_modelo':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_marca':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_num_motor':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_num_placa_vehiculo':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_anio_fabrica':forms.DateInput(attrs={'class':'form-control'}),
			'desc_activo_usuario_modifica':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_motivo_modifica':forms.Select(attrs={'class':'form-control'}),
			'desc_activo_pc_procesador':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_pc_memoria':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_pc_disco':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_fecha_ingre':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
			'desc_activo_proveedor':forms.TextInput(attrs={'class':'form-control'}),
			'motivo_no_se_puede_identificar':forms.TextInput(attrs={'class':'form-control'}),
			
			
			}

class EditaActivoIngreso(forms.ModelForm):
	
	class Meta:
		model = detalle_desc_activo

#Campos del modelo que vamos a utilizar en el formulario
		fields = [
			'desc_activo_codigo_mba',
			'desc_activo_fecha_ingre',
			'desc_activo_custodio',
			'desc_activo_cod_responsable',
			'desc_activo_num_serie',
			'desc_activo_modelo',
			'desc_activo_marca',
			'desc_activo_num_motor',
			'desc_activo_num_placa_vehiculo',
			'desc_activo_anio_fabrica',
			'desc_activo_usuario_modifica',
			'desc_activo_motivo_modifica',	
			'desc_activo_pc_procesador',
			'desc_activo_pc_memoria',
			'desc_activo_pc_disco',	
			'motivo_no_se_puede_identificar',			
		]

#Etiquetas que van a aparecer a la hora de mostrar el formulario

		labels = {
			'desc_activo_codigo_mba':'Código MBA',
			'desc_activo_fecha_ingre':'Fecha de Compra',
			'desc_activo_custodio':'Nombre Custodio',
			'desc_activo_cod_responsable':'Código Empleado Custodio',
			'desc_activo_num_serie':'Número de Serie',
			'desc_activo_modelo':'Modelo',
			'desc_activo_marca':'Marca/Fabricante',
			'desc_activo_num_motor':'Número de  Motor',
			'desc_activo_num_placa_vehiculo':'Número de Placa Vehículo',
			'desc_activo_anio_fabrica':'Año de Fabricación',
			'desc_activo_usuario_modifica':'Usuario modifica',
			'desc_activo_motivo_modifica':'Motivo de la Modificación',
			'desc_activo_pc_procesador':'CPU Arquitectura Procesador',
			'desc_activo_pc_memoria':'CPU Memoria RAM',
			'desc_activo_pc_disco':'CPU Tamaño Disco',
			'motivo_no_se_puede_identificar':'Motivo no se puede Identificar:'
	
			}
#Son los que se van a pintar como etiquetas de HTML

		widgets = {
			'desc_activo_codigo_mba':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_custodio':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_cod_responsable':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_num_serie':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_modelo':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_marca':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_num_motor':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_num_placa_vehiculo':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_anio_fabrica':forms.DateInput(attrs={'class':'form-control'}),
			'desc_activo_usuario_modifica':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_motivo_modifica':forms.Select(attrs={'class':'form-control'}),
			'desc_activo_pc_procesador':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_pc_memoria':forms.TextInput(attrs={'class':'form-control'}),
			'desc_activo_pc_disco':forms.TextInput(attrs={'class':'form-control'}),
			# 'desc_activo_fecha_ingre':forms.DateInput(attrs={'class':'form-control', 'placeholder':'yyyy-mm-dd'}),
			'desc_activo_fecha_ingre':forms.DateInput(attrs={'class':'form-control','type':'date'}),
			'motivo_no_se_puede_identificar':forms.TextInput(attrs={'class':'form-control'}),
			
			}

class MuestraNomenclatura(forms.ModelForm):
	class Meta:
		model = activo_nomenclatura

		fields = [
			'nomenclatura_mix',
		]

		labels = {
			'nomenclatura_mix':'Nomenclatura',
		}
		
		widgets = {
			'nomenclatura_mix':forms.Select(attrs={'class':'form-control'}),
		}
