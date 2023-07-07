from django import forms


class DateForm(forms.Form):
    analyze_day = forms.DateField(label='Дата')
