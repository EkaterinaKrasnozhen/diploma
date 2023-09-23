from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth = models.DateField()
    passport = models.CharField(max_length=10)
    expirity_pass = models.DateField()
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
    def __repr__(self):
        return f'Client({self.name}, {self.surname}, {self.birth}, {self.passport}, {self.expirity_pass})'
    
    def __str__(self):
        return f'Имя: {self.name}, Фамилия: {self.surname}, дата рождения: {self.birth}, \
                паспорт: {self.passport}, срок действия: {self.expirity_pass}'
                
    def get_name_surname(self):
        return f'{self.name} {self.surname}'
    
    def get_passport(self):
        return f'{self.passport} {self.expirity_pass}'
    
    def get_birth(self):
        return self.birth
  
  
class Country(models.Model):
    name = models.CharField(max_length=50) 
    
    def __str__(self):
        return f'{self.name}'
    
    
class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.country, self.city_name}'
    
    def __repr__(self):
        return f'City({self.country}, {self.city_name})'
    
    def get_country(self):
        return self.country


class Hotel(models.Model):
    location = models.ForeignKey(City, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=100)  
    hotel_star = models.CharField(max_length=5)
    
    def get_location(self):
        return self.location
    
    def __repr__(self):
        return f'Hotel({self.hotel_name}, {self.hotel_star})'
    
     
class Tour(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    start_date = models.DateField()
    nights = models.IntegerField()    
    meal = models.CharField(max_length=5)
    room = models.CharField(max_length=20)
    transfer = models.CharField(max_length=50, default='групповой')
    extra_insurance = models.CharField(max_length=50, default=None)
    extra_service = models.CharField(max_length=50, default=None)
    

