from django.shortcuts import render

# Create your views here.
def meseros_list(request):

    return render(request, 'meseros_list.html', context=None)