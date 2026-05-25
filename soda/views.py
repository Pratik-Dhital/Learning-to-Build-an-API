from django.shortcuts import render
from .models import Drink
from django.http import JsonResponse, request
from .serializers import DrinksSerializer
# Create your views here.

def drink_list(request):
    drinks = Drink.objects.all()
    serializer = DrinksSerializer(drinks, many=True)
    return JsonResponse(serializer.data, safe=False)