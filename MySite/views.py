from django.shortcuts import render
from . models import Property


def list_house(request):

    houses = Property.objects.all()

    context = {'data_list': houses}
    return render(request, 'list.html', context)
