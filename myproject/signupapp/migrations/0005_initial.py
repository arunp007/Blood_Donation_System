# Generated by Django 4.0.1 on 2022-07-01 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signupapp', '0004_delete_donor'),
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
                ('image', models.CharField(max_length=100)),
                ('day', models.TextField(max_length=100)),
                ('month', models.TextField(max_length=100)),
                ('year', models.TextField(max_length=100)),
                ('gender', models.TextField(max_length=100)),
                ('address', models.TextField(max_length=100)),
                ('state', models.TextField(max_length=100)),
                ('district', models.TextField(max_length=100)),
                ('pin', models.TextField(max_length=100)),
                ('phone', models.IntegerField()),
                ('email', models.TextField(max_length=100)),
                ('password', models.TextField(max_length=100)),
                ('cpassword', models.TextField(max_length=100)),
                ('auth', models.TextField(max_length=50)),
            ],
            options={
                'db_table': 'donordetails',
            },
        ),
    ]
