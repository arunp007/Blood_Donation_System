# Generated by Django 4.0.1 on 2022-09-22 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0011_hospitals'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donors',
            old_name='authentication',
            new_name='location',
        ),
        migrations.RemoveField(
            model_name='donors',
            name='pin',
        ),
    ]