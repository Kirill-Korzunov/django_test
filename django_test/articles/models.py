from django.db import models

class Article(models.Model):
    title = models.CharField('Название', max_length=255)
    text = models.TextField('Содержание')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    modified = models.DateTimeField('Дата изменения', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
