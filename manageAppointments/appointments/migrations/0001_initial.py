# Generated by Django 3.0.8 on 2020-09-18 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Appoint_ID', models.CharField(max_length=20)),
                ('Ap_Cus_name', models.CharField(max_length=200)),
                ('Ap_Cus_address', models.CharField(max_length=200)),
                ('Ap_Cus_email', models.EmailField(max_length=254)),
                ('Ap_Purpose', models.CharField(max_length=200)),
                ('Ap_Date_time', models.DateTimeField()),
                ('Ap_Venue', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'App_details',
            },
        ),
    ]
