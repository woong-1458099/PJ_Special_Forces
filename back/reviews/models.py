from django.db import models
from django.contrib.auth import get_user_model
from places.models import Place
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', verbose_name='작성자')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='reviews', verbose_name='장소')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='평점'
    )
    content = models.TextField(verbose_name='리뷰 내용')
    images = models.JSONField(default=list, blank=True, verbose_name='이미지 URL 목록')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')

    class Meta:
        verbose_name = '리뷰'
        verbose_name_plural = '리뷰들'
        ordering = ['-created_at']
        unique_together = ['user', 'place']

    def __str__(self):
        return f"{self.user.username} - {self.place.name} ({self.rating}★)"
