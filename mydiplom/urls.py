from django.urls import path
from .views import add_client_form, index, add_hotel_form, add_city_form, add_country_form, add_tour_form

urlpatterns = [
    path('', index, name='index'), # по пустому пути ''
    path('add/client/', add_client_form, name='client_form'),
    path('add/hotel/', add_hotel_form, name='hotel_form'),
    path('add/city/', add_city_form, name='city_form'),
    path('add/country/', add_country_form, name='country_form'),
    path('add/tour/', add_tour_form, name='tour_form'),
]