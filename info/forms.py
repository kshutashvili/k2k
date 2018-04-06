#!/usr/bin/python
# -*- coding: utf-8 -*-
from .models import Question
from django import forms


class QuestionForm(forms.ModelForm):
    question = forms.CharField()
    
    class Meta:
        model = Question
        fields = ['theme', 'email', 'name', 'question']

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['theme'].widget.attrs = {'class': 'form__item select'}



