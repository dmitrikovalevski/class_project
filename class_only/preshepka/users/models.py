from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    image = models.ImageField(upload_to='user', null=True)
    phone = models.CharField(max_length=20, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


