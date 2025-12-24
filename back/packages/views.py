from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Package, PackagePlace
from .serializers import (
    PackageSerializer, PackageCreateSerializer,
    PackageListSerializer, PackagePlaceSerializer
)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate(request):
    """AI 패키지 생성 (현재는 간단한 패키지 생성)"""
    serializer = PackageCreateSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        package = serializer.save()
        return Response(
            PackageSerializer(package).data,
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save(request):
    """패키지 저장"""
    serializer = PackageCreateSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        package = serializer.save()

        # 패키지에 장소 추가 (places 데이터가 있는 경우)
        places_data = request.data.get('places', [])
        for place_data in places_data:
            PackagePlace.objects.create(
                package=package,
                place_id=place_data['place_id'],
                day=place_data.get('day', 1),
                order=place_data.get('order', 1),
                notes=place_data.get('notes', '')
            )

        return Response(
            PackageSerializer(package).data,
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mine(request):
    """내 패키지 목록 조회"""
    packages = Package.objects.filter(user=request.user)
    serializer = PackageListSerializer(packages, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove(request, package_id):
    """패키지 삭제"""
    try:
        package = Package.objects.get(id=package_id, user=request.user)
        package.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Package.DoesNotExist:
        return Response(
            {'error': '패키지를 찾을 수 없습니다.'},
            status=status.HTTP_404_NOT_FOUND
        )
