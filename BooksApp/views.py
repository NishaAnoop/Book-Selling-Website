from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.shortcuts import redirect, HttpResponse
from django.http import HttpResponse
from django.http import JsonResponse, request
from django.db.models import OuterRef, Subquery
from BooksApp.forms import UserRegister, CustomerRegister, AddBooks, CustomerAddress, FeaturedAuthor
from BooksApp.models import Customers, Books_data, User, customer_address, featured_authors, Cart_books, wishlist


# Create your views here.
def home(request):
    book = Books_data.objects.all()
    return render(request, 'index.html', {'book': book})


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('adminindex')
            elif user.is_customer:
                return redirect('customer_index')
        else:
            messages.info(request, 'Not a registered user')
    return render(request, 'login.html')


def register(request):
    form1 = UserRegister()
    form2 = CustomerRegister()
    if request.method == 'POST':
        form1 = UserRegister(request.POST)
        form2 = CustomerRegister(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_customer = True
            user.save()
            customer = form2.save(commit=False)
            customer.user = user
            customer.save()
            return redirect('loginpage')

    return render(request, 'register.html', {'form1': form1, 'form2': form2})


def logout(request):
    request.session.clear()
    return redirect('home')




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def adminindex(request):
    return render(request, 'admin_index.html')


def customer_index(request):
    return render(request, 'customer_index.html')


def viewCustomer(request):
    data = Customers.objects.all()
    return render(request, 'viewcustomer.html', {'data': data})


def deletecustomer(request, user_id):
    data = Customers.objects.get(user_id=user_id)
    data.delete()
    return redirect('viewCustomer')


def viewCustomer(request):
    data = Customers.objects.all()
    return render(request, 'viewcustomer.html', {'data': data})


def OrderAdmin(request):
    order = Order_items.objects.all()
    count = Order_items.objects.count()
    print(count, "###count##")

    return render(request, 'order_admin.html', {'order': order, 'count': count})


# ...................................................................................................
#   Books...............................................................................................
def addbooks(request):
    form3 = AddBooks()
    if request.method == 'POST':
        form3 = AddBooks(request.POST, request.FILES)
        if form3.is_valid():
            book = form3.save(commit=False)
            book.save()
            return redirect('viewbooks')
    return render(request, 'addbooks.html', {'form3': form3})


def viewbooks(request):
    data = Books_data.objects.all()
    return render(request, 'viewbooks.html', {'data': data})


def deletebooks(request, id):
    data = Books_data.objects.get(id=id)
    data.delete()
    return redirect('viewbooks')


# def editbooks(request, id):
#   data =Books_data .objects.get(id=id)
#  return render(request,'edit.html', {'data':data})
def updatebooks(request, id):
    data = Books_data.objects.get(id=id)
    form = AddBooks(instance=data)
    if request.method == 'POST':
        form = AddBooks(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('viewbooks')
    return render(request, 'edit.html', {'form': form})


# Books End..................................................................................
# Customers  .Start...............................................................................

#
# def customer_index(request,user_id):
#     data = Customers.objects.get(user_id=user_id)
#     return render(request, 'customer_index.html',{'data',data})


def updateaccount(request):
    data = Customers.objects.get(user=request.user)
    form = CustomerRegister(instance=data)
    if request.method == 'POST':
        form = CustomerRegister(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('customer_index')
    return render(request, 'clientview.html', {'form': form, 'data': data})


def passwd_update(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_index')
    else:
        form = PasswordChangeForm(user)
    return render(request, 'password.html', {'form': form})


def myaddress(request):
    # data=customer_address.objects.all()
    data = customer_address.objects.filter(customer=Customers.objects.get(user=request.user))
    print(data)
    # tr
    # data=customer_address.objects.all()
    # data = customer_address.objects.filter(customer=User.objects.get(user=request.user))
    # data = customer.customer_address.objects.get(user=request.user)
    # print(data.city)
    # except:
    #   print("Data not available")

    return render(request, 'myaddress.html', {'data': data})


# def myaddress(request):
#   data=customer_address.objects.get(user=request.user)


def update_address(request):
    data = customer_address.objects.filter(customer=Customers.objects.get(user=request.user)).first()
    form1 = CustomerAddress()
    if request.method == 'POST':
        form1 = CustomerAddress(request.POST, instance=data)
        if form1.is_valid():
            customer = form1.save(commit=False)
            customer.save()
            return redirect('myaddress')
    return render(request, 'addaddress.html', {'form1': form1})


# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

# Featured Authors

def featuredadmin(request):
    form1 = FeaturedAuthor()
    if request.method == 'POST':
        form1 = FeaturedAuthor(request.POST, request.FILES)
        if form1.is_valid():
            book = form1.save(commit=False)
            book.save()
            return redirect('viewfeatured')
    return render(request, 'featuredadmin.html', {'form1': form1})


def viewfeatured(request):
    data = featured_authors.objects.all()
    return render(request, 'viewfeatured.html', {'data': data})


def customer_authors(request):
    newcontent = ''
    data = featured_authors.objects.all()
    for i in data:
        summary = i.content
        s1 = slice(200)
        newcontent = summary[s1]
        print(newcontent)
    return render(request, 'featured.html', {'data': data, 'newcontent': newcontent})


def authors(request, id):
    author = featured_authors.objects.get(id=id)
    bk_author=author.author
    book=Books_data.objects.filter(author1=bk_author)
    count=len(book)
    print(count,"count***********")
    #book = Books_data.objects.annotate(author1=Subquery(featured_authors.author))
    return render(request, 'authors.html', {'author': author, 'book': book,'count':count})


def bookstheme(request):
    return render(request, 'books_theme.html')


# ..............................................

# Fiction Books

def fiction_books(request):
    data = Books_data.objects.filter(category='Fiction')
    return render(request, 'fiction_books.html', {'data': data})


def non_fiction(request):
    data = Books_data.objects.filter(category='Non-Fiction')
    return render(request, 'non_fiction.html', {'data': data})


def business(request):
    data = Books_data.objects.filter(category='Business')
    return render(request, 'business.html', {'data': data})


def children(request):
    data = Books_data.objects.filter(category='Kids Story')
    return render(request, 'children.html', {'data': data})


def shopping(request, id):
    data = Books_data.objects.get(id=id)
    return render(request, 'shopping.html', {'data': data})


#               Cart Details
# __________________________________________

def cart_details(request):
    data = Cart_books.objects.filter(user=request.user, id=id)
    quantity = data.qty
    price = data.book.price
    total_price = quantity * price

    return render(request, 'view_cart.html', {'data': data, 'total_price': total_price})


def add_to_cart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            book_id = int(request.POST.get('book_id'))
            print(book_id, "book id")
            qty1 = int(request.POST.get('qty1'))
            print(qty1, "quantity")
            book_price = int(request.POST.get('book_price'))
            print(book_price, "book price")
            user = request.user
            print(user, "customer")
            data = Books_data.objects.get(id=book_id)
            bk = Cart_books()
            bk.user = user
            bk.book = data
            bk.qty = qty1
            bk.price = book_price
            bk.save()

            cart = request.session.get('cart')

        # cart.add(book=book)
        response = JsonResponse({'book title:': bk.book.book})
        return redirect('shopping')


def gotocart(request):
    cart = request.session.get('cart')
    price = 0
    if cart is None:
        messages.info(request, 'Your Cart is empty')
    if request.user.is_authenticated:
        cart_items = Cart_books.objects.filter(user=request.user)
        for item in cart_items:
            item.total_amount = item.qty * item.price
            price = item.total_amount
            print(item.total_amount, "**********")
        total_amount = sum(item.total_amount for item in cart_items)
        return render(request, 'go_to_cart.html',
                      {'cart_items': cart_items, 'total_amount': total_amount, 'price': price})


def wished_lists(request, id):
    data = Books_data.objects.get(id=id)
    wish_book, created = wishlist.objects.get_or_create(wished_book=data, user=request.user)
    wish_book.save()
    messages.info(request, 'the product added to wish list')
    wish_list = wishlist.objects.filter(wished_book=Books_data.objects.get(id=id))
    return render(request, 'wishlist.html', {'wish_list': wish_list})


def remove_from_wishlist(request, id):
    data = wishlist.objects.get(id=id)
    data.delete()
    return redirect('gotocart')


def remove_from_cart(request, id):
    data = Cart_books.objects.get(id=id)
    data.delete()
    return redirect('gotocart')


@login_required(login_url='loginpage')
def buynow(request):
    #
    # s=request.session()
    # bk_id=int(s.get('id'))
    # print(bk_id)

    if request.user.is_authenticated:
        order_items = Order_items.objects.filter(user=request.user)
        address = customer_address.objects.filter(customer=Customers.objects.get(user=request.user)).first()

    else:

        messages.info(request, 'Authentication Required')

    return render(request, 'buynow.html', {'order_items': order_items, 'address': address})


def buydirect(request):
    # data=Books_data.objects.get(id=id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            book_id = int(request.POST.get('book_id'))
            print(book_id, "book id")
            quantity = int(request.POST.get('qty1'))
            print(quantity, "quantity")
            book_price = int(request.POST.get('book_price'))
            print(book_price, "book price")
            book = Books_data.objects.get(id=book_id)
            user = request.user
            order = Order_items()
            order.user = user
            order.book = book
            order.quantity = quantity
            order.price = book_price
            order.total = quantity * book_price
            print(order.total, "total*********")
            order.save()
            response = JsonResponse({'book title:': order.book.book})
            address = customer_address.objects.filter(customer=Customers.objects.get(user=request.user)).first()
            order_items = Order_items.objects.filter(user=request.user)
        return render(request, 'buynow.html', {'order_items': order_items, 'address': address})


from django.shortcuts import redirect, HttpResponse
from .models import Cart_books, Order_items


def add_to_order(request):
    if request.method == 'POST':
        cart_items = Cart_books.objects.filter(user=request.user)

        if cart_items.exists():
            # Transfer items from cart to order
            for cart_item in cart_items:
                order_item, created = Order_items.objects.get_or_create(
                    user=request.user,
                    book=cart_item.book,
                    defaults={'quantity': 0, 'total': 0}  # Provide default values
                )
                order_item.quantity += cart_item.qty
                order_item.price = cart_item.price
                order_item.total = order_item.quantity * order_item.price  # Calculate total
                order_item.save()

            # Delete items from cart after transferring to order
            cart_items.delete()

            messages.success(request, 'Items transferred to your order.')
            return redirect('buynow')  # Redirect to view_order page
        else:
            return HttpResponse("No items added to the order.")
    else:
        # Handle cases where request method is not POST
        return HttpResponse("Method not allowed.")


def view_order(request):
    order_items = Order_items.objects.filter(user=request.user)
    return render(request, 'view_order.html', {'order_items': order_items})


def complete_order(request):
    order_items = Order_items.objects.filter(user=request.user)
    total_price = sum(item.total for item in order_items)
    # Create Order object if necessary and save it in the database
    # Remove items from the user's order
    order_items.delete()
    messages.success(request, 'Your order has been completed successfully.')
    return redirect('action')


def checkout(request):
    return render(request, 'checkout.html')


# -----------------------------------------------------------------
# -------------------------------------------------------------------
def search_view(request):
    query = request.GET.get("q")
    books = Books_data.objects.filter(book_icontains - query, author1_icontains - query).order_by("date")
    context = {
        "books": books,
        "query": query
    }
    return render(request, 'search_view.html', context)

def action(request):
    return render(request, 'success.html')