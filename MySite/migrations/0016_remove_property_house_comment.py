# Generated by Django 5.0.1 on 2024-02-11 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0015_remove_property_images_property_house_comment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='house_comment',
        ),
    ]
