from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Project


# -----------------------------
#   USER REGISTER SERIALIZER
# -----------------------------
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # Validation du mot de passe (minimum 8 caractères)
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Le mot de passe doit contenir au moins 8 caractères.")
        return value

    # Hash du mot de passe après validation
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


# -----------------------------
#   USER DETAIL SERIALIZER
# -----------------------------
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


# -----------------------------
#   PROJECT SERIALIZER
# -----------------------------
class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'created_at', 'owner']
