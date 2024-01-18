from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Address)
admin.site.register(Book)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Opinion)