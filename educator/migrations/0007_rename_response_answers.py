# Generated by Django 3.2 on 2021-05-19 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educator', '0006_response'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='response',
            new_name='answers',
        ),
    ]
