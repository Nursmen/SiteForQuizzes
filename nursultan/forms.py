from django import forms

from .models import Test, Queston
from django import forms
from django.forms import inlineformset_factory

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Queston
        fields = '__all__'

class TestForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = '__all__'

QuestionFormSet = inlineformset_factory(Test, Queston, form=QuestionForm, extra=1, can_delete=True, can_delete_extra=True)