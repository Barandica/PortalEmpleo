from django.contrib import admin
from .models import TipoDocumento, Ciudad, Personas, TipoContrato, Cargos, Plazas

admin.site.register(TipoDocumento)
admin.site.register(Ciudad)
admin.site.register(Personas)
admin.site.register(TipoContrato)
admin.site.register(Cargos)
admin.site.register(Plazas)

