from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from MySite.dto import Dto
from .models import Property, Review, Document
from .forms import LoginForm, UserForm, ProfileForm, PropertyForm, ReviewForm, DocumentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
import sweetify
from django.db.models import Q


def homepage(request):
    properties = Property.objects.select_related('house_owner').filter(is_submit=True)
    return render(request, 'index.html', {'properties': properties})


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def search_view(request):
    query = request.GET.get('query')
    msg = None
    properties = None
    if query:
        properties = Property.objects.select_related('re').filter(title__icontains=query)
        context = {'properties': properties, 'query': query, 'msg': msg}
        return render(request, 'home.html', context)
    else:
        msg = 'Not Found'

    context = {'properties': properties, 'query': query, 'msg': msg}
    return render(request, 'home.html', context)


def property_view(request, property_id):
    prop = Property.objects.select_related('house_owner').get(id=property_id)
    comments = comments = Review.objects.filter(property_id=property_id).order_by('-time').values('comment')
    dto = Dto(prop.title, prop.house_review, prop.house_quality,
              prop.house_location, prop.house_price, prop.house_landlord, prop.house_neighborhood,
              prop.house_transportation)
    return render(request, 'Reviews.html', {'prop': dto, 'comments': comments})


def logout_view(request):
    logout(request)
    return redirect('login-page')


def register(request):
    msg = None
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid():
            if user_form.cleaned_data.get('password') == user_form.cleaned_data.get('confirm_password'):
                user = user_form.save(commit=False)
                hashed_password = make_password(user_form.cleaned_data['password'])
                # Create a user object but don't save
                user.password = hashed_password
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user  # Associate the profile with the user
                profile.save()
                return redirect('login-page')
            else:
                msg = 'Password should be equal to password confirm'
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'msg': msg
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
        sweetify.error(request, 'Access Denied')
        return redirect('home-page')


@login_required()
def review_submit(request, property_id):
    if request.user.profileuser.role == 'T':
        try:
            Document.objects.get(property_id=property_id, uploader_id=request.user.profileuser.id, status='Accepted')
            Review.objects.get(property_id=property_id, tenant_id=request.user.profileuser.id)
            sweetify.info(request, 'you already rate this house')
            return redirect('home-page')
        except Review.DoesNotExist:
            if request.method == 'POST':
                review_form = ReviewForm(request.POST)
                if review_form.is_valid():
                    prop = Property.objects.get(id=property_id)
                    review = review_form.save(commit=False)
                    review.tenant = request.user.profileuser
                    review.property = prop
                    review.save()
                    sweetify.success(request, 'Your review have been Submitted')
                    return redirect('home-page')
            else:
                review_form = ReviewForm()

            return render(request, 'reviewRegister.html', {'form': review_form})
        except Document.DoesNotExist:

            sweetify.error(request, 'first Your doc should be accepted by admin')
            return redirect('home-page')

    else:
        sweetify.error(request, 'Access Denied')
        return redirect('home-page')
        

@login_required()
def upload_view(request, property_id):
    if request.user.profileuser.role == 'T':
        form = DocumentForm(request.POST or None, request.FILES or None)
        try:
            Document.objects.get(Q(property_id=property_id) &
                                 Q(uploader_id=request.user.profileuser.id) &
                                 (Q(status='Pending') | Q(status='Accepted')))
            sweetify.info(request, 'you uploaded your doc')
            return redirect('home-page')
        except Document.DoesNotExist:
            if request.method == 'POST':
                form = DocumentForm(request.POST, request.FILES)
                if form.is_valid():
                    property_instance = Property.objects.get(id=property_id)
                    upload = form.save(commit=False)
                    upload.file = request.FILES['file']
                    upload.property = property_instance
                    upload.uploader = request.user.profileuser
                    upload.save()
                    sweetify.success(request, 'Your doc have been uploaded. wait for admin to accept it')
                    return redirect('home-page')
                else:
                    form = DocumentForm()
                return render(request, 'upload.html', {'form': form, 'msg': 'credentials incorrect'})
            else:
                return render(request, 'upload.html', {'form': form})

    else:
        sweetify.error(request, 'Access Denied')
        return redirect('home-page')
