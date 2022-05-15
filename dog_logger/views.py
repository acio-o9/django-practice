from django.http import HttpResponse
from django.shortcuts import render

from .models import ActionHistory, ActionType, Dog, Owner
from .serializers import OwnerSerializer
from rest_framework import serializers

# Create your views here.

def index(request):
    owners = Owner.objects.all()
    dogs = Dog.objects.all()
    action_types = ActionType.objects.all()
    action_histories = ActionHistory.objects.all()
    context = {
            'owners': OwnerSerializer(owners, many=True).data,
            'dogs': dogs,
            'action_types': action_types,
            'action_histories': action_histories,
            }
    return render(request, 'dog_logger/index.html', context)

def owner(request, owner_id):
    owner = Owner.objects.filter(pk=owner_id).first()
    if not owner:
        return HttpResponse('not found.')
    serializer = OwnerSerializer(owner)
    context = serializer.data

    return render(request, 'dog_logger/owner.html', context)


