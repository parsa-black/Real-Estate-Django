# Generated by Django 5.0.1 on 2024-04-19 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0020_profileuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Mysite/images'),
        ),
    ]
