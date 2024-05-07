from django.urls import path

from BooksApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('register', views.register, name='Register'),
    path('logout', views.logout, name='logout'),

    # users................................................
    path('adminindex', views.adminindex, name='adminindex'),
    path('customer_index', views.customer_index, name='customer_index'),
    path('viewCustomer', views.viewCustomer, name='viewCustomer'),
    path('deletecustomer/<int:user_id>', views.deletecustomer, name='deletecustomer'),

    # -------------------------------------------------------------------------
    # books related - Admin

    path('addbooks', views.addbooks, name='addbooks'),
    path('viewbooks', views.viewbooks, name='viewbooks'),
    path('deletebooks/<int:id>', views.deletebooks, name='deletebooks'),
    # path('editbooks/<int:id>', views.editbooks, name='editbooks'),
    path('updatebooks/<int:id>', views.updatebooks, name='updatebooks'),
    # ...........................................................
    # Customers

    path('updateaccount', views.updateaccount, name='updateaccount'),
    path('passwd_update', views.passwd_update, name='passwd_update'),
    path('myaddress', views.myaddress, name='myaddress'),
    path('update_address', views.update_address, name='update_address'),
    path('bookstheme', views.bookstheme, name='bookstheme'),

    # --------------------------------------------------------------
    # Categories

    path('featuredadmin', views.featuredadmin, name='featuredadmin'),
    path('viewfeatured', views.viewfeatured, name='viewfeatured'),
    path('customer_authors', views.customer_authors, name='customer_authors'),
    path('authors/<int:id>', views.authors, name='authors'),
    path('fiction_books', views.fiction_books, name='fiction_books'),
    path('non_fiction', views.non_fiction, name='non_fiction'),
    path('business', views.business, name='business'),
    path('children', views.children, name='children'),

    # -------------------------------------------------------------------
    # Cart
    path('shopping/<int:id>', views.shopping, name='shopping'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('wished_lists/<int:id>', views.wished_lists, name='wished_lists'),
    path('remove_from_wishlist/<int:id>', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('gotocart', views.gotocart, name='gotocart'),
    path('remove_from_cart/<int:id>', views.remove_from_cart, name='remove_from_cart'),
    # .............................................
    # Buy Order
    path('checkout', views.checkout, name='checkout'),
    path('buynow', views.buynow, name='buynow'),
    path('buydirect', views.buydirect, name='buydirect'),
    path('add_to_order', views.add_to_order, name='add_to_order'),
    path('view_order', views.view_order, name='view_order'),
    path('OrderAdmin', views.OrderAdmin, name='OrderAdmin'),
    path('complete_order', views.complete_order, name='complete_order'),

    path('checkout', views.checkout, name='checkout'),
    path('action', views.action, name='action'),

    path('search_view', views.search_view, name='search_view'),

]
