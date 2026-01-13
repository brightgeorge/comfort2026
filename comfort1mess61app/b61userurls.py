from django.urls import path, include

from . import admin_branch61
from . import admin_branch61
from . import branch61
from . import reports61
from . import payment61
from . import admin_dashboard_calculations_br61
from . import accounts61

urlpatterns = [

    path('branch1_dashboard_ob_ch61/', branch61.branch1_dashboard_ob_ch61, name='branch1_dashboard_ob_ch61'),
    path('user_dashboard_calculations_ob_ch61/',branch61.user_dashboard_calculations_ob_ch61,name='user_dashboard_calculations_ob_ch61'),

    path('background_ob_ch61',branch61.background_ob_ch61,name='background_ob_ch61'),
    path('background_regi_ob_ch61',branch61.background_regi_ob_ch61,name='background_regi_ob_ch61'),
    path('custom_background_regi_ob_ch61',branch61.custom_background_regi_ob_ch61,name='custom_background_regi_ob_ch61'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch61/',admin_branch61.branch1_room_create_regi_ob_ch61,name='branch1_room_create_regi_ob_ch61'),
    path('view_all_room_ob_ch61/',admin_branch61.view_all_room_ob_ch61,name='view_all_room_ob_ch61'),
    path('delete_room_ob_ch61/<id>',admin_branch61.delete_room_ob_ch61,name='delete_room_ob_ch61'),

    path('branch1_room_create_ob_ch61/',admin_branch61.branch1_room_create_ob_ch61,name='branch1_room_create_ob_ch61'),

    path('multiple_branch1_room_create_regi61/',admin_branch61.multiple_branch1_room_create_regi61,name='multiple_branch1_room_create_regi61'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch61/', admin_branch61.pg1_bed_create_regi_ob_ch61, name='pg1_bed_create_regi_ob_ch61'),
    path('pg1_view_all_beds_ob_ch61/', admin_branch61.pg1_view_all_beds_ob_ch61, name='pg1_view_all_beds_ob_ch61'),
    path('delete_bed_ob_ch61/<id>', admin_branch61.delete_bed_ob_ch61, name='delete_bed_ob_ch61'),

    path('pg1_bed_create_ob_ch61/', admin_branch61.pg1_bed_create_ob_ch61, name='pg1_bed_create_ob_ch61'),

    path('single_pg1_bed_create_regi_ob_ch61/',admin_branch61.single_pg1_bed_create_regi_ob_ch61,name='single_pg1_bed_create_regi_ob_ch61'),
    path('update_bed_basic_details_ob_ch61/<id>',admin_branch61.update_bed_basic_details_ob_ch61, name='update_bed_basic_details_ob_ch61'),

    path('multiple_single_pg1_bed_create_regi61/',admin_branch61.multiple_single_pg1_bed_create_regi61,name='multiple_single_pg1_bed_create_regi61'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch61/<id>',branch61.br1_admit_guest_ob_ch61,name='br1_admit_guest_ob_ch61'),
    path('view_all_new_guest_ob_ch61/',branch61.view_all_new_guest_ob_ch61,name='view_all_new_guest_ob_ch61'),
    path('update_br1_admit_guest_ob_ch61/<id>',branch61.update_br1_admit_guest_ob_ch61,name='update_br1_admit_guest_ob_ch61'),
    path('vacate_br1_guest_ob_ch61/<id>',branch61.vacate_br1_guest_ob_ch61,name='vacate_br1_guest_ob_ch61'),

    path('active_guest_details_ob_ch61/<guest_code>',branch61.active_guest_details_ob_ch61,name='active_guest_details_ob_ch61'),
    path('view_all_guest_ob_ch61/',branch61.view_all_guest_ob_ch61,name='view_all_guest_ob_ch61'),
    path('shift_guest_ob_ch61/<id>',branch61.shift_guest_ob_ch61,name='shift_guest_ob_ch61'),
    path('shift_guest_regi_ob_ch61/',branch61.shift_guest_regi_ob_ch61,name='shift_guest_regi_ob_ch61'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch61/',branch61.update_all_rent_ob_ch61,name='update_all_rent_ob_ch61'),

    path('multiple_br1_admit_guest61/<id>',branch61.multiple_br1_admit_guest61,name='multiple_br1_admit_guest61'),

#guest end here


##################################
#_ADVANCE_ob_ch61 START HERE
################################


    path('choose_months_advance_ob_ch61/',branch61.choose_months_advance_ob_ch61,name='choose_months_advance_ob_ch61'),

    path('jan_advance_ob_ch61/', branch61.jan_advance_ob_ch61, name='jan_advance_ob_ch61'),
    path('jan_make_payments_advance_ob_ch61/<id>', branch61.jan_make_payments_advance_ob_ch61,name='jan_make_payments_advance_ob_ch61'),
    path('feb_advance_ob_ch61/', branch61.feb_advance_ob_ch61, name='feb_advance_ob_ch61'),
    path('feb_make_payments_advance_ob_ch61/<id>', branch61.feb_make_payments_advance_ob_ch61,name='feb_make_payments_advance_ob_ch61'),
    path('march_advance_ob_ch61/', branch61.march_advance_ob_ch61, name='march_advance_ob_ch61'),
    path('march_make_payments_advance_ob_ch61/<id>', branch61.march_make_payments_advance_ob_ch61,name='march_make_payments_advance_ob_ch61'),
    path('april_advance_ob_ch61/', branch61.april_advance_ob_ch61, name='april_advance_ob_ch61'),
    path('april_make_payments_advance_ob_ch61/<id>', branch61.april_make_payments_advance_ob_ch61, name='april_make_payments_advance_ob_ch61'),

    path('may_advance_ob_ch61/',branch61.may_advance_ob_ch61,name='may_advance_ob_ch61'),
    path('may_make_payments_advance_ob_ch61/<id>', branch61.may_make_payments_advance_ob_ch61, name='may_make_payments_advance_ob_ch61'),
    path('june_advance_ob_ch61/',branch61.june_advance_ob_ch61,name='june_advance_ob_ch61'),
    path('june_make_payments_advance_ob_ch61/<id>', branch61.june_make_payments_advance_ob_ch61, name='june_make_payments_advance_ob_ch61'),
    path('july_advance_ob_ch61/',branch61.july_advance_ob_ch61,name='july_advance_ob_ch61'),
    path('july_make_payments_advance_ob_ch61/<id>', branch61.july_make_payments_advance_ob_ch61, name='july_make_payments_advance_ob_ch61'),
    path('auguest_advance_ob_ch61/', branch61.auguest_advance_ob_ch61, name='auguest_advance_ob_ch61'),
    path('auguest_make_payments_advance_ob_ch61/<id>', branch61.auguest_make_payments_advance_ob_ch61, name='auguest_make_payments_advance_ob_ch61'),

    path('sept_advance_ob_ch61/', branch61.sept_advance_ob_ch61, name='sept_advance_ob_ch61'),
    path('sept_make_payments_advance_ob_ch61/<id>', branch61.sept_make_payments_advance_ob_ch61,name='sept_make_payments_advance_ob_ch61'),
    path('october_advance_ob_ch61/', branch61.october_advance_ob_ch61, name='october_advance_ob_ch61'),
    path('october_make_payments_advance_ob_ch61/<id>', branch61.october_make_payments_advance_ob_ch61, name='october_make_payments_advance_ob_ch61'),
    path('nov_advance_ob_ch61/', branch61.nov_advance_ob_ch61, name='nov_advance_ob_ch61'),
    path('nov_make_payments_advance_ob_ch61/<id>', branch61.nov_make_payments_advance_ob_ch61,name='nov_make_payments_advance_ob_ch61'),
    path('dec_advance_ob_ch61/', branch61.dec_advance_ob_ch61, name='dec_advance_ob_ch61'),
    path('dec_make_payments_advance_ob_ch61/<id>', branch61.dec_make_payments_advance_ob_ch61, name='dec_make_payments_advance_ob_ch61'),



##################################
#_ADVANCE_ob_ch61 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch61/',branch61.choose_months_ob_ch61,name='choose_months_ob_ch61'),

    path('jan_ob_ch61/',branch61.jan_ob_ch61,name='jan_ob_ch61'),
    path('jan_manke_payments_ob_ch61/<id>',branch61.jan_manke_payments_ob_ch61,name='jan_manke_payments_ob_ch61'),

    path('feb_ob_ch61/',branch61.feb_ob_ch61,name='feb_ob_ch61'),
    path('feb_manke_payments_ob_ch61/<id>',branch61.feb_manke_payments_ob_ch61,name='feb_manke_payments_ob_ch61'),

    path('march_ob_ch61/',branch61.march_ob_ch61,name='march_ob_ch61'),
    path('march_manke_payments_ob_ch61/<id>',branch61.march_manke_payments_ob_ch61,name='march_manke_payments_ob_ch61'),

    path('april_ob_ch61/',branch61.april_ob_ch61,name='april_ob_ch61'),
    path('april_make_payments_ob_ch61/<id>',branch61.april_make_payments_ob_ch61,name='april_make_payments_ob_ch61'),

    path('may_ob_ch61/',branch61.may_ob_ch61,name='may_ob_ch61'),
    path('may_make_payments_ob_ch61/<id>',branch61.may_make_payments_ob_ch61,name='may_make_payments_ob_ch61'),

    path('june_ob_ch61/',branch61.june_ob_ch61,name='june_ob_ch61'),
    path('june_make_payments_ob_ch61/<id>',branch61.june_make_payments_ob_ch61,name='june_make_payments_ob_ch61'),

    path('july_ob_ch61/',branch61.july_ob_ch61,name='july_ob_ch61'),
    path('july_make_payments_ob_ch61/<id>',branch61.july_make_payments_ob_ch61,name='july_make_payments_ob_ch61'),

    path('aug_ob_ch61/',branch61.aug_ob_ch61,name='aug_ob_ch61'),
    path('aug_make_payments_ob_ch61/<id>',branch61.aug_make_payments_ob_ch61,name='aug_make_payments_ob_ch61'),

    path('sept_ob_ch61/',branch61.sept_ob_ch61,name='sept_ob_ch61'),
    path('sept_make_payments_ob_ch61/<id>',branch61.sept_make_payments_ob_ch61,name='sept_make_payments_ob_ch61'),

    path('oct_ob_ch61/',branch61.oct_ob_ch61,name='oct_ob_ch61'),
    path('oct_make_payments_ob_ch61/<id>',branch61.oct_make_payments_ob_ch61,name='oct_make_payments_ob_ch61'),

    path('nov_ob_ch61/',branch61.nov_ob_ch61,name='nov_ob_ch61'),
    path('nov_make_payments_ob_ch61/<id>',branch61.nov_make_payments_ob_ch61,name='nov_make_payments_ob_ch61'),

    path('dec_ob_ch61/',branch61.dec_ob_ch61,name='dec_ob_ch61'),
    path('dec_make_payments_ob_ch61/<id>',branch61.dec_make_payments_ob_ch61,name='dec_make_payments_ob_ch61'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch61/', payment61.choose_user_ob_ch61, name='choose_user_ob_ch61'),
    path('payment_user_details_ob_ch61/<id>', payment61.payment_user_details_ob_ch61, name='payment_user_details_ob_ch61'),
    path('close_choose_user_ob_ch61/<id>',payment61.close_choose_user_ob_ch61,name='close_choose_user_ob_ch61'),

    path('monthly_jan_make_payments_ob_ch61/<id>', payment61.monthly_jan_make_payments_ob_ch61, name='monthly_jan_make_payments_ob_ch61'),
    path('monthly_feb_make_payments_ob_ch61/<id>', payment61.monthly_feb_make_payments_ob_ch61, name='monthly_feb_make_payments_ob_ch61'),
    path('monthly_march_make_payments_ob_ch61/<id>', payment61.monthly_march_make_payments_ob_ch61, name='monthly_march_make_payments_ob_ch61'),
    path('monthly_april_make_payments_ob_ch61/<id>', payment61.monthly_april_make_payments_ob_ch61, name='monthly_april_make_payments_ob_ch61'),
    path('monthly_may_make_payments_ob_ch61/<id>', payment61.monthly_may_make_payments_ob_ch61, name='monthly_may_make_payments_ob_ch61'),
    path('monthly_june_make_payments_ob_ch61/<id>', payment61.monthly_june_make_payments_ob_ch61, name='monthly_june_make_payments_ob_ch61'),

    path('monthly_july_make_payments_ob_ch61/<id>', payment61.monthly_july_make_payments_ob_ch61, name='monthly_july_make_payments_ob_ch61'),
    path('monthly_aug_make_payments_ob_ch61/<id>', payment61.monthly_aug_make_payments_ob_ch61, name='monthly_aug_make_payments_ob_ch61'),
    path('monthly_sept_make_payments_ob_ch61/<id>', payment61.monthly_sept_make_payments_ob_ch61, name='monthly_sept_make_payments_ob_ch61'),
    path('monthly_oct_make_payments_ob_ch61/<id>', payment61.monthly_oct_make_payments_ob_ch61, name='monthly_oct_make_payments_ob_ch61'),
    path('monthly_nov_make_payments_ob_ch61/<id>', payment61.monthly_nov_make_payments_ob_ch61, name='monthly_nov_make_payments_ob_ch61'),
    path('monthly_dec_make_payments_ob_ch61/<id>', payment61.monthly_dec_make_payments_ob_ch61, name='monthly_dec_make_payments_ob_ch61'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch61/',branch61.unpaid_rent_choose_months_ob_ch61,name='unpaid_rent_choose_months_ob_ch61'),

    path('jan_unpaid_rent_ob_ch61/', branch61.jan_unpaid_rent_ob_ch61, name='jan_unpaid_rent_ob_ch61'),
    path('table_jan_unpaid_rent_ob_ch61/', branch61.table_jan_unpaid_rent_ob_ch61, name='table_jan_unpaid_rent_ob_ch61'),
    path('feb_unpaid_rent_ob_ch61/', branch61.feb_unpaid_rent_ob_ch61, name='feb_unpaid_rent_ob_ch61'),
    path('table_feb_unpaid_rent_ob_ch61/', branch61.table_feb_unpaid_rent_ob_ch61, name='table_feb_unpaid_rent_ob_ch61'),
    path('mar_unpaid_rent_ob_ch61/', branch61.mar_unpaid_rent_ob_ch61, name='mar_unpaid_rent_ob_ch61'),
    path('table_mar_unpaid_rent_ob_ch61/', branch61.table_mar_unpaid_rent_ob_ch61, name='table_mar_unpaid_rent_ob_ch61'),
    path('april_unpaid_rent_ob_ch61/', branch61.april_unpaid_rent_ob_ch61, name='april_unpaid_rent_ob_ch61'),
    path('table_april_unpaid_rent_ob_ch61/', branch61.table_april_unpaid_rent_ob_ch61, name='table_april_unpaid_rent_ob_ch61'),

    path('may_unpaid_rent_ob_ch61/', branch61.may_unpaid_rent_ob_ch61, name='may_unpaid_rent_ob_ch61'),
    path('table_may_unpaid_rent_ob_ch61/', branch61.table_may_unpaid_rent_ob_ch61, name='table_may_unpaid_rent_ob_ch61'),
    path('june_unpaid_rent_ob_ch61/', branch61.june_unpaid_rent_ob_ch61, name='june_unpaid_rent_ob_ch61'),
    path('table_june_unpaid_rent_ob_ch61/', branch61.table_june_unpaid_rent_ob_ch61, name='table_june_unpaid_rent_ob_ch61'),
    path('july_unpaid_rent_ob_ch61/', branch61.july_unpaid_rent_ob_ch61, name='july_unpaid_rent_ob_ch61'),
    path('table_july_unpaid_rent_ob_ch61',branch61.table_july_unpaid_rent_ob_ch61,name='table_july_unpaid_rent_ob_ch61'),
    path('aug_unpaid_rent_ob_ch61/', branch61.aug_unpaid_rent_ob_ch61, name='aug_unpaid_rent_ob_ch61'),
    path('table_aug_unpaid_rent_ob_ch61/',branch61.table_aug_unpaid_rent_ob_ch61,name='table_aug_unpaid_rent_ob_ch61'),

    path('sept_unpaid_rent_ob_ch61/', branch61.sept_unpaid_rent_ob_ch61, name='sept_unpaid_rent_ob_ch61'),
    path('table_sept_unpaid_rent_ob_ch61/', branch61.table_sept_unpaid_rent_ob_ch61, name='table_sept_unpaid_rent_ob_ch61'),
    path('oct_unpaid_rent_ob_ch61/', branch61.oct_unpaid_rent_ob_ch61, name='oct_unpaid_rent_ob_ch61'),
    path('table_oct_unpaid_rent_ob_ch61/', branch61.table_oct_unpaid_rent_ob_ch61, name='table_oct_unpaid_rent_ob_ch61'),
    path('nov_unpaid_rent_ob_ch61/', branch61.nov_unpaid_rent_ob_ch61, name='nov_unpaid_rent_ob_ch61'),
    path('table_nov_unpaid_rent_ob_ch61/', branch61.table_nov_unpaid_rent_ob_ch61, name='table_nov_unpaid_rent_ob_ch61'),
    path('dec_unpaid_rent_ob_ch61/', branch61.dec_unpaid_rent_ob_ch61, name='dec_unpaid_rent_ob_ch61'),
    path('table_dec_unpaid_rent_ob_ch61/', branch61.table_dec_unpaid_rent_ob_ch61, name='table_dec_unpaid_rent_ob_ch61'),

    path('details_of_unpaid_guests_ob_ch61/<id>',branch61.details_of_unpaid_guests_ob_ch61,name='details_of_unpaid_guests_ob_ch61'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch61/',branch61.paid_rent_choose_months_ob_ch61,name='paid_rent_choose_months_ob_ch61'),
    path('partially_paid_guest_choose_months_ob_ch61/',reports61.partially_paid_guest_choose_months_ob_ch61,name='partially_paid_guest_choose_months_ob_ch61'),

    path('jan_paid_rent_ob_ch61/', branch61.jan_paid_rent_ob_ch61, name='jan_paid_rent_ob_ch61'),
    path('table_jan_paid_rent_ob_ch61/', branch61.table_jan_paid_rent_ob_ch61, name='table_jan_paid_rent_ob_ch61'),
    path('jan_full_paid_guest_ob_ch61/', reports61.jan_full_paid_guest_ob_ch61, name='jan_full_paid_guest_ob_ch61'),
    path('jan_partially_paid_guest_ob_ch61/', reports61.jan_partially_paid_guest_ob_ch61, name='jan_partially_paid_guest_ob_ch61'),
    path('table_jan_partially_paid_guest_ob_ch61/', reports61.table_jan_partially_paid_guest_ob_ch61,name='table_jan_partially_paid_guest_ob_ch61'),

    path('feb_paid_rent_ob_ch61/', branch61.feb_paid_rent_ob_ch61, name='feb_paid_rent_ob_ch61'),
    path('table_feb_paid_rent_ob_ch61/', branch61.table_feb_paid_rent_ob_ch61, name='table_feb_paid_rent_ob_ch61'),
    path('feb_full_paid_guest_ob_ch61/', reports61.feb_full_paid_guest_ob_ch61, name='feb_full_paid_guest_ob_ch61'),
    path('feb_partially_paid_guest_ob_ch61/', reports61.feb_partially_paid_guest_ob_ch61, name='feb_partially_paid_guest_ob_ch61'),
    path('table_feb_partially_paid_guest_ob_ch61/', reports61.table_feb_partially_paid_guest_ob_ch61,name='table_feb_partially_paid_guest_ob_ch61'),

    path('mar_paid_rent_ob_ch61/', branch61.mar_paid_rent_ob_ch61, name='mar_paid_rent_ob_ch61'),
    path('table_mar_paid_rent_ob_ch61/', branch61.table_mar_paid_rent_ob_ch61, name='table_mar_paid_rent_ob_ch61'),
    path('march_full_paid_guest_ob_ch61/', reports61.march_full_paid_guest_ob_ch61, name='march_full_paid_guest_ob_ch61'),
    path('march_partially_paid_guest_ob_ch61/', reports61.march_partially_paid_guest_ob_ch61, name='march_partially_paid_guest_ob_ch61'),
    path('table_march_partially_paid_guest_ob_ch61/', reports61.table_march_partially_paid_guest_ob_ch61,name='table_march_partially_paid_guest_ob_ch61'),

    path('april_paid_rent_ob_ch61/', branch61.april_paid_rent_ob_ch61, name='april_paid_rent_ob_ch61'),
    path('table_april_paid_rent_ob_ch61/', branch61.table_april_paid_rent_ob_ch61, name='table_april_paid_rent_ob_ch61'),
    path('april_full_paid_guest_ob_ch61/', reports61.april_full_paid_guest_ob_ch61, name='april_full_paid_guest_ob_ch61'),
    path('april_partially_paid_guest_ob_ch61/', reports61.april_partially_paid_guest_ob_ch61, name='april_partially_paid_guest_ob_ch61'),
    path('table_april_partially_paid_guest_ob_ch61/', reports61.table_april_partially_paid_guest_ob_ch61,name='table_april_partially_paid_guest_ob_ch61'),

    path('may_paid_rent_ob_ch61/', branch61.may_paid_rent_ob_ch61, name='may_paid_rent_ob_ch61'),
    path('table_may_paid_rent_ob_ch61/', branch61.table_may_paid_rent_ob_ch61, name='table_may_paid_rent_ob_ch61'),
    path('may_full_paid_guest_ob_ch61/', reports61.may_full_paid_guest_ob_ch61, name='may_full_paid_guest_ob_ch61'),
    path('may_partially_paid_guest_ob_ch61/', reports61.may_partially_paid_guest_ob_ch61, name='may_partially_paid_guest_ob_ch61'),
    path('table_may_partially_paid_guest_ob_ch61/', reports61.table_may_partially_paid_guest_ob_ch61, name='table_may_partially_paid_guest_ob_ch61'),

    path('june_paid_rent_ob_ch61/', branch61.june_paid_rent_ob_ch61, name='june_paid_rent_ob_ch61'),
    path('table_june_paid_rent_ob_ch61/', branch61.table_june_paid_rent_ob_ch61, name='table_june_paid_rent_ob_ch61'),
    path('june_full_paid_guest_ob_ch61/', reports61.june_full_paid_guest_ob_ch61, name='june_full_paid_guest_ob_ch61'),
    path('june_partially_paid_guest_ob_ch61/', reports61.june_partially_paid_guest_ob_ch61, name='june_partially_paid_guest_ob_ch61'),
    path('table_june_partially_paid_guest_ob_ch61/', reports61.table_june_partially_paid_guest_ob_ch61, name='table_june_partially_paid_guest_ob_ch61'),

    path('july_paid_rent_ob_ch61/', branch61.july_paid_rent_ob_ch61, name='july_paid_rent_ob_ch61'),
    path('table_july_paid_rent_ob_ch61/', branch61.table_july_paid_rent_ob_ch61, name='table_july_paid_rent_ob_ch61'),
    path('july_full_paid_guest_ob_ch61/', reports61.july_full_paid_guest_ob_ch61, name='july_full_paid_guest_ob_ch61'),
    path('july_partially_paid_guest_ob_ch61/', reports61.july_partially_paid_guest_ob_ch61, name='july_partially_paid_guest_ob_ch61'),
    path('table_july_partially_paid_guest_ob_ch61/', reports61.table_july_partially_paid_guest_ob_ch61, name='table_july_partially_paid_guest_ob_ch61'),

    path('aug_paid_rent_ob_ch61/', branch61.aug_paid_rent_ob_ch61, name='aug_paid_rent_ob_ch61'),
    path('table_aug_paid_rent_ob_ch61/', branch61.table_aug_paid_rent_ob_ch61, name='table_aug_paid_rent_ob_ch61'),
    path('auguest_full_paid_guest_ob_ch61/', reports61.auguest_full_paid_guest_ob_ch61, name='auguest_full_paid_guest_ob_ch61'),
    path('auguest_partially_paid_guest_ob_ch61/', reports61.auguest_partially_paid_guest_ob_ch61,name='auguest_partially_paid_guest_ob_ch61'),
    path('table_auguest_partially_paid_guest_ob_ch61/', reports61.table_auguest_partially_paid_guest_ob_ch61,name='table_auguest_partially_paid_guest_ob_ch61'),

    path('sept_paid_rent_ob_ch61/', branch61.sept_paid_rent_ob_ch61, name='sept_paid_rent_ob_ch61'),
    path('table_sept_paid_rent_ob_ch61/', branch61.table_sept_paid_rent_ob_ch61, name='table_sept_paid_rent_ob_ch61'),
    path('sept_full_paid_guest_ob_ch61/', reports61.sept_full_paid_guest_ob_ch61, name='sept_full_paid_guest_ob_ch61'),
    path('sept_partially_paid_guest_ob_ch61/', reports61.sept_partially_paid_guest_ob_ch61, name='sept_partially_paid_guest_ob_ch61'),
    path('table_sept_partially_paid_guest_ob_ch61/', reports61.table_sept_partially_paid_guest_ob_ch61,name='table_sept_partially_paid_guest_ob_ch61'),

    path('oct_paid_rent_ob_ch61/', branch61.oct_paid_rent_ob_ch61, name='oct_paid_rent_ob_ch61'),
    path('table_oct_paid_rent_ob_ch61/', branch61.table_oct_paid_rent_ob_ch61, name='table_oct_paid_rent_ob_ch61'),
    path('october_full_paid_guest_ob_ch61/', reports61.october_full_paid_guest_ob_ch61, name='october_full_paid_guest_ob_ch61'),
    path('october_partially_paid_guest_ob_ch61/', reports61.october_partially_paid_guest_ob_ch61,name='october_partially_paid_guest_ob_ch61'),
    path('table_october_partially_paid_guest_ob_ch61/', reports61.table_october_partially_paid_guest_ob_ch61,name='table_october_partially_paid_guest_ob_ch61'),

    path('nov_paid_rent_ob_ch61/', branch61.nov_paid_rent_ob_ch61, name='nov_paid_rent_ob_ch61'),
    path('table_nov_paid_rent_ob_ch61/', branch61.table_nov_paid_rent_ob_ch61, name='table_nov_paid_rent_ob_ch61'),
    path('nov_full_paid_guest_ob_ch61/', reports61.nov_full_paid_guest_ob_ch61, name='nov_full_paid_guest_ob_ch61'),
    path('nov_partially_paid_guest_ob_ch61/', reports61.nov_partially_paid_guest_ob_ch61, name='nov_partially_paid_guest_ob_ch61'),
    path('table_nov_partially_paid_guest_ob_ch61/', reports61.table_nov_partially_paid_guest_ob_ch61,name='table_nov_partially_paid_guest_ob_ch61'),

    path('dec_paid_rent_ob_ch61/', branch61.dec_paid_rent_ob_ch61, name='dec_paid_rent_ob_ch61'),
    path('table_dec_paid_rent_ob_ch61/', branch61.table_dec_paid_rent_ob_ch61, name='table_dec_paid_rent_ob_ch61'),
    path('dec_full_paid_guest_ob_ch61/', reports61.dec_full_paid_guest_ob_ch61, name='dec_full_paid_guest_ob_ch61'),
    path('dec_partially_paid_guest_ob_ch61/', reports61.dec_partially_paid_guest_ob_ch61, name='dec_partially_paid_guest_ob_ch61'),
    path('table_dec_partially_paid_guest_ob_ch61/', reports61.table_dec_partially_paid_guest_ob_ch61,name='table_dec_partially_paid_guest_ob_ch61'),

    path('details_of_paid_guests_ob_ch61/<id>',branch61.details_of_paid_guests_ob_ch61,name='details_of_paid_guests_ob_ch61'),
    path('full_paid_guest_ob_ch61/',reports61.full_paid_guest_ob_ch61,name='full_paid_guest_ob_ch61'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch61/',branch61.viewall_vacate_guest_ob_ch61,name='viewall_vacate_guest_ob_ch61'),
    path('details_of_vacate_guest_ob_ch61/<id>',branch61.details_of_vacate_guest_ob_ch61,name='details_of_vacate_guest_ob_ch61'),
    path('full_vacated_guest_details_ob_ch61',branch61.full_vacated_guest_details_ob_ch61,name='full_vacated_guest_details_ob_ch61'),
    path('full_vacated_guest_table_ob_ch61',branch61.full_vacated_guest_table_ob_ch61,name='full_vacated_guest_table_ob_ch61'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch61/<id>', branch61.jan_manke_payments_vacate_ob_ch61, name='jan_manke_payments_vacate_ob_ch61'),
    path('feb_manke_payments_vacate_ob_ch61/<id>', branch61.feb_manke_payments_vacate_ob_ch61, name='feb_manke_payments_vacate_ob_ch61'),
    path('march_manke_payments_vacate_ob_ch61/<id>', branch61.march_manke_payments_vacate_ob_ch61, name='march_manke_payments_vacate_ob_ch61'),
    path('april_make_payments_vacate_ob_ch61/<id>', branch61.april_make_payments_vacate_ob_ch61, name='april_make_payments_vacate_ob_ch61'),

    path('may_make_payments_vacate_ob_ch61/<id>', branch61.may_make_payments_vacate_ob_ch61, name='may_make_payments_vacate_ob_ch61'),
    path('june_make_payments_vacate_ob_ch61/<id>', branch61.june_make_payments_vacate_ob_ch61, name='june_make_payments_vacate_ob_ch61'),
    path('july_make_payments_vacate_ob_ch61/<id>', branch61.july_make_payments_vacate_ob_ch61, name='july_make_payments_vacate_ob_ch61'),
    path('aug_make_payments_vacate_ob_ch61/<id>', branch61.aug_make_payments_vacate_ob_ch61, name='aug_make_payments_vacate_ob_ch61'),

    path('sept_make_payments_vacate_ob_ch61/<id>', branch61.sept_make_payments_vacate_ob_ch61, name='sept_make_payments_vacate_ob_ch61'),
    path('oct_make_payments_vacate_ob_ch61/<id>', branch61.oct_make_payments_vacate_ob_ch61, name='oct_make_payments_vacate_ob_ch61'),
    path('nov_make_payments_vacate_ob_ch61/<id>', branch61.nov_make_payments_vacate_ob_ch61, name='nov_make_payments_vacate_ob_ch61'),
    path('dec_make_payments_vacate_ob_ch61/<id>', branch61.dec_make_payments_vacate_ob_ch61, name='dec_make_payments_vacate_ob_ch61'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch61/',branch61.detail_guest_general_ob_ch61,name='detail_guest_general_ob_ch61'),

    path('jan_print_ob_ch61/',branch61.jan_print_ob_ch61,name='jan_print_ob_ch61'),
    path('feb_print_ob_ch61/',branch61.feb_print_ob_ch61,name='feb_print_ob_ch61'),
    path('march_print_ob_ch61/',branch61.march_print_ob_ch61,name='march_print_ob_ch61'),
    path('april_print_ob_ch61/',branch61.april_print_ob_ch61,name='april_print_ob_ch61'),

    path('may_print_ob_ch61/',branch61.may_print_ob_ch61,name='may_print_ob_ch61'),
    path('june_print_ob_ch61/',branch61.june_print_ob_ch61,name='june_print_ob_ch61'),
    path('july_print_ob_ch61/', branch61.july_print_ob_ch61, name='july_print_ob_ch61'),
    path('aug_print_ob_ch61/', branch61.aug_print_ob_ch61, name='aug_print_ob_ch61'),

    path('sept_print_ob_ch61/', branch61.sept_print_ob_ch61, name='sept_print_ob_ch61'),
    path('oct_print_ob_ch61/', branch61.oct_print_ob_ch61, name='oct_print_ob_ch61'),
    path('nov_print_ob_ch61/', branch61.nov_print_ob_ch61, name='nov_print_ob_ch61'),
    path('dec_print_ob_ch61/', branch61.dec_print_ob_ch61, name='dec_print_ob_ch61'),

    path('new_year_jan_print_ob_ch61/', branch61.new_year_jan_print_ob_ch61, name='new_year_jan_print_ob_ch61'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch61/', branch61.jan_close_ob_ch61, name='jan_close_ob_ch61'),
    path('jan_close_decision_page_ob_ch61/', branch61.jan_close_decision_page_ob_ch61, name='jan_close_decision_page_ob_ch61'),
    path('feb_close/', branch61.feb_close_ob_ch61, name='feb_close_ob_ch61'),
    path('feb_close_decision_page_ob_ch61/', branch61.feb_close_decision_page_ob_ch61, name='feb_close_decision_page_ob_ch61'),
    path('mar_close_ob_ch61/', branch61.mar_close_ob_ch61, name='mar_close_ob_ch61'),
    path('mar_close_decision_page/', branch61.mar_close_decision_page_ob_ch61, name='mar_close_decision_page_ob_ch61'),
    path('apr_close_ob_ch61/', branch61.apr_close_ob_ch61, name='apr_close_ob_ch61'),
    path('apr_close_decision_page_ob_ch61/', branch61.apr_close_decision_page_ob_ch61, name='apr_close_decision_page_ob_ch61'),

    path('may_close_ob_ch61/', branch61.may_close_ob_ch61, name='may_close_ob_ch61'),
    path('may_close_decision_page_ob_ch61/', branch61.may_close_decision_page_ob_ch61, name='may_close_decision_page_ob_ch61'),
    path('jun_close_ob_ch61/', branch61.jun_close_ob_ch61, name='jun_close_ob_ch61'),
    path('jun_close_decision_page_ob_ch61/', branch61.jun_close_decision_page_ob_ch61, name='jun_close_decision_page_ob_ch61'),
    path('jul_close_ob_ch61/', branch61.jul_close_ob_ch61, name='jul_close_ob_ch61'),
    path('jul_close_decision_page_ob_ch61/', branch61.jul_close_decision_page_ob_ch61, name='jul_close_decision_page_ob_ch61'),
    path('aug_close_ob_ch61/', branch61.aug_close_ob_ch61, name='aug_close_ob_ch61'),
    path('aug_close_decision_page_ob_ch61/', branch61.aug_close_decision_page_ob_ch61, name='aug_close_decision_page_ob_ch61'),

    path('sep_close_ob_ch61/', branch61.sep_close_ob_ch61, name='sep_close_ob_ch61'),
    path('sep_close_decision_page_ob_ch61/', branch61.sep_close_decision_page_ob_ch61, name='sep_close_decision_page_ob_ch61'),
    path('oct_close_ob_ch61/', branch61.oct_close_ob_ch61, name='oct_close_ob_ch61'),
    path('oct_close_decision_page_ob_ch61/', branch61.oct_close_decision_page_ob_ch61, name='oct_close_decision_page_ob_ch61'),
    path('nov_close_ob_ch61/', branch61.nov_close_ob_ch61, name='nov_close_ob_ch61'),
    path('nov_close_decision_page_ob_ch61/', branch61.nov_close_decision_page_ob_ch61, name='nov_close_decision_page_ob_ch61'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch61/',reports61.detailed_report_choose_months_ob_ch61,name='detailed_report_choose_months_ob_ch61'),

    path('jan_details_live_ob_ch61/', reports61.jan_details_live_ob_ch61, name='jan_details_live_ob_ch61'),
    path('jan_print_live_ob_ch61/', reports61.jan_print_live_ob_ch61, name='jan_print_live_ob_ch61'),
    path('feb_details_live_ob_ch61/', reports61.feb_details_live_ob_ch61, name='feb_details_live_ob_ch61'),
    path('feb_print_live_ob_ch61/', reports61.feb_print_live_ob_ch61, name='feb_print_live_ob_ch61'),
    path('march_details_live_ob_ch61/', reports61.march_details_live_ob_ch61, name='march_details_live_ob_ch61'),
    path('march_print_live_ob_ch61/', reports61.march_print_live_ob_ch61, name='march_print_live_ob_ch61'),

    path('april_details_live_ob_ch61/', reports61.april_details_live_ob_ch61, name='april_details_live_ob_ch61'),
    path('april_print_live_ob_ch61/', reports61.april_print_live_ob_ch61, name='april_print_live_ob_ch61'),
    path('may_details_live_ob_ch61/', reports61.may_details_live_ob_ch61, name='may_details_live_ob_ch61'),
    path('may_print_live_ob_ch61/', reports61.may_print_live_ob_ch61, name='may_print_live_ob_ch61'),
    path('june_details_live_ob_ch61/',reports61.june_details_live_ob_ch61,name='june_details_live_ob_ch61'),
    path('june_print_live_ob_ch61/', reports61.june_print_live_ob_ch61, name='june_print_live_ob_ch61'),

    path('july_details_live_ob_ch61/', reports61.july_details_live_ob_ch61, name='july_details_live_ob_ch61'),
    path('july_print_live_ob_ch61/', reports61.july_print_live_ob_ch61, name='july_print_live_ob_ch61'),
    path('auguest_details_live_ob_ch61/', reports61.auguest_details_live_ob_ch61, name='auguest_details_live_ob_ch61'),
    path('auguest_print_live_ob_ch61/', reports61.auguest_print_live_ob_ch61, name='auguest_print_live_ob_ch61'),
    path('sept_details_live_ob_ch61/', reports61.sept_details_live_ob_ch61, name='sept_details_live_ob_ch61'),
    path('sept_print_live_ob_ch61/', reports61.sept_print_live_ob_ch61, name='sept_print_live_ob_ch61'),

    path('october_details_live_ob_ch61/', reports61.october_details_live_ob_ch61, name='october_details_live_ob_ch61'),
    path('october_print_live_ob_ch61/', reports61.october_print_live_ob_ch61, name='october_print_live_ob_ch61'),
    path('nov_details_live_ob_ch61/', reports61.nov_details_live_ob_ch61, name='nov_details_live_ob_ch61'),
    path('nov_print_live_ob_ch61/', reports61.nov_print_live_ob_ch61, name='nov_print_live_ob_ch61'),
    path('dec_details_live_ob_ch61/', reports61.dec_details_live_ob_ch61, name='dec_details_live_ob_ch61'),
    path('dec_print_live_ob_ch61/', reports61.dec_print_live_ob_ch61, name='dec_print_live_ob_ch61'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch61/', reports61.viewall_vaccant_room_ob_ch61, name='viewall_vaccant_room_ob_ch61'),

    path('d_ob_ch61/', branch61.dynamic, name='dynamic'),

    path('manage_bed_ob_ch61/', branch61.manage_bed_ob_ch61, name='manage_bed_ob_ch61'),
    path('manage_new_guest_ob_ch61/', branch61.manage_new_guest_ob_ch61, name='manage_new_guest_ob_ch61'),
    path('manage_update_new_guest_ob_ch61/<id>', branch61.manage_update_new_guest_ob_ch61, name='manage_update_new_guest_ob_ch61'),
    path('manage_update_beds_ob_ch61/<id>', branch61.manage_update_beds_ob_ch61, name='manage_update_beds_ob_ch61'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch61/', branch61.view_all_due_amt_ob_ch61, name='view_all_due_amt_ob_ch61'),
    path('due_amt_mgt_choose_months_ob_ch61/', branch61.due_amt_mgt_choose_months_ob_ch61, name='due_amt_mgt_choose_months_ob_ch61'),

    path('view_jan_account_details_ob_ch61/', branch61.view_jan_account_details_ob_ch61, name='view_jan_account_details_ob_ch61'),
    path('jan_account_mgt_ob_ch61/<id>',branch61.jan_account_mgt_ob_ch61,name='jan_account_mgt_ob_ch61'),
    path('view_feb_account_details_ob_ch61/', branch61.view_feb_account_details_ob_ch61, name='view_feb_account_details_ob_ch61'),
    path('feb_account_mgt_ob_ch61/<id>',branch61.feb_account_mgt_ob_ch61,name='feb_account_mgt_ob_ch61'),
    path('view_march_account_details_ob_ch61/', branch61.view_march_account_details_ob_ch61, name='view_march_account_details_ob_ch61'),
    path('march_account_mgt_ob_ch61/<id>',branch61.march_account_mgt_ob_ch61,name='march_account_mgt_ob_ch61'),
    path('view_april_account_details_ob_ch61/', branch61.view_april_account_details_ob_ch61, name='view_april_account_details_ob_ch61'),
    path('april_account_mgt_ob_ch61/<id>',branch61.april_account_mgt_ob_ch61,name='april_account_mgt_ob_ch61'),

    path('view_may_account_details_ob_ch61/',branch61.view_may_account_details_ob_ch61,name='view_may_account_details_ob_ch61'),
    path('may_account_mgt_ob_ch61/<id>', branch61.may_account_mgt_ob_ch61, name='may_account_mgt_ob_ch61'),
    path('view_june_account_details_ob_ch61/', branch61.view_june_account_details_ob_ch61, name='view_june_account_details_ob_ch61'),
    path('june_account_mgt_ob_ch61/<id>',branch61.june_account_mgt_ob_ch61,name='june_account_mgt_ob_ch61'),
    path('view_july_account_details_ob_ch61/', branch61.view_july_account_details_ob_ch61, name='view_july_account_details_ob_ch61'),
    path('july_account_mgt_ob_ch61/<id>',branch61.july_account_mgt_ob_ch61,name='july_account_mgt_ob_ch61'),
    path('view_auguest_account_details_ob_ch61/', branch61.view_auguest_account_details_ob_ch61, name='view_auguest_account_details_ob_ch61'),
    path('auguest_account_mgt_ob_ch61/<id>',branch61.auguest_account_mgt_ob_ch61,name='auguest_account_mgt_ob_ch61'),

    path('view_sept_account_details_ob_ch61/', branch61.view_sept_account_details_ob_ch61, name='view_sept_account_details_ob_ch61'),
    path('sept_account_mgt_ob_ch61/<id>',branch61.sept_account_mgt_ob_ch61,name='sept_account_mgt_ob_ch61'),
    path('view_october_account_details_ob_ch61/', branch61.view_october_account_details_ob_ch61, name='view_october_account_details_ob_ch61'),
    path('october_account_mgt_ob_ch61/<id>',branch61.october_account_mgt_ob_ch61,name='october_account_mgt_ob_ch61'),
    path('view_nov_account_details_ob_ch61/', branch61.view_nov_account_details_ob_ch61, name='view_nov_account_details_ob_ch61'),
    path('nov_account_mgt_ob_ch61/<id>',branch61.nov_account_mgt_ob_ch61,name='nov_account_mgt_ob_ch61'),
    path('view_dec_account_details_ob_ch61/', branch61.view_dec_account_details_ob_ch61, name='view_dec_account_details_ob_ch61'),
    path('dec_account_mgt_ob_ch61/<id>',branch61.dec_account_mgt_ob_ch61,name='dec_account_mgt_ob_ch61'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch61', admin_dashboard_calculations_br61.monthly_details_due_ob_ch61, name='monthly_details_due_ob_ch61'),
    path('monthly_collection_details_ob_ch61/', admin_dashboard_calculations_br61.monthly_collection_details_ob_ch61, name='monthly_collection_details_ob_ch61'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch61/',branch61.guest_all_ob_ch61,name='guest_all_ob_ch61'),






#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************

path('accounts_dash_board_ob_ch61/',accounts61.accounts_dash_board_ob_ch61,name='accounts_dash_board_ob_ch61'),

]

