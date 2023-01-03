from django.urls import path
from apps.catalog.views import CategoryIndexView, ProductsByCategoryView, ProductDeteilView


urlpatterns = [
    path('', CategoryIndexView.as_view(), name='catalog'),
    path('<str:slug>/', ProductsByCategoryView.as_view(), name='categories'),
    path('product/<str:slug>/', ProductDeteilView.as_view(), name='product')
]