from django.shortcuts import render
from .models import MenuItem
from rest_framework import viewsets
from .serializers import MenuItemSerializer

# Create your views here.


class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']
    search_fields = ['title', 'category__title']
