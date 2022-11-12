# Generated by Django 4.1.2 on 2022-11-12 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_user_mellicode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Address',
            field=models.CharField(max_length=100, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Age',
            field=models.IntegerField(default=0, verbose_name='سن'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('مذکر', 'آقا'), ('مونث', 'خانم')], default='مذکر', max_length=5, verbose_name='جنسیت'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_driver',
            field=models.BooleanField(default=False, verbose_name='وضعیت راننده بودن'),
        ),
    ]
