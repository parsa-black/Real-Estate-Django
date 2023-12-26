from django import forms
from .models import Users


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
    birth_date = forms.DateField(
        label='Birth Date',
        widget=forms.DateInput(attrs={'placeholder': 'BirthDate'})
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
    email = forms.EmailField(
        label='Email',
        max_length=255,
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}),
        error_messages={'required': 'Please Enter Your Email Address',
                        'max_length': 'Email Max Length Must Be 255 Characters'}
    )

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'username', 'birth_date', 'phone_number', 'email']
