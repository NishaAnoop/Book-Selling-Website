# Generated by Django 5.0.2 on 2024-04-11 16:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksApp', '0017_alter_customer_address_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_address',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BooksApp.customers'),
        ),
    ]
