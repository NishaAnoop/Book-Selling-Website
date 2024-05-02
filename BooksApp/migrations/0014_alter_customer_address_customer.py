# Generated by Django 5.0.2 on 2024-04-07 11:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksApp', '0013_alter_customer_address_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_address',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]