from django.shortcuts import render
from machines.models import Machines 
# Create your views here.

def index(request):
    machines = Machines.objects.all()
    context = { 
        'machines':machines
    }
    return render(request, "machines/index.html", context=context)



def machine_01(request):
    return render(request, 'machines/machine-01.html')


 