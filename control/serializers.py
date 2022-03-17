from rest_framework import serializers
from .models import Division, GroupPolicy, DomenUser, Computers


class GroupPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupPolicy
        fields = '__all__'
        
class DivisionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Division
        fields = '__all__'

class DomenUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DomenUser
        fields = '__all__'
        
class ComputerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Computers
        fields = '__all__'