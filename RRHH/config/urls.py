
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('apps.solicita_puestos.urls', 'solicita_puestos')))
    # path('', HttpResponse('<h1>Hello</h1>'))
]
