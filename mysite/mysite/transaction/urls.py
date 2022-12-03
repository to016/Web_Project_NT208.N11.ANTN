from django.urls import path
from . import views

app_name = 'transaction'

urlpatterns = [
    path('create/<int:id_sp>', views.transaction_create, name='transaction_create'),
    path('list/', views.transaction_list, name='transaction_list'),
    path('details/<str:transaction_code>', views.transaction_details, name='transaction_details'),
    path('update/',views.transaction_update ,name="transaction_update")
]