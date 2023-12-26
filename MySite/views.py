from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from .models import Property
from .froms import UserForm


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
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            print(user_form.cleaned_data)
            return redirect(reverse('home-page'))
    else:
        user_form = UserForm()

    return render(request, 'register.html', {
        'user_form': user_form
    })
