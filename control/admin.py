from django.contrib import admin

from . import models

admin.site.register(models.GroupPolicy)
admin.site.register(models.OrgUnit)
admin.site.register(models.DomainUser)
admin.site.register(models.Host)
admin.site.register(models.ParamsSchema)
admin.site.register(models.HistoryParamsSchema)
admin.site.register(models.HistoryGroupPolicy)
