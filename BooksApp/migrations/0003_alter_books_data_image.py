# Generated by Django 5.0.2 on 2024-03-12 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksApp', '0002_books_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books_data',
            name='image',
            field=models.ImageField(upload_to='bookimages'),
        ),
    ]
