from django.shortcuts import render

# Create your views here.
def platos_list(request):
    return render(request, 'platos_list.html', context=None)
