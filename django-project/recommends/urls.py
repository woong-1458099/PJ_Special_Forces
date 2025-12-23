from django.urls import path, include
from .views import (
    PlaceClickAPIView,
    AIRecommendLogAPIView,
    TopRecommendAPIView,
)

urlpatterns = [
    path('click/', PlaceClickAPIView.as_view()),
    path('ai-log/', AIRecommendLogAPIView.as_view()),
    path('top/', TopRecommendAPIView.as_view()),
    ]
