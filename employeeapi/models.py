from django.db import models

# Create your models here.


class Employee2(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)

    # Create / Insert / Add - POST
    # Retrieve /  Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE


class Category(models.Model):
    name = models.CharField(max_length=100)


class Ideabox(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
