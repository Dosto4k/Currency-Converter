from django import forms
from .services import get_currency_codes


class ConvForm(forms.Form):
    from_ = forms.ChoiceField(choices=[(i, i) for i in get_currency_codes()])
    to = forms.ChoiceField(choices=[(i, i) for i in get_currency_codes()])
    sum_ = forms.IntegerField(min_value=1)
