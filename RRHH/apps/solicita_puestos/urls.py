from django.urls import path
from .views import *

urlpatterns = [
    path('', SolicitaPuestoList, name = 'listar_solicita_puesto'),
    path('form/', SolicitaPuestoCreateView.as_view(), name='crear_solicita_puesto'),
    path('form/edit/<int:pk>/', SolicitaPuestoUpdateView.as_view(), name='editar_solicita_puesto' ),
    path('delete/<int:pk>/', SolicitaPuestoDeleteView.as_view(), name='eliminar_solicita_puesto' )
    
]
