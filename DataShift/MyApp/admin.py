# from django.contrib import admin
# from .models import Location, Amenity, Property, Image

# @admin.register(Location)
# class LocationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'type', 'latitude', 'longitude')
#     list_filter = ('type',)
#     search_fields = ('name', 'type')

# @admin.register(Amenity)
# class AmenityAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)

# class ImageInline(admin.TabularInline):
#     model = Image
#     extra = 1

# @admin.register(Property)
# class PropertyAdmin(admin.ModelAdmin):
#     # Display these fields in the list view
#     list_display = ('property_id', 'title', 'create_date', 'update_date')
#     search_fields = ('property_id', 'title', 'description')
#     list_filter = ('create_date', 'update_date')
#     inlines = [ImageInline]
#     filter_horizontal = ('locations', 'amenities')
    
#     # Add property_id to the fields in the form view
#     fields = ('property_id', 'title', 'description', 'locations', 'amenities', 'create_date', 'update_date')
    
#     readonly_fields = ('create_date', 'update_date')

# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('property', 'img_src')
#     search_fields = ('property__title',)



# from django.contrib import admin
# from django.utils.html import format_html
# from .models import Location, Amenity, Property, Image

# @admin.register(Location)
# class LocationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'type', 'latitude', 'longitude')
#     list_filter = ('type',)
#     search_fields = ('name', 'type')

# @admin.register(Amenity)
# class AmenityAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)

# class ImageInline(admin.TabularInline):
#     model = Image
#     extra = 1

# @admin.register(Property)
# class PropertyAdmin(admin.ModelAdmin):
#     list_display = ('property_id', 'title', 'create_date', 'update_date')
#     search_fields = ('property_id', 'title', 'description')
#     list_filter = ('create_date', 'update_date')
#     inlines = [ImageInline]
#     filter_horizontal = ('locations', 'amenities')
#     fields = ('property_id', 'title', 'description', 'locations', 'amenities', 'create_date', 'update_date')
#     readonly_fields = ('create_date', 'update_date')

#     def first_image_thumbnail(self, obj):
#         # Get the first image for the property
#         first_image = obj.image_set.first()  # Assuming reverse relation from Property to Image
#         if first_image and first_image.img_src:
#             img_url = first_image.img_src
#             return format_html('<img src="{}" style="width: 100px; height: auto;">', img_url)
#         return "No Image"
#     first_image_thumbnail.short_description = 'First Image'

# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('property', 'img_src', 'image_thumbnail')
#     search_fields = ('property__title',)
    
#     def image_thumbnail(self, obj):
#         if obj.img_src:
#             # Adjust the URL to include MEDIA_URL prefix
#             img_url = obj.img_src
#             return format_html('<img src="{}" style="width: 100px; height: auto;">', img_url)
#         return "No Image"
#     image_thumbnail.short_description = 'Thumbnail'





from django.contrib import admin
from django.utils.html import format_html
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
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.img_src:
            return format_html('<img src="{}" style="width: 150px; height: auto;">', obj.img_src)
        return "No Image"

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_id', 'title', 'create_date', 'update_date', 'first_image_thumbnail')
    search_fields = ('property_id', 'title', 'description')
    list_filter = ('create_date', 'update_date')
    inlines = [ImageInline]
    filter_horizontal = ('locations', 'amenities')
    fields = ('property_id', 'title', 'description', 'locations', 'amenities', 'create_date', 'update_date')
    readonly_fields = ('create_date', 'update_date', 'first_image_thumbnail')

    def first_image_thumbnail(self, obj):
        # Assuming Image has a ForeignKey to Property named 'property'
        first_image = Image.objects.filter(property=obj).first()
        if first_image and first_image.img_src:
            return format_html('<img src="{}" style="width: 150px; height: auto;">', first_image.img_src)
        return "No Image"
    first_image_thumbnail.short_description = 'First Image'

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'img_src', 'image_thumbnail')
    search_fields = ('property__title',)
    
    def image_thumbnail(self, obj):
        if obj.img_src:
            return format_html('<img src="{}" style="width: 150px; height: auto;">', obj.img_src)
        return "No Image"
    image_thumbnail.short_description = 'Thumbnail'