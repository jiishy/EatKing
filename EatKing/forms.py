from django import forms
from .models import *

class New_shopForm(forms.ModelForm):
    class Meta:
        model = New_shop
        fields = ('lcoation', 'tel', 'time', 'name', 'price', 'area_id', 'type_id', 'rate')
