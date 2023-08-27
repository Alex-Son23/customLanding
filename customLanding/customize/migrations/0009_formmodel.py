# Generated by Django 4.2.4 on 2023-08-26 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customize', '0008_cardmodel_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название формы')),
                ('mail_to', models.CharField(max_length=128, verbose_name='Почта куда отправлять данные пользователей')),
            ],
            options={
                'verbose_name': 'Форма',
                'verbose_name_plural': 'Формы',
            },
        ),
    ]