# Generated by Django 5.1 on 2024-08-19 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
