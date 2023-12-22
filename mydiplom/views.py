from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
import logging
from django import forms
from .forms import ClientForm, Hotel_Form, City_Form, Country_Form, TourForm, Tour_By_Client_Id_Form
from .models import Client, Hotel, City, Country, Tour

logger = logging.getLogger(__name__)


def start(request):
    my_list = ['Красножен', 'Екатерина', 'Леонидовна']
    my_dict = {
        'группа': 'программист python',
        'поток': '2023',
        'программа': 'Университет 2025',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'mydiplom/start.html', context)


def add_client_form(request):
    """
        add new client to database
    """
    if request.method == 'POST':
        form = ClientForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            birth = form.cleaned_data['birth']
            passport = form.cleaned_data['passport']
            expirity_pass = form.cleaned_data['expirity_pass']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            logger.info('получены данные клиента')
            client = Client(name=name, surname=surname, birth=birth, passport=passport,\
                          expirity_pass=expirity_pass, phone=phone, email=email)
            client.save()
            message = 'Пользователь сохранён'
    else:
        form = ClientForm()
        message = 'Заполните форму'
    return render(request, 'mydiplom/form.html', {'form': form, 'message': message})


def add_tour_form(request):
    """
        add new tour to database
    """
    if request.method == 'POST':
        form = TourForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            client = form.cleaned_data['client']
            hotel = form.cleaned_data['hotel']
            start_date = form.cleaned_data['start_date']
            nights = form.cleaned_data['nights']    
            meal = form.cleaned_data['meal']
            room = form.cleaned_data['room']
            transfer = form.cleaned_data['transfer']
            extra_insurance = form.cleaned_data['extra_insurance']
            extra_service = form.cleaned_data['extra_service']
            tour = Tour(client=client, hotel=hotel, start_date=start_date,\
                        nights=nights, meal=meal, room=room, transfer=transfer,\
                        extra_insurance=extra_insurance, extra_service=extra_service)
            tour.save()
            message = 'Тур сохранён'
    else:
        form = TourForm()
        message = 'Заполните форму'
    return render(request, 'mydiplom/form.html', {'form': form, 'message': message}) 
    
    
def add_hotel_form(request):
    """
        add new hotel to database
    """
    if request.method == 'POST':
        form = Hotel_Form(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            location = form.cleaned_data['location']
            hotel_name = form.cleaned_data['hotel_name']
            hotel_star = form.cleaned_data['hotel_star']
            logger.info('получены данные клиента')
            hotel = Hotel(location=location, hotel_name=hotel_name, hotel_star=hotel_star)
            hotel.save()
            message = 'Отель сохранён'
    else:
        form = Hotel_Form()
        message = 'Заполните форму'
    return render(request, 'mydiplom/form.html', {'form': form, 'message': message})


def add_city_form(request):
    """
        add new city to database
    """
    if request.method == 'POST':
        form = City_Form(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            country = form.cleaned_data['country']
            city_name = form.cleaned_data['city_name']
            city = City(country=country, city_name=city_name)
            city.save()
            message = 'Курорт сохранён'
    else:
        form = City_Form()
        message = 'Заполните форму'
    return render(request, 'mydiplom/form.html', {'form': form, 'message': message})
    
    
def add_country_form(request):
    """
        add new country to databse
    """
    if request.method == 'POST':
        form = Country_Form(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            logger.info('получены данные клиента')
            country = Country(name=name)
            country.save()
            message = 'Страна сохранена'
    else:
        form = Country_Form()
        message = 'Заполните форму'
    return render(request, 'mydiplom/form.html', {'form': form, 'message': message})


def tours(request):
    """
        get all trips of client
    """
    if request.method == 'POST':
        client_id = request.POST.get('client')
        client = Client.objects.filter(pk=client_id).first()
        tours = Tour.objects.filter(client=client) 
        context = {'client': client, 'tours': tours}
        return render(request, 'mydiplom/client_tour.html', context)            
    else:
        form = Tour_By_Client_Id_Form()
        return render(request, 'mydiplom/form.html', {'form': form})
        