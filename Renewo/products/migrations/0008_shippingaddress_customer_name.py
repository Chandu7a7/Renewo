# Generated by Django 4.2 on 2023-10-07 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0007_remove_shippingaddress_c_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='customer_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
