# Generated by Django 4.2.4 on 2023-09-08 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customize', '0014_newsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Title страницы')),
                ('description', models.CharField(max_length=256, verbose_name='Description страницы')),
                ('header', models.TextField(verbose_name='Заголовок страницы')),
                ('media_image', models.ImageField(upload_to='images/')),
                ('text', models.TextField(verbose_name='Текст страницы')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
        ),
    ]