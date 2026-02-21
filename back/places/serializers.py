from rest_framework import serializers
from .models import Place

class PlaceSerializer(serializers.ModelSerializer):
    reviews_count = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = [
            'id', 'name', 'category', 'address', 'description',
            'latitude', 'longitude', 'image_url', 'rating',
            'reviews_count', 'average_rating', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_reviews_count(self, obj):
        return obj.reviews.count()

    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews.exists():
            return round(sum(r.rating for r in reviews) / reviews.count(), 2)
        return 0.0


class PlaceListSerializer(serializers.ModelSerializer):
    """간단한 장소 목록용 Serializer"""
    class Meta:
        model = Place
        fields = ['id', 'name', 'category', 'address', 'image_url', 'rating']
