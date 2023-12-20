from django.db import models
from django.core.validators import MaxValueValidator


class user(models.Model):
    username = models.CharField(max_length=30, blank=True, primary_key=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=10, unique=True)  # 0(912 345 6789)
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.username


class userProfile(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE, primary_key=True)
    is_owner = models.BooleanField(default=False)
    is_tenant = models.BooleanField(default=False)


class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    area = models.PositiveIntegerField()
    yard_area = models.PositiveIntegerField()
    year = models.PositiveIntegerField(validators=[MaxValueValidator(2099)])
    garage = models.BooleanField()
    is_available = models.BooleanField(default=True)
    is_submit = models.BooleanField(default=False, editable=False)
    house_owner = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    house_review = models.FloatField(editable=False, blank=True)

    def __str__(self):
        return f"{self.title} - {self.house_owner.user.username}"


class Document(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    uploader = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')


class Review(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant = models.ForeignKey(userProfile, on_delete=models.CASCADE)
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
        total_rating = self.quality + self.location + self.price + self.landlord + self.neighborhood + self.Transportation
        self.rating = total_rating / criteria_count
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.property.title} - {self.tenant.user.username}"
