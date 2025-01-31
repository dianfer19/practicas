from django.contrib import admin

from prueba.models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'edad',  'email', 'telefono', 'direccion', 
                    )
    search_fields = ('nombre', 'apellido')
    list_filter = ('created', 'updated')

# Register your models here.
admin.site.register(Author, AuthorAdmin)