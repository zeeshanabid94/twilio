from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse

class UserInputForm(forms.Form):
    name = forms.CharField(max_length = 256, required=True)
    number = forms.CharField(max_length=16, required=True)
    time = forms.CharField(max_length=2, required=True)
