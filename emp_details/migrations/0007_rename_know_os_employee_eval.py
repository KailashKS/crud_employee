# Generated by Django 3.2 on 2021-04-29 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_details', '0006_rename_eval_employee_know_os'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='know_os',
            new_name='eval',
        ),
    ]