# Generated by Django 4.0.1 on 2022-07-01 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signupapp', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donors',
            name='image',
        ),
    ]
