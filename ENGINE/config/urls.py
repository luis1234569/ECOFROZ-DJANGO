
from django.contrib import admin
from django.urls import path
from procesosAdministrativos.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',listarLugares)
]
