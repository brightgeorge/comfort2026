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


def vaccant_room_details(request):
    comfort1_rangl = []
    comfort1_rang = branch1app.models.room_pg1.objects.all()
    for i in comfort1_rang:
        comfort1_rangl.append(i.share_type)
    comfort1_largest = max(comfort1_rangl)

    comfort1_tsv = []
    for i in range(comfort1_largest):
        a = i + 1
        comfort1_total_guest = branch1app.models.pg1_new_beds.objects.all().filter(share_type=a).exclude(flag=2)
        comfort1_tsv.append(len(comfort1_total_guest))

    ###############################################################

    comfort = []
    total_guest_br1 = branch1app.models.pg1_new_beds.objects.all().exclude(flag=2)
    comfort.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().exclude(flag=2)
    comfort.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().exclude(flag=2)
    comfort.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().exclude(flag=2)
    comfort.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().exclude(flag=2)
    comfort.append(len(total_guest_br5))
    total_guest_br6 = branch6app.models.pg1_new_beds.objects.all().exclude(flag=2)
    comfort.append(len(total_guest_br6))
    total_guest_br7 = branch7app.models.pg1_new_beds.objects.all().exclude(flag=2)
    comfort.append(len(total_guest_br7))

    prestige = []
    total_guest_br21 = branch21app.models.pg1_new_beds.objects.all().exclude(flag=2)
    prestige.append(len(total_guest_br21))
    total_guest_br22 = branch22app.models.pg1_new_beds.objects.all().exclude(flag=2)
    prestige.append(len(total_guest_br22))
    total_guest_br23 = branch23app.models.pg1_new_beds.objects.all().exclude(flag=2)
    prestige.append(len(total_guest_br23))
    total_guest_br24 = branch24app.models.pg1_new_beds.objects.all().exclude(flag=2)
    prestige.append(len(total_guest_br24))

    perfect = []
    total_guest_br31 = branch31app.models.pg1_new_beds.objects.all().exclude(flag=2)
    perfect.append(len(total_guest_br31))
    total_guest_br32 = branch32app.models.pg1_new_beds.objects.all().exclude(flag=2)
    perfect.append(len(total_guest_br32))
    total_guest_br33 = branch33app.models.pg1_new_beds.objects.all().exclude(flag=2)
    perfect.append(len(total_guest_br33))
    total_guest_br34 = branch34app.models.pg1_new_beds.objects.all().exclude(flag=2)
    perfect.append(len(total_guest_br34))

    happy_homes = []
    total_guest_br41 = branch41app.models.pg1_new_beds.objects.all().exclude(flag=2)
    happy_homes.append(len(total_guest_br41))
    total_guest_br42 = branch42app.models.pg1_new_beds.objects.all().exclude(flag=2)
    happy_homes.append(len(total_guest_br42))

    comfort_ladies = []
    total_guest_br51 = branch51app.models.pg1_new_beds.objects.all().exclude(flag=2)
    comfort_ladies.append(len(total_guest_br51))
    total_guest_br52 = branch52app.models.pg1_new_beds.objects.all().exclude(flag=2)
    comfort_ladies.append(len(total_guest_br52))
    total_guest_br53 = branch53app.models.pg1_new_beds.objects.all().exclude(flag=2)
    comfort_ladies.append(len(total_guest_br53))

    total_guest = sum(comfort) + sum(prestige) + sum(perfect) + sum(happy_homes) + sum(comfort_ladies)

    context = {
        'comfort': comfort,
        'prestige': prestige,
        'perfect': perfect,
        'happy_homes': happy_homes,
        'comfort_ladies': comfort_ladies,

        'total_comfort': sum(comfort),
        'total_prestige': sum(prestige),
        'total_perfect': sum(perfect),
        'total_happy_homes': sum(happy_homes),
        'total_comfort_ladies': sum(comfort_ladies),

        'total_guest': total_guest,
    }
    return render(request,'admindashboard/vaccant_rooms/vaccant_room_details.html',context)


