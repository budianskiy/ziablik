from django.urls import path
from apps.order.views import add_to_cart_view, cart_view, create_order_view, delete_from_cart_view


urlpatterns = [
    path('add_to_cart_view/', add_to_cart_view, name='add_to_cart_view'),
    path('cart/', cart_view, name='cart'),
    path('create/', create_order_view, name='create_order'),
    path('delete/<int:product_id>/', delete_from_cart_view, name='delete_from_cart'),
]
