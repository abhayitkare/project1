from django.db import models

# Create your models here.

class stu1(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(unique=True,null=False)
    city = models.CharField(max_length=50)
    marks = models.IntegerField()
    pass_date = models.DateField()

    def __str__(self):
        return self.name