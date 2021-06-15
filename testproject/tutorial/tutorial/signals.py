
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from service.models import Service
from django.contrib.auth.models import User


@receiver(post_save, sender=Service)
def created_service(sender, instance, created, **kwargs):
    if created:
        print('Услуга', instance, 'добавлена')


# post_save.connect(created_service, sender=Service)

@receiver(post_save, sender=Service)
def update_service(sender, instance, created, **kwargs):
    if not created:
        instance.user.save()
        print('Услуга', instance, 'изменена')


# @receiver(post_delete, sender=Service)
# def delete_service(sender, instance, **kwargs):
#     if instance.id.delete():
#         print(instance, 'deleted')

