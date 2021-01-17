import re

from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Profile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True,
                                     label='Password', style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], password=validated_data['password'])
        profile = user.profile
        profile.user = user
        user.set_password(validated_data['password'])
        return user

    def validate_email(self, value):
        email = value.strip().lower()
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User with given email already exists')
        return email

    def validate_password(self, value):
        if not re.match(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}', value):
            raise serializers.ValidationError(
                "Your password must be at least 8 characters, "
                "and must include at least one upper case letter, "
                "one lower case letter, and one numeric digit."
            )
        return value


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', required=False)
    update_profile = serializers.HyperlinkedIdentityField(view_name='profile-update')
    gender_display = serializers.CharField(source='get_gender_display', read_only=True)

    def update(self, instance, validated_data):
        instance.gender = validated_data.get('gender', instance.gender)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.save(update_fields=['full_name', 'gender', 'date_of_birth'])
        return instance

    class Meta:
        model = Profile
        fields = ('id',  'update_profile', 'full_name', 'gender', 'gender_display',  'date_of_birth', 'email')


class VerifyEmailSerializer(serializers.Serializer):
    key = serializers.CharField()


class ProfilesListSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email', read_only=True)
    gender_display = serializers.CharField(source='get_gender_display', read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'email', 'full_name', 'gender', 'gender_display', 'date_of_birth')


