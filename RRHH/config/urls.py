
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.puestos.urls'))
    # path('', HttpResponse('<h1>Hello</h1>'))
]
