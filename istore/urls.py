from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('sub/', views.subscription, name="sub"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('activate/<uidb64><token>', views.activate, name="activate")

]