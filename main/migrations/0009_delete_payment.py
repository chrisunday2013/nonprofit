# Generated by Django 4.1.5 on 2023-04-29 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_donate_payment_alter_donate_amount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
