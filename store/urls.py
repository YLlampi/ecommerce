from django.urls import path
from . import views

from store.controller import authview

urlpatterns = [
    path('', views.index, name="index"),

    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

    path('detail/<str:prod_slug>', views.view_product, name="view_product"),
    #path('detail/', views.view_product, name="view_product"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

    path('register/', authview.register, name="register"),
    path('login/', authview.loginpage, name="loginpage"),
    path('logout/', authview.logoutpage, name="logout"),

    #path('user_customer/', views.create_user, name="create_user"),
]