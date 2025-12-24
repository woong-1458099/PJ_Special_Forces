from django.db import models

class Place(models.Model):
    CATEGORY_CHOICES = [
        ('tourist', '관광지'),
        ('restaurant', '맛집'),
        ('hotel', '숙박'),
        ('activity', '액티비티'),
        ('shopping', '쇼핑'),
    ]

    name = models.CharField(max_length=200, verbose_name='장소명')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name='카테고리')
    address = models.CharField(max_length=300, verbose_name='주소')
    description = models.TextField(verbose_name='설명', blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name='위도')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name='경도')
    image_url = models.URLField(max_length=500, blank=True, verbose_name='이미지 URL')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0, verbose_name='평점')
    average_price = models.IntegerField(null=True, blank=True, verbose_name='평균 가격')
    price_level = models.IntegerField(null=True, blank=True, verbose_name='가격 레벨 (1-5)')
    tags = models.JSONField(default=list, blank=True, verbose_name='태그')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')

    class Meta:
        verbose_name = '장소'
        verbose_name_plural = '장소들'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.category})"
