from django import forms
from .models import proveedor,proveedor_det, documentos_prove, proveedor_categoria, proveedor_encuesta, \
    proveedor_segmento, proveedor_fichas, proveedor_documentos
from django.forms.models import inlineformset_factory
import datetime


class CargaFichasForm(forms.ModelForm):
    class Meta:
        model = proveedor_fichas
        fields = [
            'nombre_ficha',
            
        ]

        labels = {
            'nombre_ficha': 'Nombre Ficha usa Ecofroz',
    
        }


class ExpiraDocumentos(forms.Form):
    nombre_empresa = forms.ModelChoiceField(queryset = proveedor.objects.all(), widget = forms.Select(attrs={'class':'seleccion1', 'id':'nombre_empresa'}))
    nombre_documento = forms.ModelChoiceField(queryset= proveedor_documentos.objects.all(),widget= forms.Select(attrs={'class':'seleccion1','id':'nombre_documento'}))

    def __init__(self, *args, **kwargs):
        super(ExpiraDocumentos, self).__init__(*args, **kwargs)
        self.fields['nombre_empresa'].queryset = proveedor.objects.all().order_by('nombre_empresa')
        self.fields['nombre_empresa'].label_from_instance = lambda obj: "%s" % (obj.nombre_empresa)
        self.fields['nombre_documento'].queryset = proveedor_documentos.objects.all().order_by('nombre_documento')
        self.fields['nombre_documento'].label_from_instance = lambda obj: "%s" % (obj.nombre_documento)



class NombreEmpresaForm(forms.Form):
    nombre_empresa = forms.ModelChoiceField(queryset = proveedor.objects.all(), widget = forms.Select(attrs={'class':'seleccion1', 'id':'nombre_empresa', 'required': 'true'}))

    def __init__(self, *args, **kwargs):
        super(NombreEmpresaForm, self).__init__(*args, **kwargs)
        self.fields['nombre_empresa'].queryset = proveedor.objects.all().order_by('nombre_empresa')
        self.fields['nombre_empresa'].label_from_instance = lambda obj: "%s" % (obj.nombre_empresa)
        

class NombreEmpresaConRespuestasForm(forms.Form):
    nombre_empresa = forms.ModelChoiceField(queryset = proveedor.objects.all(), widget = forms.Select(attrs={'class':'seleccion1','id':'id_nombre_empresa','required':'false'}))

    def __init__(self, *args, **kwargs):
        super(NombreEmpresaConRespuestasForm, self).__init__(*args, **kwargs)
        self.fields['nombre_empresa'].queryset = proveedor.objects.all().order_by('nombre_empresa').filter(respondio_encuesta=True)
        self.fields['nombre_empresa'].label_from_instance = lambda obj: "%s" % (obj.nombre_empresa)

class SegmentoForm(forms.Form):
    nombre_segmento = forms.ModelChoiceField(queryset = proveedor_segmento.objects.all(), widget = forms.Select(attrs={'class':'seleccion1', 'id':'segmento', 'required': 'true'}))

    def __init__(self, *args, **kwargs):
        super(SegmentoForm, self).__init__(*args, **kwargs)
        self.fields['nombre_segmento'].queryset = proveedor_segmento.objects.all().order_by('id')
        self.fields['nombre_segmento'].label_from_instance = lambda obj: "%s" % (obj.nombre_segmento)


class ParaExportarExcelForm(forms.Form):

    categoria = forms.ModelChoiceField(queryset = proveedor_categoria.objects.all(), widget = forms.Select(attrs={'onchange' : 'this.form.submit()','class':'seleccion1', 'id':'categoria2', 'required': 'true'}))
    
    segmento = forms.ModelChoiceField(queryset = proveedor_segmento.objects.all(), widget = forms.Select(attrs={'onchange' : 'this.form.submit()','class':'seleccion1', 'id':'segmento2', 'required': 'true'}))

    def __init__(self, *args, **kwargs):
        super(ParaExportarExcelForm, self).__init__(*args, **kwargs)
        self.fields['segmento'].queryset = proveedor_segmento.objects.all().exclude(id=14).order_by('id')
        self.fields['segmento'].label_from_instance = lambda obj: "%s" % (obj.nombre_segmento)


class ResultadoConsultaForm(forms.Form):

    categoria = forms.ModelChoiceField(queryset = proveedor_categoria.objects.all(), widget = forms.Select(attrs={'onchange' : 'this.form.submit()','class':'seleccion1', 'id':'categoria3', 'required': 'true'}))
    
    proveedor1 = forms.ModelChoiceField(queryset = proveedor.objects.all(), widget = forms.Select(attrs={'class':'proveedor1', 'id':'proveedor1', 'required': 'true'}))

    proveedorm = forms.ModelChoiceField(queryset = proveedor.objects.all(), widget = forms.Select(attrs={'class':'proveedor1', 'id':'proveedorm', 'required': 'true'}))

    proveedor2 = forms.ModelChoiceField(queryset = proveedor.objects.all(), widget = forms.Select(attrs={'onchange' : 'this.form.submit()','class':'proveedor2', 'id':'proveedor2', 'required': 'true'}))

    
    def __init__(self, *args, **kwargs):
        self._categoria = kwargs.pop('categoria', None)
        self._proveedor1 = kwargs.pop('proveedor1', None)
        self._proveedor2 = kwargs.pop('proveedor2', None)
        super(ResultadoConsultaForm, self).__init__(*args, **kwargs)
        # without the next line label_from_instance does NOT work
        self.fields['categoria'].queryset = proveedor_categoria.objects.all().order_by('nombre_categoria')
        self.fields['categoria'].label_from_instance = lambda obj: "%s" % (obj.nombre_categoria)
        # self.fields['proveedor1'].queryset= proveedor.objects.all()
        # self.fields['proveedor1'].label_from_instance = lambda obj: "%s" % (obj.nombre_empresa)
        self.fields['proveedor1'].queryset= proveedor.objects.filter(categoria=self._categoria).filter(respondio_encuesta=True).order_by('nombre_empresa')
        self.fields['proveedor1'].label_from_instance = lambda obj: "%s" % (obj.nombre_empresa)
        self.fields['proveedor2'].queryset= proveedor.objects.filter(categoria=self._categoria).filter(respondio_encuesta=True).order_by('nombre_empresa')
        self.fields['proveedor2'].label_from_instance = lambda obj: "%s" % (obj.nombre_empresa)
        


