# Generated by Django 4.0.1 on 2023-01-12 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_alter_notification_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notification',
        ),
    ]