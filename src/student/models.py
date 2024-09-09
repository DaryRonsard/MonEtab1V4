'''from django.db import models
from base.models.person_models import Person
# Create your models here.


class Student(Person):
    matricule = models.CharField(max_length=20, unique=True)
    phone_number_father = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.matricule}"

'''