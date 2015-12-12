from django.contrib import admin
from .models import Producto,Sector,Subsector,Produccion


admin.site.register(Subsector)
admin.site.register(Sector)


class AdminProduccionInline(admin.TabularInline):
    model = Produccion
    extra = 1

class AdminProducto(admin.ModelAdmin):
    inlines = [
        AdminProduccionInline,
        
    ]

admin.site.register(Producto,AdminProducto)




"""
class AdminProduccionInicialInline(admin.TabularInline):
    model = Produccion_periodo_inicial
    extra = 1

class AdminProduccionFinalInline(admin.TabularInline):
    model = Produccion_periodo_final
    extra = 1

class AdminProducto(admin.ModelAdmin):
    inlines = [
        AdminProduccionInicialInline,
        AdminProduccionFinalInline,
        # AdminProduccionResultadoInline,
    ]

admin.site.register(Producto,AdminProducto)

admin.site.register(Produccion_resultado)
"""