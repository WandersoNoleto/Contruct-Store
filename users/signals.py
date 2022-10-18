from django.db.models.signals import post_save
from django.dispatch import receiver
from rolepermissions.roles import assign_role

from users.models import Users


@receiver(post_save, sender=Users)
def define_permissions(sender, instance, created, **kwargs):
    if created:
        if instance.position == "V":
            assign_role(instance, 'seller')
        elif instance.position == "G":
            assign_role(instance, 'manager')
