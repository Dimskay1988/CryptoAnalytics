# Generated by Django 4.0.7 on 2022-09-01 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0002_alter_profile_options_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id_user',
            field=models.PositiveIntegerField(unique=True, verbose_name='ID пользователя в сети'),
        ),
    ]
