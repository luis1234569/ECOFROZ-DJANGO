
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('apps.solicita_puestos.urls', 'solicita_puestos')))
    # path('', HttpResponse('<h1>Hello</h1>'))
]
