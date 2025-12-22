from django.urls import path
from .views import place_list, place_detail, place_search

urlpatterns = [
    path('', place_list),
    path('search/', place_search),
    path('<int:place_id>/', place_detail),
]
