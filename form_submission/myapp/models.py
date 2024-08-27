from django.db import models

# Create your models here.
class FormData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contact = models.BigIntegerField()
    address1_field = models.CharField(max_length=50)
    address2_field = models.CharField(max_length=50)
    state_field = models.CharField(max_length=50)
    country_field = models.CharField(max_length=50)
    post_field = models.CharField(max_length=50)
    area_field = models.CharField(max_length=50)