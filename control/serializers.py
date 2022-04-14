from django.forms import CharField
from rest_framework import serializers
from .models import (
    DomainUser, 
    GroupPolicy,
    HistoryGroupPolicy, 
    HistoryParamsSchema, 
    Host, 
    OrgUnit, 
    ParamsSchema,
    )
import json
import re

class BodyField(serializers.JSONField):
    
    def to_representation(self, value):
        return json.loads(value)
        
    
    def to_internal_value(self, data):
        try:
            json.loads(data)
        except (TypeError, ValueError):
            self.fail('invalid')
        return data
    

     
class GroupPolicySerializer(serializers.ModelSerializer):
   
    body = serializers.CharField(required=False)
    
    class Meta:
        model = GroupPolicy
        fields = ('id', 'name', 'body',)
        

        
        
class OrgUnitSerializer(serializers.ModelSerializer):
    parent = serializers.SlugRelatedField(slug_field='name', queryset=OrgUnit.objects.all(), required=False)
    group_policies = serializers.SlugRelatedField(many=True, slug_field='name', queryset=GroupPolicy.objects.all(), required=False)
    class Meta:
        model = OrgUnit
        fields = ('id', 'name', 'parent', 'group_policies',)
        
class OrgUnitCreatedUpdateSerializer(serializers.ModelSerializer):
    parent = serializers.SlugRelatedField(slug_field='id', queryset=OrgUnit.objects.all(), required=False)
    group_policies = serializers.SlugRelatedField(many=True, slug_field='id', queryset=GroupPolicy.objects.all(), required=False)
    class Meta:
        model = OrgUnit
        fields = ('id', 'name', 'parent', 'group_policies',)
        
        


class DomainUserSerializer(serializers.ModelSerializer):
    orgunit = serializers.SlugRelatedField(slug_field='name',  queryset=OrgUnit.objects.all(), required=False)
    
    class Meta:
        model = DomainUser
        fields = ('id','name', 'login', 'orgunit',)
        
class DomainUserCreateSerializer(serializers.ModelSerializer):
    orgunit = serializers.SlugRelatedField(slug_field='id',  queryset=OrgUnit.objects.all(), required=False)
    login = serializers.CharField(required=True)
    
    def validate_login(self, login):
        if re.search('[а-яА-Я]', login):
            raise serializers.ValidationError('Login must contain only latin latters')
        return login
    
    class Meta:
        model = DomainUser
        fields = ('id','name', 'login','orgunit',)
        
class DomainUserUpdateSerializer(serializers.ModelSerializer):
    orgunit = serializers.SlugRelatedField(slug_field='id',  queryset=OrgUnit.objects.all(), required=False)
    
    class Meta:
        model = DomainUser
        fields = ('id','name','orgunit')

        
        
class HostSerializer(serializers.ModelSerializer):
    orgunit = serializers.SlugRelatedField(slug_field='name',  queryset=OrgUnit.objects.all(), required=False)
    class Meta:
        model = Host
        fields = ('id','name', 'orgunit',)
        
class HostCreateUpdateSerializer(serializers.ModelSerializer):
    orgunit = serializers.SlugRelatedField(slug_field='id',  queryset=OrgUnit.objects.all(), required=False)
    class Meta:
        model = Host
        fields = ('id','name', 'orgunit',)
        

        
class ParamsSchemaSerializer(serializers.ModelSerializer):
    body = CharField(required=False)
    
    class Meta:
        model = ParamsSchema
        fields = ('type', 'body', )
        

    
class HistoryParamsSchemaSerializer(serializers.ModelSerializer):
    updated = serializers.DateTimeField(format='%H:%M:%S %d/%m/%Y')
    
    class Meta:
        model = HistoryParamsSchema
        fields = ('id', 'type', 'body', 'updated')
        

class HistoryGroupPolicySerializer(serializers.ModelSerializer):
    history_of = GroupPolicySerializer()
    updated = serializers.DateTimeField(format='%H:%M:%S %d/%m/%Y')
    
    class Meta:
        model = HistoryGroupPolicy
        fields = ('id', 'name', 'body', 'updated', 'history_of')