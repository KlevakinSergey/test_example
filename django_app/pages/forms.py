from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Ваше имя', 'class': 'form-control', 'id': 'exampleFormControlInput'}))
    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Телефон', 'class': 'form-control', 'id': 'exampleFormControlInput'}))

    class Meta:
        model = Application
        fields = ('name', 'phone_number', 'text')
