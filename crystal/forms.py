from django import forms


class CrystalForm(forms.Form):
    space_group = forms.CharField(label='space_group', max_length=100)
    a = forms.DecimalField(max_value=500, min_value=0)
    b = forms.DecimalField(max_value=500, min_value=0)
    c = forms.DecimalField(max_value=500, min_value=0)
    alpha = forms.DecimalField(max_value=180, min_value=0)
    beta = forms.DecimalField(max_value=180, min_value=0)
    gamma = forms.DecimalField(max_value=180, min_value=0)
    low_res = forms.DecimalField(min_value=0)
    high_res = forms.DecimalField(min_value=0)
