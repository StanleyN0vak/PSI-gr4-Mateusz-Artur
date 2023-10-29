from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Adres)
admin.site.register(Ksiazka)
admin.site.register(Klient)
admin.site.register(Zamowienie)
admin.site.register(StatusZamowienia)
admin.site.register(SzczegolyZamowienia)
admin.site.register(StatusKsiazka)
admin.site.register(Gatunek)
admin.site.register(Autor)
admin.site.register(Wydawnictwo)
admin.site.register(Opinie)
