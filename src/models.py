from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    GENDER_CHOICES = [('Male', 'male'), ('Female', 'female'), ('Other', 'other')]

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    joined_date = models.DateField()
    termination_date = models.DateField(null=True, blank=True)