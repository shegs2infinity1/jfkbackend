# users/serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import UserProfile, Biodata, Order, CustomizationOption,Measurement
from django.contrib.auth.hashers import make_password
# from .models import UserValidation
from rest_framework import serializers


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role
        user_id = user.id
        return token


class BiodataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biodata
        fields = ['id', 'user', 'name', 'age', 'gender', 'role']


class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = UserProfile
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(password=validated_data['password'])
        user = UserProfile.objects.create(

            username=validated_data['username'],
            password=validated_data['password'],
            role=validated_data['role'],
            firstname=validated_data['firstname'],
            lastname=validated_data['lastname'],
            phonenumber=validated_data['phonenumber'],
            email=validated_data['email'],
            gender=validated_data['gender'],
            birthdate=validated_data['birthdate'],
        )
        return user

class CustomizationOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomizationOption
        fields = ['id','name','description']


class OrderSerializer(serializers.ModelSerializer):
    customization_options = CustomizationOptionSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = '__all__'

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'
