from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


class UserModel(DateTimeModel):
    school = models.ForeignKey('school.SchoolModel', on_delete=models.CASCADE)
    role = models.ForeignKey('user.RoleUserModel', on_delete=models.CASCADE)
    pseudo = models.CharField(max_length=255)
    password = models.CharField(max_length=255)