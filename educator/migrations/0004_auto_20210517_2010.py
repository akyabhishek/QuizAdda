# Generated by Django 3.2 on 2021-05-17 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educator', '0003_auto_20210511_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='enddate',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='endtime',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='pubdate',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='pubtime',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='startdate',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='starttime',
        ),
    ]