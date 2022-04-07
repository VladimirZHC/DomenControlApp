from rest_framework import viewsets
from .models import OrgUnit, GroupPolicy, Host, DomainUser, ParamsSchema
from .serializers import (
    GroupPolicySerializer, 
    DomainUserSerializer, 
    OrgUnitSerializer, 
    ParamsSchemaSerializer, 
    HostSerializer,
    OrgUnitCreatedUpdateSerializer,
                        )
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination



class OrgUnitViewSet(viewsets.ModelViewSet):
    serializer_class = OrgUnitSerializer
    queryset = OrgUnit.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend, ]
    filterset_fields = ['name', 'group_policies']
    search_fields = ['name' ]
    
    # def get_serializer(self, request, *args, **kwargs):
    #     if request.method == 'POST' or request.method == 'PUT':
    #         return OrgUnitCreatedUpdateSerializer
    #     return OrgUnitSerializer
            
        
    
    def list(self, request, *args, **kwargs):
        data = super().list(request, *args, **kwargs)
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
    
    def retrieve(self, request, *args, **kwargs):
        data = super().retrieve(request, *args, **kwargs)
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
        

    def create(self, request, *args, **kwargs):
        serializer = OrgUnitCreatedUpdateSerializer(request, data=request.data.get('data'))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return self.retrieve(serializer.data.get('id'))
        
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = OrgUnitCreatedUpdateSerializer(instance, request, data=request.data.get('data'), partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return self.retrieve(serializer.data.get('id'))
    
    def destroy(self, request, *args, **kwargs):
        data =  super().destroy(request, *args, **kwargs)
        body = {
            'data': "string",
            'success': True
        }
        return Response(data=body, status=200)

    
class GroupPolicyViewSet(viewsets.ModelViewSet):
    queryset = GroupPolicy.objects.all()
    serializer_class = GroupPolicySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend, ]
    filterset_fields = ['name',]
    search_fields = ['name', ]
    
    def list(self, request, *args, **kwargs):
        data = super().list(request, *args, **kwargs)
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
    def retrieve(self, request, *args, **kwargs):
        data = super().retrieve(request, *args, **kwargs)
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
        

    def create(self, request, *args, **kwargs):
        data =  super().create(request, *args, **kwargs)
    
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
    
    def update(self, request, *args, **kwargs):
        data =  super().update(request, *args, **kwargs)
    
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
    
    def destroy(self, request, *args, **kwargs):
        data =  super().destroy(request, *args, **kwargs)
        body = {
            'data': "string",
            'success': True
        }
        return Response(data=body, status=200)


class DomainUserViewSet(viewsets.ModelViewSet):
    queryset = DomainUser.objects.all()
    serializer_class = DomainUserSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, ]
    filterset_fields = ['name', 'orgunit']
    search_fields = ['name', ]
    
    def list(self, request, *args, **kwargs):
        data = super().list(request, *args, **kwargs)
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
    def retrieve(self, request, *args, **kwargs):
        data = super().retrieve(request, *args, **kwargs)
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
        

    def create(self, request, *args, **kwargs):
        data =  super().create(request, *args, **kwargs)
    
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
    
    def update(self, request, *args, **kwargs):
        data =  super().update(request, *args, **kwargs)
    
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
    
    def destroy(self, request, *args, **kwargs):
        data =  super().destroy(request, *args, **kwargs)
        body = {
            'data': "string",
            'success': True
        }
        return Response(data=body, status=200)
    

class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, ]
    filterset_fields = ['name', 'orgunit']
    search_fields = ['name', ]
    
    def list(self, request, *args, **kwargs):
        data = super().list(request, *args, **kwargs)
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
    def retrieve(self, request, *args, **kwargs):
        data = super().retrieve(request, *args, **kwargs)
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
        

    def create(self, request, *args, **kwargs):
        data =  super().create(request, *args, **kwargs)
    
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
    
    def update(self, request, *args, **kwargs):
        data =  super().update(request, *args, **kwargs)
    
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
    
    def destroy(self, request, *args, **kwargs):
        data =  super().destroy(request, *args, **kwargs)
        body = {
            'data': "string",
            'success': True
        }
        return Response(data=body, status=200)
    

class ParamsSchemaViewSet(viewsets.ModelViewSet):
    queryset = ParamsSchema.objects.all()
    serializer_class = ParamsSchemaSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, ]
    filterset_fields = ['type',]
    def list(self, request, *args, **kwargs):
        data = super().list(request, *args, **kwargs)
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
    def retrieve(self, request, *args, **kwargs):
        data = super().retrieve(request, *args, **kwargs)
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
    
    def update(self, request, *args, **kwargs):
        data =  super().update(request, *args, **kwargs)
    
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
    
    

class PageNumberPaginationDataOnly(PageNumberPagination):

    def get_paginated_response(self, data):
        return Response(data)
    
