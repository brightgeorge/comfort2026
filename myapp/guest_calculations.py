from django.shortcuts import render
from django.contrib import messages
from myapp.models import *

import branch1app
import branch2app
import branch3app
import branch4app
import branch5app
import branch6app
import branch7app

import branch21app
import branch22app
import branch23app
import branch24app

import branch31app
import branch32app
import branch33app
import branch34app

import branch41app
import branch42app

import branch51app
import branch52app
import branch53app




def branchwise_guest_details(request):
    comfort=[]
    total_guest_br1 = branch1app.models.pg1_new_beds.objects.all().filter(flag=2)
    comfort.append(len(total_guest_br1))
    total_guest_br2= branch2app.models.pg1_new_beds.objects.all().filter(flag=2)
    comfort.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(flag=2)
    comfort.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(flag=2)
    comfort.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(flag=2)
    comfort.append(len(total_guest_br5))
    total_guest_br6 = branch6app.models.pg1_new_beds.objects.all().filter(flag=2)
    comfort.append(len(total_guest_br6))
    total_guest_br7 = branch7app.models.pg1_new_beds.objects.all().filter(flag=2)
    comfort.append(len(total_guest_br7))

    prestige=[]
    total_guest_br21 = branch21app.models.pg1_new_beds.objects.all().filter(flag=2)
    prestige.append(len(total_guest_br21))
    total_guest_br22 = branch22app.models.pg1_new_beds.objects.all().filter(flag=2)
    prestige.append(len(total_guest_br22))
    total_guest_br23 = branch23app.models.pg1_new_beds.objects.all().filter(flag=2)
    prestige.append(len(total_guest_br23))
    total_guest_br24 = branch24app.models.pg1_new_beds.objects.all().filter(flag=2)
    prestige.append(len(total_guest_br24))

    perfect=[]
    total_guest_br31 = branch31app.models.pg1_new_beds.objects.all().filter(flag=2)
    perfect.append(len(total_guest_br31))
    total_guest_br32 = branch32app.models.pg1_new_beds.objects.all().filter(flag=2)
    perfect.append(len(total_guest_br32))
    total_guest_br33 = branch33app.models.pg1_new_beds.objects.all().filter(flag=2)
    perfect.append(len(total_guest_br33))
    total_guest_br34 = branch34app.models.pg1_new_beds.objects.all().filter(flag=2)
    perfect.append(len(total_guest_br34))

    happy_homes=[]
    total_guest_br41 = branch41app.models.pg1_new_beds.objects.all().filter(flag=2)
    happy_homes.append(len(total_guest_br41))
    total_guest_br42 = branch42app.models.pg1_new_beds.objects.all().filter(flag=2)
    happy_homes.append(len(total_guest_br42))

    comfort_ladies=[]
    total_guest_br51 = branch51app.models.pg1_new_beds.objects.all().filter(flag=2)
    comfort_ladies.append(len(total_guest_br51))
    total_guest_br52 = branch52app.models.pg1_new_beds.objects.all().filter(flag=2)
    comfort_ladies.append(len(total_guest_br52))
    total_guest_br53 = branch53app.models.pg1_new_beds.objects.all().filter(flag=2)
    comfort_ladies.append(len(total_guest_br53))

    total_guest = sum(comfort) + sum(prestige) + sum(perfect) + sum(happy_homes) + sum(comfort_ladies)

    context={
        'comfort' : comfort,
        'prestige' : prestige,
        'perfect' : perfect,
        'happy_homes' : happy_homes,
        'comfort_ladies' : comfort_ladies,

        'total_comfort': sum(comfort),
        'total_prestige': sum(prestige),
        'total_perfect': sum(perfect),
        'total_happy_homes': sum(happy_homes),
        'total_comfort_ladies': sum(comfort_ladies),

        'total_guest' : total_guest,


    }
    return render(request,'admindashboard/guest_details/branchwise_guest_details.html', context)