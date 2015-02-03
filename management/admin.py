from django.contrib import admin

# Register your models here.
from management import models as management_models
from django.db.models.base import ModelBase
from management.models import *

admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Service)
admin.site.register(Instanciasaplicaciones)
admin.site.register(Partners)
