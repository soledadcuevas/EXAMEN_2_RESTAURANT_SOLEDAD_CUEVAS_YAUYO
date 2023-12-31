from django.shortcuts import render
from django.db.models import F, Q
from django.shortcuts import redirect
from django.urls import  reverse_lazy
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from clientes.models import Clientes
from clientes.forms import ClientesForm
from clientes.serializers import ClientesSerializer
# Create your views here.
def clientes_list(request):

    data_context = [
        {
            'nombre': 'Ernesta',
            'apellido': 'Gomez',
            'dni': "648809021",
        },
        {
            'nombre': 'Juan',
            'apellido': 'Perez',
            'dni': "648809444",
        }
    ]


    return render(request, 'clientes_list.html', context={'data': data_context})

def clientes_orm(request):


    #clientes = Clientes(nombre="Arnold", apellido= 'Benites', dni=63487511)
    #clientes.save()

    data_context = Clientes.objects.all()
    #print(data_context)
    "filtros"

    #data_context = Clientes.objects.filter(procedencia='Perú', edad__gt='30')

    return render(request, 'clientes_orm.html', context={'data': data_context})

def clientes_search(request):
    query = request.GET.get('q', '')
    print("QUERY: {}".format(query))

    data_context = []

    return render(request, 'clientes_search.html', context={'data': data_context, 'query':query})
def clientes_details(request):
    data_context = Clientes.objects.all()

    return render(request, 'clientes_details.html', context={'data': data_context})
def clientes_delete(request, id_clientes):

    clientes = Clientes.objects.get(id=id_clientes)
    clientes.delete()

    return redirect('clientes_details')
def clientes_edit(request, id_clientes):
    print("ID de clientes: {}".format(id_clientes))

    clientes = Clientes.objects.get(id=id_clientes)
    print("Datos de clientes a editar: {}".format(clientes))
    form = ClientesForm(initial={'nombre': clientes.nombre, 'edad': clientes.edad,'apellido': clientes.apellido ,'dni': clientes.dni,'procedencia': clientes.procedencia})

    if request.method == 'POST':
        form = ClientesForm(request.POST, instance=clientes)
        if form.is_valid():
            form.save()
            return redirect('clientes_details')
    return render(request, 'clientes_update.html', context={'data': form})

def clientes_create(request):
    form = ClientesForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('clientes_details')
    else:
        form = ClientesForm()
    return render(request, 'clientes_create.html', context={'data': form})

class ClientesCreate(CreateView):
    model = Clientes
    form_class = ClientesForm
    template_name = 'clientes_create.html'
    #success_url = reverse_lazy('clientes_list_vc')

@api_view(['POST', 'GET'])
def clientes_api_view(request):

    if request.method == 'POST':
        print("Data CLIENTES: {}".format(request.data))
        serializers_class = ClientesSerializer(data=request.data)
        if serializers_class.is_valid():
            serializers_class.save()
            return Response(serializers_class.data, status=status.HTTP_201_CREATED)
        return Response(serializers_class.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        print('Ingreso a Get')
        queryset = Clientes.objects.all()
        serializers_class = ClientesSerializer(queryset, many=True)

        return Response(serializers_class.data, status=status.HTTP_200_OK)
@api_view(['GET', 'PUT', 'DELETE'])
def clientes_details_view(request, pk):
    clientes = Clientes.objects.filter(edad__gte=40)
    return Response(serializers_class.data)



