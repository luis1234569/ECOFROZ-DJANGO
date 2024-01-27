from django.shortcuts import render
from django import template
import random

register = template.Library()

@register.simple_tag
def random_color():
    colors = ['#f8d7da', '#d4edda', '#cce5ff', '#fff3cd', '#d1ecf1', '#f5c6cb']
    return random.choice(colors)


# Create your views here.
def listarLugares(request):
    # Aquí, obtendrías los datos reales del usuario y los lugares visitados
    nombre_usuario = 'Luis'
    lugares_visitados = [
    {'nombre': 'Parque Central', 'descripcion': 'Un hermoso parque en el centro de la ciudad.', 'fecha_visita': '2024-01-20', 'hora_visita': '15:00', 'imagen_url': 'url_a_imagen_del_parque.jpg'},
    {'nombre': 'Museo de Historia', 'descripcion': 'Un museo interactivo con exposiciones sobre la historia local e internacional.', 'fecha_visita': '2024-01-22', 'hora_visita': '10:30', 'imagen_url': 'url_a_imagen_del_museo.jpg'},
    {'nombre': 'Playa Los Cocos', 'descripcion': 'Una playa tranquila y pintoresca, perfecta para un día de descanso.', 'fecha_visita': '2024-02-05', 'hora_visita': '12:00', 'imagen_url': 'url_a_imagen_de_la_playa.jpg'},
    {'nombre': 'Biblioteca Municipal', 'descripcion': 'Una amplia biblioteca con una colección variada y zonas de lectura confortables.', 'fecha_visita': '2024-01-28', 'hora_visita': '16:00', 'imagen_url': 'url_a_imagen_de_la_biblioteca.jpg'},
    {'nombre': 'Mirador de la Ciudad', 'descripcion': 'Ofrece las mejores vistas panorámicas de la ciudad, ideal para visitar al atardecer.', 'fecha_visita': '2024-02-10', 'hora_visita': '18:30', 'imagen_url': 'url_a_imagen_del_mirador.jpg'},
    {'nombre': 'Jardín Botánico', 'descripcion': 'Un espacio dedicado a la conservación de plantas y flores, con recorridos educativos.', 'fecha_visita': '2024-02-15', 'hora_visita': '11:00', 'imagen_url': 'url_a_imagen_del_jardin_botanico.jpg'}
    ]

    context = {'nombre_usuario': nombre_usuario, 'lugares_visitados': lugares_visitados}
    return render(request, 'listar-lugar-ubica.html', context)


def generar_qr(request):
    
    return render()