# Generated by Django 4.2.4 on 2023-09-07 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customize', '0011_alter_cardmodel_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='buttonmodel',
            name='add_form',
            field=models.BooleanField(blank=True, null=True, verbose_name='Форма номер 2'),
        ),
    ]
