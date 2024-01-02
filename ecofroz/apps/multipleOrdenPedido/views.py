import logging
import io
from io import BytesIO
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404, FileResponse
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import EmailMessage, EmailMultiAlternatives, send_mail
from django.template import context, loader
from django.contrib.sites.shortcuts import get_current_site
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
#from wkhtmltopdf.views import PDFTemplateView

from .models import OrdenesPedidosMulti, DetallePedidoMulti, CotizaPedidoMulti
from .forms import OrdenMultiForm, DetMultiForm, DetMultiFormSet
from apps.usuarios.models import User, Cotizador, Autorizador, Generador, Email
from apps.activos.models import activo_tipo, desc_activo, activo_nomenclatura, activo_grupo, \
    activo_depar, activo_areas

# Create your views here.

logger = logging.getLogger(__name__)

### FUNCIONES INTERNAS ###

def envioMail(subject, email, template, queryset, queryset2):
    html_message = loader.render_to_string(
        'ordenPedido/pedidotmp/%s' %template,
            {
                'aprob':queryset,
                'aprob2':queryset2,
            }
        )
    email_subject = subject
    to_list = email
    mail = EmailMultiAlternatives(
            email_subject, '', '', [to_list])
    mail.attach_alternative(html_message, "text/html")
    try:
        mail.send()
    except:
        logger.error("Unable to send mail.")

### VISTAS ###

def ordenesPedidoMulti(request):
    queryset = request.GET.get("buscar")
    if queryset:
        orden = OrdenesPedidosMulti.objects.filter(
            Q(numpedido__icontains = queryset) |
            Q(numproyecto__icontains = queryset) 
        ).filter(usuario_solicita_id = request.user.id).distinct()
    else:
        orden = OrdenesPedidosMulti.objects.filter(usuario_solicita_id = request.user.id)
    return render(request, 'multiOrdenPedido/listar_ordenes.html', {'form':orden})

def ingresoPedidoMulti(request):
    template_name = 'multiOrdenPedido/ingreso_pedido.html'
    if request.method == 'GET':
        form = OrdenMultiForm(request.GET or None)
        form2 = DetMultiFormSet(request.GET or None, queryset=DetallePedidoMulti.objects.none())
    elif request.method == 'POST':
        form = OrdenMultiForm(request.POST, request.FILES)
        form2 = DetMultiFormSet(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            print(form)
            print(form2)
            pedido = form.save()
            for i in form2:
                detalle = i.save(commit=False)
                detalle.numpedido = pedido
                detalle.save()
            
            return redirect('ordenpedido:listar_multi_ordenes')

    return render(request, template_name, {'form':form, 'form2':form2})

def editaPedidoMulti(request):
    template_name = 'multiOrdenPedido/ingreso_pedido.html'
    if request.method == 'GET':
        form = OrdenMultiForm(request.GET or None)
        form2 = DetMultiFormSet(request.GET or None, queryset=DetallePedidoMulti.objects.none())
    elif request.method == 'POST':
        form = OrdenMultiForm(request.POST, request.FILES)
        form2 = DetMultiFormSet(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            print(form)
            print(form2)
            pedido = form.save()
            for i in form2:
                detalle = i.save(commit=False)
                detalle.numpedido = pedido
                detalle.save()
            
            return redirect('ordenpedido:listar_multi_ordenes')

    return render(request, template_name, {'form':form, 'form2':form2})