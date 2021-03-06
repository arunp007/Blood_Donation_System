# Generated by Django 4.0.1 on 2022-07-06 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.TextField(max_length=100)),
                ('lname', models.TextField(max_length=100)),
                ('blood', models.TextField(max_length=100)),
                ('aadhaar', models.TextField(max_length=100)),
                ('day', models.TextField(max_length=100)),
                ('month', models.TextField(max_length=100)),
                ('year', models.TextField(max_length=100)),
                ('gender', models.TextField(max_length=100)),
                ('address', models.TextField(max_length=100)),
                ('state', models.TextField(max_length=100)),
                ('district', models.TextField(max_length=100)),
                ('pin', models.TextField(max_length=100)),
                ('phone', models.TextField(max_length=100)),
                ('email', models.TextField(max_length=100)),
                ('password', models.TextField(max_length=100)),
                ('cpassword', models.TextField(max_length=100)),
                ('authentication', models.TextField(max_length=50)),
            ],
            options={
                'db_table': 'donordetails',
            },
        ),
        migrations.CreateModel(
            name='Hospitals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.TextField(max_length=100)),
                ('address', models.TextField(max_length=100)),
                ('location', models.TextField(max_length=100)),
                ('state', models.TextField(max_length=100)),
                ('district', models.TextField(max_length=100)),
                ('pin', models.TextField(max_length=100)),
                ('phone', models.TextField(max_length=100)),
                ('email', models.TextField(max_length=100)),
                ('password', models.TextField(max_length=100)),
                ('cpassword', models.TextField(max_length=100)),
                ('authentication', models.TextField(max_length=50)),
            ],
            options={
                'db_table': 'hospitaldetails',
            },
        ),
        migrations.CreateModel(
            name='Recipients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.TextField(max_length=100)),
                ('lname', models.TextField(max_length=100)),
                ('blood', models.TextField(max_length=100)),
                ('aadhaar', models.TextField(max_length=100)),
                ('day', models.TextField(max_length=100)),
                ('month', models.TextField(max_length=100)),
                ('year', models.TextField(max_length=100)),
                ('gender', models.TextField(max_length=100)),
                ('address', models.TextField(max_length=100)),
                ('state', models.TextField(max_length=100)),
                ('district', models.TextField(max_length=100)),
                ('pin', models.TextField(max_length=100)),
                ('phone', models.TextField(max_length=100)),
                ('email', models.TextField(max_length=100)),
                ('password', models.TextField(max_length=100)),
                ('cpassword', models.TextField(max_length=100)),
                ('authentication', models.TextField(max_length=50)),
            ],
            options={
                'db_table': 'recipientdetails',
            },
        ),
    ]
