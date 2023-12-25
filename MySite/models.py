from django.db import models
from django.core.validators import MaxValueValidator


class Users(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=30, blank=True, primary_key=True, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=10, unique=True)  # 0(912 345 6789)
    email = models.EmailField(max_length=255, unique=True)
    Owner = 'O'
    Tenant = 'T'
    User = 'U'
    ROLE_CHOICES = [
        (Owner, 'Owner'),
        (Tenant, 'Tenant'),
        (User, 'User'),
    ]
    role = models.CharField(
        max_length=1, choices=ROLE_CHOICES, default=User)

    def __str__(self):
        return self.username

    class Meta:
        indexes = [
            models.Index(fields=['first_name', 'last_name'])
        ]


class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)
    house_city = models.CharField(max_length=30)
    house_address = models.TextField()
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    area = models.PositiveIntegerField()
    yard_area = models.PositiveIntegerField()
    year = models.PositiveIntegerField(validators=[MaxValueValidator(2099)])
    garage = models.BooleanField()
    is_available = models.BooleanField(default=False)
    is_submit = models.BooleanField(default=False)
    house_review = models.FloatField(null=True, blank=True)
    house_owner = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.house_owner.username}"

    class Meta:
        indexes = [
            models.Index(fields=['title'])
        ]


class Document(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    uploader = models.ForeignKey(Users, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    status = models.BooleanField(default=False)


class Review(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Users, on_delete=models.CASCADE)
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
        total_rating = self.quality + self.location + self.price + self.landlord\
                                    + self.neighborhood + self.Transportation
        self.rating = total_rating / criteria_count
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.property.title} - {self.tenant.username}"
