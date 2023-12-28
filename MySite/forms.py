from django import forms
from .models import User, ProfileUser


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

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']


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

    class Meta:
        model = ProfileUser
        fields = ['birth_date', 'phone_number']


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