class FiltrarFormSegmento(forms.Form):
  
    segmento = forms.ModelChoiceField(queryset = proveedor_segmento.objects.all(), widget = forms.Select(attrs={'onchange' : 'this.form.submit()','class':'seleccion1', 'id':'list-segmento', 'required': 'true'}))

    def __init__(self, *args, **kwargs):
        super(FiltrarFormSegmento, self).__init__(*args, **kwargs)
        self.fields['segmento'].queryset = proveedor_segmento.objects.all().exclude(id=14).exclude(id=3).order_by('id')
        self.fields['segmento'].label_from_instance = lambda obj: "%s" % (obj.nombre_segmento)



# class FiltrarFormSegmento(forms.ModelForm):
#     class Meta:
#         model = proveedor_encuesta

#         fields = [
#             'segmento',
#         ]
#         labels = {
#             'segmento':'Filtre las preguntas por segmento',
#         }
#         widgets = {
#             'segmento':forms.Select(attrs={'onchange' : 'this.form.submit()','class':'form-control'}),

#         }




class Documentos(forms.ModelForm):
    class Meta:
        model = documentos_prove
        fields = ['archivos', 
                  
        ]
    
class Fichas(forms.ModelForm):
    class Meta:
        model = documentos_prove
        fields = [
            'archivos',
            'es_ficha',

        ]

class HojasMSDS(forms.ModelForm):
    class Meta:
        model = documentos_prove
        fields = [
            'archivos',
            'es_hoja_msds',

        ]

class EtiquetasProductos(forms.ModelForm):
    class Meta:
        model = documentos_prove
        fields = [
            'archivos',
            'es_etiqueta_producto',

        ]



class ProveedorN(forms.ModelForm):
    class Meta:
        model = documentos_prove
        fields = [ 
                  'proveedor',
        ]


class FiltrarForm(forms.ModelForm):
    class Meta:
        model = proveedor

        fields = [
            'nombre_empresa',
        ]
        labels = {
            'nombre_empresa':'Nombre empresa',
        }
        widgets = {
            'nombre_empresa':forms.Select(attrs={'class':'form-control'}),

        }



class FiltrarFormDet(forms.ModelForm):
	
	class Meta:
		model = proveedor_det

#Campos del modelo que vamos a utilizar en el formulario
		fields = [
            'categoria_proveedor',
            'codigo_id',
            

			
		]
		
#Etiquetas que van a aparecer a la hora de mostrar el formulario

		labels = {
			'categoria_proveedor':'Categoria',
            'codigo_id':'Nombre empresa',
						
		}
#Son los que se van a pintar como etiquetas de HTML

		widgets = {
			'categoria_proveedor':forms.Select(attrs={'class':'form-control'}),
            'codigo_id':forms.Select(attrs={'class':'form-control'}),
			}



class RegistroFormP(forms.ModelForm):
	
	class Meta:
		model = proveedor

#Campos del modelo que vamos a utilizar en el formulario
		fields = [
			'nombre_empresa',
            'nombre_comercial',
			'direccion_matriz',
			'horario_trabajo',
			'representante_legal',
			'ruc',
			'nombre_contacto_ecofroz',
			'telefono',
			'celular',
            'calificacion',
            'estado',
            'respondio_encuesta',
            'proveedor_critico',
            'proveedor_revisado',
            'categoria',
            'usuario_modifica',
            
		]
		
#Etiquetas que van a aparecer a la hora de mostrar el formulario

		labels = {
		    'nombre_empresa':'Empresa o Nombre',
            'nombre_comercial':'Nombre Comercial',
			'direccion_matriz':'Dirección',
			'horario_trabajo':'Horario de Trabajo',
			'representante_legal':'Nombre Rep Legal',
			'ruc':'Número de Ruc o Cédula',
			'nombre_contacto_ecofroz':'Nombre de persona que se contacta con Ecofroz',
			'telefono':'Teléfono Convencional',
			'celular':'Celular',
            'calificacion':'Calificación Proveedor',
            'estado':'Estado Proveedor',
            'respondio_encuesta':'Ha respondido la encuesta de proveedores?',
            'proveedor_critico':'Es proveedor Crítico?',
            'categoria':'Categoria Proveedor',
            'usuario_modifica':'Modificado por:',
            'proveedor_revisado':'Revisado Administracion',
            
						
		}
#Son los que se van a pintar como etiquetas de HTML

		widgets = {
			'nombre_empresa':forms.TextInput(attrs={'class':'form-control'}),
            'nombre_comercial':forms.TextInput(attrs={'class':'form-control'}),
            'direccion_matriz':forms.TextInput(attrs={'class':'form-control'}),
			'horario_trabajo':forms.TextInput(attrs={'class':'form-control'}),
            'representante_legal':forms.TextInput(attrs={'class':'form-control'}),
            'ruc':forms.TextInput(attrs={'class':'form-control'}),
            'nombre_contacto_ecofroz':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'celular':forms.TextInput(attrs={'class':'form-control'}),
            'calificacion':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.Select(attrs={'class':'form-control'}),
            'categoria':forms.Select(attrs={'class':'form-control'}),
            # 'usuario_modifica':forms.TextInput(attrs={'class':'form-control'}),
           
            }

