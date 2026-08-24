
from django.apps import AppConfig


class SunamoebiConfig(AppConfig):

    name = 'Sunamoebi'

    def ready(self):
        import Sunamoebi.signals