# Generated by Django 4.1.5 on 2023-04-19 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationFlutter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]