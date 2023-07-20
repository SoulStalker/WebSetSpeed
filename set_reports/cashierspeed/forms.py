from django import forms


class DateForm(forms.Form):
    analyze_day = forms.DateField(label='Дата')
    filter_shop = forms.BooleanField(required=False, label='Фильтр по магазину')
    shop_num = forms.IntegerField(required=False, label='Номер магазина')
