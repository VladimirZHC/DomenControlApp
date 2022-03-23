from __future__ import division
from asyncore import read
from rest_framework import serializers
from .models import Division, GroupPolicy, DomenUser, Computers, SchemaParams
import json


class BodyField(serializers.JSONField):
    
    
    def to_representation(self, value):
        return json.loads(value)
        
    
    def to_internal_value(self, data):
        try:
            json.loads(data)
        except (TypeError, ValueError):
            self.fail('invalid_json')
        return data


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
        fields = ('name', 'departament', 'group_policy',)
        
        

class DomenUserSerializer(serializers.ModelSerializer):
    division = serializers.SlugRelatedField(slug_field='name',  queryset=Division.objects.all())
    class Meta:
        model = DomenUser
        fields = ('name', 'division',)
        
class ComputerSerializer(serializers.ModelSerializer):
    division = serializers.SlugRelatedField(slug_field='name',  queryset=Division.objects.all())
    class Meta:
        model = Computers
        fields = ('name', 'division',)
        
        
        
        
class SchemaParamsSerializer(serializers.ModelSerializer):
    body = BodyField()
    
    class Meta:
        model = SchemaParams
        fields = ('type', 'body', )