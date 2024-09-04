from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['user_id', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user
