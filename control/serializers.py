from rest_framework import serializers
from .models import DomainUser, GroupPolicy, Host, OrgUnit, ParamsSchema
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
        fields = ('id', 'name', 'body',)
        
        
class OrgUnitSerializer(serializers.ModelSerializer):
    parent = serializers.SlugRelatedField(slug_field='name', queryset=OrgUnit.objects.all())
    group_policies = serializers.SlugRelatedField(many=True, slug_field='name', queryset=GroupPolicy.objects.all())
    class Meta:
        model = OrgUnit
        fields = ('id', 'name', 'parent', 'group_policies',)
        
        

class DomainUserSerializer(serializers.ModelSerializer):
    orgunit = serializers.SlugRelatedField(slug_field='name',  queryset=OrgUnit.objects.all())
    class Meta:
        model = DomainUser
        fields = ('id','name', 'orgunit',)
        
class HostSerializer(serializers.ModelSerializer):
    orgunit = serializers.SlugRelatedField(slug_field='name',  queryset=OrgUnit.objects.all())
    class Meta:
        model = Host
        fields = ('id','name', 'orgunit',)
        
        
        
        
class ParamsSchemaSerializer(serializers.ModelSerializer):
    body = BodyField()
    
    class Meta:
        model = ParamsSchema
        fields = ('type', 'body', )