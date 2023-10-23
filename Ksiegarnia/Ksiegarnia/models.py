from django.db import models


class Post(models.Model):
    active = models.BooleanField(verbose_name='aktywny', default=False)
    title = models.CharField(max_length=255, verbose_name='tytuł')
    slug = models.SlugField(unique=True)
    body = models.TextField(verbose_name='treść')
    lead = models.TextField(verbose_name='zajawka')

    def __str__(self):
        return self.title