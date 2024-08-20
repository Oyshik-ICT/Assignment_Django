# models.py

from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=[
        ('country', 'Country'),
        ('state', 'State'),
        ('city', 'City'),
    ])
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"


class Amenity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Property(models.Model):
    # property_id = models.AutoField(primary_key=True)
    property_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    locations = models.ManyToManyField(Location)
    amenities = models.ManyToManyField(Amenity)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    property = models.ForeignKey(
        Property, related_name='images', on_delete=models.CASCADE)
    img_src = models.URLField()

    def __str__(self):
        return f"Image for {self.property.title}"
