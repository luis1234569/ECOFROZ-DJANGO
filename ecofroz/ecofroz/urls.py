"""ecofroz URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import handler404, handler500

from apps.usuarios.views import login, Inicio, logout, LandingPage, EnConstruccion, Sia
# from apps.ordenTrabajo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='home'),
    # path('', Inicio.as_view(), name = 'home'),
    path('sia', Sia.as_view(), name='sia'),
    path('landing', LandingPage.as_view(), name='landing'),
    path('cons', EnConstruccion.as_view(), name='cons'),
    # path('autentificacion/', include(('apps.usuarios.urls', 'autentificacion'))),
    path('logout', logout, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ordenpedido/', include(('apps.ordenPedido.urls', 'ordenpedido'))),
    path('multiordenpedido/', include(('apps.multipleOrdenPedido.urls', 'multiordenpedido'))),
    path('activos/', include(('apps.activos.urls', 'activos'))),
    path('proveedores/', include(('apps.proveedores.urls', 'proveedores'))),
    path('personal/', include(('apps.controlPersonal.urls', 'personal'))),
    path('trabajos/', include(('apps.ordenTrabajo.urls', 'trabajos'))),
    path('soporte/', include(('apps.soporteIt.urls', 'soporte'))),
    path('trabajosinternos/', include(('apps.trabajosInternos.urls', 'trabajosinternos'))),
    path('photos/', include(('apps.photos.urls', 'photos'))),
    path('parametrosglobales/', include(('apps.parametrosGlobales.urls', 'parametrosglobales'))),
    path('procesosadministrativos/', include(('apps.procesosAdministrativos.urls', 'procesosadministrativos'))),
    
    path('password_update/', auth_views.PasswordChangeView.as_view(template_name='auth/password_changed_form.html'), name='password_change'),
    path('password_update_done', auth_views.PasswordChangeDoneView.as_view(template_name='auth/password_change_done.html'), name='password_change_done'),
   
   
    # path('password_update/', auth_views.PasswordChangeView.as_view(), {
    #     'template_name':'auth/password_change_form.html',
    #     'post_change_redirect':'auth_password_change_done',   
    # }, name='password_change'),
    # path('password_update_done', auth_views.PasswordChangeDoneView.as_view(), {
    #     'template_name':'auth/password_change_done.html'
    # }, name='password_change_done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
handler404 = 'apps.ordenTrabajo.views.handler404'
