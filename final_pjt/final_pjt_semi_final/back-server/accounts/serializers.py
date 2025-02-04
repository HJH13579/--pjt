from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password', )
        extra_kwargs = {'password': {'write_only': True}}

class UserDetailSerializer(serializers.ModelSerializer):

    class Meta : 
        model = User
        fields = ('username','id')