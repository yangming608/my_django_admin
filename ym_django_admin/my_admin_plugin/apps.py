from django.apps import AppConfig
from django.contrib import admin
# admin.site.register()
class MyAdminPluginConfig(AppConfig):
    name = 'my_admin_plugin'
    def ready(self):
        super(MyAdminPluginConfig,self).ready()

        from django.utils.module_loading import autodiscover_modules
        autodiscover_modules("my_admin")