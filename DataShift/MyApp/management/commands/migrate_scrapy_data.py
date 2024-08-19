# from django.core.management.base import BaseCommand
# from django.db import connections, transaction
# from MyApp.models import Property, Location, Image, Amenity

# class Command(BaseCommand):
#     help = 'Migrate data from Scrapy database to Django database'

#     def handle(self, *args, **kwargs):
#         # Connect to the Scrapy database
#         scrapy_connection = connections['scrapy']

#         with scrapy_connection.cursor() as cursor:
#             cursor.execute("SELECT * FROM hotels")
#             hotels = cursor.fetchall()

#             # Get the column names to map the fields
#             columns = [col[0] for col in cursor.description]

#             # Begin a transaction for the default database
#             with transaction.atomic(using='default'):
#                 for hotel in hotels:
#                     hotel_data = dict(zip(columns, hotel))

#                     # Sanitize and truncate data to fit model constraints
#                     full_address = hotel_data['fullAddress'][:100]  # Adjust max length as needed
#                     hotel_name = hotel_data['hotelName'][:100]  # Adjust max length as needed
#                     brief = hotel_data['brief'][:500]  # Adjust max length as needed

#                     # Create or get Location
#                     location, created = Location.objects.using('default').get_or_create(
#                         name=full_address,
#                         defaults={
#                             'type': 'city', 
#                             'latitude': hotel_data.get('lat', None), 
#                             'longitude': hotel_data.get('lon', None)
#                         }
#                     )

#                     # Update or create Property
#                     property_obj, created = Property.objects.using('default').update_or_create(
#                         property_id=hotel_data['hotelId'],
#                         defaults={
#                             'title': hotel_name,
#                             'description': brief,
#                         }
#                     )
#                     if created:
#                         property_obj.locations.add(location)

#                     # Clear existing amenities and add new ones
#                     if hotel_data.get('hotelFacilityList'):
#                         amenities = []
#                         for amenity_name in hotel_data['hotelFacilityList']:
#                             amenity_name = amenity_name[:100]  # Adjust max length as needed
#                             amenity, created = Amenity.objects.using('default').get_or_create(name=amenity_name)
#                             amenities.append(amenity)
#                         property_obj.amenities.set(amenities)

#                     # Add or update images
#                     img_src = hotel_data.get('imgUrl', '')[:255]  # Adjust max length as needed
#                     Image.objects.using('default').update_or_create(
#                         property=property_obj,
#                         img_src=img_src,
#                         defaults={'img_src': img_src}
#                     )

#         self.stdout.write(self.style.SUCCESS('Data migration from Scrapy to Django completed successfully!'))


import shutil
import os
from django.core.management.base import BaseCommand
from django.db import connections, transaction
from MyApp.models import Property, Location, Image, Amenity
from django.conf import settings

class Command(BaseCommand):
    help = 'Migrate data and images from Scrapy database to Django database'

    def handle(self, *args, **kwargs):
        # Connect to the Scrapy database
        scrapy_connection = connections['scrapy']

        with scrapy_connection.cursor() as cursor:
            cursor.execute("SELECT * FROM hotels")
            hotels = cursor.fetchall()

            # Get the column names to map the fields
            columns = [col[0] for col in cursor.description]

            # Begin a transaction for the default database
            with transaction.atomic(using='default'):
                for hotel in hotels:
                    hotel_data = dict(zip(columns, hotel))

                    # Sanitize and truncate data to fit model constraints
                    full_address = hotel_data['fullAddress'][:100]  # Adjust max length as needed
                    hotel_name = hotel_data['hotelName'][:100]  # Adjust max length as needed
                    brief = hotel_data['brief'][:500]  # Adjust max length as needed

                    # Create or get Location
                    location, created = Location.objects.using('default').get_or_create(
                        name=full_address,
                        defaults={
                            'type': 'city', 
                            'latitude': hotel_data.get('lat', None), 
                            'longitude': hotel_data.get('lon', None)
                        }
                    )

                    # Update or create Property
                    property_obj, created = Property.objects.using('default').update_or_create(
                        property_id=hotel_data['hotelId'],
                        defaults={
                            'title': hotel_name,
                            'description': brief,
                        }
                    )
                    if created:
                        property_obj.locations.add(location)

                    # Clear existing amenities and add new ones
                    if hotel_data.get('hotelFacilityList'):
                        amenities = []
                        for amenity_name in hotel_data['hotelFacilityList']:
                            amenity_name = amenity_name[:100]  # Adjust max length as needed
                            amenity, created = Amenity.objects.using('default').get_or_create(name=amenity_name)
                            amenities.append(amenity)
                        property_obj.amenities.set(amenities)

                    # Correct and add or update images
                    img_src = hotel_data.get('imgUrl', '')
                    img_src = f'/media/hotel_images/{os.path.basename(img_src)}'  # Adjust according to your setup

                    if img_src:
                        # Ensure the image URL points to a valid file
                        Image.objects.using('default').update_or_create(
                            property=property_obj,
                            img_src=img_src,
                            defaults={'img_src': img_src}
                        )

        # Migrate images from Scrapy to Django media directory
        self.migrate_images()

        self.stdout.write(self.style.SUCCESS('Data and images migrated from Scrapy to Django successfully!'))

    def migrate_images(self):
        # Define source and destination directories
        scrapy_image_dir = '/home/w3e55/w3_assignment/Assignment_5_modified/hotalInfo/hotel_images'
        django_image_dir = os.path.join(settings.BASE_DIR, 'media', 'hotel_images')

        # Create destination directory if it does not exist
        if not os.path.exists(django_image_dir):
            os.makedirs(django_image_dir)

        # Copy images from Scrapy to Django media directory
        for filename in os.listdir(scrapy_image_dir):
            src = os.path.join(scrapy_image_dir, filename)
            dst = os.path.join(django_image_dir, filename)
            shutil.copy(src, dst)

