from rest_framework import viewsets
from django.shortcuts import render
from .models import Division, GroupPolicy, DomenUser, Computers
from .serializers import DivisionSerializer, DomenUserSerializer, ComputerSerializer, GroupPolicySerializer



class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    
class GroupPolicyViewSet(viewsets.ModelViewSet):
    queryset = GroupPolicy.objects.all()
    serializer_class = GroupPolicySerializer


class DomenUserViewSet(viewsets.ModelViewSet):
    queryset = DomenUser.objects.all()
    serializer_class = DomenUserSerializer

class ComputersViewSet(viewsets.ModelViewSet):
    queryset = Computers.objects.all()
    serializer_class = ComputerSerializer