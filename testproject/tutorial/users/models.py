from django.db import models
from django.contrib.auth.models import User


class UserAccount(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile', null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def delete(self, *args, **kwargs):
        self.picture.delete()
        super().delete(*args, **kwargs)
