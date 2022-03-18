
from rest_framework import serializers
from .models import Division, GroupPolicy, DomenUser, Computers, SchemaParams
import json


class BodyField(serializers.JSONField):
    def to_representation(self, value):
        return json.loads(value)


class GroupPolicySerializer(serializers.ModelSerializer):
   
    body = BodyField()
    
    class Meta:
        model = GroupPolicy
        fields = ('name', 'body',)
        
        
class DivisionSerializer(serializers.ModelSerializer):
    departament = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Division.objects.all())
    group_policy = serializers.SlugRelatedField(many=True, slug_field='name', queryset=GroupPolicy.objects.all())
    class Meta:
        model = Division
        fields = ('name', 'departament', 'group_policy', 'types' )
        
        

class DomenUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DomenUser
        fields = ('name', 'divisions',)
        
class ComputerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Computers
        fields = ('name', 'divisions',)
        
class SchemaParamsSerializer(serializers.ModelSerializer):
    body = BodyField()
        
    class Meta:
        model = SchemaParams
        fields = ('type', 'body', )