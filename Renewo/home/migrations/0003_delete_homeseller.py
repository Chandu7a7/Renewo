# Generated by Django 4.2 on 2023-09-29 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_order_customer_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='homeseller',
        ),
    ]
