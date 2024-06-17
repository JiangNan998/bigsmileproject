from rest_framework import serializers
from bigsmile.models import Classes,Productinfo

class Classes_data(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Classes
        fields = '__all__'

class Productinfo_data(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Productinfo
        fields = '__all__'