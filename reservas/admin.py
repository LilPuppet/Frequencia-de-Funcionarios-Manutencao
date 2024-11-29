from django.contrib import admin

from reservas.models import ReservaModel, SalaModel

# Register your models here.

admin.site.register(SalaModel)
admin.site.register(ReservaModel)