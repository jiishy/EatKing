from django import forms
from .models import *

class New_shopForm(forms.ModelForm):
    class Meta:
        model = New_shop
        fields = ('lcoation', 'tel', 'time', 'name', 'price', 'area_id', 'type_id', 'rate')

class Accuse_shopForm(forms.ModelForm):
    class Meta:
        model = Accuse_shop
        fields = ('content', )

class comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('taste_score', 'env_score', 'serv_score', 'content')

