from django.forms import ModelForm

from .models import Pozos

class PozosForm(ModelForm):
    class Meta:
        model = Pozos
        fields = '__all__'
