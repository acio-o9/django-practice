from django.http import HttpResponse
from django.shortcuts import render

from .models import ActionType, Dog, Owner

# Create your views here.

def index(request):
    owners = Owner.objects.all()
    dogs = Dog.objects.all()
    action_types = ActionType.objects.all()
    context = {
            'owners': owners,
            'dogs': dogs,
            'action_types': action_types,
            }
    return render(request, 'dog_logger/index.html', context)

def owner(request, owner_id):
    owner = Owner.objects.filter(pk=owner_id).first()
    if not owner:
        return HttpResponse('not found.')
    context = {'id': owner.pk, 'name': owner.name}

    return render(request, 'dog_logger/owner.html', context)
