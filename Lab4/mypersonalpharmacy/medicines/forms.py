from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *


class FeedBackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].empty_label = 'Имя не введено'
        self.fields['last_name'].empty_label = 'Фамилия не введена'
        self.fields['rating'].empty_label = 'Вы не поставили оценку'
        self.fields['feedback'].empty_label = 'Вы не оставили отзыв'

    def clean_feedback(self):
        feedback = self.cleaned_data['feedback']

        if len(feedback) <= 0:
            raise ValidationError('Отзыв не был введен')

        return feedback

    def clean_name(self):
        name = self.cleaned_data['name']

        if len(name) <= 0:
            raise ValidationError('Имя не введено')

        return name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']

        if len(last_name) <= 0:
            raise ValidationError('Фамилия не введена')

        return last_name

    class Meta:
        model = FeedBack
        fields = ['name',
                  'last_name',
                  'rating',
                  'feedback']



