from django.db import models
from datetime import date
# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
class Department(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Manager(models.Model):
    full_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.full_name
    
        

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    date_employed = models.DateField(auto_now=False,default=date.today)
    address = models.CharField(max_length=100)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
"""
after modifying models 
go to django_migrations table, 
delete row with app = "app-name"
delete initial app tables
got to django folder, delete migration files
then run python manage.py makemigrations app-name
then python manage.py migrate
"""