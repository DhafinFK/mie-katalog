from django.forms import ModelForm
from .models import Indomie


class IndomieForm(ModelForm):
    class Meta:
        model = Indomie
        fields = ['name', 'amount', 'description', 'price', 'type']
