from rest_framework import serializers
from .models import Package, PackagePlace
from places.serializers import PlaceListSerializer

class PackagePlaceSerializer(serializers.ModelSerializer):
    place = PlaceListSerializer(read_only=True)
    place_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = PackagePlace
        fields = ['id', 'place', 'place_id', 'day', 'order', 'notes', 'created_at']
        read_only_fields = ['id', 'created_at']


class PackageSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    package_places = PackagePlaceSerializer(
        source='packageplace_set',
        many=True,
        read_only=True
    )
    places_count = serializers.SerializerMethodField()

    class Meta:
        model = Package
        fields = [
            'id', 'user', 'title', 'description',
            'start_date', 'end_date', 'budget',
            'package_places', 'places_count',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def get_places_count(self, obj):
        return obj.places.count()


class PackageCreateSerializer(serializers.ModelSerializer):
    """패키지 생성용 Serializer"""
    class Meta:
        model = Package
        fields = ['title', 'description', 'start_date', 'end_date', 'budget']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class PackageListSerializer(serializers.ModelSerializer):
    """간단한 패키지 목록용 Serializer"""
    places_count = serializers.SerializerMethodField()

    class Meta:
        model = Package
        fields = ['id', 'title', 'start_date', 'end_date', 'places_count', 'created_at']

    def get_places_count(self, obj):
        return obj.places.count()
