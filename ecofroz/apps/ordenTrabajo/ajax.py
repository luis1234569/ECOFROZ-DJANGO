from django.http import JsonResponse

from apps.activos.models import activo_ubica, activo_areas

def get_areas(request):
    ubica_id = request.GET.get('ubica')
    print(ubica_id)
    ubica_id = 1
    areas = activo_areas.objects.none()
    options = '<option value="" selected="selected">-------</option>'
    if ubica_id:
        areas = activo_areas.objects.filter(area_ubica=ubica_id)
        # print(areas.pk)
        for area in areas:
            options += '<option value="%s">%s</option)' % (areas, areas)
        response = {}
        response['areas'] = options
        print(response)
        return JsonResponse(response)
        