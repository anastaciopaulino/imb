from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
	laytout = 'horizontal'	

class SystemConfig(AppConfig):
    name = 'system'


