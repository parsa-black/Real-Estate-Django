# from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Property, User
from .forms import LoginForm, UserForm, ProfileForm, PropertyForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password


def homepage(request):
    return render(request, 'home.html')


def logout_view(request):
    logout(request)
    return redirect('login-page')


def list_house(request):
    try:
        houses = Property.objects.all()
        context = {'data_list': houses}
        return render(request, 'list.html', context)
    except ObjectDoesNotExist:
        pass


def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            hashed_password = make_password(user_form.cleaned_data['password'])  # Create a user object but don't save
            user.password = hashed_password
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user  # Associate the profile with the user
            profile.save()
            return redirect('home-page')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home-page')

    form = LoginForm(request.POST or None)
    msg = None

    if request.method == 'POST':

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home-page')
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, 'login.html', {'form': form, 'msg': msg})


@login_required()
def property_register(request):
    if request.method == 'POST':
        property_form = PropertyForm(request.POST)
        if property_form.is_valid():
            property_form.instance.house_owner = request.user
            property_form.save()
            return redirect('home-page')
    else:
        property_form = PropertyForm()

    return render(request, 'propertyRegister.html', {
        'property_form': property_form
    })
