from django.urls import path
from .views import add_client_form, add_hotel_form, add_city_form, add_country_form, add_tour_form, start, tours,find_client 

urlpatterns = [
    path('', start, name='start'), # по пустому пути ''
    path('mydiplom/add/client/', add_client_form, name='client_form'),
    path('mydiplom/add/hotel/', add_hotel_form, name='hotel_form'),
    path('mydiplom/add/city/', add_city_form, name='city_form'),
    path('mydiplom/add/country/', add_country_form, name='country_form'),
    path('mydiplom/add/tour/', add_tour_form, name='tour_form'),
    path('mydiplom/get/tours', tours, name='tours'),
    path('mydiplom/get/client', find_client, name='find_client'),
]