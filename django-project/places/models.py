from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    concept = models.CharField(max_length=30, blank=True)  # 카페/힐링/헬스 등
    address = models.CharField(max_length=200, blank=True)

    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)

    rating = models.FloatField(null=True, blank=True)
    opening_hours = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
