from django.contrib import admin

from management.models import *


class ServiceAdmin(admin.ModelAdmin):
    pass


class InstanciasaplicacionesAdmin(admin.ModelAdmin):
    list_display = ('aplicacion', 'identificador', 'alta')


class ContractAdmin(admin.ModelAdmin):
    pass


class ClientAdmin(admin.ModelAdmin):
    pass


class PartnersAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ticker')


admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Instanciasaplicaciones, InstanciasaplicacionesAdmin)
admin.site.register(Partners, PartnersAdmin)
