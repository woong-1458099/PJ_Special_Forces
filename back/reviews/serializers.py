from rest_framework import serializers
from .models import Review
from places.serializers import PlaceListSerializer

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    place = PlaceListSerializer(read_only=True)

    class Meta:
        model = Review
        fields = [
            'id', 'user', 'username', 'place', 'rating',
            'content', 'images', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']


class ReviewCreateSerializer(serializers.ModelSerializer):
    """리뷰 생성용 Serializer"""
    class Meta:
        model = Review
        fields = ['rating', 'content', 'images']

    def validate_rating(self, value):
        if not 1 <= value <= 5:
            raise serializers.ValidationError("평점은 1-5 사이여야 합니다.")
        return value

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['place_id'] = self.context['place_id']
        return super().create(validated_data)


class ReviewListSerializer(serializers.ModelSerializer):
    """간단한 리뷰 목록용 Serializer"""
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'username', 'rating', 'content', 'created_at']
