# Generated by Django 3.2 on 2021-05-01 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_details', '0004_alter_employee_eval'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.IntegerField(default=20),
        ),
    ]