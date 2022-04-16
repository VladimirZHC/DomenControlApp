from ast import Return
from rest_framework import viewsets
from uritemplate import partial
from .models import HistoryGroupPolicy, HistoryParamsSchema, OrgUnit, GroupPolicy, Host, DomainUser, ParamsSchema
from .serializers import (
    GroupPolicySerializer, 
    DomainUserSerializer,
    HistoryGroupPolicySerializer,
    HistoryParamsSchemaSerializer, 
    OrgUnitSerializer, 
    ParamsSchemaSerializer, 
    HostSerializer,
    OrgUnitCreatedUpdateSerializer,
    HostCreateUpdateSerializer,
    DomainUserCreateSerializer,
    DomainUserUpdateSerializer,
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
        serializer = OrgUnitCreatedUpdateSerializer(data=request.data.get('data'))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data =  OrgUnitSerializer(serializer.instance)
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
        
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = OrgUnitCreatedUpdateSerializer(instance, data=request.data.get('data'), partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data =  OrgUnitSerializer(serializer.instance)
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
    
    
    def destroy(self, request, *args, **kwargs):
        data =  super().destroy(request, *args, **kwargs)
        body = {
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
        serializer = GroupPolicySerializer(data=request.data.get('data'))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data =  GroupPolicySerializer(serializer.instance)
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
        
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = GroupPolicySerializer(instance, data=request.data.get('data'), partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data =  GroupPolicySerializer(serializer.instance)
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
    
    def destroy(self, request, *args, **kwargs):
        data =  super().destroy(request, *args, **kwargs)
        body = {
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
        serializer = DomainUserCreateSerializer(data=request.data.get('data'))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data =  DomainUserSerializer(serializer.instance)
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
        
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = DomainUserUpdateSerializer(instance, data=request.data.get('data'), partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data =  DomainUserSerializer(serializer.instance)
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
    
    def destroy(self, request, *args, **kwargs):
        data =  super().destroy(request, *args, **kwargs)
        body = {
            'success': True
        }
        return Response(data=body, status=200)
    
    def policy(self, request, *args, **kwargs):
        def retrieve_policies(obj, policies):
            policies.extend(obj.group_policies.all())
            if obj.parent is not None:
                return retrieve_policies(obj.parent, policies)
            return policies
        user = DomainUser.objects.get(id=kwargs.get('pk'))
        result = retrieve_policies(user.orgunit, [])
        serializer = GroupPolicySerializer(result, many=True)
        body = {
            'data': serializer.data,
            'success': True
        }
        return Response(body, status=200)
    

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
        serializer = HostCreateUpdateSerializer(data=request.data.get('data'))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data =  HostSerializer(serializer.instance)
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
        
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = HostCreateUpdateSerializer(instance, data=request.data.get('data'), partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data =  HostSerializer(serializer.instance)
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
    
    def destroy(self, request, *args, **kwargs):
        data =  super().destroy(request, *args, **kwargs)
        body = {
            'success': True
        }
        return Response(data=body, status=200)
    
    def policy(self, request, *args, **kwargs):
        def retrieve_policies(obj, policies):
            policies.extend(obj.group_policies.all())
            if obj.parent is not None:
                return retrieve_policies(obj.parent, policies)
            return policies
        host = Host.objects.get(id=kwargs.get('pk'))
        result = retrieve_policies(host.orgunit, [])
        serializer = GroupPolicySerializer(result, many=True)
        body = {
            'data': serializer.data,
            'success': True
        }
        return Response(body, status=200)
    

class ParamsSchemaViewSet(viewsets.ModelViewSet):
    queryset = ParamsSchema.objects.all()
    serializer_class = ParamsSchemaSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, ]
    filterset_fields = ['type',]
    lookup_field = 'type'
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
        instance = self.get_object()
        serializer = ParamsSchemaSerializer(instance, data=request.data.get('data'), partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data =  ParamsSchemaSerializer(serializer.instance)
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
    
    

class PageNumberPaginationDataOnly(PageNumberPagination):

    def get_paginated_response(self, data):
        return Response(data)
    
    
class HistoryParamsSchemaViewSet(viewsets.ModelViewSet):
    serializer_class = HistoryParamsSchemaSerializer
    
    
    def get_queryset(self):
        type = self.kwargs.get('type', None)
        queryset =  HistoryParamsSchema.objects.filter(type=type)
        if len(queryset) > 0:
            return queryset
        raise Exception
    
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
        data = self.get_object()
        instance = ParamsSchema.objects.get(type=kwargs.get('type'))
        serializer = ParamsSchemaSerializer(
            data={'body': data.body},
            instance=instance,
            )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        body = {
            'data': serializer.data,
            'success': True,
        }
        return Response(body, status=200)



class HistoryGroupPolicyViewSet(viewsets.ModelViewSet):
    serializer_class = HistoryGroupPolicySerializer
    lookup_kwarg = 'pk'
    
    def get_queryset(self):
        id = self.kwargs.get('history_of', None)
        queryset =  HistoryGroupPolicy.objects.filter(history_of=id)
        if len(queryset) > 0:
            return queryset
        raise Exception
    
    
    def list(self, request, *args, **kwargs):
        data = super().list(request, *args, **kwargs)
        body = {
            'data': data.data,
            'success': True
        }
        return Response(body, status=200)
    
    def retrieve(self, request, *args, **kwargs):
        data = super().retrieve(request, *args, **kwargs)
        body = {
            'data': data.data,
            'success': True
        }
        return Response(data=body, status=200)
    
        
    def update(self, request, *args, **kwargs):
        data =  HistoryGroupPolicy.objects.get(id=kwargs.get('pk'), history_of=kwargs.get('history_of'))
        instance = GroupPolicy.objects.get(id=kwargs.get('history_of'))
        serializer = GroupPolicySerializer(
            data={'body': data.body},
            instance=instance,
            partial=True,
            )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        body = {
            'data': serializer.data,
            'success': True,
        }
        return Response(body, status=200)
