from django.forms import ModelForm
from meseros.models import Meseros

class MeserosForm(ModelForm):
    class Meta:
        model = Meseros
        fields = ('nombre', 'edad', 'nacionalidad', 'dni')