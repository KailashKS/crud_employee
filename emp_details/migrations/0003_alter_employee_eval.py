# Generated by Django 3.2 on 2021-04-30 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_details', '0002_alter_employee_doj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='eval',
            field=models.CharField(max_length=200),
        ),
    ]