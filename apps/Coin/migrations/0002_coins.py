# Generated by Django 4.1 on 2022-08-15 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coins',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('symbol', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
