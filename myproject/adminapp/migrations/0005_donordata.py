# Generated by Django 4.0.1 on 2023-01-16 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donordata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('blood', models.TextField(max_length=100)),
                ('location', models.TextField(max_length=100)),
                ('phone', models.TextField(max_length=100)),
            ],
        ),
    ]
