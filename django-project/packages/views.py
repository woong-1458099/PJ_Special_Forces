from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from places.models import Place
from .models import Package, PackageItem
from .serializers import PackageSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate(request):
    concept = request.data.get('concept', '')
    place_ids = request.data.get('placeIds', [])

    places = list(Place.objects.filter(id__in=place_ids))

    items = []
    for idx, p in enumerate(places):
        items.append({
            'order': idx + 1,
            'time': f'{10+idx}:00',
            'place': {
                'id': p.id,
                'name': p.name,
                'concept': p.concept,
                'rating': p.rating,
            }
        })

    return Response({'title': f'{concept} 코스', 'concept': concept, 'items': items})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save(request):
    title = request.data.get('title', '')
    concept = request.data.get('concept', '')
    items = request.data.get('items', [])

    pkg = Package.objects.create(user=request.user, title=title, concept=concept)

    for it in items:
        place_id = (it.get('place') or {}).get('id')
        if not place_id:
            continue
        place = get_object_or_404(Place, id=place_id)
        PackageItem.objects.create(
            package=pkg,
            place=place,
            order=it.get('order', 1),
            time=it.get('time', '')
        )

    return Response(PackageSerializer(pkg).data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mine(request):
    qs = Package.objects.filter(user=request.user).order_by('-created_at')
    return Response(PackageSerializer(qs, many=True).data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove(request, package_id):
    pkg = get_object_or_404(Package, id=package_id, user=request.user)
    pkg.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
