from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddBreedForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Not selected'

    class Meta:
        model = Breeds
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'category']
        widgets = {
            'content': forms.Textarea(
                attrs={'cols': 60, 'rows': 10}),
            'category': forms.Select(attrs={'class': 'form-select p-1'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Length of title cannot be higher than 200 symbols.')
        return title
