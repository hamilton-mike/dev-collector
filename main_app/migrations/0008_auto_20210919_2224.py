# Generated by Django 3.2.7 on 2021-09-19 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20210919_1958'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interview',
            options={'ordering': ['-date']},
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('dev', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.dev')),
            ],
        ),
    ]