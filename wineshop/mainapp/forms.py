from django import forms
from mainapp.models import wine_shop


class mywine_form(forms.ModelForm):
    brand_name=forms.CharField()
    brand_dis=forms.CharField()
    brand_rate=forms.IntegerField()
    brand_type=forms.CharField()
    class Meta:
        model=wine_shop
        fields='__all__'

    