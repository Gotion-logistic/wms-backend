from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Pack, Location

# --- Model Serializers ---

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['location_code', 'zone']

class PackSerializer(serializers.ModelSerializer):
    location_code = serializers.CharField(source='location.location_code', read_only=True)

    class Meta:
        model = Pack
        fields = [
            'serial_number',
            'part_number',
            'status',
            'location',
            'location_code',
            'created_at'
        ]
        read_only_fields = ('serial_number', 'created_at')

# --- Authentication Serializers ---

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user