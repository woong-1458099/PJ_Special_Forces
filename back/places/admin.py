from django.contrib import admin
from .models import Place

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'address', 'rating', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'address', 'description']
    ordering = ['-created_at']
