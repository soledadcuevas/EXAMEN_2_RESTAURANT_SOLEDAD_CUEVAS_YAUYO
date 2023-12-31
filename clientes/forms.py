from django.forms import ModelForm
from clientes.models import Clientes


class ClientesForm(ModelForm):
    class Meta:
        model = Clientes
        fields = ('nombre', 'edad', 'apellido', 'dni', 'procedencia')