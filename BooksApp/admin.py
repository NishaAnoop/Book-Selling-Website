from django.contrib import admin

from BooksApp import models

# Register your models here.
admin.site.register(models.Customers)
admin.site.register(models.Books_data)
admin.site.register(models.customer_address)
admin.site.register(models.featured_authors)
admin.site.register(models. Cart_books)
admin.site.register(models. Order_items)

