from django import forms


class CoopForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    position = forms.CharField(required=True)
    text = forms.CharField(required=True)
    file = forms.FileField(required=False)