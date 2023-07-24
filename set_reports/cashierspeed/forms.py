from django import forms
from django.forms import widgets


class DateForm(forms.Form):
    analyze_day_start = forms.DateField(label='Дата начала', widget=widgets.DateInput(attrs={'type': 'date', 'style': 'width: 200px;'}))
    analyze_day_end = forms.DateField(label='Дата окончания', widget=widgets.DateInput(attrs={'type': 'date', 'style': 'width: 200px;'}))
    filter_shop = forms.BooleanField(required=False, label='Фильтр по магазину')
    shop_num = forms.IntegerField(required=False, label='Номер магазина')
