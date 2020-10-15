from django.contrib import admin
from .models import Team, Testemonial


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'ativo', 'modificado')


@admin.register(Testemonial)
class TestemonialAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'modificado')
