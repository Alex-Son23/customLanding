# Generated by Django 4.2.4 on 2023-09-07 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customize', '0013_alter_buttonmodel_add_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название новости')),
                ('href', models.TextField(verbose_name='Ссылка')),
                ('date', models.CharField(max_length=64, verbose_name='Дата публикации новости')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
