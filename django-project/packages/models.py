from django.db import models
from django.conf import settings
from places.models import Place

class Package(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    concept = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class PackageItem(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    order = models.IntegerField(default=1)
    time = models.CharField(max_length=20, blank=True)
