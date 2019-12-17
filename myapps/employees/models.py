from django.db import models


# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    emp_code = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
