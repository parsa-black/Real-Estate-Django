# Generated by Django 5.0.1 on 2024-02-16 21:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0018_alter_profileuser_requestrole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='area',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='property',
            name='bathrooms',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='property',
            name='bedrooms',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='property',
            name='rent_price',
            field=models.DecimalField(decimal_places=2, default=1000000, max_digits=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='year',
            field=models.PositiveIntegerField(default=2000, validators=[django.core.validators.MaxValueValidator(2099)]),
        ),
    ]
