# Generated by Django 4.0.1 on 2022-06-13 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipientapp', '0004_urgent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urgent',
            name='blood',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='urgent',
            name='location',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='urgent',
            name='name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='urgent',
            name='phone',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterModelTable(
            name='urgent',
            table='urgentblood',
        ),
    ]
