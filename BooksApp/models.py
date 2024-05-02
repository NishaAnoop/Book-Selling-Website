from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)


class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='customer')
    name = models.CharField(max_length=30)
    mobile = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


booktype = (
    ('Fiction', 'Fiction'),
    ('Non-Fiction', 'Non-Fiction'),
    ('Business', 'Business'),
    ('Kids Story', 'Kids Story'),
    ('Biographies', 'Biographies')
)


class Books_data(models.Model):
    book = models.CharField(max_length=300)
    author1 = models.CharField(max_length=320)
    author2 = models.CharField(max_length=100, null=True, blank=True)
    publisher = models.CharField(max_length=300)
    category = models.CharField(max_length=100, choices=booktype)
    summary = models.CharField(max_length=300000)
    binding = models.CharField(max_length=300)
    language = models.CharField(max_length=300)
    edition = models.IntegerField()
    pages = models.IntegerField()
    release = models.DateField()
    price = models.IntegerField()
    isbn = models.IntegerField()
    image = models.ImageField(upload_to='bookimages')


# Customer Address Model

states = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh'),
    ('Gujarath', 'Gujarath'),
    ('Kerala', 'Kerala'),
    ('Karnataka', 'Karnataka'),
    ('TamilNadu', 'TamilNadu')
)


# user=get_user_model()
class customer_address(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField("Full Name", max_length=200)
    company = models.CharField("Company Name", max_length=200)
    street = models.TextField("Street Address", max_length=200)
    landmark = models.TextField("Land Mark")
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100, choices=states)
    city = models.CharField("City ", max_length=100)
    zip_code = models.CharField("pin/Zip code", max_length=100)
    mobile = models.IntegerField("Mobile")


class featured_authors(models.Model):
    author = models.CharField(max_length=30)
    image = models.ImageField(upload_to='authorimages')
    content = models.TextField()


class Cart_books(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Books_data, on_delete=models.CASCADE, null=True, blank=True)
    qty = models.IntegerField()
    order_date = models.DateField(auto_now=True)
    price = models.IntegerField(null=True, blank=True)

    def calculate_total_amount(cart_books):
        total_amount = 0
        for item in cart_books:
            total_amount += item.qty * item.price
        return total_amount
    # def __str__(self):
    #     return self.user

    @property
    def total_price(self):
         return self.qty * self.price
    #
    # @property
    # def subtotal(self):
    #     return sum((self.qty * self.price))
    # @property
    # def subtotal(self):
    #     return sum(self.total_price)
    # def __int__(self):
    #     return self.book.verbose_name


class wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wished_book = models.ForeignKey(Books_data, on_delete=models.CASCADE)
    added_date = models.DateField(auto_now_add=True)


status_choices = (
    ('PLACED', 'Your order Is Placed'),
    ('SHIPPED', 'Your Order is Ready For Shipping'),
    ('CANCELLED', 'Your Order Is Cancelled'),
)
#
#
class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #order_items = models.ForeignKey(Order_items, on_delete=models.CASCADE, null=True, blank=True)
    address = models.ForeignKey(customer_address, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=100, choices=status_choices)
    date=models.DateField(auto_now_add=True)

class Order_items(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books_data, on_delete=models.CASCADE, null=True, blank=True)
    quantity=models.IntegerField()
    price = models.IntegerField(null=True, blank=True)
    total = models.IntegerField()
    added_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=status_choices,null=True,blank=True)
