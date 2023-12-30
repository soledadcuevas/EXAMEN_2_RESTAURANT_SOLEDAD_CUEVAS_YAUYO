from django.shortcuts import render

# Create your views here.
def clientes_list(request):

    data_context = {
        'nombre': 'Ernesta',
        'apellido': 'Gomez',
        'dni': "648809021",

    }
    return render(request, 'clientes_list.html', context={'data': data_context})

