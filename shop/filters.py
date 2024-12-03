import django_filters
from django import forms
from shop.models import Product

MIN_PRICE = 1
MAX_PRICE = 100


class SearchFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Название блюда',
                                     field_name='name',
                                     lookup_expr='icontains',
                                     required=False,
                                     widget=forms.TextInput(attrs={'class': 'filter'}))

    min_price = django_filters.NumberFilter(label='Минимальная цена',
                                            field_name='price',
                                            lookup_expr='gte',
                                            required=False,
                                            widget=forms.NumberInput(attrs={'class': 'filter'}))

    max_price = django_filters.NumberFilter(label='Максимальная цена',
                                            field_name='price',
                                            lookup_expr='lte',
                                            required=False,
                                            widget=forms.NumberInput(attrs={'class': 'filter'}))

    class Meta:
        model = Product
        fields = ['name', 'min_price', 'max_price']

    def clean_min_price(self):
        value = self.form.cleaned_data.get('min_price')
        if value is not None and value < MIN_PRICE:
            value = MIN_PRICE
        return value

    def clean_max_price(self):
        value = self.form.cleaned_data.get('max_price')
        if value is not None and value > MAX_PRICE:
            value = MAX_PRICE
        return value
