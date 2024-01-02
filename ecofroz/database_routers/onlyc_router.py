class OnlyCSqlRouter:
    router_app_labels = {'ONLYCONTROL'}
    # router_app_labels = {'recepcionMp'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.router_app_labels:
            return 'onlyc_db'
        return None