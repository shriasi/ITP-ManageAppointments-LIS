# Generated by Django 3.0.8 on 2020-09-18 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='Ap_Date_time',
            field=models.DateTimeField(default='2015-05-11 13:01:01'),
        ),
    ]
