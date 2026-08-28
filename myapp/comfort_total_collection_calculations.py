#comfort_total_collection_calculations
from django.shortcuts import render
from django.contrib import messages


import branch1app
import branch2app
import branch3app
import branch4app
import branch5app
import branch6app
import branch7app

import branch53app

def total_collection_details(request):
    comfort1_total_collection = branch1app.admin_dashboard_calculations_br1.grand_total_collection()
    comfort2_total_collection = branch2app.admin_dashboard_calculations_br2.grand_total_collection()
    comfort3_total_collection = branch3app.admin_dashboard_calculations_br3.grand_total_collection()
    comfort4_total_collection = branch4app.admin_dashboard_calculations_br4.grand_total_collection()
    comfort4sub_total_collection = branch53app.admin_dashboard_calculations_br53.grand_total_collection()

    print('comfort4sub_total_collection',comfort4sub_total_collection)
    c4=sum(comfort4sub_total_collection)
    print('sumofc4',c4)

    comfort5_total_collection = branch5app.admin_dashboard_calculations_br5.grand_total_collection()
    comfort6_total_collection = branch6app.admin_dashboard_calculations_br6.grand_total_collection()
    comfort7_total_collection = branch7app.admin_dashboard_calculations_br7.grand_total_collection()

    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    comfort_total_collection = []
    comfort_total_collection.append(comfort1_total_collection[cm])
    comfort_total_collection.append(comfort2_total_collection[cm])
    comfort_total_collection.append(comfort3_total_collection[cm])
    comfort_total_collection.append(comfort4_total_collection[cm])
    comfort_total_collection.append((comfort4sub_total_collection[cm]))
    comfort_total_collection.append(comfort5_total_collection[cm])
    comfort_total_collection.append(comfort6_total_collection[cm])
    comfort_total_collection.append(comfort7_total_collection[cm])

    print('comfort_total_collection', comfort_total_collection)
    sum0f_comoft_tot = sum(comfort_total_collection)
    print('sum0f_comoft_tot',sum0f_comoft_tot)
