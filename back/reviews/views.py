from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Review
from places.models import Place
from .serializers import ReviewSerializer, ReviewCreateSerializer, ReviewListSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def list_by_place(request, place_id):
    """장소별 리뷰 목록 조회"""
    try:
        place = Place.objects.get(id=place_id)
    except Place.DoesNotExist:
        return Response(
            {'error': '장소를 찾을 수 없습니다.'},
            status=status.HTTP_404_NOT_FOUND
        )

    reviews = Review.objects.filter(place=place)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request, place_id):
    """리뷰 작성"""
    try:
        place = Place.objects.get(id=place_id)
    except Place.DoesNotExist:
        return Response(
            {'error': '장소를 찾을 수 없습니다.'},
            status=status.HTTP_404_NOT_FOUND
        )

    # 이미 리뷰를 작성했는지 확인
    if Review.objects.filter(user=request.user, place=place).exists():
        return Response(
            {'error': '이미 리뷰를 작성하셨습니다.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = ReviewCreateSerializer(
        data=request.data,
        context={'request': request, 'place_id': place_id}
    )
    if serializer.is_valid():
        review = serializer.save()
        return Response(
            ReviewSerializer(review).data,
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
