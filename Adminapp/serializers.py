from rest_framework import serializers
from django.contrib.auth import authenticate
from dj_rest_auth.serializers import LoginSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from .models import User, Xodimlar
from dj_rest_auth.serializers import LoginSerializer


# =========================
# REGISTER SERIALIZER
# =========================
class CustomRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'role')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data.get('email'),
            role=validated_data.get('role')
        )
        user.set_password(validated_data['password1'])
        user.save()
        setup_user_email(self.context['request'], user, [])
        return user


# =========================
# LOGIN SERIALIZER (MUHIM)
# =========================
class CustomLoginSerializer(LoginSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )

        if not user:
            raise serializers.ValidationError({
                "detail": "Username yoki parol noto‘g‘ri"
            })

        attrs['user'] = user
        return attrs


# =========================
# XODIMLAR SERIALIZER
# =========================
class XodimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xodimlar
        fields = '__all__'


# =========================
# TATIL UPDATE SERIALIZER
# =========================
class TatilUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xodimlar
<<<<<<< HEAD
        fields = ['tatil_holati', 'tatil_boshlanish_sana', 'tatil_tugash_sana']

class CustomLoginSerializer(LoginSerializer):
    pass
=======
        fields = [
            'tatil_holati',
            'tatil_boshlanish_sana',
            'tatil_tugash_sana'
        ]
>>>>>>> fd59482c8aa9883a99f5de8060b7b1a170901ce0
