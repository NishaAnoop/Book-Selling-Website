# Generated by Django 5.0.2 on 2024-03-15 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksApp', '0005_alter_books_data_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books_data',
            name='category',
            field=models.CharField(choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction'), ('Business', 'Business'), ('Kids Story', 'Kids Story'), ('Biographies', 'Biographies')], max_length=100),
        ),
    ]
