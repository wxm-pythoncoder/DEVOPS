from django.shortcuts import render
from .models import *
# Create your views here.


def find_machine(request):
    performance_obj = Performance.objects.all()
    return render(request, 'assets.html', {"performance_obj":performance_obj})

def detail(request):
    asset = Asset.objects.all()
    return render(request,'detail.html',{"asset":asset})

def index(request):
    assets = Asset.objects.all()
    return render(request, 'index.html', {"assets":assets})

def dashboard(request):
    total = Asset.objects.count()
    upline = Asset.objects.filter(status=0).count()
    offline = Asset.objects.filter(status=1).count()
    unknown = Asset.objects.filter(status=2).count()
    breakdown = Asset.objects.filter(status=3).count()
    backup = Asset.objects.filter(status=4).count()
    up_rate =1
    o_rate = 1
    un_rate = 1
    bd_rate = 1
    bu_rate =1
    server_number = Server.objects.count()
    networkdevice_number = NetworkDevice.objects.count()
    storagedevice_number = StorageDevice.objects.count()
    securitydevice_number = SecurityDevice.objects.count()
    software_number = Software.objects.count()

    return render(request, 'dashboard.html', locals())