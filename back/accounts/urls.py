from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import signup, me

urlpatterns = [
    path('signup/', signup),
    path('login/', TokenObtainPairView.as_view()),   # JWT 발급
    path('refresh/', TokenRefreshView.as_view()),
    path('me/', me),
]
