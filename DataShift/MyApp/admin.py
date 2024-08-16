# from django.contrib import admin
# from .models import Property, Location, Amenity, Image

# # Customize the admin interface for the Property model
# class PropertyAdmin(admin.ModelAdmin):
#     # Display these fields in the list view
#     list_display = ('title', 'create_date', 'update_date')
    
#     # Add filtering options based on create_date and update_date
#     list_filter = ('create_date', 'update_date')
    
#     # Make the create_date and update_date fields read-only in the admin form
#     readonly_fields = ('create_date', 'update_date')

# # Register your models here
# admin.site.register(Property, PropertyAdmin)
# admin.site.register(Location)
# admin.site.register(Amenity)
# admin.site.register(Image)

from django.contrib import admin
from .models import Location, Amenity, Property, Image

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'latitude', 'longitude')
    list_filter = ('type',)
    search_fields = ('name', 'type')

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'update_date')
    search_fields = ('title', 'description')
    list_filter = ('create_date', 'update_date')
    inlines = [ImageInline]
    filter_horizontal = ('locations', 'amenities')
    readonly_fields = ('create_date', 'update_date')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'img_src')
    search_fields = ('property__title',)

