from django import forms
from .models import *


class AddBreedForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    is_published = forms.BooleanField(required=False, initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Not selected',
                                      widget=forms.Select(attrs={'class': 'form-select p-1'}))
