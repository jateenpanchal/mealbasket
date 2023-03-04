from django.apps import AppConfig


class CustomerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer'

    def ready(self):
        import customer.signals
        
        from django.apps import AppConfig

# class MyAppConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'myapp'

#     def ready(self):
#         import myapp.signals
