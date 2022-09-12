# Generated by Django 4.0.7 on 2022-09-12 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('usd', models.FloatField(max_length=30)),
                ('eur', models.FloatField(max_length=30)),
                ('uah', models.FloatField(max_length=30)),
                ('cny', models.FloatField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
