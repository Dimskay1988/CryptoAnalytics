# Generated by Django 4.0.1 on 2022-09-25 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='id_user',
            new_name='id_telegram',
        ),
    ]
