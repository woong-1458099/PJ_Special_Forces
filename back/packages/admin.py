from django.contrib import admin
from .models import Package, PackagePlace

class PackagePlaceInline(admin.TabularInline):
    model = PackagePlace
    extra = 1

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'start_date', 'end_date', 'budget', 'created_at']
    list_filter = ['created_at', 'start_date']
    search_fields = ['title', 'description', 'user__username']
    ordering = ['-created_at']
    inlines = [PackagePlaceInline]

@admin.register(PackagePlace)
class PackagePlaceAdmin(admin.ModelAdmin):
    list_display = ['package', 'place', 'day', 'order', 'created_at']
    list_filter = ['day', 'created_at']
    ordering = ['package', 'day', 'order']
