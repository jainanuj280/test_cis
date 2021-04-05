import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','routerProject.settings')

import django
django.setup()
import socket
import struct
import random
from random import randint
from router_app.models import RouterDetails


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def generator(num):
    print("in here")
    for i in range(0,num):
        print("in for")
        loopBack = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        macAdd = "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        sapId = random_with_N_digits(18)
        hostName = random_with_N_digits(14)
        RouterDetails.objects.create(sapId=sapId, hostName=hostName,
                                         loopBack=loopBack,
                                         macAdd=macAdd)





val = int(input("Enter your value: "))
generator(val)