class RegistroFormDetP(forms.ModelForm):
    
    class Meta:
        model = proveedor_det
        fields = [
			'carta_presentacion',
            'giro_negocio',
            'monto_ventas_2018',
            'monto_ventas_2019',
            'monto_ventas_2020',
            'monto_ventas_2021',
            'antiguedad',
            'num_trabajadores_fijos',
            'num_clientes',
            'num_proveedores',
            'valores_empresa',
            'tieneweb',
            'web',
            'actividad',
            'otra_actividad',
            'empresa_tipo',
            'categoria_proveedor',
            'otra_categoria',
            'ruc_adjunto',
            'referencia_bancaria',
            'certificado_iess',
            'servicio_basico',
            'ref_comercial_prove1',
            'ref_comercial_prove2',
            'ref_comercial_prove3',
            'ref_comercial_cliente1',
            'ref_comercial_cliente2',
            'ref_comercial_cliente3',
            'rep_legal',
            'accionistas',
            'anios_como_proveedor',
            'ventas_ecofroz_2018',
            'ventas_ecofroz_2019',
            'ventas_ecofroz_2020',
            'ventas_ecofroz_2021',
            'subcontrata',
            'actividades_subcontratadas',
            'confirmacion_canal_comunicacion',
            'tiene_certificado_migracion_fundas',
            'certificado_migracion_fundas',
            'tiene_documento_aceptacion_especificaciones_ecofroz',
            'documento_aceptacion_especificaciones_ecofroz',
            'tiene_especificacion_material_empaque',
            'especificacion_material_empaque',
            'tiene_aprobaciones_contacto_alimentos',
            'aprobaciones_contacto_alimentos',
            'tiene_certificacion_basc',
            'certificado_basc',
            'tiene_homologacion_auditoria_basc_ecofroz',
            'certificado_homologacion_ecofroz',
            'tiene_homologacion_gfsi',
            'certificado_hologacion_gfsi',
            'tiene_certificado_auditoria_ecofroz_por_no_gfsi',
            'certificado_auditoria_ecofroz_por_no_gfsi',
            'tiene_certificado_calidad_por_lote',
            'tiene_certificado_transporte_exclusivo',
            'certificado_transporte_exclusivo',
            'tiene_certificado_transporte_sellado',
            'certificado_transporte_sellado',
            'tiene_formato_informacion_contacto_emergencia',
            'formato_informacion_contacto_emergencia',
            'contrato_vigente_ecofroz',
            'tiene_certificado_npma',
            'certificado_npma',
            'tiene_certificado_aecpu',
            'certificado_aecpu',
            'tiene_certificado_mip_personal',
            'certificado_mip_personal',
            'tiene_fichas_tecnicas_y_registros_sanitarios',
            'fichas_tecnicas_y_registros_sanitarios',
            'tiene_poliza_responsabilidad_civil',
            'poliza_responsabilidad_civil',
            'tiene_certificado_arcsa',
            'certificado_arcsa',
            'tiene_permiso_funcionamiento',
            'permiso_funcionamiento',
            'tiene_certificacion_gfsi_o_bpm',
            'certificacion_gfsi_o_bpm',
            'tiene_copia_hoja_seguridad_datos_msds',
            'copia_hoja_seguridad_datos_msds',
            'tiene_ingredientes_activos_aprobados',
            'ingredientes_activos_aprobados',
            'tiene_certificado_determinar_concentracion_quimico',
            'certificado_determinar_concentracion_quimico',
            'tiene_certificado_biodegradabilidad',
            'certificado_biodegradabilidad',
            'tiene_certificado_validaciones_reduccion_logaritmica',
            'certificado_validaciones_reduccion_logaritmica',
            'tiene_analisis_composicion_concentraciones',
            'analisis_composicion_concentraciones',
            'tiene_especificaciones_fichas_tecnicas',
            'especificaciones_fichas_tecnicas',
            'tiene_certificado_buenas_practicas_manufactura',
            'certificado_buenas_practicas_manufactura',
            'tiene_seguimiento_medico_trabajadores',
            'seguimiento_medico_trabajadores',
            'tiene_reporte_inspeccion_permiso_funcionamiento',
            'reporte_inspeccion_permiso_funcionamiento',
            'tiene_afiliacion_empleados_iess',
            'afiliacion_empleados_iess',
            'tiene_certificado_iso_17025',
            'certificado_iso_17025',
            'tiene_carta_garantia',
            'carta_garantia',
            'tiene_certificado_tiempo_analisis',
            'certificado_tiempo_analisis',
            'tiene_certificado_logistica_producto',
            'certificado_logistica_producto',
            'tiene_certificado_calidad_producto',
            'certificado_calidad_producto',
            'tiene_certificado_insumos_aoac',
            'certificado_insumos_aoac',
            'tiene_certificado_patrones_trazables_baja_incertidumbre',
            'certificado_patrones_trazables_baja_incertidumbre',
            'tiene_certificado_ambiental',
            'certificado_ambiental',
            'tiene_licencia_unica_funcionamiento_luae',
            'licencia_unica_funcionamiento_luae',
            'tiene_certificado_destruccion_material_x_carga',
            'certificado_destruccion_material_x_carga',
            'tiene_formato_seleccion_materia_prima',
            'formato_seleccion_materia_prima',
            'certificado_de_manejo_otros_productos',
            'tiene_analisis_cumplimiento_fda_173310',
            'analisis_cumplimiento_fda_173310',
            'tiene_certificado_fabricacion_libre_alergenicos',
            'certificado_fabricacion_libre_alergenicos',
            'tiene_certificado_nfs_h1_h2',
            'certificado_nfs_h1_h2',
            'tiene_ficha_tecnica_hoja_seguridad_registro_sanitario',
            'ficha_tecnica_hoja_seguridad_registro_sanitario',
            'tiene_certificado_iso_21469',
            'certificado_iso_21469',
            'tiene_lista_choferes_autorizados',
            'lista_choferes_autorizados',
            'nombre_cooperativa_y_o_compania_pertenecen_vehiculos',
            'tiene_permiso_operacion_transporte',
            'permiso_operacion_transporte',
            'tiene_matricula_vehiculo_actualizada',
            'matricula_vehiculo_actualizada',
            'vehiculos_estan_asegurados',
            'poliza_seguro_vehiculos',
            'tiene_seguro_ocupantes_vehiculo',
            'poliza_seguro_ocupantes_vehiculo',
            'tiene_sistema_calidad_iso9001',
            'otro_sistema_calidad',
            'tiene_procedimientos_ventas_no_conformes',
            'tiene_procesos_mejora_continua',
            'tiene_plan_respuesta_riesgos',
            'tiene_programa_auditoria_interna',
            'tiene_sistema_seguridad_logistica_transporte',
            'utiliza_transporte_propio',
            'tiene_documentos_habilitantes_vehiculos',
            'tiene_cobertura_seguro_vehiculos',
            'tiene_cobertura_seguro_ocupantes_vehiculos',
            'tiene_sistema_comunicacion_transmision_datos',
            'hace_respaldos_periodicos_informacion_empresa',
            'tiene_activos_asegurados',
            'hace_mantenimiento_preventivo',
            'tipo_instalaciones',
            'giro_negocio_igual',
            'descripcion_giro_negocio_otras_empresas',
            'requiere_certificado_ambiental',
            'certificado_ambiental',
            'tiene_certificado_ambiental',
            'tiene_politica_proteccion_ambiente',
            'describa_politica_ambiente',
            'optimiza_uso_recursos',
            'tiene_programa_manejo_desechos',
            'tiene_politica_responsabilidad_social',
            'descripcion_politica_responsabilidad_social',
            'tiene_politica_prevencion_actos_corrupcion',
            'tiene_politica_prevencion_actos_acoso',
            'tiene_mecanismo_discrimen',
            'tiene_codigo_conducta',
            'tiene_plan_continuidad_negocio',
            'tiene_reglamento_interno_trabajo',
            'tiene_reglamento_interno_seguridad_salud_laboral',
            'tiene_politica_inclusion_social',
            'tiene_practicas_no_discriminacion_laboral',
            'capacita_usuarios_prevencion_accidentes',
            'prioriza_contratacion_personal_zona',
            'realiza_simulacro_emergencia',
            'trabajadores_menores_16anios',
            'tiene_sistema_evaluacion_seleccion_proveedores',
            'tiene_mecanismo_satisfaccion_cliente',
            'mecanismo_satisfaccion_cliente',
            'ecofroz_explico_proceso_compra',
            'especificaciones_oportunas_claras',
            'proceso_compra_agil',
            'sugerencia_proceso_compra',
            'conoce_proceso_pago',
            'cumplimiento_proceso_pago',
            'sugerencia_proceso_pago',
            'conoce_proceso_recepcion',
            'sugerencia_proceso_recepcion',
            'es_atendido_bien',
            'sugerencia_relacion_comercial',
            'es_proveedor_maquinaria_o_equipo',
            'tipo_maquinaria_equipo_que_provee',
            'tipo_producto_servicio_provee',
            'proveedor_pesticidas_requisitos_indispensables',
            'proveedor_fertilizantes_requisitos_indispensables',
            'proveedor_foliares_requisitos_indispensables',
            'proveedor_materia_organica_requisitos_indispensables',
            #Campos de uso interno Ecofroz. Para presentar a proveedores será necesario retirar estos campos
            'cumple_procedimiento_facturacion',
            'cumple_procedimiento_entrega',
            'cumple_procedimiento_compra',
            'antecedentes_verificados_rep_legal',
            'otros_documentos_enviados1',
            'otros_documentos_enviados2',
            'otros_documentos_enviados3',
            'otros_documentos_enviados4',
            'otros_documentos_enviados5',
            'tiene_fichas',
            'numero_de_fichas',
            'num_documentos_solicitados_categoria',
            'observaciones_administrativas',
            'contesta_reclamos_administrativos',
            'contesta_reclamos_calidad',
            'proveedor_mant_externo',
            'proveedor_ruta_fija',

            ]
        
        labels = {
            'carta_presentacion':'Carta de Presentación',
            'giro_negocio':'Actividad/Giro del Negocio',
            'monto_ventas_2018':'Ventas 2018',
            'monto_ventas_2019':'Ventas 2019',
            'monto_ventas_2020':'Ventas 2020',
            'monto_ventas_2021':'Ventas 2021',
            'antiguedad':'Años de Antiguedad',
            'num_trabajadores_fijos':'Número de Trabajadores Fijos',
            'num_clientes':'Número de Clientes',
            'num_proveedores':'Número de Proveedores',
            'valores_empresa':'Valores de la empresa',
            'tieneweb':'Tiene página Web',
            'web':'Dirección de página Web',
            'actividad':'Actividad Económica',
            'otra_actividad':'Producto/Servicio Ecofroz',
            'empresa_tipo':'Tipo de empresa',
            'categoria_proveedor':'Categoria:',
            'otra_categoria':'Describa Otra Categoría',
            'ruc_adjunto':'Copia de RUC o Cédula de Ciudadanía',
            'referencia_bancaria':'Referencia Bancaria',
            'certificado_iess':'Certificado de cumplimiento obligaciones IESS',
            'servicio_basico': 'Carta de Servicio Básico',
            'ref_comercial_prove1':'Referencia Comercial de Provedor # 1',
            'ref_comercial_prove2':'Referencia Comercial de Provedor # 2',
            'ref_comercial_prove3':'Referencia Comercial de Provedor # 3',
            'ref_comercial_cliente1':'Referencia Comercial de Cliente # 1',
            'ref_comercial_cliente2':'Referencia Comercial de Cliente # 2',
            'ref_comercial_cliente3':'Referencia Comercial de Cliente # 3',
            'rep_legal':'Nombramiento de Representate Legal',
            'accionistas':'Accionistas',
            'anios_como_proveedor':'Años como proveedor',
            'ventas_ecofroz_2018':'Ventas a Ecofroz 2018',
            'ventas_ecofroz_2019':"Ventas a Ecofroz 2019",
            'ventas_ecofroz_2020':"Ventas a Ecofroz 2020",
            'ventas_ecofroz_2021':"Ventas a Ecofroz 2021",
            'subcontrata':'Subcontrata',
            'actividades_subcontratadas':'Describa las actividades que subcontrata',
            'confirmacion_canal_comunicacion':'El canal de consulta y/o ayuda y/o denuncia que usted tuviere en cualquier instancia de su relación con Ecofroz S.A, es vía correo electrónico a la siguiente dirección: gerencia.administrativa@ecofroz.com ó pborja@ecofroz.com. Confirma usted que está informado de cómo canalizar sus consultas, quejas y denuncias?',
            'tiene_certificado_migracion_fundas':'Tiene Certificado de Migración (Solo Fundas Impresas)',
            'certificado_migracion_fundas':'Certificado de Migración (Solo Fundas Impresas)',
            'tiene_documento_aceptacion_especificaciones_ecofroz':'Tiene Documento de Aceptación de las especificaciones de Ecofroz S.A',
            'documento_aceptacion_especificaciones_ecofroz':'Documento de Aceptación de las especificaciones de Ecofroz S.A',
            'tiene_especificacion_material_empaque':'Tiene la especificación de material de empaque?',
            'especificacion_material_empaque':'Especificación de material de empaque (Vigencia 1 año)',
            'tiene_aprobaciones_contacto_alimentos':'Tiene aprobaciones de contacto con los alimentos (materia prima)',
            'aprobaciones_contacto_alimentos':'Aprobaciones de contacto con los alimentos (materia prima)',
            'tiene_certificacion_basc':'Tiene Certificación BASC',
            'certificado_basc':'Copia Vigente Certificado BASC',
            'tiene_homologacion_auditoria_basc_ecofroz':'En caso de que no tenga certificación BASC, tiene homologación y/o Ecofroz ha realizado una auditoría a su empresa?',
            'certificado_homologacion_ecofroz':'Copia Vigente de Homologación Ecofroz',
            'tiene_homologacion_gfsi':'Tiene certificado de homolagación GFSI',
            'certificado_hologacion_gfsi':'Copia de Certificado vigente de Homologación GFSI',
            'tiene_certificado_auditoria_ecofroz_por_no_gfsi':'En caso de no tener certificado de homologación GFSI, tiene certificado actualizado de auditoría Ecofroz?',
            'certificado_auditoria_ecofroz_por_no_gfsi':'Copia de Certificado actualizado de auditoría Ecofroz',
            'tiene_certificado_calidad_por_lote':'Entrega certificado de calidad por lote?',
            'tiene_certificado_transporte_exclusivo':'Tiene certificado de transporte exclusivo para este material?',
            'certificado_transporte_exclusivo':'Certificado de que el transporte es exclusivo para este material o procedimiento de limpieza cuando haya cambio de producto',
            'tiene_certificado_transporte_sellado':'Tiene certificado de que el transporte debe llegar sellado a Ecofroz S.A?',
            'certificado_transporte_sellado':'Certificado de que el transporte debe llegar sellado a Ecofroz S.A',
            'tiene_formato_informacion_contacto_emergencia':'Envió el formato de información del contacto de emergencia debidamente completado?',
            'formato_informacion_contacto_emergencia':'Formato de información del contacto debidamente completado',
            'contrato_vigente_ecofroz':'Tiene contrato vigente firmado con Ecofroz S.A?',
            'tiene_certificado_npma':'Tiene certificado NPMA (National Pest Management Association)?',
            'certificado_npma':'Certificado NPMA(National Pest Management Association)',
            'tiene_certificado_aecpu':'Tiene certificado AECPU (Asociación ecuatoriana de Controladores de Plagas Urbanas)?',
            'certificado_aecpu':'Certificado AECPU (Asociación ecuatoriana de Controladores de Plagas Urbanas)?',
            'tiene_certificado_mip_personal':'Tiene certificado de entrenamiento en MIP del personal (vigencia de una año)?',
            'certificado_mip_personal':'Certificado de entrenamiento en MIP del personal (vigencia 1 año)',
            'tiene_fichas_tecnicas_y_registros_sanitarios':'Envió las fichas técnicas y registros sanitarios de los productos químicos utilizados y las autorizaciones (de autoridad competente) para su uso?',
            'fichas_tecnicas_y_registros_sanitarios':'Fichas técnicas y registros sanitarios de los productos químicos utilizados y las autorizaciones (de autoridad competente) para su uso',
            'tiene_poliza_responsabilidad_civil':'Tiene póliza de responsabilidad civil?',
            'poliza_responsabilidad_civil':'Póliza de responsabilidad civil',
            'tiene_certificado_arcsa':'Tiene certificado ACSA vigente?',
            'certificado_arcsa':'Certificado ARCSA vigente',
            'tiene_permiso_funcionamiento':'Tiene permiso de funcionamiento',
            'permiso_funcionamiento':'Permiso de funcionamiento vigente',
            'tiene_certificacion_gfsi_o_bpm':'Tiene certificación GFI ó BPM?',
            'certificacion_gfsi_o_bpm':'Certificación GFSI ó BPM',
            'tiene_copia_hoja_seguridad_datos_msds':'Envió la copia de la Hoja de seguridad de datos MSDS?',
            'copia_hoja_seguridad_datos_msds':'Copia de la Hoja de seguridad de datos MSDS',
            'tiene_ingredientes_activos_aprobados':'Envió el archivo de los Ingredientes activos aprobados en las legislaciones de Japón - EEUU - Unión Europea?',
            'ingredientes_activos_aprobados':'Archivo de los Ingredientes activos aprobados en las legislaciones de Japón - EEUU - Unión Europea?',
            'tiene_certificado_determinar_concentracion_quimico':'Envió el certificado o análisis para determinar la concentración del químico?',
            'certificado_determinar_concentracion_quimico':'Certificado o análisis para determinar la concentración del químico',
            'tiene_certificado_biodegradabilidad':'Cargó el certificado de biodegradabilidad?',
            'certificado_biodegradabilidad':'Certificado de biodegradabilidad?',
            'tiene_certificado_validaciones_reduccion_logaritmica':'Tiene certificado de validaciones en reducción logarítmica de microorganismos?',
            'certificado_validaciones_reduccion_logaritmica':'Certificado de validaciones en reducción logarítmica de microorganismos?',
            'tiene_analisis_composicion_concentraciones':'Tiene documento de análisis de composición y concentraciones?',
            'analisis_composicion_concentraciones':'Documento de análisis de composición y concentraciones?',
            'tiene_especificaciones_fichas_tecnicas':'Tiene documento con las especificaciones/fichas técnicas de todos los productos vendidos a Ecofroz S.A?',
            'especificaciones_fichas_tecnicas':'Documento con las especificaciones/fichas técnicas de todos los productos vendidos a Ecofroz S.A?',
            'tiene_certificado_buenas_practicas_manufactura':'Tiene certificado de capacitación al personal en temas de Buenas Prácticas de Manufactura (vigencia 1 año)',
            'certificado_buenas_practicas_manufactura':'Certificado de capacitación al personal en temas de Buenas Prácticas de Manufactura (vigencia 1 año)',
            'tiene_seguimiento_medico_trabajadores':'Tiene documento de seguimiento médico a los trabajadores?',
            'seguimiento_medico_trabajadores':'Documento de seguimiento médico a trabajadores',
            'tiene_reporte_inspeccion_permiso_funcionamiento':'Tiene reporte de la inspección realizada para la obtención del permiso de funcionamiento?',
            'reporte_inspeccion_permiso_funcionamiento':'Reporte de la inspección realizada para la obtención del permiso de funcionamiento',
            'tiene_afiliacion_empleados_iess':'Tiene archivo de afiliación de los empleados al IESS?',
            'afiliacion_empleados_iess':'Archivo de afiliación de los  empleados al IESS',
            'tiene_certificado_iso_17025':'Tiene Certificado ISO 17025 vigente y el alcance correspondiente?',
            'certificado_iso_17025':'Certificado ISO 17025 vigente y el alcance correspondiente',
            'tiene_carta_garantia':'Tiene Carta de garantía actualizada',
            'carta_garantia':'Carta de garantía actualizada',
            'tiene_certificado_tiempo_analisis':'Tiene certificado donde se indique el tiempo de respuesta de análisis?',
            'certificado_tiempo_analisis':'Certificado donde se indica el tiempo de respuesta de análisis',
            'tiene_certificado_logistica_producto':'Tiene certificado de logística del producto (condiciones de almacenamiento)',
            'certificado_logistica_producto':'Certificado de logística del producto (condiciones de almacenamiento)',
            'tiene_certificado_calidad_producto':'Tiene Certificado de calidad del producto?',
            'certificado_calidad_producto':'Certificado de calidad del producto',
            'tiene_certificado_insumos_aoac':'Tiene Certificado de insumos aprobado por la AOAC (kits o insumos para métodos de análisis)',
            'certificado_insumos_aoac':'Certificado de insumos aprobado por la AOAC (kits o insumos para métodos de análisis)',
            'tiene_certificado_patrones_trazables_baja_incertidumbre':'Tiene certificado de patrones trazables con baja incertidumbre?',
            'certificado_patrones_trazables_baja_incertidumbre':'Certificado de patrones trazables con baja incertidumbre',
            'tiene_certificado_ambiental':'Tiene registro, licencia o certificación ambiental?',
            'certificado_ambiental':'Registro, licencia o certificación ambiental',
            'tiene_licencia_unica_funcionamiento_luae':'Tiene LUAE o permiso de boberos?',
            'licencia_unica_funcionamiento_luae':'Licencia única de funcionamiento (LUAE) o permiso de bomberos si no está ubicado en Quito',
            'tiene_certificado_destruccion_material_x_carga':'Tine certificado de destrucción de material de empaque por carga (slo para los que tengan marca)?',
            'certificado_destruccion_material_x_carga':'Certificado de destrucción de material de empaque por carga (solo para los que tengan marca)',
            'tiene_formato_seleccion_materia_prima':'Tiene el formato de selección de materia prima debidamente completado?',
            'formato_seleccion_materia_prima':'Formato de selección de materia prima debidamente completado',
            'certificado_de_manejo_otros_productos':'Certificado donde se declare el Manejo de Otros Productos (opcional)',
            'tiene_analisis_cumplimiento_fda_173310':'Tiene el análisis de cumplimiento FDA 173.310?',
            'analisis_cumplimiento_fda_173310':'Análisis de cumplimiento FDA 173.310?',
            'tiene_certificado_fabricacion_libre_alergenicos':'Tiene el certificado de que la fabricación del producto es libre de alergenicos?',
            'certificado_fabricacion_libre_alergenicos':'Tiene el certificado de que la fabricación del producto es libre de alergenicos',
            'tiene_certificado_nfs_h1_h2':'Tiene certificado de la NFS que es H1 o H2?',
            'certificado_nfs_h1_h2':'Certificado de la NFS que es H1 o H2',
            'tiene_ficha_tecnica_hoja_seguridad_registro_sanitario':'Tiene ficha técnica, hoja de seguridad y registro sanitario?',
            'ficha_tecnica_hoja_seguridad_registro_sanitario':'Ficha técnica, hoja de seguridad y registro sanitario',
            'Tiene certificado_iso_21469':'Tiene certificado ISO 21469 (Opcional)',
            'certificado_iso_21469':'Certificado ISO 21469 (Opcional)',
            'tiene_lista_choferes_autorizados':'Tiene listado de choferes autorizados',
            'lista_choferes_autorizados':'Listado de choferes autorizados',
            'nombre_cooperativa_y_o_compania_pertenecen_vehiculos':'Nombre de la cooperativa y/o comapañía a la que pertene/n el/los vehiculo/s',
            'tiene_permiso_operacion_transporte':'Tiene permiso de operación?',
            'permiso_operacion_transporte':'Copia de permiso de operación',
            'tiene_matricula_vehiculo_actualizada':'Tiene matrícula actualizada?',
            'matricula_vehiculo_actualizada':'Copia de la matrícula actualizada',
            'vehiculos_estan_asegurados':'El/los vehículos están asegurados?',
            'poliza_seguro_vehiculos':'Copia de la poliza de seguro de vehiculos',
            'tiene_seguro_ocupantes_vehiculo':'Actualmente tiene seguro para ocupantes del vehículo?',
            'poliza_seguro_ocupantes_vehiculo':'Copia de la póliza de seguro para ocupantes del vehiculo',
            'tiene_sistema_calidad_iso9001':'Cuenta con un sistema de  calidad basado en ISO 9001?',
            'otro_sistema_calidad':'En caso de que su sistema de calidad sea  diferente a ISO 9001, escriba cuál es. Si no tiene ningún sistema de calidad escriba NO LO TENGO',
            'tiene_procedimientos_ventas_no_conformes':'Tiene procedimientos para ventas no conformes (devoluciones, reclamos) de sus productos o servicios?',
            'tiene_procesos_mejora_continua':'Tiene procesos establecidos para desarrollo y mejora contínua de  sus productos y/o servicios?',
            'tiene_plan_respuesta_riesgos':'Cuenta con un plan de respuesta para los riesgos que puedan afectar su operación?',
            'tiene_programa_auditoria_interna':'Cuenta con un programa de auditoría interna y lo ejecuta?', 
            'tiene_sistema_seguridad_logistica_transporte':'Tiene un sistema de seguridad de la logística del transporte de sus productos?',
            'utiliza_transporte_propio':'Utiliza transporte propio para la entrega de  sus productos y/o servicios?',
            'tiene_documentos_habilitantes_vehiculos':'Tiene documentos habilitantes vigentes de todos los vehículos que utiliza en su negocio?',
            'tiene_cobertura_seguro_vehiculos':'Tiene cobertura de seguro para los vehículos en los que transporta sus productos?',
            'tiene_cobertura_seguro_ocupantes_vehiculos':'Tiene cobertura de seguro para los ocupantes de los vehículos en los que transporta sus productos?',
            'tiene_sistema_comunicacion_transmision_datos':'Cuenta con sistemas de comunicación y transmisión de datos?',
            'hace_respaldos_periodicos_informacion_empresa':'Hace respaldos periódicos de la base de información de su compañía?',
            'tiene_activos_asegurados':'Sus activos han sido asegurados apropiadamente?', 
            'hace_mantenimiento_preventivo':'Hace mantenimiento preventivo de sus equipos y/o maquinaria?',
            'tipo_instalaciones':'Sus instalaciones son?',
            'giro_negocio_igual':'En caso de que la respuesta a  la pregunta anterior sea "Compartida por varias empresas". ¿Las otras empresas tienen el mismo giro del negocio que la suya?',
            'descripcion_giro_negocio_otras_empresas':'En caso de que la respuesta  la pregunta anterior sea "NO". Escriba el nombre de la/s empresa/s y el giro del negocio al cual corresponde',
            'requiere_certificado_ambiental':'¿De acuerdo a su giro del negocio, requiere de Certificado Ambiental, Registros Ambientales o Estudio de Impacto Ambiental según corresponda, de acuerdo a la Normativa ambiental aplicable?',
            'certificado_ambiental':'En caso de que si tenga Certificado Ambiental, Registros Ambientales o Estudio de Impacto Ambiental según corresponda, adjunte una copia vigente',
            'tiene_certificado_ambiental':'¿ Envió la copia del certificado Ambiental, Registros Ambientales o Estudio de Impacto Ambiental ?',
            'tiene_politica_proteccion_ambiente':'¿Cuenta con una política de protección al medio ambiente?',
            'describa_politica_ambiente':'En caso de que la respuesta a la pregunta anterior sea "SI", mencione un plan de acción relevante que haya realizado en favor del ambiente, y en caso de ser "NO", escriba no aplica.',
            'optimiza_uso_recursos':'¿Optimiza el uso de recursos (luz, agua, papel, etc.)?',
            'tiene_programa_manejo_desechos':'¿Cuenta con un programa de Manejo de Desechos?',
            'tiene_politica_responsabilidad_social':'¿Cuenta con una política de Responsabilidad Social?',
            'descripcion_politica_responsabilidad_social':'Si su respuesta es afirmativa, describa breve mente la política de Responsabilidad Social',
            'tiene_politica_prevencion_actos_corrupcion':'¿Cuenta con una política de prevención contra actos de corrupción?',
            'tiene_politica_prevencion_actos_acoso':'¿Cuenta con una política de prevención contra actos de acoso?',
            'tiene_mecanismo_discrimen':'¿Cuenta con un mecanismo de denuncia contra el discrimen?',
            'tiene_codigo_conducta':'¿Tiene Código de Conducta?',
            'tiene_plan_continuidad_negocio':'¿Tiene un plan de continuidad del negocio?',
            'tiene_reglamento_interno_trabajo':'¿Posee un reglamento interno de trabajo actualizado?',
            'tiene_reglamento_interno_seguridad_salud_laboral':'¿Posee un Reglamento Interno de Seguridad y Salud Laboral o un Plan mínimo de Prevención?',
            'tiene_politica_inclusion_social':'¿Cuenta con una política de inclusión social?',
            'tiene_practicas_no_discriminacion_laboral':'¿Existen prácticas que garanticen la no discriminación en el ámbito laboral?',
            'capacita_usuarios_prevencion_accidentes':'¿Ha capacitado a sus trabajadores en temas de prevención de accidentes y enfermedades profesionales?',
            'prioriza_contratacion_personal_zona':'¿En su empresa se prioriza la contratación de personal de la zona o zonas donde opera (cantones, parroquias rurales y suburbanas)?',
            'realiza_simulacro_emergencia':'¿Ha realizado por lo menos un simulacro de emergencia y tiene conformada las brigadas de emergencia?',
            'trabajadores_menores_16anios':'¿Su empresa se asegura de que no existan trabajadores menores de 16 años de edad?',
            'tiene_sistema_evaluacion_seleccion_proveedores':'¿Tiene un sistema de evaluación y selección de proveedores?',
            'tiene_mecanismo_satisfaccion_cliente':'¿Tiene un mecanismo de evaluación de satisfacción al cliente?',
            'mecanismo_satisfaccion_cliente':'En caso de que la respuesta a la pregunta anterior sera "SI", escriba cual es su mecanismo de evaluación de satisfacción del cliente, y en caso de ser "NO", escriba no aplica',
            'ecofroz_explico_proceso_compra':'¿Ecofroz S.A explicó su proceso de compra?',
            'especificaciones_oportunas_claras':'¿Las especificaciones para la cotización fueron oportunas y claras?',
            'proceso_compra_agil':'¿El proceso de compra fue ágil, claro y eficaz?',
            'sugerencia_proceso_compra':'¿Tiene alguna sugerencia o comentario con respecto al procedimiento de compra?',
            'conoce_proceso_pago':'¿Conoce usted el proceso de pago de Ecofroz S.A?',
            'cumplimiento_proceso_pago':'¿Se cumplió con los términos y plazos de pago?',
            'sugerencia_proceso_pago':'¿Tiene alguna sugerencia o comentario con respecto al proceso de pago?',
            'conoce_proceso_recepcion':'¿Conoce usted el proceso de recepción de Ecofroz S.A para los productos que usted provee?',
            'sugerencia_proceso_recepcion':'¿Tiene alguna sugerencia o comentario con respecto al proceso de recepción de sus productos?',
            'es_atendido_bien':'¿Usted es atendido oportuna y eficientemente por los colaboradores de Ecofroz S.A en la recepción de sus productos?',
            'sugerencia_relacion_comercial':'¿Tiene alguna sugerencia o comentario con respecto a la relación comercial con Ecofroz S.A y posibles puntos de mejora?',
            'es_proveedor_maquinaria_o_equipo':'Es proveedor de maquinaria o equipo, repuestos de: ',
            'tipo_maquinaria_equipo_que_provee':'Si su respuesta a la pregunta anterior es  positiva,  indique el tipo de maquinaria o equipo que provee, la o las marcas de esos equipos y/o el tipo de repuestos y/o de mantenimiento que provee',
            'tipo_producto_servicio_provee':'Si su repuesta fue NO, explique el tipo de producto o servicio que provee',
            'proveedor_pesticidas_requisitos_indispensables':'PESTICIDAS: Si es usted proveedor de Pesticidas CONFIRME que adjunto a este formulario, envió por correo o, en documento físico, los siguientes requisitos indispensables para ser considerado en el proceso de selección',
            'proveedor_fertilizantes_requisitos_indispensables':'FERTILIZANTES: Si es usted proveedor de Fertilizantes CONFIRME que adjunto a este formulario, envió por correo o, en documento físico, los siguientes requisitos indispensables para ser considerado en el proceso de selección',
            'proveedor_foliares_requisitos_indispensables':'FOLIARES: Si es usted proveedor de  FOLIARES, CONFIRME  que adjunto a este formulario, envió por correo o, en documento físico, los siguientes requisitos indispensables para ser considerado en el proceso de selección',
            'proveedor_materia_organica_requisitos_indispensables':'MATERIA ORGÁNICA: Si es usted proveedor de MATERIA ORGÁNICA confirme que adjunto a este formulario, envió por correo o, en documento físico, los siguientes requisitos indispensables para ser considerado en el proceso de selección',
            'cumple_procedimiento_facturacion':'¿El proveedor encuestado cumple muy frecuentemente con el procedimiento de facturacion?',
            'cumple_procedimiento_entrega':'¿El proveedor encuestado cumple muy frecuentemente con el procedimiento de entrega?',
            'cumple_procedimiento_compra':'¿El proveedor encuestado cumple muy frecuentemente con el procedimiento de compra?',
            'antecedentes_verificados_rep_legal':'¿ De acuerdo con la normativa BASC,  se ha verificado antecedentes del  Representante Legal de la Empresa ?',
            'otros_documentos_enviados1':'Otros documentos enviados # 1',
            'otros_documentos_enviados2':'Otros documentos enviados # 2',
            'otros_documentos_enviados3':'Otros documentos enviados # 3',
            'otros_documentos_enviados4':'Otros documentos enviados # 4',
            'otros_documentos_enviados5':'Otros documentos enviados # 5',
            'tiene_fichas':"Tiene fichas de productos ?",
            'numero_de_fichas':"Número de Fichas:",
            'num_documentos_solicitados_categoria':"Número de documentos solicitados",
            'observaciones_administrativas':'Observaciones Administrativas para Calidad',
            'contesta_reclamos_administrativos':'El proveedor contesta los reclamos dentro del tiempo esperado?',
            'contesta_reclamos_calidad':'El proveedor contesta los reclamos dentro del tiempo esperado?',
            'proveedor_mant_externo':'Atiende Mantenimiento externo?',
            'proveedor_ruta_fija':'Es Ruta Fija?',
   
   }
		
        widgets = {
            'giro_negocio':forms.TextInput(attrs={'class':'form-control'}),
            'monto_ventas_2018':forms.TextInput(attrs={'class':'form-control'}),
            'monto_ventas_2019':forms.TextInput(attrs={'class':'form-control'}),
            'monto_ventas_2020':forms.TextInput(attrs={'class':'form-control'}),
            'monto_ventas_2021':forms.TextInput(attrs={'class':'form-control'}),
            
            'antiguedad':forms.TextInput(attrs={'class':'form-control'}),
            'num_trabajadores_fijos':forms.TextInput(attrs={'class':'form-control'}),
            'num_clientes':forms.TextInput(attrs={'class':'form-control'}),
            'num_proveedores':forms.TextInput(attrs={'class':'form-control'}),
            'valores_empresa':forms.Textarea(attrs={'class':'form-control'}),
            'tieneweb':forms.Select(attrs={'class':'form-control'}),
            'web':forms.TextInput(attrs={'class':'form-control'}),
            'actividad':forms.Select(attrs={'class':'form-control'}),
            'otra_actividad':forms.TextInput(attrs={'class':'form-control'}),
            'empresa_tipo':forms.Select(attrs={'class':'form-control'}),
            'categoria_proveedor':forms.Select(attrs={'class':'form-control'}),
            'otra_categoria':forms.TextInput(attrs={'class':'form-control'}),
            'anios_como_proveedor':forms.TextInput(attrs={'class':'form-control'}),
            'ventas_ecofroz_2018':forms.TextInput(attrs={'class':'form-control'}),
            'ventas_ecofroz_2019':forms.TextInput(attrs={'class':'form-control'}),
            'ventas_ecofroz_2020':forms.TextInput(attrs={'class':'form-control'}),
            'ventas_ecofroz_2021':forms.TextInput(attrs={'class':'form-control'}),
            
            'subcontrata':forms.Select(attrs={'class':'form-control'}),
            'actividades_subcontratadas':forms.Textarea(attrs={'class':'form-control'}),
            'nombre_cooperativa_y_o_compania_pertenecen_vehiculos':forms.TextInput(attrs={'class':'form-control'}),
            'otro_sistema_calidad':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion_giro_negocio_otras_empresas':forms.TextInput(attrs={'class':'form-control'}),
            'tiene_certificado_ambiental':forms.Select(attrs={'class':'form-control'}),
            'describa_politica_ambiente':forms.Textarea(attrs={'class':'form-control'}),
            'descripcion_politica_responsabilidad_social':forms.Textarea(attrs={'class':'form-control'}),
            'mecanismo_satisfaccion_cliente':forms.Textarea(attrs={'class':'form-control'}),
            'sugerencia_proceso_compra': forms.Textarea(attrs={'class':'form-control'}),
            'sugerencia_proceso_pago':forms.Textarea(attrs={'class':'form-control'}),
            'sugerencia_proceso_recepcion':forms.Textarea(attrs={'class':'form-control'}),
            'sugerencia_relacion_comercial':forms.Textarea(attrs={'class':'form-control'}),
            'es_proveedor_maquinaria_o_equipo':forms.Select(attrs={'class':'form-control'}),
            'tipo_maquinaria_equipo_que_provee':forms.Textarea(attrs={'class':'form-control'}),
            'tipo_producto_servicio_provee':forms.Textarea(attrs={'class':'form-control'}),
            'proveedor_pesticidas_requisitos_indispensables':forms.Select(attrs={'class':'form-control'}),
            'proveedor_fertilizantes_requisitos_indispensables':forms.Select(attrs={'class':'form-control'}),
            'proveedor_foliares_requisitos_indispensables':forms.Select(attrs={'class':'form-control'}),
            'proveedor_materia_organica_requisitos_indispensables':forms.Select(attrs={'class':'form-control'}),
            #'tiene_fichas':forms.Select(attrs={'class':'form-control'}),
            #'numero_de_fichas':forms.TextInput(attrs={'class':'form-control', 'id':'numero_de_fichas'}),
            'num_documentos_solicitados_categoria':forms.TextInput(attrs={'class':'form-control'}),
            'observaciones_administrativas':forms.Textarea(attrs={'class':'form-control','rows':4}),
            
        }
		
            
      