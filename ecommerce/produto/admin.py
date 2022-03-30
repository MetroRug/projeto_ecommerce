from pyexpat import model
from django.contrib import admin
from . import models


class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1


class ProdutoAdmn(admin.ModelAdmin):
    inlines = [
        VariacaoInline
    ]


admin.site.register(models.Produto, ProdutoAdmn)
admin.site.register(models.Variacao)
