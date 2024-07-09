from django.db import models

# Create your models here.
class events_news(models.Model):
        title = models.CharField('Название новости', max_length=50)
        name = models.CharField('Автор новости', max_length=50)
        short_description = models.CharField('Краткое описание новости', max_length=200)
        text = models.TextField('Новость')
        pub_date = models.DateTimeField('Дата публикации')

        class Meta:
                verbose_name = 'Новость'
                verbose_name_plural = 'События и новости'