# Generated by Django 5.0.6 on 2024-07-10 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='events_news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название новости')),
                ('name', models.CharField(max_length=50, verbose_name='Автор новости')),
                ('short_description', models.CharField(max_length=200, verbose_name='Краткое описание новости')),
                ('text', models.TextField(verbose_name='Новость')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'События и новости',
            },
        ),
    ]
