from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from . models import Property


def list_house(request):
    try:
        houses = Property.objects.all()
    except ObjectDoesNotExist:
        pass

    context = {'data_list': houses}
    return render(request, 'list.html', context)
