from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Place
from .serializers import PlaceSerializer, PlaceListSerializer
import random

@api_view(['GET'])
@permission_classes([AllowAny])
def place_list(request):
    """장소 목록 조회 (예산/카테고리/태그 필터 지원)"""
    category = request.query_params.get('category', None)
    search = request.query_params.get('search', None)
    budget = request.query_params.get('budget', None)
    price_level = request.query_params.get('price_level', None)
    tags = request.query_params.get('tags', None)
    random_pick = request.query_params.get('random', None)

    places = Place.objects.all()

    # 카테고리 필터
    if category:
        places = places.filter(category=category)

    # 검색
    if search:
        places = places.filter(name__icontains=search)

    # 예산 필터링
    if budget:
        try:
            budget_int = int(budget)
            places = places.filter(average_price__lte=budget_int)
        except ValueError:
            pass

    # 가격 레벨 필터링 (1-5)
    if price_level:
        try:
            price_level_int = int(price_level)
            places = places.filter(price_level__lte=price_level_int)
        except ValueError:
            pass

    # 태그 필터링
    if tags:
        tag_list = tags.split(',')
        for tag in tag_list:
            places = places.filter(tags__contains=[tag.strip()])

    # 랜덤 추천
    if random_pick:
        try:
            count = int(random_pick)
            places_list = list(places)
            if len(places_list) > count:
                places = random.sample(places_list, count)
            serializer = PlaceListSerializer(places, many=True)
            return Response(serializer.data)
        except ValueError:
            pass

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


@api_view(['POST'])
@permission_classes([AllowAny])
def recommend_places(request):
    """AI 기반 여행지 추천"""
    from .ai_recommendations import get_gpt_recommendation

    user_preferences = {
        'concept': request.data.get('concept', ''),
        'budget': request.data.get('budget', 0),
        'duration': request.data.get('duration', 1),
        'companions': request.data.get('companions', ''),
        'preferences': request.data.get('preferences', ''),
    }

    # AI 추천 실행
    recommended_names = get_gpt_recommendation(user_preferences)

    # 추천된 장소명으로 DB에서 검색
    places = Place.objects.filter(name__in=recommended_names)

    # DB에 없는 경우 유사한 장소 검색
    if not places.exists():
        concept = user_preferences.get('concept', '')
        budget = user_preferences.get('budget', 0)

        filters = {}
        if concept:
            # 컨셉에 맞는 카테고리 매핑
            category_map = {
                '액티비티': 'activity',
                '맛집': 'restaurant',
                '관광': 'tourist',
                '쇼핑': 'shopping',
                '숙박': 'hotel'
            }
            for key, value in category_map.items():
                if key in concept:
                    filters['category'] = value
                    break

        if budget:
            filters['average_price__lte'] = budget

        if filters:
            places = Place.objects.filter(**filters)[:5]
        else:
            places = Place.objects.all().order_by('-rating')[:5]

    serializer = PlaceSerializer(places, many=True)
    return Response(serializer.data)
