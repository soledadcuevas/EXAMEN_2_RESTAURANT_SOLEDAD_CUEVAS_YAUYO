from django.shortcuts import render
from django.db.models import F, Q
from django.shortcuts import redirect
from django.urls import  reverse_lazy
from django.core import serializers as ssr
from django.http import HttpResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from meseros.models import Meseros
from meseros.forms import MeserosForm
from meseros.serializers import MeserosSerializer
# Create your views here.
class ExampleView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        content = {
            'status': 'La solicitud no está permitida'
        }
        return Response(content)
def meseros_list(request):

    data_context = {
        'nombre': "Sara",
        'edad': 48,
        'nacionalidad': 'Perú',
        'dni': '25375462',
    }

    return render(request, 'meseros_list.html', context={'data': data_context})

def meseros_orm(request):
    # meseros = Meseros(nombre="Miguel", edad=56, dni=63487522)
    # meseros.save()

    data_context = Meseros.objects.all()
    #print(data_context)

    #data_context = Meseros.objects.get(dni="00000000")
    'para ordenar'
    #data_context = Meseros.objects.order_by('edad')
    'para encadenar concatenando busquedas'
    #data_context = Meseros.objects.filter(nacionalidad='peruano').order_by('edad')
    'acortar datos'
    #data_context = Meseros.objects.all()[0:3]
    'elimnando un dato'

    #data_context = Meseros.objects.get(nombre='Juana')
    #data_context.delete()

    'actulizar datos'
    #Meseros.objects.filter(edad=56).update(nacionalidad="boliviano")
    'usar F expressions'
    #Meseros.objects.filter(edad=26).update(edad=F('edad') + 5)

    "consultas complejas"
    #query = Q(nacionalidad__startswith='arg') | ~Q(edad=31)
    #data_context = Meseros.objects.filter(query)

    return render(request, 'meseros_orm.html', context={'data': data_context})
def meseros_search(request):
    query = request.GET.get('q', '')
    print("QUERY: {}".format(query))

    data_context = []

    return render(request, 'meseros_search.html', context={'data': data_context, 'query': query})

def meseros_details(request):

    data_context = Meseros.objects.all()

    return render(request, 'meseros_details.html', context={'data': data_context})

def meseros_delete(request, id_meseros):

    meseros = Meseros.objects.get(id=id_meseros)
    meseros.delete()

    return redirect('meseros_details')

def meseros_edit(request, id_meseros):
    print("ID de meseros: {}".format(id_meseros))

    meseros = Meseros.objects.get(id=id_meseros)
    print("Datos de meseros a editar: {}".format(meseros))
    form = MeserosForm(initial={'nombre': meseros.nombre, 'edad': meseros.edad, 'nacionalidad': meseros.nacionalidad, 'dni': meseros.dni})

    if request.method == 'POST':
        form = MeserosForm(request.POST, instance=meseros)
        if form.is_valid():
            form.save()
            return redirect('meseros_details')

    return render(request, 'meseros_update.html', context={'data': form})
def meseros_create(request):
    form = MeserosForm(request.POST)
    if form.is_valid():
         nombre = form.cleaned_data['nombre']
         edad = form.cleaned_data['edad']
         nacionalidad = form.cleaned_data['nacionalidad']
         dni = form.cleaned_data['dni']
         form.save()
         return redirect('meseros_details')
    else:
        form = MeserosForm()
    return render(request, 'meseros_create.html', context={'data': form})


class MeserosCreate(CreateView):
    model = Meseros
    form_class = MeserosForm
    template_name = 'meseros_create.html'
    #success_url = reverse_lazy('meseros_list_vc')

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def meseros_api_view(request):
    if request.method == 'POST':
        print("Data MESEROS: {}".format(request.data))
        serializers_class = MeserosSerializer(data=request.data)
        if serializers_class.is_valid():
            serializers_class.save()
            return Response(serializers_class.data, status=status.HTTP_201_CREATED)
        return Response(serializers_class.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        print('Ingresó a Get')
        queryset = Meseros.objects.all()
        serializers_class = MeserosSerializer(queryset, many=True)

        return Response(serializers_class.data, status=status.HTTP_200_OK)


