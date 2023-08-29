from front.models import FeaturesModel
from django import forms

class FeaturesForm(forms.ModelForm):
    class Meta:
        model = FeaturesModel
        fields = ['age', 'x', 'y', 'k']