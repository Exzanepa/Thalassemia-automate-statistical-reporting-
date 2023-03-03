from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Image

from .models import noisemap





admin.site.register(Image)

admin.register(noisemap)
class noisemapadmin(ImportExportActionModelAdmin):
    list_display =('x','y','z')
