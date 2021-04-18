from django.apps import AppConfig


class User1Config(AppConfig):
    name = 'user1'

    def ready(self):
        import user1.signals  
