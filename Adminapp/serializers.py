from rest_framework import serializers
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from .models import User, Xodimlar

class CustomRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'role')

    def validate_password1(self, value):
        # passwordni tekshirish, allauthdan foydalansa ham bo'ladi
        return value

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password1'])
        user.save()
        setup_user_email(self.context['request'], user, [])
        return user

class XodimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xodimlar
        fields = '__all__'


class TatilUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xodimlar
        fields = ['tatil_holati', 'tatil_boshlanish_sana', 'tatil_tugash_sana']
