from rest_framework import viewsets
from .models import OrgUnit, GroupPolicy, Host, DomainUser, ParamsSchema
from .serializers import GroupPolicySerializer, DomainUserSerializer, OrgUnitSerializer, ParamsSchemaSerializer, HostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



class OrgUnitViewSet(viewsets.ModelViewSet):
    queryset = OrgUnit.objects.all()
    serializer_class = OrgUnitSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend, ]
    filterset_fields = ['name', 'group_policies']
    search_fields = ['name' ]
    

    
class GroupPolicyViewSet(viewsets.ModelViewSet):
    queryset = GroupPolicy.objects.all()
    serializer_class = GroupPolicySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend, ]
    filterset_fields = ['name',]
    search_fields = ['name', ]


class DomainUserViewSet(viewsets.ModelViewSet):
    queryset = DomainUser.objects.all()
    serializer_class = DomainUserSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, ]
    filterset_fields = ['name', 'orgunit']
    search_fields = ['name', ]
    

class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, ]
    filterset_fields = ['name', 'orgunit']
    search_fields = ['name', ]
    

class ParamsSchemaViewSet(viewsets.ModelViewSet):
    queryset = ParamsSchema.objects.all()
    serializer_class = ParamsSchemaSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, ]
    filterset_fields = ['type',]