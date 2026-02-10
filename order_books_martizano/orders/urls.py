from django.urls import path
from .views import order_list, order_detail

urlpatterns = [
    path('', order_list, name='order-list'),           # GET all / POST new
    path('<str:orderId>/', order_detail, name='order-detail'),  # GET, DELETE specific
]
