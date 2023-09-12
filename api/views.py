from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
from api.models import Pokdx
from api.serializers import PokdxSerializer

# Create your views here.
class PokdxList(generics.ListAPIView):
    queryset = Pokdx.objects.all()
    serializer_class = PokdxSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name','type1','type2']
    ordering_fields = ['pokedex_number', 'height_m','weight_kg']
    ordering = ['pokedex_number']
    
class PokdxDetail(generics.RetrieveAPIView):
    queryset = Pokdx.objects.all()
    serializer_class = PokdxSerializer