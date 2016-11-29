from django.contrib import admin
from models import *
# Register your models here.

class ImageCarruselInline(admin.TabularInline):
	model = ImageCarrusel

class CarruselAdmin(admin.ModelAdmin):
	inlines = [ImageCarruselInline,]

admin.site.register(Pagina)
admin.site.register(Bloque)
admin.site.register(Carrusel,CarruselAdmin)
admin.site.register(ImageCarrusel)