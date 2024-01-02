from import_export import resources
from .models import carga_respuestas, carga_respuestas_prod_serv_varios

class RespuestasResource(resources.ModelResource):  
    class Meta:  
#        model = carga_respuestas  
        model = carga_respuestas_prod_serv_varios
        import_id_fields = ('marca_temporal',)


# class UpdateResource(resources.ModelResource):
#     def before_import(self, dataset, using_transactions, dry_run, **kwargs):
#        dataset.headers = ['marca_temporal', 'p001','p002']

   
#     class Meta:
#         model = carga_respuestas_prod_serv_varios
#         import_id_fields = ('marca_temporal',)
        