def total_vaccant_share1():
    tsv = []
    total_guest_br1 = branch1app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br6 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br6))
    total_guest_br7 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br7))

    total_guest_br21 = branch21app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br21))
    total_guest_br22 = branch22app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br22))
    total_guest_br23 = branch23app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br23))
    total_guest_br24 = branch24app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br24))

    total_guest_br31 = branch31app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br31))
    total_guest_br32 = branch32app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br32))
    total_guest_br33 = branch33app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br33))
    total_guest_br34 = branch34app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br34))

    total_guest_br41 = branch41app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br41))
    total_guest_br42 = branch42app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br42))

    total_guest_br51 = branch51app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br51))
    total_guest_br52 = branch52app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br52))
    total_guest_br53 = branch53app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br53))

    return sum(tsv)

def total_vaccant_share2():
    tsv = []
    total_guest_br1 = branch1app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br6 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br6))
    total_guest_br7 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br7))

    total_guest_br21 = branch21app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br21))
    total_guest_br22 = branch22app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br22))
    total_guest_br23 = branch23app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br23))
    total_guest_br24 = branch24app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br24))

    total_guest_br31 = branch31app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br31))
    total_guest_br32 = branch32app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br32))
    total_guest_br33 = branch33app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br33))
    total_guest_br34 = branch34app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br34))

    total_guest_br41 = branch41app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br41))
    total_guest_br42 = branch42app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br42))

    total_guest_br51 = branch51app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br51))
    total_guest_br52 = branch52app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br52))
    total_guest_br53 = branch53app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br53))

    return sum(tsv)

def total_vaccant_share3():
    tsv = []
    total_guest_br1 = branch1app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br6 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br6))
    total_guest_br7 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br7))

    total_guest_br21 = branch21app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br21))
    total_guest_br22 = branch22app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br22))
    total_guest_br23 = branch23app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br23))
    total_guest_br24 = branch24app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br24))

    total_guest_br31 = branch31app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br31))
    total_guest_br32 = branch32app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br32))
    total_guest_br33 = branch33app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br33))
    total_guest_br34 = branch34app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br34))

    total_guest_br41 = branch41app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br41))
    total_guest_br42 = branch42app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br42))

    total_guest_br51 = branch51app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br51))
    total_guest_br52 = branch52app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br52))
    total_guest_br53 = branch53app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br53))

    return sum(tsv)

def total_vaccant_share4():
    tsv = []
    total_guest_br1 = branch1app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br6 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br6))
    total_guest_br7 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br7))

    total_guest_br21 = branch21app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br21))
    total_guest_br22 = branch22app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br22))
    total_guest_br23 = branch23app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br23))
    total_guest_br24 = branch24app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br24))

    total_guest_br31 = branch31app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br31))
    total_guest_br32 = branch32app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br32))
    total_guest_br33 = branch33app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br33))
    total_guest_br34 = branch34app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br34))

    total_guest_br41 = branch41app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br41))
    total_guest_br42 = branch42app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br42))

    total_guest_br51 = branch51app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br51))
    total_guest_br52 = branch52app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br52))
    total_guest_br53 = branch53app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br53))

    return sum(tsv)

def total_vaccant_share5():
    tsv = []
    total_guest_br1 = branch1app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br6 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br6))
    total_guest_br7 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br7))

    total_guest_br21 = branch21app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br21))
    total_guest_br22 = branch22app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br22))
    total_guest_br23 = branch23app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br23))
    total_guest_br24 = branch24app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br24))

    total_guest_br31 = branch31app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br31))
    total_guest_br32 = branch32app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br32))
    total_guest_br33 = branch33app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br33))
    total_guest_br34 = branch34app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br34))

    total_guest_br41 = branch41app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br41))
    total_guest_br42 = branch42app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br42))

    total_guest_br51 = branch51app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br51))
    total_guest_br52 = branch52app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br52))
    total_guest_br53 = branch53app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br53))

    return sum(tsv)

