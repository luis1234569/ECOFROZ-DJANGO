class SiaRouter:
    router_app_labels = {'activo'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.router_app_labels:
            return 'sia_db'
        return None

    
    