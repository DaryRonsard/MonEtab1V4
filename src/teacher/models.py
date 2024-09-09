'''from django.db import models
from base.models.person_models import Person
# Create your models here.


class Teacher(Person):
    available = models.BooleanField(default=True)
    specialty = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.specialty}"
'''