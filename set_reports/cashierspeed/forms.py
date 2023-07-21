from django import forms
from django.forms import widgets
from django.forms.widgets import DateInput


class DateForm(forms.Form):
    analyze_day = forms.DateField(label='Дата', widget=widgets.DateInput(attrs={'type': 'date', 'style': 'width: 200px;'}))
    filter_shop = forms.BooleanField(required=False, label='Фильтр по магазину')
    shop_num = forms.IntegerField(required=False, label='Номер магазина')
