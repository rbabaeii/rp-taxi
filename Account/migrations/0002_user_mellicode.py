# Generated by Django 4.1.2 on 2022-11-12 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mellicode',
            field=models.CharField(default='', max_length=10, verbose_name='کدملی'),
            preserve_default=False,
        ),
    ]