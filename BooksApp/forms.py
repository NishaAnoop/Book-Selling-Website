from django.contrib.auth.forms import UserCreationForm
from django import forms

from BooksApp.models import User, Customers, Books_data, customer_address, featured_authors


class DateInput(forms.DateInput):
    input_type = 'date'


class UserRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class CustomerRegister(forms.ModelForm):
    class Meta:
        model = Customers
        exclude = ('user',)


class AddBooks(forms.ModelForm):
    release = forms.DateField(widget=DateInput)

    class Meta:
        model = Books_data
        fields = "__all__"


class CustomerAddress(forms.ModelForm):
    class Meta:
        model = customer_address
        exclude = ('customer',)


class FeaturedAuthor(forms.ModelForm):
    class Meta:
        model = featured_authors
        fields = "__all__"

