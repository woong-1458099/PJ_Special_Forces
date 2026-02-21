from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def root(request):
    return Response({
        "message": "Trip Connection API Server",
        "endpoints": {
            "auth": "/api/v1/auth/",
            "places": "/api/v1/places/",
            "packages": "/api/v1/packages/",
            "reviews": "/api/v1/reviews/",
        }
    })

urlpatterns = [
    path('', root),  # ✅ 추가
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('accounts.urls')),
    path('api/v1/places/', include('places.urls')),
    path('api/v1/packages/', include('packages.urls')),
    path('api/v1/reviews/', include('reviews.urls')),
]
