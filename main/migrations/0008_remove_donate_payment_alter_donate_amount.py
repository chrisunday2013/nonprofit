# Generated by Django 4.1.5 on 2023-04-19 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_donationflutter_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donate',
            name='payment',
        ),
        migrations.AlterField(
            model_name='donate',
            name='amount',
            field=models.CharField(max_length=100),
        ),
    ]
