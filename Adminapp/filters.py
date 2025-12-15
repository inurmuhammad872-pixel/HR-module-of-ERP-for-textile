# app/filters.py
import django_filters
from .models import Xodimlar, Jins, IshHolati, ShartnomaTuri

class XodimlarFilter(django_filters.FilterSet):
    ism = django_filters.CharFilter(lookup_expr='icontains', label="Ism")
    familiya = django_filters.CharFilter(lookup_expr='icontains', label="Familiya")
    lavozim = django_filters.CharFilter(lookup_expr='icontains')
    bolim = django_filters.CharFilter(lookup_expr='icontains')

    jins = django_filters.ChoiceFilter(choices=Jins.choices)
    ish_holati = django_filters.ChoiceFilter(choices=IshHolati.choices)
    shartnoma_turi = django_filters.ChoiceFilter(choices=ShartnomaTuri.choices)

    oylik_min = django_filters.NumberFilter(field_name="oylik", lookup_expr='gte', label="Oylik min")
    oylik_max = django_filters.NumberFilter(field_name="oylik", lookup_expr='lte', label="Oylik max")

    class Meta:
        model = Xodimlar
        fields = [
            'ism', 'familiya', 'lavozim', 'bolim',
            'jins', 'ish_holati', 'shartnoma_turi'
        ]
