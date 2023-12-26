from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from .models import Property


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
        print(request.POST)
        return redirect(reverse('home-page'))
    return render(request, 'register.html', {})
