# Generated by Django 4.1 on 2022-08-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coin', '0002_alter_coins_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coins',
            name='id',
            field=models.TextField(max_length=130, primary_key=True, serialize=False),
        ),
    ]