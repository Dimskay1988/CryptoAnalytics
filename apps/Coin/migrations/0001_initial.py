# Generated by Django 4.0.7 on 2022-09-01 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coins',
            fields=[
                ('id', models.TextField(max_length=130, primary_key=True, serialize=False)),
                ('symbol', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('platforms', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ListCurrencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=20)),
            ],
        ),
    ]
