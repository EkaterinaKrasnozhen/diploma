import datetime
from django import forms
from .models import Client, Hotel, City, Country


class ClientForm(forms.Form):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    birth = forms.DateField(initial=datetime.date.today,
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    passport = forms.CharField(max_length=10)
    expirity_pass = forms.DateField(initial=datetime.date.today,
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    phone = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    
    def clean_date(self):
        expirity_pass = self.cleaned_data['expirity_pass']
        if expirity_pass < datetime.date.today():
            raise forms.ValidationError('Срок действия паспорта не подходит')
        return expirity_pass
    
    
class TourForm(forms.Form):
    client = forms.ModelChoiceField(queryset= Client.objects.all())
    hotel = forms.ModelChoiceField(queryset= Hotel.objects.all())
    start_date = forms.DateField(initial=datetime.date.today,
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))#forms.DateField()
    nights = forms.IntegerField()    
    meal = forms.CharField(max_length=5)
    room = forms.CharField(max_length=20)
    transfer = forms.CharField(max_length=50)
    extra_insurance = forms.CharField(max_length=50)
    extra_service = forms.CharField(max_length=50)
    
    
class Hotel_Form(forms.Form):
    location = forms.ModelChoiceField(queryset= City.objects.all())
    hotel_name = forms.CharField(max_length=100)  
    hotel_star = forms.CharField(max_length=5)
    

class City_Form(forms.Form):
    country = forms.ModelChoiceField(queryset= Country.objects.all())
    city_name = forms.CharField(max_length=100)  
    
    
class Country_Form(forms.Form):
    name = forms.CharField(max_length=100) 
    

class Tour_By_Client_Id_Form(forms.Form):
    client = forms.ModelChoiceField(label="Клиенты", queryset=Client.objects.all())
    

class Find_ClientForm(forms.Form):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    birth = forms.DateField(initial=datetime.date.today,
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    
    
