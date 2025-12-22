from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Place
from .serializers import PlaceSerializer

@api_view(['GET'])
def place_list(request):
    concept = request.GET.get('concept', '')
    sort = request.GET.get('sort', 'rating')
    q = request.GET.get('q', '')  # 검색 겸용

    qs = Place.objects.all()

    if concept:
        qs = qs.filter(concept__icontains=concept)
    if q:
        qs = qs.filter(name__icontains=q)

    if sort == 'rating':
        qs = qs.order_by('-rating', 'id')
    elif sort == 'name':
        qs = qs.order_by('name')

    return Response(PlaceSerializer(qs[:50], many=True).data)

@api_view(['GET'])
def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    return Response(PlaceSerializer(place).data)

@api_view(['GET'])
def place_search(request):
    q = request.GET.get('q', '')
    qs = Place.objects.all()
    if q:
        qs = qs.filter(name__icontains=q)
    return Response(PlaceSerializer(qs[:50], many=True).data)
