from rest_framework import serializers
from .models import Xodimlar, User


class XodimlarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Xodimlar
        fields = '__all__'
        read_only_fields = ['id', 'yaratilgan_vaqt']
class XodimlarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xodimlar
        fields = [
            'id',
            'ism',
            'familiya',
            'telefon'
        ]
