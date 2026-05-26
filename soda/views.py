from django.shortcuts import render
from .models import Drink
from django.http import JsonResponse, request
from .serializers import DrinksSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinksSerializer(drinks, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = DrinksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)     

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):

    try: 
        drinks = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinksSerializer(drinks)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DrinksSerializer(drinks, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        drinks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



