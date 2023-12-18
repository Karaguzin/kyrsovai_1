from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    Desc = models.TextField('Описание')
    URL = models.CharField(max_length=25, default='')

    def __str__(self):
        return self.title

class Drug(models.Model):
    purpose = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    img = models.TextField()
    slug = models.SlugField(max_length=255, default='')

    class Meta:
        verbose_name = 'Лекарства'
        verbose_name_plural = 'Лекарства'