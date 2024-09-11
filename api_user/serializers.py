from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserInfo



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','password','username','email']

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'

