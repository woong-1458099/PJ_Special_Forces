from django.db import models
from django.contrib.auth import get_user_model
from places.models import Place

User = get_user_model()

class Package(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='packages', verbose_name='사용자')
    title = models.CharField(max_length=200, verbose_name='패키지명')
    description = models.TextField(verbose_name='설명', blank=True)
    places = models.ManyToManyField(Place, through='PackagePlace', related_name='packages', verbose_name='포함 장소')
    start_date = models.DateField(null=True, blank=True, verbose_name='시작일')
    end_date = models.DateField(null=True, blank=True, verbose_name='종료일')
    budget = models.IntegerField(null=True, blank=True, verbose_name='예산')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')

    class Meta:
        verbose_name = '패키지'
        verbose_name_plural = '패키지들'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.user.username}"


class PackagePlace(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, verbose_name='패키지')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='장소')
    day = models.IntegerField(verbose_name='여행 날짜')
    order = models.IntegerField(verbose_name='순서')
    notes = models.TextField(blank=True, verbose_name='메모')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')

    class Meta:
        verbose_name = '패키지 장소'
        verbose_name_plural = '패키지 장소들'
        ordering = ['day', 'order']
        unique_together = ['package', 'place', 'day', 'order']

    def __str__(self):
        return f"{self.package.title} - Day {self.day} - {self.place.name}"
