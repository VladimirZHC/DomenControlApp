from django.contrib import admin

from . import models

admin.site.register(models.GroupPolicy)
admin.site.register(models.Division)
admin.site.register(models.DomenUser)
admin.site.register(models.Computers)
admin.site.register(models.SchemaParams)

