from rest_framework import viewsets
from django.shortcuts import render
from .models import Division, GroupPolicy, DomenUser, Computers, SchemaParams
from .serializers import DivisionSerializer, DomenUserSerializer, ComputerSerializer, GroupPolicySerializer, SchemaParamsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend, ]
    filterset_fields = ['name', 'group_policy']
    search_fields = ['name' ]
    

    
class GroupPolicyViewSet(viewsets.ModelViewSet):
    queryset = GroupPolicy.objects.all()
    serializer_class = GroupPolicySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend, ]
    filterset_fields = ['name', 'body']
    search_fields = ['name', ]


class DomenUserViewSet(viewsets.ModelViewSet):
    queryset = DomenUser.objects.all()
    serializer_class = DomenUserSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, ]
    filterset_fields = ['name', 'division']
    search_fields = ['name', ]
    

class ComputersViewSet(viewsets.ModelViewSet):
    queryset = Computers.objects.all()
    serializer_class = ComputerSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, ]
    filterset_fields = ['name', 'division']
    search_fields = ['name', ]
    

class SchemaParamsViewSet(viewsets.ModelViewSet):
    queryset = SchemaParams.objects.all()
    serializer_class = SchemaParamsSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, ]
    filterset_fields = ['type',]