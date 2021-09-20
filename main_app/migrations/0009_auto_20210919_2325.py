# Generated by Django 3.2.7 on 2021-09-19 23:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0008_auto_20210919_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='dev',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dev',
            name='location',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='dev',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]