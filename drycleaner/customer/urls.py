from django.urls import path
from .views import  Customerlist,CustomerDetail,CustomerCreate,CustomerUpdate,CustomerDeleteview


urlpatterns = [

    path('', Customerlist.as_view(), name='customers'),
    path('customer/<int:pk>/', CustomerDetail.as_view(), name='customers_detail'),
    path('customer-create', CustomerCreate.as_view(), name='customer_create'),
    path('customer-edit/<int:pk>/', CustomerUpdate.as_view(), name='customer-update'),
    path('customer-delete/<int:pk>/', CustomerDeleteview.as_view(), name='customer-delete'),

]