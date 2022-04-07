from rest_framework import viewsets
from .models import OrgUnit, GroupPolicy, Host, DomainUser, ParamsSchema
from .serializers import (
    GroupPolicySerializer, 
    DomainUserSerializer, 
    OrgUnitSerializer, 
    ParamsSchemaSerializer, 
    HostSerializer,
    OrgUnitCreatedUpdateSerializer,
    DomainUserCreateUpdateSerializer,
    HostCreateUpdateSerializer,
                        )
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view


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
        serializer = DomainUserCreateUpdateSerializer(data=request.data.get('data'))
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
        serializer = DomainUserCreateUpdateSerializer(instance, data=request.data.get('data'), partial=True)
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
    

@api_view(('GET',))
def getgrouppolicyhistory(request):
    body = {
  "data": [
    {
      "id": 1,
      "name": "Энергосбережение",
      "body": "{\"user\":{\"hardware\":{\"power_mgmt\":{\"notifications\":{\"batt_full\":\"Please unplug\"},\"screen_timeout\":180,\"sleep_timeout\":600}}}}",
      "updated": "2022-04-07T14:53:51.139Z",
      "history_of": {
        "id": 1,
        "name": "Энергосбережение",
        "body": "{\"user\":{\"hardware\":{\"power_mgmt\":{\"notifications\":{\"batt_full\":\"Please unplug\"},\"screen_timeout\":180,\"sleep_timeout\":600}}}}"
      }
    }
  ],
  "success": True
}
    return Response(body, status=200)


@api_view(('GET',))
def getgrouppolicyhistoryid(request):
    body = {
  "data": {
    "id": 1,
    "name": "Энергосбережение",
    "body": "{\"user\":{\"hardware\":{\"power_mgmt\":{\"notifications\":{\"batt_full\":\"Please unplug\"},\"screen_timeout\":180,\"sleep_timeout\":600}}}}",
    "updated": "2022-04-07T16:36:36.648Z",
    "history_of": {
      "id": 1,
      "name": "Энергосбережение",
      "body": "{\"user\":{\"hardware\":{\"power_mgmt\":{\"notifications\":{\"batt_full\":\"Please unplug\"},\"screen_timeout\":180,\"sleep_timeout\":600}}}}"
    }
  },
  "success": True
}
    return Response(body, status=200)


@api_view(('POST',))
def getgrouppolicyhistoryrollback(request):
    body = {
  "data": {
    "id": 1,
    "name": "Энергосбережение",
    "body": "{\"user\":{\"hardware\":{\"power_mgmt\":{\"notifications\":{\"batt_full\":\"Please unplug\"},\"screen_timeout\":180,\"sleep_timeout\":600}}}}"
  },
  "success": True
}
    return Response(body, status=200)




@api_view(('GET',))
def getschemahistory(request):
    body = {
  "data": [
    {
      "id": 0,
      "type": "USER",
      "body": "{\"system\":{\"autorun\":{\"apps\":[{\"name\":\"\",\"cmd\":\"\",\"icon\":\"\"}],\"links\":[{\"name\":\"\",\"url\":\"\"}]},\"datetime\":{\"timezone\":\"\",\"time_format\":\"\"},\"env_vars\":{\"settings\":{\"source\":\"\"},\"vars\":[{\"name\":\"\",\"value\":\"\"}]},\"mime_types\":{\"associations\":[{\"app\":\"\",\"types\":\"\"}],\"mailto\":\"\",\"http\":\"\"}},\"desktop\":{\"start_menu\":{\"apps\":[{\"name\":\"\",\"cmd\":\"\",\"icon\":\"\"}],\"links\":[{\"name\":\"\",\"url\":\"\"}],\"folders\":[{\"name\":\"\"}]},\"quicklaunch\":{\"apps\":[{\"name\":\"\",\"cmd\":\"\",\"icon\":\"\"}],\"links\":[{\"name\":\"\",\"url\":\"\"}],\"folders\":[{\"name\":\"\"}]}},\"hardware\":{\"power_mgmt\":{\"notifications\":{\"batt_low\":\"\",\"batt_full\":\"\",\"plugged_in\":\"\",\"unplugged\":\"\"},\"screen_timeout\":600,\"lock_when_screen_off\":true,\"sleep_timeout\":1200,\"script_timeout\":300,\"script_after_timeout\":\"\"}}}",
      "updated": "2022-04-07T16:40:47.376Z"
    }
  ],
  "success": True
}
    return Response(body, status=200)