def total_vaccant_share6():
    tsv = []
    total_guest_br1 = branch1app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br6 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br6))
    total_guest_br7 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br7))

    total_guest_br21 = branch21app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br21))
    total_guest_br22 = branch22app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br22))
    total_guest_br23 = branch23app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br23))
    total_guest_br24 = branch24app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br24))

    total_guest_br31 = branch31app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br31))
    total_guest_br32 = branch32app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br32))
    total_guest_br33 = branch33app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br33))
    total_guest_br34 = branch34app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br34))

    total_guest_br41 = branch41app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br41))
    total_guest_br42 = branch42app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br42))

    total_guest_br51 = branch51app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br51))
    total_guest_br52 = branch52app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br52))
    total_guest_br53 = branch53app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br53))

    return sum(tsv)

def total_vaccant_room():
    tsv = []
    total_vaccant_room_br1 = total_vaccant_share1()
    tsv.append(total_vaccant_room_br1)
    total_vaccant_room_br2 = total_vaccant_share2()
    tsv.append(total_vaccant_room_br2)
    total_vaccant_room_br3 = total_vaccant_share3()
    tsv.append(total_vaccant_room_br3)
    total_vaccant_room_br4 = total_vaccant_share4()
    tsv.append(total_vaccant_room_br4)
    total_vaccant_room_br5 = total_vaccant_share5()
    tsv.append(total_vaccant_room_br5)
    total_vaccant_room_br6 = total_vaccant_share6()
    tsv.append(total_vaccant_room_br6)

    return sum(tsv)


def total_vaccant_share_branch1():
    tsv = []
    total_guest_br1 = branch1app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch1app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch1app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch1app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch1app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch1app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch2():
    tsv = []
    total_guest_br1 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch3():
    tsv = []
    total_guest_br1 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch4():
    tsv = []
    total_guest_br1 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch5():
    tsv = []
    total_guest_br1 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch6():
    tsv = []
    total_guest_br1 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch7():
    tsv = []
    total_guest_br1 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch8():
    tsv = []
    total_guest_br1 = branch8app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch8app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch8app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch8app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch8app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch8app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch9():
    tsv = []
    total_guest_br1 = branch9app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch9app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch9app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch9app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch9app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch9app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch10():
    tsv = []
    total_guest_br1 = branch10app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch10app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch10app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch10app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch10app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch10app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch11():
    tsv = []
    total_guest_br1 = branch11app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch11app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch11app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch11app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch11app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch11app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch12():
    tsv = []
    total_guest_br1 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch13():
    tsv = []
    total_guest_br1 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch14():
    tsv = []
    total_guest_br1 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch15():
    tsv = []
    total_guest_br1 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch16():
    tsv = []
    total_guest_br1 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv



def total_vaccant_share_choose_branches(request):
    context = {
        'br1' : total_vaccant_share_branch1(),
        'br2': total_vaccant_share_branch2(),
        'br3': total_vaccant_share_branch3(),
        'br4': total_vaccant_share_branch4(),
        'br5': total_vaccant_share_branch5(),

        'br6': total_vaccant_share_branch6(),
        'br7': total_vaccant_share_branch7(),
        'br8': total_vaccant_share_branch8(),
        'br9': total_vaccant_share_branch9(),

        'br10': total_vaccant_share_branch10(),
        'br11': total_vaccant_share_branch11(),
        'br12': total_vaccant_share_branch12(),
        'br13': total_vaccant_share_branch13(),
        'br14': total_vaccant_share_branch14(),

        'br15': total_vaccant_share_branch15(),
        'br16': total_vaccant_share_branch16(),

    }
    return render(request,'admindashboard/admin_dashboard_reports/total_vaccant_share_choose_branches.html',context)
