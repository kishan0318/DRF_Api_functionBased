from django.shortcuts import render
from rest_framework.response import Response
from .models import Items
from .serializer import ItemSerl
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def list_items(request):
    items=Items.objects.all()
    ser=ItemSerl(items,many=True)
    return Response(ser.data)

@api_view(['GET'])
def detailed_view(request,pk):
    items=Items.objects.get(id=pk)
    ser=ItemSerl(items,many=False)
    return Response(ser.data)

@api_view(['PUT'])
def create_view(request):
    ser=ItemSerl(data=request.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)

@api_view(['PUT'])
def update_view(request,pk):
    items=Items.objects.get(id=pk)
    ser=ItemSerl(instance=items,data=request.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)

@api_view(['DELETE'])
def delete_view(request,pk):
    items=Items.objects.get(id=pk)
    items.delete()
    return Response('Item Deleted Succesfully')


     
