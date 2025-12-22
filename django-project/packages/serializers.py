from rest_framework import serializers
from .models import Package, PackageItem
from places.serializers import PlaceSerializer

class PackageItemOutSerializer(serializers.ModelSerializer):
    place = PlaceSerializer(read_only=True)

    class Meta:
        model = PackageItem
        fields = ('order', 'time', 'place')

class PackageSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = Package
        fields = ('id', 'title', 'concept', 'created_at', 'items')

    def get_items(self, obj):
        qs = PackageItem.objects.filter(package=obj).select_related('place').order_by('order')
        return PackageItemOutSerializer(qs, many=True).data
