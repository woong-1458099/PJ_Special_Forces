from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import PlaceClickLog
from places.models import Place

from .models import AIRecommendLog
from packages.models import Package

from places.serializers import PlaceSerializer
from .utils import calculate_place_score

# Create your views here.


class PlaceClickAPIView(APIView):
    def post(self, request):
        place_id = request.data.get('place_id')
        source = request.data.get('source')  # map / recommend / package

        if not place_id or not source:
            return Response(
                {"error": "place_id와 source는 필수입니다."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            place = Place.objects.get(id=place_id)
        except Place.DoesNotExist:
            return Response(
                {"error": "존재하지 않는 장소입니다."},
                status=status.HTTP_404_NOT_FOUND
            )

        PlaceClickLog.objects.create(
            user=request.user if request.user.is_authenticated else None,
            place=place,
            source=source
        )

        return Response(
            {"message": "클릭 로그 저장 완료"},
            status=status.HTTP_201_CREATED
        )

class AIRecommendLogAPIView(APIView):
    def post(self, request):
        package_id = request.data.get('package_id')
        place_ids = request.data.get('place_ids')  # 리스트 형태

        if not package_id or not place_ids:
            return Response(
                {"error": "package_id와 place_ids는 필수입니다."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            package = Package.objects.get(id=package_id)
        except Package.DoesNotExist:
            return Response(
                {"error": "존재하지 않는 패키지입니다."},
                status=status.HTTP_404_NOT_FOUND
            )

        places = Place.objects.filter(id__in=place_ids)

        logs = []
        for place in places:
            logs.append(
                AIRecommendLog(
                    user=request.user if request.user.is_authenticated else None,
                    place=place,
                    package=package
                )
            )

        AIRecommendLog.objects.bulk_create(logs)

        return Response(
            {"message": "AI 추천 노출 로그 저장 완료"},
            status=status.HTTP_201_CREATED
        )

class TopRecommendAPIView(APIView):
    def get(self, request):
        limit = request.query_params.get('limit', 10)
        limit = int(limit)

        places = Place.objects.all()

        scored_places = []
        for place in places:
            score = calculate_place_score(place)
            scored_places.append((place, score))

        # 점수 기준 내림차순 정렬
        scored_places.sort(key=lambda x: x[1], reverse=True)

        # 상위 N개만 추출
        top_places = [place for place, score in scored_places[:limit]]

        serializer = PlaceSerializer(top_places, many=True)
        return Response(serializer.data)
