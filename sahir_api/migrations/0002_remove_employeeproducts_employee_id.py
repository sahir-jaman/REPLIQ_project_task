# Generated by Django 4.2.1 on 2023-05-29 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sahir_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeproducts',
            name='Employee_id',
        ),
    ]
