from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title


class Img(models.Model):
    image = models.FileField(upload_to='post_img')
    model = models.OneToOneField(Post, null=True, on_delete=models.CASCADE)
