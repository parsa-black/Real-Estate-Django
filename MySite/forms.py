from django import forms
from .models import User, ProfileUser, Property, Review, Document

ROLE_CHOICES = [
        ('Owner', 'Owner'),
        ('Tenant', 'Tenant'),
        ('User', 'User'),
    ]


class UserForm(forms.ModelForm):
    first_name = forms.CharField(
        label='FirstName',
        max_length=25,
        widget=forms.TextInput(attrs={'placeholder': 'FirstName'}),
        error_messages={'required': 'Please Enter Your First Name',
                        'max_length': 'FirstName Max Length Must Be 25 Characters'}
    )
    last_name = forms.CharField(
        label='LastName',
        max_length=25,
        widget=forms.TextInput(attrs={'placeholder': 'LastName'}),
        error_messages={'required': 'Please Enter Your Last Name',
                        'max_length': 'LastName Max Length Must Be 25 Characters'}
    )
    username = forms.CharField(
        label='UserName',
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'UserName'}),
        error_messages={'required': 'Please Enter Your UserName',
                        'max_length': 'UserName Max Length Must Be 30 Characters'}
    )
    password = forms.CharField(
        label='Password',
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Password'}),
        error_messages={'required': 'Please Enter Your Password',
                        'max_length': 'Password Max Length Must Be 30 Characters'}
    )
    email = forms.EmailField(
        label='Email',
        max_length=255,
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}),
        error_messages={'required': 'Please Enter Your Email Address',
                        'max_length': 'Email Max Length Must Be 255 Characters'}
    )

    confirm_password = password = forms.CharField(
        label='Password',
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Password'}),
        error_messages={'required': 'Please Enter Your Password',
                        'max_length': 'Password Max Length Must Be 30 Characters'}
    )


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email',
                  'confirm_password']


class ProfileForm(forms.ModelForm):
    birth_date = forms.DateField(
        label='Birth Date',
        widget=forms.DateInput(attrs={'placeholder': 'BirthDate', 'type': 'date'})
    )
    phone_number = forms.CharField(
        label='Phone Number',
        max_length=10,
        min_length=10,
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}),
        error_messages={'required': 'Please Enter Your Phone Number',
                        'max_length': 'Phone Number must be 10 Characters',
                        'min_length': 'Phone Number must be 10 Characters'}
    )
    requestRole = forms.ChoiceField(
        label='RequestRole',
        choices=ROLE_CHOICES,
    )
    class Meta:
        model = ProfileUser
        fields = ['birth_date', 'phone_number', 'requestRole']


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    remember = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(),
    )

    class Meta:
        model = User
        fields = ['username', 'password']


class PropertyForm(forms.ModelForm):
    title = forms.CharField(
        label='Property Title',
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Property Title'}),
        error_messages={'required': 'Please Enter The Title',
                        'max_length': 'Max Length Must Be 255'}
    )
    description = forms.CharField(
        label='Description',
        max_length=400,
        widget=forms.Textarea(attrs={'placeholder': 'Descriptions'}),
        error_messages={'required': 'Please Enter The Description',
                        'max_length': 'Description Must Be Under 400 Characters'}
    )
    rent_price = forms.DecimalField(
        label='Rent Price',
        max_digits=10,
        decimal_places=2,
        min_value=0,
        max_value=9999999,
        initial=1000000,
        error_messages={'required': 'Please Property Must Have Rent Price',
                        'min_value': 'Please Price can not be less than Zero',
                        'max_value': 'Please Price can not be More than 10 digits'}
    )
    house_city = forms.CharField(
        label='House City',
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'City'}),
        error_messages={'required': 'Please Enter House City',
                        'max_length': 'Max Length Must Be 30 Characters'}
    )
    house_address = forms.CharField(
        label='House Address',
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Address'}),
        error_messages={'required': 'Please Enter Address',
                        'max_length': 'Max Length Must Be 255'}
    )
    bedrooms = forms.IntegerField(
        min_value=0,
        max_value=20,
        initial=0,
        error_messages={'required': 'House Must Have Bedrooms',
                        'max_value': 'Max is 20',
                        'min_value': 'Min is 0'}
    )
    bathrooms = forms.IntegerField(
        min_value=0,
        max_value=20,
        initial=0,
        error_messages={'required': 'House Must Have Bathroom',
                        'max_value': 'Max is 20',
                        'min_value': 'Min is 0'}
    )
    area = forms.IntegerField(
        min_value=0,
        initial=0,
        max_value=99999,
        error_messages={'required': 'Property Must Have Area',
                        'min_value': 'Size Must Be Positive',
                        'max_value': 'Size is too High'}
    )
    yard_area = forms.IntegerField(
        min_value=0,
        max_value=99999,
        initial=0,
        required=False,
        error_messages={'min_value': 'Size Must Be Positive',
                        'max_value': 'Size is too High'}
    )
    year = forms.IntegerField(
        min_value=1900,
        max_value=2099,
        initial=2000,
        error_messages={'required': 'Property Must Have Built Year',
                        'max_value': 'Max is 2099',
                        'min_value': 'Min is 1900'}
    )
    garage = forms.BooleanField(
        required=False
    )

    image = forms.ImageField(
        required=False
    )

    class Meta:
        model = Property
        fields = ['title', 'description', 'rent_price', 'house_city', 'house_address', 'bedrooms', 'bathrooms',
                  'area', 'yard_area', 'year', 'garage', 'image']


class ReviewForm(forms.ModelForm):
    quality = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type': 'range', 'min': '1', 'max': '5', 'value': '3'}),
        min_value=1,
        max_value=5,
        initial=3,
    )
    location = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type': 'range', 'min': '1', 'max': '5', 'value': '3'}),
        min_value=1,
        max_value=5,
        initial=3,
    )
    price = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type': 'range', 'min': '1', 'max': '5', 'value': '3'}),
        min_value=1,
        max_value=5,
        initial=3,
    )
    landlord = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type': 'range', 'min': '1', 'max': '5', 'value': '3'}),
        min_value=1,
        max_value=5,
        initial=3,
    )
    neighborhood = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type': 'range', 'min': '1', 'max': '5', 'value': '3'}),
        min_value=1,
        max_value=5,
        initial=3,
    )
    transportation = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type': 'range', 'min': '1', 'max': '5', 'value': '3'}),
        min_value=1,
        max_value=5,
        initial=3,
    )
    comment = forms.CharField(
        label='Comment',
        max_length=400,
        widget=forms.Textarea(attrs={'placeholder': 'Comment'}),
        error_messages={'required': 'Please provide your Comment',
                        'max_length': 'Description Must Be Under 400 Characters'}
    )

    class Meta:
        model = Review
        fields = ['quality', 'location', 'price', 'landlord', 'neighborhood', 'transportation', 'comment']


class DocumentForm(forms.ModelForm):
    file = forms.FileField()

    class Meta:
        model = Document
        fields = ['file']
        widgets = {'upload': forms.FileInput(attrs={'required': True})}
