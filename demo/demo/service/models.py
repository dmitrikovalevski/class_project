from django.db import models
from django.urls import reverse


class Service(models.Model):
    name = models.CharField('Название услуги', max_length=200)
    category = models.CharField('Категория услуг', max_length=200)
    description = models.TextField('Описание услуги')
    price = models.IntegerField('Цена', blank=False)
    photo = models.ImageField(upload_to='transfers')

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('post_detail', args=[(self.id)])
