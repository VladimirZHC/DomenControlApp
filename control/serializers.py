
from rest_framework import serializers
from .models import Division, GroupPolicy, DomenUser, Computers, SchemaParams



class GroupPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupPolicy
        fields = ('name', 'body',)
        
        
class DivisionSerializer(serializers.ModelSerializer):
    departament = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Division.objects.all())
    policy = GroupPolicySerializer(source='group_policy', many=True)
    class Meta:
        model = Division
        fields = ('name', 'departament', 'policy', 'types' )
        
        

class DomenUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DomenUser
        fields = ('name', 'divisions',)
        
class ComputerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Computers
        fields = ('name', 'divisions',)
        
class SchemaParamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchemaParams
        fields = '__all__'