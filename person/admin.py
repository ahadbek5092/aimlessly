from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from person.models import Person, Genral, Uprav, Otdel
# Register your models here.
@admin.register(Genral)
class GenralAdmin(ImportExportModelAdmin):
    list_display = ('name', 'url')
    pass
@admin.register(Uprav)
class UpravAdmin(ImportExportModelAdmin):
    list_display = ('name', 'gend')

@admin.register(Otdel)
class OtdelAdmin(ImportExportModelAdmin):
    list_display = ('name', 'uprav')

@admin.register(Person)
class RersonAdmin(ImportExportModelAdmin):
    list_display = ('pod', 'kod', 'kat', 'fio')
    pass
