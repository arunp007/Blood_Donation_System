# Generated by Django 4.0.1 on 2022-09-22 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0012_rename_authentication_donors_location_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipients',
            old_name='authentication',
            new_name='location',
        ),
        migrations.RemoveField(
            model_name='hospitals',
            name='authentication',
        ),
        migrations.RemoveField(
            model_name='recipients',
            name='pin',
        ),
    ]
