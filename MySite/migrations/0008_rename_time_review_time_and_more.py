# Generated by Django 5.0 on 2024-01-04 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0007_alter_review_transportation_alter_review_landlord_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='Transportation',
            new_name='transportation',
        ),
    ]
