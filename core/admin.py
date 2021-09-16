from django.contrib import admin
from core.models import Evento

# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id','titulo', 'dataEvento', 'dataCriacaoEvento')
    list_filter = ('titulo', 'dataEvento')

admin.site.register(Evento, EventoAdmin)