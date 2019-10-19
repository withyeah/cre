from django.db import models

# Create your models here.
class City(models.Model):
    city_code = models.IntegerField(primary_key=True)
    city_name = models.TextField()
    city_name_en = models.TextField()
    country_name = models.TextField()
    country_name_en = models.TextField()
    city_area = models.FloatField()

class Gu(models.Model):
    gu_code = models.IntegerField(primary_key=True)
    gu_name = models.TextField()
    gu_name_en = models.TextField()
    city_code = models.IntegerField()
    city_name = models.TextField()
    city_name_en = models.TextField()
    country_name = models.TextField()
    country_name_en = models.TextField()
    gu_area = models.FloatField()

class Dong(models.Model):
    dong_code = models.IntegerField(primary_key=True)
    dong_name = models.TextField()
    dong_name_en = models.TextField()
    gu_code = models.IntegerField()
    gu_name = models.TextField()
    gu_name_en = models.TextField()
    city_code = models.IntegerField()
    city_name = models.TextField()
    city_name_en = models.TextField()
    country_name = models.TextField()
    country_name_en = models.TextField()
    dong_area = models.FloatField()