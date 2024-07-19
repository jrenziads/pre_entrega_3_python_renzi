from django import forms
from .models import Car, Brand, Owner

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'country']

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'price']

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'car']
        
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

