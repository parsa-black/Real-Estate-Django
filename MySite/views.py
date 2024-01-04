# from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Property
from .forms import LoginForm, UserForm, ProfileForm, PropertyForm, ReviewForm, DocumentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password


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
    if request.user.profileuser.role == 'O':
        if request.method == 'POST':
            property_form = PropertyForm(request.POST)
            if property_form.is_valid():
                property_instance = property_form.save(commit=False)
                property_form.instance.house_owner = request.user.profileuser
                property_form.save()
                return redirect('home-page')
        else:
            property_form = PropertyForm()

        return render(request, 'propertyRegister.html', {
            'property_form': property_form
        })
    else:
        return render(request, 'access_denied.html', {})


@login_required()
def review_submit(request):
    if request.user.profileuser.role == 'T':
        if request.method == 'POST':
            review_form = ReviewForm(request.POST)
            document_form = DocumentForm(request.user, request.POST, request.FILES)

            if review_form.is_valid() and document_form.is_valid():
                # Save the review
                review = review_form.save(commit=False)
                review.tenant = request.user.profileuser
                review.save()

                # Save the document
                document = document_form.save(commit=False)
                review.property = document.property
                document.uploader = request.user.profileuser
                document.save()

                return redirect('home-page')  # Redirect to a success page or another view

        else:
            review_form = ReviewForm(request.user)
            document_form = DocumentForm()

        return render(request, 'review.html', {'review_form': review_form, 'document_form': document_form})
    else:
        return render(request, 'access_denied.html', {})
