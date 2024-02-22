from rest_framework import serializers
from company.models import Emp, Team

class EmpSerializerTeam(serializers.ModelSerializer):
    
   class Meta:
        model=Emp
        fields="__all__"


class TeamSerializer(serializers.ModelSerializer):
    manager=EmpSerializerTeam()
    class Meta:
        model = Team
        fields = "__all__"

class EmpSerializer(serializers.ModelSerializer):
     team=TeamSerializer()
     class Meta:
        model=Emp
        fields="__all__"
