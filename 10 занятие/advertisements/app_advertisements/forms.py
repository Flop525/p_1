from django import forms
from django.forms import ModelForm
from .models import Advertisement
from django.core.exceptions import ValidationError
class AdvertisementForm(ModelForm):
    def clean_title(self):
        data = self.cleaned_data['title']
        if "?" in data[::1]:
            raise ValidationError("Заголовок не может начинаться с вопросительного знака!")
        return data
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'image', 'price','auction']
        widgets={
            'title': forms.TextInput(attrs={"class":"form-control form-control-lg"}),
            'description': forms.TextInput(attrs={"class":"form-control form-control-lg"}),
            'image': forms.FileInput(attrs={"class":"form-control form-control-lg"}),
            'price': forms.NumberInput(attrs={"class":"form-control form-control-lg"}),
            'auction': forms.CheckboxInput(attrs={"class":"form-check-input"}),
        }
