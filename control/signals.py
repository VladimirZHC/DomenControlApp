from .models import ParamsSchema, HistoryParamsSchema, GroupPolicy, HistoryGroupPolicy
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


# @receiver(post_save, sender=GroupPolicy)
# def create_history_group_policy(sender, instance, created, **kwargs):
#     if created:
#         HistoryGroupPolicy.objects.create(
#         history_of = instance,
#         name = instance.name,
#         body = instance.body,
#     )
        
@receiver(post_save, sender=GroupPolicy)
def save_history_group_policy(sender, instance, **kwargs):
        HistoryGroupPolicy.objects.create(
        history_of = instance,
        name = instance.name,
        body = instance.body,
    )
        


   
@receiver(pre_save, sender=ParamsSchema)
def save_history_paramsschema(sender, instance, **kwargs):
    HistoryParamsSchema.objects.create(
        type = instance,
        body = instance.body,
    )