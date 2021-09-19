#from ProjectApp.views import index
from django.conf.urls import include,url
from django.shortcuts import redirect
from django.urls import path
from django.contrib import admin
from ProjectApp import views



urlpatterns = [
    #path('products/', views.products, name = 'index'),
    path('', views.index,name='index'),
    path('redirectlogin',views.redirectlogin,name='redirectlogin'),
    path('userproduct',views.login,name='userproduct'),
    path('selectproduct', views.selectproduct,name='selectproduct'),
    path('editproduct',views.update,name='editproduct'),
    path('update1',views.update1,name='update1'),
    path('delete',views.delete,name='delete'),
    path('addproducts', views.addproducts,name='addproducts'),
    path('add_to_cart', views.add_to_cart,name='add_to_cart'),
    path('cart',views.cart,name='cart'),
]

