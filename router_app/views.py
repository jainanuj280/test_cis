from django.shortcuts import render, redirect
from router_app.forms import RouterDetailsForm
from router_app.models import RouterDetails
import socket
import struct
import random
from random import randint
# Create your views here.

def create(request):
    print('got here')
    if request.method == "POST":
        print('got post')
        form = RouterDetailsForm(request.POST)
        print('form',form)
        if form.is_valid():
            print('form valid')
            try:
                form.save()
                return redirect('/show')
            except:
                print('data invalid')
    else:
        form = RouterDetailsForm()
    return render(request,'index.html',{'form':form})


def show(request):
    routerObjs = RouterDetails.objects.all()
    return render(request,"show.html",{'routerObjs':routerObjs})


def edit(request, id):
    print("in edit")
    routerObj = RouterDetails.objects.get(id=id)
    print(routerObj.macAdd)
    return render(request,'edit.html', {'routerObj':routerObj})

def update(request, id):
    routerObj = RouterDetails.objects.get(id=id)

    form = RouterDetailsForm(request.POST, instance = routerObj)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'routerObj': routerObj})

def delete(request, id):
    routerObj = RouterDetails.objects.get(id=id)
    routerObj.delete()
    return redirect("/show")

#### Show 10 record
def showten(request):
    routerObjs = RouterDetails.objects.all().order_by('-id')[:10]
    return render(request,{'routerObjs':routerObjs})



def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

#### insert 10 record
def insertten(request):
    try:
        for i in range(0,10):
            loopBack = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
            macAdd = "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
            sapId = random_with_N_digits(18)
            hostName = random_with_N_digits(14)
            RouterDetails.objects.create(sapId=sapId, hostName=hostName,
                                             loopBack=loopBack,
                                             macAdd=macAdd)
        return render(request,{'output':"ten records added sucessfully"})
    except Exception as e:
        return render(request,{'output':"adding 10 recods has failed"})
