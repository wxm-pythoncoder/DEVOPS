from django.shortcuts import render
import paramiko
from .models import System,Performance
# Create your views here.


def find_machine(request):
    performance_obj = Performance.objects.all()
    return render(request,'index.html',{"performance_obj":performance_obj})

def test1(request):
    return render(request,'test.html')

def test2(request):
    return render(request,'test.html')