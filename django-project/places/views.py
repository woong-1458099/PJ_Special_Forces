from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Place
from .serializers import PlaceSerializer, PlaceListSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def place_list(request):
    """장소 목록 조회"""
    category = request.query_params.get('category', None)
    search = request.query_params.get('search', None)

    places = Place.objects.all()

    if category:
        places = places.filter(category=category)

    if search:
        places = places.filter(name__icontains=search)

    serializer = PlaceListSerializer(places, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def place_detail(request, place_id):
    """장소 상세 조회"""
    try:
        place = Place.objects.get(id=place_id)
    except Place.DoesNotExist:
        return Response(
            {'error': '장소를 찾을 수 없습니다.'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = PlaceSerializer(place)
    return Response(serializer.data)
