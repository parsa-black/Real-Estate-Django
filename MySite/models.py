from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db.models import Avg


class User(AbstractUser):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)


class ProfileUser(models.Model):
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=10, unique=True,
                                    validators=[
                                        MinLengthValidator(limit_value=10),
                                        MaxLengthValidator(limit_value=10),
                                    ])  # 0(912 345 6789)
    Owner = 'O'
    Tenant = 'T'
    UserNormal = 'U'
    ROLE_CHOICES = [
        (Owner, 'Owner'),
        (Tenant, 'Tenant'),
        (UserNormal, 'User'),
    ]
    role = models.CharField(
        max_length=1, choices=ROLE_CHOICES, default=UserNormal)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def username(self):
        return self.user.username

    def password(self):
        return self.user.password

    def email(self):
        return self.user.email

    class Meta:
        verbose_name = 'User'


class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=400)
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)
    house_city = models.CharField(max_length=30)
    house_address = models.CharField(max_length=255)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    area = models.PositiveIntegerField()
    yard_area = models.PositiveIntegerField(default=0)
    year = models.PositiveIntegerField(validators=[MaxValueValidator(2099)])
    garage = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)
    is_submit = models.BooleanField(default=False)
    house_review = models.FloatField(null=True, blank=True)
    house_owner = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)

    def update_average_rating(self):
        # Retrieve the average rating for the property
        average_rating = Review.objects.filter(property=self).aggregate(Avg('rating'))['rating__avg']

        # Update the house_review field
        self.house_review = round(average_rating, 2) if average_rating else 0
        self.save()

    def __str__(self):
        return f"{self.title} - {self.house_owner.username}"

    class Meta:
        indexes = [
            models.Index(fields=['title'])
        ]
        ordering = ["is_submit", "is_available"]


class Document(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    uploader = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    status = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.property} - {self.uploader.username}"

    class Meta:
        ordering = ['status']


class Review(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    quality = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    location = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    price = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    landlord = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    neighborhood = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    Transportation = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    rating = models.FloatField(default=0, editable=False)
    comment = models.TextField()
    Time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calculate the average rating
        criteria_count = 6  # Number of criteria for evaluation
        total_rating = self.quality + self.location + self.price + self.landlord + self.neighborhood \
                                    + self.Transportation
        self.rating = round(total_rating / criteria_count, 2)

        super().save(*args, **kwargs)

        # Update the average rating for the associated Property
        self.property.update_average_rating()

    def __str__(self):
        return f"{self.property.title} - {self.tenant.username}"
