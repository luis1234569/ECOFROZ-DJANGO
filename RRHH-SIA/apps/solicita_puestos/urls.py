from django.urls import path
from .views import *

urlpatterns = [
    path('', SolicitaPuestoList, name = 'listar_solicita_puesto'),
    path('form-solicita-puesto/', SolicitaPuestoCreateView.as_view(), name='crear_solicita_puesto'),
    path('form-solicita-puesto/edit/<int:pk>/', SolicitaPuestoUpdateView.as_view(), name='editar_solicita_puesto' ),
    path('delete-solicita-puesto/<int:pk>/', SolicitaPuestoDeleteView.as_view(), name='eliminar_solicita_puesto' ),
    path('list-solicita-puesto-aprueba/', SolicitaPuestoListAprueba, name='listar_solicita_puesto_aprueba'  ),
    path('form-solicita-puesto_aprueba/edit/<int:pk>/', SolicitaPuestoApruebaUpdateView.as_view(), name='editar_solicita_puesto_aprueba' ),
    path('aprobado/<int:pk>', SolicitarPuestoAprobar, name='aprobar_solicita_puesto'),
    path('rechazado/<int:pk>', rechazaDirect, name='rechazado_solicita_puesto'),
    path('procesosadministrativos/solicita-cargo-list/', SolicitaPuestoListRRHH, name='listar_solicita_puesto_rrhh'  ),
    # path('procesosadministrativos/solicita-cargo-list', SolicitaCargoList, name='listar_solicita_cargo_aprobado'), 
    path('procesosadministrativos/solicita-cargo-notes/<int:pk>', SolicitaCargoNotasRRHH, name='gestionar_solicita_cargo_aprobado'), 
    path('ubica_area_ajax', ubicaAreaAjax, 
         name='ubica_area_ajax'),
    path('procesosadministrativos/solicita-cargo-notes/ajax_save/', ajax_save, name='ajax_save'),
    
    path('procesosadministrativos/solicita-cargo-notes/ajax_save_status/', ajax_save_status, name='ajax_save_status'),
    
    path('none', none, name='none')
]
