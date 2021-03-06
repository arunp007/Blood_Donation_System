# Generated by Django 4.0.1 on 2022-07-06 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0007_delete_donors_delete_hospitals_delete_recipients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.TextField(max_length=50)),
                ('lname', models.TextField(max_length=50)),
                ('blood', models.TextField(max_length=50)),
                ('aadhaar', models.TextField(max_length=50)),
                ('day', models.TextField(max_length=50)),
                ('month', models.TextField(max_length=50)),
                ('year', models.TextField(max_length=50)),
                ('gender', models.TextField(max_length=50)),
                ('address', models.TextField(max_length=50)),
                ('state', models.TextField(max_length=50)),
                ('district', models.TextField(max_length=50)),
                ('pin', models.TextField(max_length=50)),
                ('phone', models.TextField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.TextField(max_length=50)),
                ('cpassword', models.TextField(max_length=50)),
                ('authentication', models.TextField(max_length=50)),
            ],
            options={
                'db_table': 'donor_details',
            },
        ),
    ]
