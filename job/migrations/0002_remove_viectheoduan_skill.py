# Generated by Django 2.2.1 on 2019-05-24 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viectheoduan',
            name='skill',
        ),
    ]
