from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Property, ProfileUser
from .forms import LoginForm, UserForm
from django.contrib.auth.hashers import make_password, check_password


def homepage(request):
    return render(request, 'home.html')


def list_house(request):
    try:
        houses = Property.objects.all()
        context = {'data_list': houses}
        return render(request, 'list.html', context)
    except ObjectDoesNotExist:
        pass


def register(request):
    print(request.method)
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            hashed_password = make_password(user_form.cleaned_data['password'])  # Create a user object but don't save
            user.password = hashed_password
            user.save()
            return redirect('home-page')
    else:
        user_form = UserForm()
    return render(request, 'register.html', {
        'user_form': user_form
    })


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home-page')

    form = LoginForm(request.POST or None)
    print(request.method)
    msg = None

    if request.method == 'POST':

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user = ProfileUser.objects.get(username=username)
            except ProfileUser.DoesNotExist:
                user = None
            if user is not None:
                password_matches = check_password(password, user.password)
                if password_matches: 
                    return redirect('home-page')
                msg = 'Invalid credentials'
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, 'login.html', {'form': form, 'msg': msg})
