from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Tym, Hrac, Zapas, StatistikaHrace

admin.site.register(Tym)
admin.site.register(Hrac)
admin.site.register(Zapas)
admin.site.register(StatistikaHrace)