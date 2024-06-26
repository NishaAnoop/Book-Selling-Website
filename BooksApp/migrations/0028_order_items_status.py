# Generated by Django 5.0.2 on 2024-04-30 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksApp', '0027_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_items',
            name='status',
            field=models.CharField(blank=True, choices=[('PLACED', 'Your order Is Placed'), ('SHIPPED', 'Your Order is Ready For Shipping'), ('CANCELLED', 'Your Order Is Cancelled')], max_length=100, null=True),
        ),
    ]
