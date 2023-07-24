from django import forms
from django.forms import widgets
from datetime import date

class DateForm(forms.Form):
    today = date.today()
    analyze_day_start = forms.DateField(
        label='Дата начала',
        widget=forms.DateInput(attrs={'type': 'date', 'style': 'width: 200px;', 'max': '2030-12-31', 'autocomplete': 'off'}),
        initial=today
    )
    analyze_day_end = forms.DateField(
        label='Дата окончания',
        widget=forms.DateInput(attrs={'type': 'date', 'style': 'width: 200px;', 'max': '2030-12-31', 'autocomplete': 'off'}),
        initial=today
    )
    filter_shop = forms.BooleanField(
        required=False,
        label='Фильтр по магазину',
        widget=forms.CheckboxInput(attrs={'id': 'id_filter_shop'})
    )
    shop_num = forms.IntegerField(
        required=False,
        label='Номер магазина',
        widget=forms.NumberInput(attrs={'id': 'id_shop_num'})
    )
