# Generated by Django 4.0.7 on 2022-09-19 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coins',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]