# Generated by Django 4.2.4 on 2023-08-26 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customize', '0007_cardmodel_href'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardmodel',
            name='name',
            field=models.CharField(default='', max_length=64, verbose_name='Название'),
            preserve_default=False,
        ),
    ]
