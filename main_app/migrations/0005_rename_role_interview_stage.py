# Generated by Django 3.2.7 on 2021-09-19 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_interview_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interview',
            old_name='role',
            new_name='stage',
        ),
    ]
