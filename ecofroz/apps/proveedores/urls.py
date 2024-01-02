"""ecofroz01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url

from .views import home, nuevo_registro, listar_proveedores, ProveedorDelete, ProveedorUpdate, \
render_template_x_tipo_proveedor, VerDocumentos, ver_preguntas, exportExcelEncuesta, BasicUploadView, \
verRespuestasEncuesta, verRespuestasCompara, exportExcelRespuestasXCategoria, verRespuestasEspecificas, \
cargaRespuestas, editarRespuestaEncuesta, listar_proveedores_para_adqui, calificaEcofroz, \
verPreguntasEspecificas,exportExcelGeneral,updateHead, auditoriayCambios,buscaCambios, \
eliminar_documentos, actualiza_contadores, verCalifSegmento, listar_proveedores_para_calidad, \
calificaEcofrozCalidad, confirma_completo, VerFichas, VerFichasAgricolas, EnviarACalidad, NotificaSuccess, \
verFichasCalidad, confirma_completo_agricola, confirma_revision_ficha, observaciones_revision_ficha, \
save_record_ficha_cal, save_observa_ficha_cal,accede_menu_subcategorias_agricolas_pes, \
accede_menu_subcategorias_agricolas_fol,accede_menu_subcategorias_agricolas_fer, \
accede_menu_subcategorias_agricolas_mao, actualizaCalificacionIndividual,VerHojasMSDS, \
actualizaCalificacionIndividualTest,VerEtiquetasProductos,verEtiquetasCalidad, \
save_observa_msds_cal,save_observa_eti_cal,save_record_msds_cal,save_record_eti_cal, \
verMSDSCalidad, observaciones_revision_msds, observaciones_revision_eti, verFichasFerCalidad, verFichasPesCalidad, \
verFichasFolCalidad,verFichasMaoCalidad,verFichasSemCalidad, verMSDSPesCalidad, verMSDSFolCalidad,verMSDSFerCalidad, \
verMSDSMaoCalidad,verMSDSSemCalidad,verAgrocalidadPesCalidad,verAgrocalidadFolCalidad,verAgrocalidadFerCalidad, \
verAgrocalidadMaoCalidad,verAgrocalidadSemCalidad, save_record_fecha_documento, verDocuSubcatesCalidad, verPlantillas, \
ConfirmaSuccessCarga, ver_proceso_calificacion, save_observa_docu_agro, auditaCabecera, auditaRespuestas,verExpiracionDocs, \
to_excelclass, actualizaMasivoFechaFicha

              
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('nuevo', nuevo_registro ,name='nuevo_registro'),
    path('nuevo', nuevo_registro ,name='nuevo_registro'),
    path('califica/<int:pk>', calificaEcofroz.as_view() ,name='califica_ecofroz'),
    path('califica_calidad/<int:pk>', calificaEcofrozCalidad,name='califica_ecofroz_calidad'),
    path('verfichasca/<int:pk>', verFichasCalidad,name='ver_fichas_calidad'),
   
    # path('verfichasferca/<int:pk>', verFichasFerCalidad,name='ver_fichas_fer_calidad'),
    # path('verfichaspesca/<int:pk>', verFichasPesCalidad,name='ver_fichas_pes_calidad'),
    # path('verfichasfolca/<int:pk>', verFichasFolCalidad,name='ver_fichas_fol_calidad'),
    # path('verfichasmaoca/<int:pk>', verFichasMaoCalidad,name='ver_fichas_mao_calidad'),
    # path('verfichassemca/<int:pk>', verFichasSemCalidad,name='ver_fichas_sem_calidad'),
    
    
    path('verhojasmsdsca/<int:pk>', verMSDSCalidad,name='ver_msds_calidad'),
    # path('verhojasmsdspesca/<int:pk>', verMSDSPesCalidad,name='ver_msds_pes_calidad'),
    # path('verhojasmsdsfolca/<int:pk>', verMSDSFolCalidad,name='ver_msds_fol_calidad'),
    # path('verhojasmsdsferca/<int:pk>', verMSDSFerCalidad,name='ver_msds_fer_calidad'),
    # path('verhojasmsdsmaoca/<int:pk>', verMSDSMaoCalidad,name='ver_msds_mao_calidad'),
    # path('verhojasmsdssemca/<int:pk>', verMSDSSemCalidad,name='ver_msds_sem_calidad'),

    # path('veragrocalidadpesca/<int:pk>', verAgrocalidadPesCalidad,name='ver_agrocalidad_pes_calidad'),
    # path('veragrocalidadfolca/<int:pk>', verAgrocalidadFolCalidad,name='ver_agrocalidad_fol_calidad'),
    # path('veragrocalidadferca/<int:pk>', verAgrocalidadFerCalidad,name='ver_agrocalidad_fer_calidad'),
    # path('veragrocalidadmaoca/<int:pk>', verAgrocalidadMaoCalidad,name='ver_agrocalidad_mao_calidad'),
    # path('veragrocalidadca/<int:pk>', verAgrocalidadSemCalidad,name='ver_agrocalidad_sem_calidad'),

    path('verdocusubcatesca/<int:pk>/<int:id>', verDocuSubcatesCalidad,name='ver_docu_subcates_calidad'),
    path('veretiquetasca/<int:pk>', verEtiquetasCalidad,name='ver_etiquetas_calidad'),
    path('listar', listar_proveedores,name='listar_proveedores'),
    path('listar_para_adqui', listar_proveedores_para_adqui,name='listar_proveedores_para_adqui'),
    path('listar_para_calidad', listar_proveedores_para_calidad,name='listar_proveedores_para_calidad'),
    #path('filtrar', filtrar_proveedores,name='filtrar_proveedores'),
    #path('filtrar', ver_preguntas,name='ver_preguntas'),
    path('preguntas', ver_preguntas,name='ver_preguntas'),
    path('proceso', ver_proceso_calificacion,name='ver_proceso_calificacion'),

    path('contadores', actualiza_contadores,name='actualiza_contadores'),
   
    path('preguntasespecificas', verPreguntasEspecificas,name='ver_preguntas_especificas'),
    
    path('eliminar/<int:pk>', ProveedorDelete.as_view(),name='eliminar_proveedor'),
    path('enviaracalidad/<int:pk>', EnviarACalidad,name='enviar_a_calidad'),
    path('notificasuccess', NotificaSuccess,name='notifica_success'),
    path('confirmasuccesscarga', ConfirmaSuccessCarga,name='confirma_success_carga'),
    
    path('editar/<int:pk>', ProveedorUpdate.as_view(),name='editar_proveedor'),
    # path('retroalimentacion/<int:pk>', retroalimentacionEcofroz,name='retroalimentacion_ecofroz'),
    # path('verdocumentos/<int:pk>', VerDocumentos.as_view(),name='ver_documentos'),
    path('toexcel/<int:pk>', exportExcelEncuesta,name='to_excel'),
    path('toexcelcat', exportExcelRespuestasXCategoria,name='to_excelcat'),
    path('respencuesta/<int:pk>', verRespuestasEncuesta,name='resp_encuesta'),
    path('comprespuestas', verRespuestasCompara,name='resp_encuesta_comp'),
    path('vercalifsegmento', verCalifSegmento,name='ver_calif_segmento'),
    
    path('respuestasespecificas', verRespuestasEspecificas,name='ver_respuestas_especificas'),
    path('editarespuesta/<int:pregunta>/<int:respuesta>/<int:prove>', editarRespuestaEncuesta,name='edita_respuestas'),
    path('toexcelgen', exportExcelGeneral,name='toexcelgen'),
    path('updatehead', updateHead,name='updatehead'),
    path('auditoria', auditoriayCambios,name='auditoria'),
    path('auditoriadetalle/<int:pk>', buscaCambios,name='auditoriadetalle'),

    path('auditoria_cabecera', auditaCabecera,name='auditoria_cabecera_csv'),
    # path('auditoria_detalle', auditaDetalle,name='auditoria_detalle'),
    path('audita_respuestas', auditaRespuestas,name='auditoria_respuestas'),

    path('eliminadocu/<int:pk>/<int:prove>', eliminar_documentos,name='eliminar_documentos'),
    path('saverecordfical/<int:pk>/<int:prove>', save_record_ficha_cal,name='save_record_ficha_cal'),
    
    path('saverecordfechadocumento/<int:pk>/<int:prove>', save_record_fecha_documento,name='save_fecha_documento'),
   
    path('saveobservafical/<int:pk>/<int:prove>', save_observa_ficha_cal,name='save_observa_ficha_cal'),
    path('saveobservadocuagro/<int:pk>/<int:prove>/<int:subcate>', save_observa_docu_agro,name='save_observa_docu_agro'),
    path('saverecordmsdscal/<int:pk>/<int:prove>', save_record_msds_cal,name='save_record_msds_cal'),
    path('saveobservamsdscal/<int:pk>/<int:prove>', save_observa_msds_cal,name='save_observa_msds_cal'),
    path('saveobservamsdscal/<int:pk>/<int:prove>', save_observa_msds_cal,name='save_observa_msds_cal'),
    path('saverecordetical/<int:pk>/<int:prove>', save_record_eti_cal,name='save_record_eti_cal'),
    path('saveobservaetical/<int:pk>/<int:prove>', save_observa_eti_cal,name='save_observa_eti_cal'),
    
    path('actualizacalif/<int:pk>', actualizaCalificacionIndividual,name='actualiza_calf_indi'),
    path('actualizacaliftest/<int:pk>', actualizaCalificacionIndividualTest,name='actualiza_calf_indi_test'),

    path('confirmarevcal/<int:id>/<int:pk>', confirma_revision_ficha,name='confirma_revision_ficha'),
    path('observaficrevcal/<int:pk>', observaciones_revision_ficha,name='observaciones_revision_ficha'),
    path('observamsdsrevcal/<int:pk>', observaciones_revision_msds,name='observaciones_revision_msds'),
    path('observaetirevcal/<int:pk>', observaciones_revision_eti,name='observaciones_revision_eti'),

    path('veropcionessubcatepes/<int:pk>/<str:respuesta>', accede_menu_subcategorias_agricolas_pes,name='accede_menu_subcategorias_agricolas_pes'),
    path('veropcionessubcatefol/<int:pk>/<str:respuesta>', accede_menu_subcategorias_agricolas_fol,name='accede_menu_subcategorias_agricolas_fol'),
    path('veropcionessubcatefer/<int:pk>/<str:respuesta>', accede_menu_subcategorias_agricolas_fer,name='accede_menu_subcategorias_agricolas_fer'),
    path('veropcionessubcatemao/<int:pk>/<str:respuesta>', accede_menu_subcategorias_agricolas_mao,name='accede_menu_subcategorias_agricolas_mao'),
  
  
    url(r'^(?P<pk>\d+)/basic-upload/$', BasicUploadView.as_view(), name='ver_documentos'),
    url(r'^(?P<pk>\d+)/ver-fichas/$', VerFichas.as_view(), name='ver_fichas'),
    url(r'^(?P<pk>\d+)/ver-hojas-msds/$', VerHojasMSDS.as_view(), name='ver_hojas_msds'),
    url(r'^(?P<pk>\d+)/ver-etiquetas-productos/$', VerEtiquetasProductos.as_view(), name='ver_etiquetas_productos'),


    url(r'^(?P<pk>\d+)/(?P<subcate_id>\d+)/ver-fichas-agricolas/$', VerFichasAgricolas.as_view(), name='ver_fichas_agricolas'),
    
    # url(r'^(?P<pk>\d+)/ver-fichas/$', VerFichas.as_view(), name='ver_fichas_foliares'),
    # url(r'^(?P<pk>\d+)/ver-fichas/$', VerFichas.as_view(), name='ver_fichas_fertilizantes'),
    # url(r'^(?P<pk>\d+)/ver-fichas/$', VerFichas.as_view(), name='ver_fichas_mao'),
    

    path('confirmacompleto/<int:pk>/<int:prove>',confirma_completo,name='confirma_completo'),
    path('confirmacompletoagricola/<int:pk>/<int:prove>/<str:tipo>',confirma_completo_agricola,name='confirma_completo_agricola'),
    path('cargarespuestas', cargaRespuestas,name='carga_respuestas'),
    # path('cargarespuestaspru', cargaRespuestasPru,name='carga_respuestas_pru'),
    
    path('verplantillas', verPlantillas,name='ver_plantillas'),
    path('verexpiraciondocumentos', verExpiracionDocs,name='ver_expiracion_docs'),
    path('toexcel', to_excelclass.as_view(),name='to_excelclass'),
    path('upfec', actualizaMasivoFechaFicha ,name='actualiza_fecha_update_ficha'),
    
 
]


