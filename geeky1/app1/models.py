from django.db import models
from django.utils import timezone
# Create your models here.
class table1(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    datetime = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name + " " + self.surname


class table2(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class table3(models.Model):
    name = models.CharField(max_length=50,blank=True) # blank=True kel tr ata he field required nhi
    surname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class table4(models.Model):
    name = models.CharField(max_length=50) 
    surname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class table5(models.Model):
    name = models.CharField(max_length=50) 
    surname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class table6(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
    
