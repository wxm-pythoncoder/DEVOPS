from django.shortcuts import render
import paramiko
from .models import System,Performance
# Create your views here.


def find_machine(request):
    system_obj = System.objects.all()
    for system in system_obj:
        print(system.type)
        print(system.system)
    return render(request,'index.html',{"system_obj":system_obj})