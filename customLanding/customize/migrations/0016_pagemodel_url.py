# Generated by Django 4.2.4 on 2023-09-08 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customize', '0015_pagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagemodel',
            name='url',
            field=models.TextField(default=' ', verbose_name='URL'),
            preserve_default=False,
        ),
    ]
