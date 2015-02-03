from django.contrib import admin

# Register your models here.
from management import models as management_models
from django.db.models.base import ModelBase

# Very hacky!
for name, var in management_models.__dict__.items():
    if type(var) is ModelBase:
        admin.site.register(var)