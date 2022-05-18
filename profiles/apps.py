from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
    # //!  overwritting the ready method
    def ready(self):
        import profiles.signals