@api_view(('GET',))
def getschemahistoryid(request):
    body = {
  "data": {
    "id": 0,
    "type": "USER",
    "body": "{\"system\":{\"autorun\":{\"apps\":[{\"name\":\"\",\"cmd\":\"\",\"icon\":\"\"}],\"links\":[{\"name\":\"\",\"url\":\"\"}]},\"datetime\":{\"timezone\":\"\",\"time_format\":\"\"},\"env_vars\":{\"settings\":{\"source\":\"\"},\"vars\":[{\"name\":\"\",\"value\":\"\"}]},\"mime_types\":{\"associations\":[{\"app\":\"\",\"types\":\"\"}],\"mailto\":\"\",\"http\":\"\"}},\"desktop\":{\"start_menu\":{\"apps\":[{\"name\":\"\",\"cmd\":\"\",\"icon\":\"\"}],\"links\":[{\"name\":\"\",\"url\":\"\"}],\"folders\":[{\"name\":\"\"}]},\"quicklaunch\":{\"apps\":[{\"name\":\"\",\"cmd\":\"\",\"icon\":\"\"}],\"links\":[{\"name\":\"\",\"url\":\"\"}],\"folders\":[{\"name\":\"\"}]}},\"hardware\":{\"power_mgmt\":{\"notifications\":{\"batt_low\":\"\",\"batt_full\":\"\",\"plugged_in\":\"\",\"unplugged\":\"\"},\"screen_timeout\":600,\"lock_when_screen_off\":true,\"sleep_timeout\":1200,\"script_timeout\":300,\"script_after_timeout\":\"\"}}}",
    "updated": "2022-04-07T16:48:50.831Z"
  },
  "success": True
}
    return Response(body, status=200)


@api_view(('POST',))
def getschemahistoryidrollback(request):
    body = {
  "data": {
    "type": "USER",
    "body": "{\"system\":{\"autorun\":{\"apps\":[{\"name\":\"\",\"cmd\":\"\",\"icon\":\"\"}],\"links\":[{\"name\":\"\",\"url\":\"\"}]},\"datetime\":{\"timezone\":\"\",\"time_format\":\"\"},\"env_vars\":{\"settings\":{\"source\":\"\"},\"vars\":[{\"name\":\"\",\"value\":\"\"}]},\"mime_types\":{\"associations\":[{\"app\":\"\",\"types\":\"\"}],\"mailto\":\"\",\"http\":\"\"}},\"desktop\":{\"start_menu\":{\"apps\":[{\"name\":\"\",\"cmd\":\"\",\"icon\":\"\"}],\"links\":[{\"name\":\"\",\"url\":\"\"}],\"folders\":[{\"name\":\"\"}]},\"quicklaunch\":{\"apps\":[{\"name\":\"\",\"cmd\":\"\",\"icon\":\"\"}],\"links\":[{\"name\":\"\",\"url\":\"\"}],\"folders\":[{\"name\":\"\"}]}},\"hardware\":{\"power_mgmt\":{\"notifications\":{\"batt_low\":\"\",\"batt_full\":\"\",\"plugged_in\":\"\",\"unplugged\":\"\"},\"screen_timeout\":600,\"lock_when_screen_off\":true,\"sleep_timeout\":1200,\"script_timeout\":300,\"script_after_timeout\":\"\"}}}"
  },
  "success": True
}
    return Response(body, status=200)



    
