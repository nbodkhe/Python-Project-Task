from django.urls import path
from food_orders.views import food_order_details

urlpatterns = [
    path('<int:month>/', food_order_details, name='food_order_details'),
]

