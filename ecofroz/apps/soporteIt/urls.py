from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from .views import IngresoTicket, ordenesSoporte, ordenesSoporteInt, IngresoTicketSop, EditaTicketSop, \
                   reporteSoporte

urlpatterns = [
    path('listar_soporte/', ordenesSoporte, name = 'listar_soporte'),
    path('generar_ticket/', IngresoTicket.as_view(), name = 'generar_ticket'),
    path('listar_soporte_int/', ordenesSoporteInt, name = 'listar_soporte_int'),
    path('generar_ticket_int/', IngresoTicketSop.as_view(), name = 'generar_ticket_int'),
    path('edita_ticket_int/<pk>', EditaTicketSop.as_view(), name = 'edita_ticket_int'),
    path('reporte_int/', reporteSoporte, name = 'reporte_int'),
]