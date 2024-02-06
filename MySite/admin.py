from django.contrib import admin
from django.db.models import Count

from . import models


@admin.register(models.ProfileUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'role', 'property_count', 'phone_number', 'requestRole']
    list_editable = ['role']
    list_per_page = 10
    search_fields = ['username']

    @admin.display(ordering='property_count')
    def property_count(self, own):
        return own.property_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(property_count=Count('property'))


@admin.register(models.Document)
class DocumentAdmin(admin.ModelAdmin):
    autocomplete_fields = ['property', 'uploader']
    readonly_fields = ['time']
    list_display = ['property', 'uploader', 'status']
    list_editable = ['status']
    list_per_page = 10
    list_select_related = ['property', 'uploader']


@admin.register(models.Property)
class PropertyAdmin(admin.ModelAdmin):
    autocomplete_fields = ['house_owner']
    readonly_fields = ['house_review']
    list_display = ['title', 'house_owner', 'is_submit', 'is_available', 'house_review']
    list_editable = ['is_submit', 'is_available']
    list_per_page = 10
    list_select_related = ['house_owner']
    search_fields = ['title']


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    autocomplete_fields = ['property', 'tenant']
    readonly_fields = ['time']
    list_display = ['property', 'tenant', 'rating']
    list_per_page = 10
    list_select_related = ['property', 'tenant']
