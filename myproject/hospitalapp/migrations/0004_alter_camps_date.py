# Generated by Django 4.0.1 on 2022-06-13 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0003_rename_organizer_camps_camp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camps',
            name='date',
            field=models.DateTimeField(max_length=100),
        ),
    ]