from django.urls import path
from apps.order.views import add_to_cart_view, cart_view


urlpatterns = [
    path('add_to_cart_view/', add_to_cart_view, name='add_to_cart_view'),
    path('cart/', cart_view, name='cart'),
]
