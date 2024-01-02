from import_export import resources
from .models import InventarioSemanal

class InvResource(resources.ModelResource):  
    class Meta:  
        model = InventarioSemanal
        import_id_fields = ('producto',)



        