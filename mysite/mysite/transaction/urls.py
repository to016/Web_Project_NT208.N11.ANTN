from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('create/<int:id_sp>', views.transaction_create, name='transaction_create'),
    path('list/', views.transaction_list, name='transaction_info'),
    path('detail/', views.transaction_detail, name='transaction_detail'),
]