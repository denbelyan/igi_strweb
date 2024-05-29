from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser, Group, Permission


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField(default="no address")
    phone = models.CharField(max_length=13)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Employee(AbstractUser):
    groups = models.ManyToManyField(Group, blank=True, related_name='employee_groups')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='employee_user_permissions')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.groups}'

class Schedule(models.Model):
    start_work = models.TimeField()
    end_work = models.TimeField()

class Hall(models.Model):
    name = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='halls')

    def __str__(self):
        return self.name

class Card(models.Model):
    name = models.CharField(max_length=100)
    hall = models.ManyToManyField(Hall)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    start_work = models.DateField()
    end_work = models.DateField()
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, related_name='created_packages')

    def __str__(self):
        return self.name

class Service(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='services')
    service_start_date = models.DateField(default=datetime.now)
    service_end_date = models.DateField(default=datetime.now)
    service_name = models.CharField(max_length=100)

class News(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news_picture')

class Timezone(models.Model):
    current_time = models.DateField(default=datetime.now)


class WorkVakansiya(models.Model):
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=8, decimal_places=2, default=0)

class feedback(models.Model):
    text = models.CharField(max_length=100)
    stars = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    author = models.CharField(max_length=100)
    time = models.DateField(default=datetime.now)

class promocodes(models.Model):
    skidka = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)