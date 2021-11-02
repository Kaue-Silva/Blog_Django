from django.contrib import admin
from core.models import Postagem

# Register your models here.
class PostagemAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'data_criacao']
    list_filter = ['autor', 'data_criacao']

admin.site.register(Postagem, PostagemAdmin)
    