from django.db import models

from base.models.helpers.named_date_time_model import NamedDateTimeModel


class SchoolModel(NamedDateTimeModel):
    app = models.OneToOneField('school.AppSettingsModel', related_name="school_app_id", on_delete=models.CASCADE)
    url_logo = models.URLField()


    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Ecole"
        verbose_name_plural = "Ecoles"
