from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    title = models.CharField('Ваше предложение', max_length=200, null=True)
    description = models.TextField('Подробное описание', null=True)
    price = models.FloatField('Цена услуги', null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    picture = models.ImageField(upload_to='service', null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

