from django import forms
from .models import proyectos_contabilidad

# class nombreProyectoForm(forms.Form):
#     nombre_proyecto = forms.ModelChoiceField(queryset = proyectos_contabilidad.objects.all(), widget = forms.Select(attrs={ 'required': 'false'}))

#     def __init__(self, *args, **kwargs):
#         super(NombreProyectoForm, self).__init__(*args, **kwargs)
#         self.fields['nombre_proyecto'].queryset = proyectos_contabilidad.objects.filter(activo=True).order_by('nombre_proyecto')
#         self.fields['nombre_proyecto'].label_from_instance = lambda obj: "%s" % (obj.nombre_proyecto)
