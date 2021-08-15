from django.db import models
from django.contrib.auth.models import User


class profile(models.Model):
    # -------relations------- #
    address = models.ForeignKey("addresses", on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # -------fields------- #
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class addresses(models.Model):
    # -------fields------- #
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street_name = models.CharField(max_length=20)
    bulding_number = models.CharField(max_length=20)
    floor_number = models.CharField(max_length=20)
    apartment_number = models.CharField(max_length=20)

    def __str__(self):
        name = f"{self.country}  {self.city}  {self.street_name}  {self.bulding_number}  {self.floor_number} {self.apartment_number}"
        return name


github_token = "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"
