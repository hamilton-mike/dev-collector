# Generated by Django 3.2.7 on 2021-09-19 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dev',
            name='remote',
            field=models.BooleanField(default=False),
        ),
    ]
