
from .models import ParamsSchema, HistoryParamsSchema
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


   
@receiver(pre_save, sender=ParamsSchema)
def save_history_paramsschema(sender, instance, **kwargs):
    HistoryParamsSchema.objects.create(
        paramsschema = instance,
        type = instance.type,
        body = instance.body,
    )