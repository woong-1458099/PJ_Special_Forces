from django.urls import path
from .views import place_list, place_detail, recommend_places

urlpatterns = [
    path('', place_list),
    path('recommend/', recommend_places),
    path('<int:place_id>/', place_detail),
]
