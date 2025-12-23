from django.urls import path, include

from . import admin_branch22
from . import admin_branch22
from . import branch22
from . import reports22
from . import payment22
from . import admin_dashboard_calculations_br22
from . import accounts22
from . import branch_settings22

urlpatterns = [

    path('branch1_dashboard_ob_ch22/', branch22.branch1_dashboard_ob_ch22, name='branch1_dashboard_ob_ch22'),
    path('branch1_dashboard22/',branch22.branch1_dashboard22,name='branch1_dashboard22'),
    path('user_dashboard_calculations_ob_ch22/',branch22.user_dashboard_calculations_ob_ch22,name='user_dashboard_calculations_ob_ch22'),

    path('background_ob_ch22',branch22.background_ob_ch22,name='background_ob_ch22'),
    path('background_regi_ob_ch22',branch22.background_regi_ob_ch22,name='background_regi_ob_ch22'),
    path('custom_background_regi_ob_ch22',branch22.custom_background_regi_ob_ch22,name='custom_background_regi_ob_ch22'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch22/',admin_branch22.branch1_room_create_regi_ob_ch22,name='branch1_room_create_regi_ob_ch22'),
    path('view_all_room_ob_ch22/',admin_branch22.view_all_room_ob_ch22,name='view_all_room_ob_ch22'),
    path('delete_room_ob_ch22/<id>',admin_branch22.delete_room_ob_ch22,name='delete_room_ob_ch22'),

    path('branch1_room_create_ob_ch22/',admin_branch22.branch1_room_create_ob_ch22,name='branch1_room_create_ob_ch22'),

    path('multiple_branch1_room_create_regi22/',admin_branch22.multiple_branch1_room_create_regi22,name='multiple_branch1_room_create_regi22'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch22/', admin_branch22.pg1_bed_create_regi_ob_ch22, name='pg1_bed_create_regi_ob_ch22'),
    path('pg1_view_all_beds_ob_ch22/', admin_branch22.pg1_view_all_beds_ob_ch22, name='pg1_view_all_beds_ob_ch22'),
    path('delete_bed_ob_ch22/<id>', admin_branch22.delete_bed_ob_ch22, name='delete_bed_ob_ch22'),

    path('pg1_bed_create_ob_ch22/', admin_branch22.pg1_bed_create_ob_ch22, name='pg1_bed_create_ob_ch22'),

    path('single_pg1_bed_create_regi_ob_ch22/',admin_branch22.single_pg1_bed_create_regi_ob_ch22,name='single_pg1_bed_create_regi_ob_ch22'),
    path('update_bed_basic_details_ob_ch22/<id>',admin_branch22.update_bed_basic_details_ob_ch22, name='update_bed_basic_details_ob_ch22'),

    path('multiple_single_pg1_bed_create_regi22/',admin_branch22.multiple_single_pg1_bed_create_regi22,name='multiple_single_pg1_bed_create_regi22'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch22/<id>',branch22.br1_admit_guest_ob_ch22,name='br1_admit_guest_ob_ch22'),
    path('view_all_new_guest_ob_ch22/',branch22.view_all_new_guest_ob_ch22,name='view_all_new_guest_ob_ch22'),
    path('update_br1_admit_guest_ob_ch22/<id>',branch22.update_br1_admit_guest_ob_ch22,name='update_br1_admit_guest_ob_ch22'),
    path('vacate_br1_guest_ob_ch22/<id>',branch22.vacate_br1_guest_ob_ch22,name='vacate_br1_guest_ob_ch22'),

    path('active_guest_details_ob_ch22/<guest_code>',branch22.active_guest_details_ob_ch22,name='active_guest_details_ob_ch22'),
    path('view_all_guest_ob_ch22/',branch22.view_all_guest_ob_ch22,name='view_all_guest_ob_ch22'),
    path('shift_guest_ob_ch22/<id>',branch22.shift_guest_ob_ch22,name='shift_guest_ob_ch22'),
    path('shift_guest_regi_ob_ch22/',branch22.shift_guest_regi_ob_ch22,name='shift_guest_regi_ob_ch22'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch22/',branch22.update_all_rent_ob_ch22,name='update_all_rent_ob_ch22'),

    path('multiple_br1_admit_guest22/<id>',branch22.multiple_br1_admit_guest22,name='multiple_br1_admit_guest22'),

#guest end here


##################################
#_ADVANCE_ob_ch22 START HERE
################################


    path('choose_months_advance_ob_ch22/',branch22.choose_months_advance_ob_ch22,name='choose_months_advance_ob_ch22'),

    path('jan_advance_ob_ch22/', branch22.jan_advance_ob_ch22, name='jan_advance_ob_ch22'),
    path('jan_make_payments_advance_ob_ch22/<id>', branch22.jan_make_payments_advance_ob_ch22,name='jan_make_payments_advance_ob_ch22'),
    path('feb_advance_ob_ch22/', branch22.feb_advance_ob_ch22, name='feb_advance_ob_ch22'),
    path('feb_make_payments_advance_ob_ch22/<id>', branch22.feb_make_payments_advance_ob_ch22,name='feb_make_payments_advance_ob_ch22'),
    path('march_advance_ob_ch22/', branch22.march_advance_ob_ch22, name='march_advance_ob_ch22'),
    path('march_make_payments_advance_ob_ch22/<id>', branch22.march_make_payments_advance_ob_ch22,name='march_make_payments_advance_ob_ch22'),
    path('april_advance_ob_ch22/', branch22.april_advance_ob_ch22, name='april_advance_ob_ch22'),
    path('april_make_payments_advance_ob_ch22/<id>', branch22.april_make_payments_advance_ob_ch22, name='april_make_payments_advance_ob_ch22'),

    path('may_advance_ob_ch22/',branch22.may_advance_ob_ch22,name='may_advance_ob_ch22'),
    path('may_make_payments_advance_ob_ch22/<id>', branch22.may_make_payments_advance_ob_ch22, name='may_make_payments_advance_ob_ch22'),
    path('june_advance_ob_ch22/',branch22.june_advance_ob_ch22,name='june_advance_ob_ch22'),
    path('june_make_payments_advance_ob_ch22/<id>', branch22.june_make_payments_advance_ob_ch22, name='june_make_payments_advance_ob_ch22'),
    path('july_advance_ob_ch22/',branch22.july_advance_ob_ch22,name='july_advance_ob_ch22'),
    path('july_make_payments_advance_ob_ch22/<id>', branch22.july_make_payments_advance_ob_ch22, name='july_make_payments_advance_ob_ch22'),
    path('auguest_advance_ob_ch22/', branch22.auguest_advance_ob_ch22, name='auguest_advance_ob_ch22'),
    path('auguest_make_payments_advance_ob_ch22/<id>', branch22.auguest_make_payments_advance_ob_ch22, name='auguest_make_payments_advance_ob_ch22'),

    path('sept_advance_ob_ch22/', branch22.sept_advance_ob_ch22, name='sept_advance_ob_ch22'),
    path('sept_make_payments_advance_ob_ch22/<id>', branch22.sept_make_payments_advance_ob_ch22,name='sept_make_payments_advance_ob_ch22'),
    path('october_advance_ob_ch22/', branch22.october_advance_ob_ch22, name='october_advance_ob_ch22'),
    path('october_make_payments_advance_ob_ch22/<id>', branch22.october_make_payments_advance_ob_ch22, name='october_make_payments_advance_ob_ch22'),
    path('nov_advance_ob_ch22/', branch22.nov_advance_ob_ch22, name='nov_advance_ob_ch22'),
    path('nov_make_payments_advance_ob_ch22/<id>', branch22.nov_make_payments_advance_ob_ch22,name='nov_make_payments_advance_ob_ch22'),
    path('dec_advance_ob_ch22/', branch22.dec_advance_ob_ch22, name='dec_advance_ob_ch22'),
    path('dec_make_payments_advance_ob_ch22/<id>', branch22.dec_make_payments_advance_ob_ch22, name='dec_make_payments_advance_ob_ch22'),



##################################
#_ADVANCE_ob_ch22 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch22/',branch22.choose_months_ob_ch22,name='choose_months_ob_ch22'),

    path('jan_ob_ch22/',branch22.jan_ob_ch22,name='jan_ob_ch22'),
    path('jan_manke_payments_ob_ch22/<id>',branch22.jan_manke_payments_ob_ch22,name='jan_manke_payments_ob_ch22'),

    path('feb_ob_ch22/',branch22.feb_ob_ch22,name='feb_ob_ch22'),
    path('feb_manke_payments_ob_ch22/<id>',branch22.feb_manke_payments_ob_ch22,name='feb_manke_payments_ob_ch22'),

    path('march_ob_ch22/',branch22.march_ob_ch22,name='march_ob_ch22'),
    path('march_manke_payments_ob_ch22/<id>',branch22.march_manke_payments_ob_ch22,name='march_manke_payments_ob_ch22'),

    path('april_ob_ch22/',branch22.april_ob_ch22,name='april_ob_ch22'),
    path('april_make_payments_ob_ch22/<id>',branch22.april_make_payments_ob_ch22,name='april_make_payments_ob_ch22'),

    path('may_ob_ch22/',branch22.may_ob_ch22,name='may_ob_ch22'),
    path('may_make_payments_ob_ch22/<id>',branch22.may_make_payments_ob_ch22,name='may_make_payments_ob_ch22'),

    path('june_ob_ch22/',branch22.june_ob_ch22,name='june_ob_ch22'),
    path('june_make_payments_ob_ch22/<id>',branch22.june_make_payments_ob_ch22,name='june_make_payments_ob_ch22'),

    path('july_ob_ch22/',branch22.july_ob_ch22,name='july_ob_ch22'),
    path('july_make_payments_ob_ch22/<id>',branch22.july_make_payments_ob_ch22,name='july_make_payments_ob_ch22'),

    path('aug_ob_ch22/',branch22.aug_ob_ch22,name='aug_ob_ch22'),
    path('aug_make_payments_ob_ch22/<id>',branch22.aug_make_payments_ob_ch22,name='aug_make_payments_ob_ch22'),

    path('sept_ob_ch22/',branch22.sept_ob_ch22,name='sept_ob_ch22'),
    path('sept_make_payments_ob_ch22/<id>',branch22.sept_make_payments_ob_ch22,name='sept_make_payments_ob_ch22'),

    path('oct_ob_ch22/',branch22.oct_ob_ch22,name='oct_ob_ch22'),
    path('oct_make_payments_ob_ch22/<id>',branch22.oct_make_payments_ob_ch22,name='oct_make_payments_ob_ch22'),

    path('nov_ob_ch22/',branch22.nov_ob_ch22,name='nov_ob_ch22'),
    path('nov_make_payments_ob_ch22/<id>',branch22.nov_make_payments_ob_ch22,name='nov_make_payments_ob_ch22'),

    path('dec_ob_ch22/',branch22.dec_ob_ch22,name='dec_ob_ch22'),
    path('dec_make_payments_ob_ch22/<id>',branch22.dec_make_payments_ob_ch22,name='dec_make_payments_ob_ch22'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch22/', payment22.choose_user_ob_ch22, name='choose_user_ob_ch22'),
    path('payment_user_details_ob_ch22/<id>', payment22.payment_user_details_ob_ch22, name='payment_user_details_ob_ch22'),
    path('close_choose_user_ob_ch22/<id>',payment22.close_choose_user_ob_ch22,name='close_choose_user_ob_ch22'),

    path('monthly_jan_make_payments_ob_ch22/<id>', payment22.monthly_jan_make_payments_ob_ch22, name='monthly_jan_make_payments_ob_ch22'),
    path('monthly_feb_make_payments_ob_ch22/<id>', payment22.monthly_feb_make_payments_ob_ch22, name='monthly_feb_make_payments_ob_ch22'),
    path('monthly_march_make_payments_ob_ch22/<id>', payment22.monthly_march_make_payments_ob_ch22, name='monthly_march_make_payments_ob_ch22'),
    path('monthly_april_make_payments_ob_ch22/<id>', payment22.monthly_april_make_payments_ob_ch22, name='monthly_april_make_payments_ob_ch22'),
    path('monthly_may_make_payments_ob_ch22/<id>', payment22.monthly_may_make_payments_ob_ch22, name='monthly_may_make_payments_ob_ch22'),
    path('monthly_june_make_payments_ob_ch22/<id>', payment22.monthly_june_make_payments_ob_ch22, name='monthly_june_make_payments_ob_ch22'),

    path('monthly_july_make_payments_ob_ch22/<id>', payment22.monthly_july_make_payments_ob_ch22, name='monthly_july_make_payments_ob_ch22'),
    path('monthly_aug_make_payments_ob_ch22/<id>', payment22.monthly_aug_make_payments_ob_ch22, name='monthly_aug_make_payments_ob_ch22'),
    path('monthly_sept_make_payments_ob_ch22/<id>', payment22.monthly_sept_make_payments_ob_ch22, name='monthly_sept_make_payments_ob_ch22'),
    path('monthly_oct_make_payments_ob_ch22/<id>', payment22.monthly_oct_make_payments_ob_ch22, name='monthly_oct_make_payments_ob_ch22'),
    path('monthly_nov_make_payments_ob_ch22/<id>', payment22.monthly_nov_make_payments_ob_ch22, name='monthly_nov_make_payments_ob_ch22'),
    path('monthly_dec_make_payments_ob_ch22/<id>', payment22.monthly_dec_make_payments_ob_ch22, name='monthly_dec_make_payments_ob_ch22'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch22/',branch22.unpaid_rent_choose_months_ob_ch22,name='unpaid_rent_choose_months_ob_ch22'),

    path('jan_unpaid_rent_ob_ch22/', branch22.jan_unpaid_rent_ob_ch22, name='jan_unpaid_rent_ob_ch22'),
    path('table_jan_unpaid_rent_ob_ch22/', branch22.table_jan_unpaid_rent_ob_ch22, name='table_jan_unpaid_rent_ob_ch22'),
    path('feb_unpaid_rent_ob_ch22/', branch22.feb_unpaid_rent_ob_ch22, name='feb_unpaid_rent_ob_ch22'),
    path('table_feb_unpaid_rent_ob_ch22/', branch22.table_feb_unpaid_rent_ob_ch22, name='table_feb_unpaid_rent_ob_ch22'),
    path('mar_unpaid_rent_ob_ch22/', branch22.mar_unpaid_rent_ob_ch22, name='mar_unpaid_rent_ob_ch22'),
    path('table_mar_unpaid_rent_ob_ch22/', branch22.table_mar_unpaid_rent_ob_ch22, name='table_mar_unpaid_rent_ob_ch22'),
    path('april_unpaid_rent_ob_ch22/', branch22.april_unpaid_rent_ob_ch22, name='april_unpaid_rent_ob_ch22'),
    path('table_april_unpaid_rent_ob_ch22/', branch22.table_april_unpaid_rent_ob_ch22, name='table_april_unpaid_rent_ob_ch22'),

    path('may_unpaid_rent_ob_ch22/', branch22.may_unpaid_rent_ob_ch22, name='may_unpaid_rent_ob_ch22'),
    path('table_may_unpaid_rent_ob_ch22/', branch22.table_may_unpaid_rent_ob_ch22, name='table_may_unpaid_rent_ob_ch22'),
    path('june_unpaid_rent_ob_ch22/', branch22.june_unpaid_rent_ob_ch22, name='june_unpaid_rent_ob_ch22'),
    path('table_june_unpaid_rent_ob_ch22/', branch22.table_june_unpaid_rent_ob_ch22, name='table_june_unpaid_rent_ob_ch22'),
    path('july_unpaid_rent_ob_ch22/', branch22.july_unpaid_rent_ob_ch22, name='july_unpaid_rent_ob_ch22'),
    path('table_july_unpaid_rent_ob_ch22',branch22.table_july_unpaid_rent_ob_ch22,name='table_july_unpaid_rent_ob_ch22'),
    path('aug_unpaid_rent_ob_ch22/', branch22.aug_unpaid_rent_ob_ch22, name='aug_unpaid_rent_ob_ch22'),
    path('table_aug_unpaid_rent_ob_ch22/',branch22.table_aug_unpaid_rent_ob_ch22,name='table_aug_unpaid_rent_ob_ch22'),

    path('sept_unpaid_rent_ob_ch22/', branch22.sept_unpaid_rent_ob_ch22, name='sept_unpaid_rent_ob_ch22'),
    path('table_sept_unpaid_rent_ob_ch22/', branch22.table_sept_unpaid_rent_ob_ch22, name='table_sept_unpaid_rent_ob_ch22'),
    path('oct_unpaid_rent_ob_ch22/', branch22.oct_unpaid_rent_ob_ch22, name='oct_unpaid_rent_ob_ch22'),
    path('table_oct_unpaid_rent_ob_ch22/', branch22.table_oct_unpaid_rent_ob_ch22, name='table_oct_unpaid_rent_ob_ch22'),
    path('nov_unpaid_rent_ob_ch22/', branch22.nov_unpaid_rent_ob_ch22, name='nov_unpaid_rent_ob_ch22'),
    path('table_nov_unpaid_rent_ob_ch22/', branch22.table_nov_unpaid_rent_ob_ch22, name='table_nov_unpaid_rent_ob_ch22'),
    path('dec_unpaid_rent_ob_ch22/', branch22.dec_unpaid_rent_ob_ch22, name='dec_unpaid_rent_ob_ch22'),
    path('table_dec_unpaid_rent_ob_ch22/', branch22.table_dec_unpaid_rent_ob_ch22, name='table_dec_unpaid_rent_ob_ch22'),

    path('details_of_unpaid_guests_ob_ch22/<id>',branch22.details_of_unpaid_guests_ob_ch22,name='details_of_unpaid_guests_ob_ch22'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch22/',branch22.paid_rent_choose_months_ob_ch22,name='paid_rent_choose_months_ob_ch22'),
    path('partially_paid_guest_choose_months_ob_ch22/',reports22.partially_paid_guest_choose_months_ob_ch22,name='partially_paid_guest_choose_months_ob_ch22'),

    path('jan_paid_rent_ob_ch22/', branch22.jan_paid_rent_ob_ch22, name='jan_paid_rent_ob_ch22'),
    path('table_jan_paid_rent_ob_ch22/', branch22.table_jan_paid_rent_ob_ch22, name='table_jan_paid_rent_ob_ch22'),
    path('jan_full_paid_guest_ob_ch22/', reports22.jan_full_paid_guest_ob_ch22, name='jan_full_paid_guest_ob_ch22'),
    path('jan_partially_paid_guest_ob_ch22/', reports22.jan_partially_paid_guest_ob_ch22, name='jan_partially_paid_guest_ob_ch22'),
    path('table_jan_partially_paid_guest_ob_ch22/', reports22.table_jan_partially_paid_guest_ob_ch22,name='table_jan_partially_paid_guest_ob_ch22'),

    path('feb_paid_rent_ob_ch22/', branch22.feb_paid_rent_ob_ch22, name='feb_paid_rent_ob_ch22'),
    path('table_feb_paid_rent_ob_ch22/', branch22.table_feb_paid_rent_ob_ch22, name='table_feb_paid_rent_ob_ch22'),
    path('feb_full_paid_guest_ob_ch22/', reports22.feb_full_paid_guest_ob_ch22, name='feb_full_paid_guest_ob_ch22'),
    path('feb_partially_paid_guest_ob_ch22/', reports22.feb_partially_paid_guest_ob_ch22, name='feb_partially_paid_guest_ob_ch22'),
    path('table_feb_partially_paid_guest_ob_ch22/', reports22.table_feb_partially_paid_guest_ob_ch22,name='table_feb_partially_paid_guest_ob_ch22'),

    path('mar_paid_rent_ob_ch22/', branch22.mar_paid_rent_ob_ch22, name='mar_paid_rent_ob_ch22'),
    path('table_mar_paid_rent_ob_ch22/', branch22.table_mar_paid_rent_ob_ch22, name='table_mar_paid_rent_ob_ch22'),
    path('march_full_paid_guest_ob_ch22/', reports22.march_full_paid_guest_ob_ch22, name='march_full_paid_guest_ob_ch22'),
    path('march_partially_paid_guest_ob_ch22/', reports22.march_partially_paid_guest_ob_ch22, name='march_partially_paid_guest_ob_ch22'),
    path('table_march_partially_paid_guest_ob_ch22/', reports22.table_march_partially_paid_guest_ob_ch22,name='table_march_partially_paid_guest_ob_ch22'),

    path('april_paid_rent_ob_ch22/', branch22.april_paid_rent_ob_ch22, name='april_paid_rent_ob_ch22'),
    path('table_april_paid_rent_ob_ch22/', branch22.table_april_paid_rent_ob_ch22, name='table_april_paid_rent_ob_ch22'),
    path('april_full_paid_guest_ob_ch22/', reports22.april_full_paid_guest_ob_ch22, name='april_full_paid_guest_ob_ch22'),
    path('april_partially_paid_guest_ob_ch22/', reports22.april_partially_paid_guest_ob_ch22, name='april_partially_paid_guest_ob_ch22'),
    path('table_april_partially_paid_guest_ob_ch22/', reports22.table_april_partially_paid_guest_ob_ch22,name='table_april_partially_paid_guest_ob_ch22'),

    path('may_paid_rent_ob_ch22/', branch22.may_paid_rent_ob_ch22, name='may_paid_rent_ob_ch22'),
    path('table_may_paid_rent_ob_ch22/', branch22.table_may_paid_rent_ob_ch22, name='table_may_paid_rent_ob_ch22'),
    path('may_full_paid_guest_ob_ch22/', reports22.may_full_paid_guest_ob_ch22, name='may_full_paid_guest_ob_ch22'),
    path('may_partially_paid_guest_ob_ch22/', reports22.may_partially_paid_guest_ob_ch22, name='may_partially_paid_guest_ob_ch22'),
    path('table_may_partially_paid_guest_ob_ch22/', reports22.table_may_partially_paid_guest_ob_ch22, name='table_may_partially_paid_guest_ob_ch22'),

    path('june_paid_rent_ob_ch22/', branch22.june_paid_rent_ob_ch22, name='june_paid_rent_ob_ch22'),
    path('table_june_paid_rent_ob_ch22/', branch22.table_june_paid_rent_ob_ch22, name='table_june_paid_rent_ob_ch22'),
    path('june_full_paid_guest_ob_ch22/', reports22.june_full_paid_guest_ob_ch22, name='june_full_paid_guest_ob_ch22'),
    path('june_partially_paid_guest_ob_ch22/', reports22.june_partially_paid_guest_ob_ch22, name='june_partially_paid_guest_ob_ch22'),
    path('table_june_partially_paid_guest_ob_ch22/', reports22.table_june_partially_paid_guest_ob_ch22, name='table_june_partially_paid_guest_ob_ch22'),

    path('july_paid_rent_ob_ch22/', branch22.july_paid_rent_ob_ch22, name='july_paid_rent_ob_ch22'),
    path('table_july_paid_rent_ob_ch22/', branch22.table_july_paid_rent_ob_ch22, name='table_july_paid_rent_ob_ch22'),
    path('july_full_paid_guest_ob_ch22/', reports22.july_full_paid_guest_ob_ch22, name='july_full_paid_guest_ob_ch22'),
    path('july_partially_paid_guest_ob_ch22/', reports22.july_partially_paid_guest_ob_ch22, name='july_partially_paid_guest_ob_ch22'),
    path('table_july_partially_paid_guest_ob_ch22/', reports22.table_july_partially_paid_guest_ob_ch22, name='table_july_partially_paid_guest_ob_ch22'),

    path('aug_paid_rent_ob_ch22/', branch22.aug_paid_rent_ob_ch22, name='aug_paid_rent_ob_ch22'),
    path('table_aug_paid_rent_ob_ch22/', branch22.table_aug_paid_rent_ob_ch22, name='table_aug_paid_rent_ob_ch22'),
    path('auguest_full_paid_guest_ob_ch22/', reports22.auguest_full_paid_guest_ob_ch22, name='auguest_full_paid_guest_ob_ch22'),
    path('auguest_partially_paid_guest_ob_ch22/', reports22.auguest_partially_paid_guest_ob_ch22,name='auguest_partially_paid_guest_ob_ch22'),
    path('table_auguest_partially_paid_guest_ob_ch22/', reports22.table_auguest_partially_paid_guest_ob_ch22,name='table_auguest_partially_paid_guest_ob_ch22'),

    path('sept_paid_rent_ob_ch22/', branch22.sept_paid_rent_ob_ch22, name='sept_paid_rent_ob_ch22'),
    path('table_sept_paid_rent_ob_ch22/', branch22.table_sept_paid_rent_ob_ch22, name='table_sept_paid_rent_ob_ch22'),
    path('sept_full_paid_guest_ob_ch22/', reports22.sept_full_paid_guest_ob_ch22, name='sept_full_paid_guest_ob_ch22'),
    path('sept_partially_paid_guest_ob_ch22/', reports22.sept_partially_paid_guest_ob_ch22, name='sept_partially_paid_guest_ob_ch22'),
    path('table_sept_partially_paid_guest_ob_ch22/', reports22.table_sept_partially_paid_guest_ob_ch22,name='table_sept_partially_paid_guest_ob_ch22'),

    path('oct_paid_rent_ob_ch22/', branch22.oct_paid_rent_ob_ch22, name='oct_paid_rent_ob_ch22'),
    path('table_oct_paid_rent_ob_ch22/', branch22.table_oct_paid_rent_ob_ch22, name='table_oct_paid_rent_ob_ch22'),
    path('october_full_paid_guest_ob_ch22/', reports22.october_full_paid_guest_ob_ch22, name='october_full_paid_guest_ob_ch22'),
    path('october_partially_paid_guest_ob_ch22/', reports22.october_partially_paid_guest_ob_ch22,name='october_partially_paid_guest_ob_ch22'),
    path('table_october_partially_paid_guest_ob_ch22/', reports22.table_october_partially_paid_guest_ob_ch22,name='table_october_partially_paid_guest_ob_ch22'),

    path('nov_paid_rent_ob_ch22/', branch22.nov_paid_rent_ob_ch22, name='nov_paid_rent_ob_ch22'),
    path('table_nov_paid_rent_ob_ch22/', branch22.table_nov_paid_rent_ob_ch22, name='table_nov_paid_rent_ob_ch22'),
    path('nov_full_paid_guest_ob_ch22/', reports22.nov_full_paid_guest_ob_ch22, name='nov_full_paid_guest_ob_ch22'),
    path('nov_partially_paid_guest_ob_ch22/', reports22.nov_partially_paid_guest_ob_ch22, name='nov_partially_paid_guest_ob_ch22'),
    path('table_nov_partially_paid_guest_ob_ch22/', reports22.table_nov_partially_paid_guest_ob_ch22,name='table_nov_partially_paid_guest_ob_ch22'),

    path('dec_paid_rent_ob_ch22/', branch22.dec_paid_rent_ob_ch22, name='dec_paid_rent_ob_ch22'),
    path('table_dec_paid_rent_ob_ch22/', branch22.table_dec_paid_rent_ob_ch22, name='table_dec_paid_rent_ob_ch22'),
    path('dec_full_paid_guest_ob_ch22/', reports22.dec_full_paid_guest_ob_ch22, name='dec_full_paid_guest_ob_ch22'),
    path('dec_partially_paid_guest_ob_ch22/', reports22.dec_partially_paid_guest_ob_ch22, name='dec_partially_paid_guest_ob_ch22'),
    path('table_dec_partially_paid_guest_ob_ch22/', reports22.table_dec_partially_paid_guest_ob_ch22,name='table_dec_partially_paid_guest_ob_ch22'),

    path('details_of_paid_guests_ob_ch22/<id>',branch22.details_of_paid_guests_ob_ch22,name='details_of_paid_guests_ob_ch22'),
    path('full_paid_guest_ob_ch22/',reports22.full_paid_guest_ob_ch22,name='full_paid_guest_ob_ch22'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch22/',branch22.viewall_vacate_guest_ob_ch22,name='viewall_vacate_guest_ob_ch22'),
    path('details_of_vacate_guest_ob_ch22/<id>',branch22.details_of_vacate_guest_ob_ch22,name='details_of_vacate_guest_ob_ch22'),
    path('full_vacated_guest_details_ob_ch22',branch22.full_vacated_guest_details_ob_ch22,name='full_vacated_guest_details_ob_ch22'),
    path('full_vacated_guest_table_ob_ch22',branch22.full_vacated_guest_table_ob_ch22,name='full_vacated_guest_table_ob_ch22'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch22/<id>', branch22.jan_manke_payments_vacate_ob_ch22, name='jan_manke_payments_vacate_ob_ch22'),
    path('feb_manke_payments_vacate_ob_ch22/<id>', branch22.feb_manke_payments_vacate_ob_ch22, name='feb_manke_payments_vacate_ob_ch22'),
    path('march_manke_payments_vacate_ob_ch22/<id>', branch22.march_manke_payments_vacate_ob_ch22, name='march_manke_payments_vacate_ob_ch22'),
    path('april_make_payments_vacate_ob_ch22/<id>', branch22.april_make_payments_vacate_ob_ch22, name='april_make_payments_vacate_ob_ch22'),

    path('may_make_payments_vacate_ob_ch22/<id>', branch22.may_make_payments_vacate_ob_ch22, name='may_make_payments_vacate_ob_ch22'),
    path('june_make_payments_vacate_ob_ch22/<id>', branch22.june_make_payments_vacate_ob_ch22, name='june_make_payments_vacate_ob_ch22'),
    path('july_make_payments_vacate_ob_ch22/<id>', branch22.july_make_payments_vacate_ob_ch22, name='july_make_payments_vacate_ob_ch22'),
    path('aug_make_payments_vacate_ob_ch22/<id>', branch22.aug_make_payments_vacate_ob_ch22, name='aug_make_payments_vacate_ob_ch22'),

    path('sept_make_payments_vacate_ob_ch22/<id>', branch22.sept_make_payments_vacate_ob_ch22, name='sept_make_payments_vacate_ob_ch22'),
    path('oct_make_payments_vacate_ob_ch22/<id>', branch22.oct_make_payments_vacate_ob_ch22, name='oct_make_payments_vacate_ob_ch22'),
    path('nov_make_payments_vacate_ob_ch22/<id>', branch22.nov_make_payments_vacate_ob_ch22, name='nov_make_payments_vacate_ob_ch22'),
    path('dec_make_payments_vacate_ob_ch22/<id>', branch22.dec_make_payments_vacate_ob_ch22, name='dec_make_payments_vacate_ob_ch22'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch22/',branch22.detail_guest_general_ob_ch22,name='detail_guest_general_ob_ch22'),

    path('jan_print_ob_ch22/',branch22.jan_print_ob_ch22,name='jan_print_ob_ch22'),
    path('feb_print_ob_ch22/',branch22.feb_print_ob_ch22,name='feb_print_ob_ch22'),
    path('march_print_ob_ch22/',branch22.march_print_ob_ch22,name='march_print_ob_ch22'),
    path('april_print_ob_ch22/',branch22.april_print_ob_ch22,name='april_print_ob_ch22'),

    path('may_print_ob_ch22/',branch22.may_print_ob_ch22,name='may_print_ob_ch22'),
    path('june_print_ob_ch22/',branch22.june_print_ob_ch22,name='june_print_ob_ch22'),
    path('july_print_ob_ch22/', branch22.july_print_ob_ch22, name='july_print_ob_ch22'),
    path('aug_print_ob_ch22/', branch22.aug_print_ob_ch22, name='aug_print_ob_ch22'),

    path('sept_print_ob_ch22/', branch22.sept_print_ob_ch22, name='sept_print_ob_ch22'),
    path('oct_print_ob_ch22/', branch22.oct_print_ob_ch22, name='oct_print_ob_ch22'),
    path('nov_print_ob_ch22/', branch22.nov_print_ob_ch22, name='nov_print_ob_ch22'),
    path('dec_print_ob_ch22/', branch22.dec_print_ob_ch22, name='dec_print_ob_ch22'),

    path('new_year_jan_print_ob_ch22/', branch22.new_year_jan_print_ob_ch22, name='new_year_jan_print_ob_ch22'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch22/', branch22.jan_close_ob_ch22, name='jan_close_ob_ch22'),
    path('jan_close_decision_page_ob_ch22/', branch22.jan_close_decision_page_ob_ch22, name='jan_close_decision_page_ob_ch22'),
    path('feb_close/', branch22.feb_close_ob_ch22, name='feb_close_ob_ch22'),
    path('feb_close_decision_page_ob_ch22/', branch22.feb_close_decision_page_ob_ch22, name='feb_close_decision_page_ob_ch22'),
    path('mar_close_ob_ch22/', branch22.mar_close_ob_ch22, name='mar_close_ob_ch22'),
    path('mar_close_decision_page/', branch22.mar_close_decision_page_ob_ch22, name='mar_close_decision_page_ob_ch22'),
    path('apr_close_ob_ch22/', branch22.apr_close_ob_ch22, name='apr_close_ob_ch22'),
    path('apr_close_decision_page_ob_ch22/', branch22.apr_close_decision_page_ob_ch22, name='apr_close_decision_page_ob_ch22'),

    path('may_close_ob_ch22/', branch22.may_close_ob_ch22, name='may_close_ob_ch22'),
    path('may_close_decision_page_ob_ch22/', branch22.may_close_decision_page_ob_ch22, name='may_close_decision_page_ob_ch22'),
    path('jun_close_ob_ch22/', branch22.jun_close_ob_ch22, name='jun_close_ob_ch22'),
    path('jun_close_decision_page_ob_ch22/', branch22.jun_close_decision_page_ob_ch22, name='jun_close_decision_page_ob_ch22'),
    path('jul_close_ob_ch22/', branch22.jul_close_ob_ch22, name='jul_close_ob_ch22'),
    path('jul_close_decision_page_ob_ch22/', branch22.jul_close_decision_page_ob_ch22, name='jul_close_decision_page_ob_ch22'),
    path('aug_close_ob_ch22/', branch22.aug_close_ob_ch22, name='aug_close_ob_ch22'),
    path('aug_close_decision_page_ob_ch22/', branch22.aug_close_decision_page_ob_ch22, name='aug_close_decision_page_ob_ch22'),

    path('sep_close_ob_ch22/', branch22.sep_close_ob_ch22, name='sep_close_ob_ch22'),
    path('sep_close_decision_page_ob_ch22/', branch22.sep_close_decision_page_ob_ch22, name='sep_close_decision_page_ob_ch22'),
    path('oct_close_ob_ch22/', branch22.oct_close_ob_ch22, name='oct_close_ob_ch22'),
    path('oct_close_decision_page_ob_ch22/', branch22.oct_close_decision_page_ob_ch22, name='oct_close_decision_page_ob_ch22'),
    path('nov_close_ob_ch22/', branch22.nov_close_ob_ch22, name='nov_close_ob_ch22'),
    path('nov_close_decision_page_ob_ch22/', branch22.nov_close_decision_page_ob_ch22, name='nov_close_decision_page_ob_ch22'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch22/',reports22.detailed_report_choose_months_ob_ch22,name='detailed_report_choose_months_ob_ch22'),

    path('jan_details_live_ob_ch22/', reports22.jan_details_live_ob_ch22, name='jan_details_live_ob_ch22'),
    path('jan_print_live_ob_ch22/', reports22.jan_print_live_ob_ch22, name='jan_print_live_ob_ch22'),
    path('feb_details_live_ob_ch22/', reports22.feb_details_live_ob_ch22, name='feb_details_live_ob_ch22'),
    path('feb_print_live_ob_ch22/', reports22.feb_print_live_ob_ch22, name='feb_print_live_ob_ch22'),
    path('march_details_live_ob_ch22/', reports22.march_details_live_ob_ch22, name='march_details_live_ob_ch22'),
    path('march_print_live_ob_ch22/', reports22.march_print_live_ob_ch22, name='march_print_live_ob_ch22'),

    path('april_details_live_ob_ch22/', reports22.april_details_live_ob_ch22, name='april_details_live_ob_ch22'),
    path('april_print_live_ob_ch22/', reports22.april_print_live_ob_ch22, name='april_print_live_ob_ch22'),
    path('may_details_live_ob_ch22/', reports22.may_details_live_ob_ch22, name='may_details_live_ob_ch22'),
    path('may_print_live_ob_ch22/', reports22.may_print_live_ob_ch22, name='may_print_live_ob_ch22'),
    path('june_details_live_ob_ch22/',reports22.june_details_live_ob_ch22,name='june_details_live_ob_ch22'),
    path('june_print_live_ob_ch22/', reports22.june_print_live_ob_ch22, name='june_print_live_ob_ch22'),

    path('july_details_live_ob_ch22/', reports22.july_details_live_ob_ch22, name='july_details_live_ob_ch22'),
    path('july_print_live_ob_ch22/', reports22.july_print_live_ob_ch22, name='july_print_live_ob_ch22'),
    path('auguest_details_live_ob_ch22/', reports22.auguest_details_live_ob_ch22, name='auguest_details_live_ob_ch22'),
    path('auguest_print_live_ob_ch22/', reports22.auguest_print_live_ob_ch22, name='auguest_print_live_ob_ch22'),
    path('sept_details_live_ob_ch22/', reports22.sept_details_live_ob_ch22, name='sept_details_live_ob_ch22'),
    path('sept_print_live_ob_ch22/', reports22.sept_print_live_ob_ch22, name='sept_print_live_ob_ch22'),

    path('october_details_live_ob_ch22/', reports22.october_details_live_ob_ch22, name='october_details_live_ob_ch22'),
    path('october_print_live_ob_ch22/', reports22.october_print_live_ob_ch22, name='october_print_live_ob_ch22'),
    path('nov_details_live_ob_ch22/', reports22.nov_details_live_ob_ch22, name='nov_details_live_ob_ch22'),
    path('nov_print_live_ob_ch22/', reports22.nov_print_live_ob_ch22, name='nov_print_live_ob_ch22'),
    path('dec_details_live_ob_ch22/', reports22.dec_details_live_ob_ch22, name='dec_details_live_ob_ch22'),
    path('dec_print_live_ob_ch22/', reports22.dec_print_live_ob_ch22, name='dec_print_live_ob_ch22'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch22/', reports22.viewall_vaccant_room_ob_ch22, name='viewall_vaccant_room_ob_ch22'),

    path('d_ob_ch22/', branch22.dynamic, name='dynamic'),

    path('manage_bed_ob_ch22/', branch22.manage_bed_ob_ch22, name='manage_bed_ob_ch22'),
    path('manage_new_guest_ob_ch22/', branch22.manage_new_guest_ob_ch22, name='manage_new_guest_ob_ch22'),
    path('manage_update_new_guest_ob_ch22/<id>', branch22.manage_update_new_guest_ob_ch22, name='manage_update_new_guest_ob_ch22'),
    path('manage_update_beds_ob_ch22/<id>', branch22.manage_update_beds_ob_ch22, name='manage_update_beds_ob_ch22'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch22/', branch22.view_all_due_amt_ob_ch22, name='view_all_due_amt_ob_ch22'),
    path('due_amt_mgt_choose_months_ob_ch22/', branch22.due_amt_mgt_choose_months_ob_ch22, name='due_amt_mgt_choose_months_ob_ch22'),

    path('view_jan_account_details_ob_ch22/', branch22.view_jan_account_details_ob_ch22, name='view_jan_account_details_ob_ch22'),
    path('jan_account_mgt_ob_ch22/<id>',branch22.jan_account_mgt_ob_ch22,name='jan_account_mgt_ob_ch22'),
    path('view_feb_account_details_ob_ch22/', branch22.view_feb_account_details_ob_ch22, name='view_feb_account_details_ob_ch22'),
    path('feb_account_mgt_ob_ch22/<id>',branch22.feb_account_mgt_ob_ch22,name='feb_account_mgt_ob_ch22'),
    path('view_march_account_details_ob_ch22/', branch22.view_march_account_details_ob_ch22, name='view_march_account_details_ob_ch22'),
    path('march_account_mgt_ob_ch22/<id>',branch22.march_account_mgt_ob_ch22,name='march_account_mgt_ob_ch22'),
    path('view_april_account_details_ob_ch22/', branch22.view_april_account_details_ob_ch22, name='view_april_account_details_ob_ch22'),
    path('april_account_mgt_ob_ch22/<id>',branch22.april_account_mgt_ob_ch22,name='april_account_mgt_ob_ch22'),

    path('view_may_account_details_ob_ch22/',branch22.view_may_account_details_ob_ch22,name='view_may_account_details_ob_ch22'),
    path('may_account_mgt_ob_ch22/<id>', branch22.may_account_mgt_ob_ch22, name='may_account_mgt_ob_ch22'),
    path('view_june_account_details_ob_ch22/', branch22.view_june_account_details_ob_ch22, name='view_june_account_details_ob_ch22'),
    path('june_account_mgt_ob_ch22/<id>',branch22.june_account_mgt_ob_ch22,name='june_account_mgt_ob_ch22'),
    path('view_july_account_details_ob_ch22/', branch22.view_july_account_details_ob_ch22, name='view_july_account_details_ob_ch22'),
    path('july_account_mgt_ob_ch22/<id>',branch22.july_account_mgt_ob_ch22,name='july_account_mgt_ob_ch22'),
    path('view_auguest_account_details_ob_ch22/', branch22.view_auguest_account_details_ob_ch22, name='view_auguest_account_details_ob_ch22'),
    path('auguest_account_mgt_ob_ch22/<id>',branch22.auguest_account_mgt_ob_ch22,name='auguest_account_mgt_ob_ch22'),

    path('view_sept_account_details_ob_ch22/', branch22.view_sept_account_details_ob_ch22, name='view_sept_account_details_ob_ch22'),
    path('sept_account_mgt_ob_ch22/<id>',branch22.sept_account_mgt_ob_ch22,name='sept_account_mgt_ob_ch22'),
    path('view_october_account_details_ob_ch22/', branch22.view_october_account_details_ob_ch22, name='view_october_account_details_ob_ch22'),
    path('october_account_mgt_ob_ch22/<id>',branch22.october_account_mgt_ob_ch22,name='october_account_mgt_ob_ch22'),
    path('view_nov_account_details_ob_ch22/', branch22.view_nov_account_details_ob_ch22, name='view_nov_account_details_ob_ch22'),
    path('nov_account_mgt_ob_ch22/<id>',branch22.nov_account_mgt_ob_ch22,name='nov_account_mgt_ob_ch22'),
    path('view_dec_account_details_ob_ch22/', branch22.view_dec_account_details_ob_ch22, name='view_dec_account_details_ob_ch22'),
    path('dec_account_mgt_ob_ch22/<id>',branch22.dec_account_mgt_ob_ch22,name='dec_account_mgt_ob_ch22'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch22', admin_dashboard_calculations_br22.monthly_details_due_ob_ch22, name='monthly_details_due_ob_ch22'),
    path('monthly_collection_details_ob_ch22/', admin_dashboard_calculations_br22.monthly_collection_details_ob_ch22, name='monthly_collection_details_ob_ch22'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch22/',branch22.guest_all_ob_ch22,name='guest_all_ob_ch22'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category22/', accounts22.view_all_category22, name='view_all_category22'),
    path('create_new_category22/', accounts22.create_new_category22, name='create_new_category22'),
    path('regi_new_category22/', accounts22.regi_new_category22, name='regi_new_category22'),
    path('update_category22/<id>',accounts22.update_category22,name='update_category22'),

    path('delete_category22/<id>', accounts22.delete_category22, name='delete_category22'),
    path('view_all_category_delete22/', accounts22.view_all_category_delete22, name='view_all_category_delete22'),

    path('regi_multiple_new_category22/', accounts22.regi_multiple_new_category22, name='regi_multiple_new_category22'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items22/', accounts22.view_all_items22, name='view_all_items22'),
    path('create_new_item22/', accounts22.create_new_item22, name='create_new_item22'),
    path('regi_new_item22/', accounts22.regi_new_item22, name='regi_new_item22'),
    path('delete_item22/<id>',accounts22.delete_item22,name='delete_item22'),
    path('update_item22/<id>', accounts22.update_item22, name='update_item22'),
    path('view_all_items_delete22/',accounts22.view_all_items_delete22,name='view_all_items_delete22'),

    path('regi_multiple_new_item22/', accounts22.regi_multiple_new_item22, name='regi_multiple_new_item22'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger22/', accounts22.view_all_ledger22, name='view_all_ledger22'),
    path('create_new_ledger22/', accounts22.create_new_ledger22, name='create_new_ledger22'),
    path('regi_new_ledger22/', accounts22.regi_new_ledger22, name='regi_new_ledger22'),
    path('delete_ledger22/<id>',accounts22.delete_ledger22,name='delete_ledger22'),
    path('update_ledger22/<id>',accounts22.update_ledger22,name='update_ledger22'),
    path('view_all_ledger_delete22/',accounts22.view_all_ledger_delete22,name='view_all_ledger_delete22'),

    path('regi_multiple_new_ledger22/', accounts22.regi_multiple_new_ledger22, name='regi_multiple_new_ledger22'),

    ##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book22/', accounts22.view_all_accounts_book22, name='view_all_accounts_book22'),
    path('create_new_accounts_book22/', accounts22.create_new_accounts_book22, name='create_new_accounts_book22'),
    path('regi_new_accounts_book22/', accounts22.regi_new_accounts_book22, name='regi_new_accounts_book22'),
    path('update_accounts_book22/<id>',accounts22.update_accounts_book22,name='update_accounts_book22'),
    path('delete_accounts_book22/<id>',accounts22.delete_accounts_book22,name='delete_accounts_book22'),
    path('view_all_accounts_book_delete22/',accounts22.view_all_accounts_book_delete22,name='view_all_accounts_book_delete22'),

    path('regi_multiple_new_accounts_book22/', accounts22.regi_multiple_new_accounts_book22,name='regi_multiple_new_accounts_book22'),

    ##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries22/', accounts22.get_countries22, name='get_countries22'),

    path('in_exp_items_entry22/', accounts22.in_exp_items_entry22, name='in_exp_items_entry22'),
    path('reg_in_exp_items_entry22/', accounts22.reg_in_exp_items_entry22, name='reg_in_exp_items_entry22'),
    path('delete_journal22/<id>',accounts22.delete_journal22,name='delete_journal22'),
    path('update_in_exp_items_entry22/<id>',accounts22.update_in_exp_items_entry22,name='update_in_exp_items_entry22'),
    path('detailed_journal_report22/',accounts22.detailed_journal_report22,name='detailed_journal_report22'),
    path('journal_report_deleted22/',accounts22.journal_report_deleted22,name='journal_report_deleted22'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise22/', accounts22.daily_category_wise22, name='daily_category_wise22'),
    path('monthly_category_based_reports22/',accounts22.monthly_category_based_reports22,name='monthly_category_based_reports22'),
    path('yearly_category_based_reports22/', accounts22.yearly_category_based_reports22,name='yearly_category_based_reports22'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed22/', accounts22.daily_detailed22, name='daily_detailed22'),
    path('monthly_detailed22/',accounts22.monthly_detailed22,name='monthly_detailed22'),
    path('yearly_detailed22/',accounts22.yearly_detailed22,name='yearly_detailed22'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports22/', accounts22.item_based_reports22, name='item_based_reports22'),
    path('daily_item_based_reports22/',accounts22.daily_item_based_reports22,name='daily_item_based_reports22'),
    path('monthly_item_based_reports22/',accounts22.monthly_item_based_reports22,name='monthly_item_based_reports22'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports22/', accounts22.ledger_based_reports22, name='ledger_based_reports22'),
    path('monthly_ledger_based_reports22/', accounts22.monthly_ledger_based_reports22, name='monthly_ledger_based_reports22'),
    path('daily_ledger_based_reports22/',accounts22.daily_ledger_based_reports22,name='daily_ledger_based_reports22'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports22/', accounts22.accounts_book_based_reports22, name='accounts_book_based_reports22'),
    path('daily_accounts_book_based_reports22/',accounts22.daily_accounts_book_based_reports22,name='daily_accounts_book_based_reports22'),
    path('monthly_accounts_book_based_reports22/',accounts22.monthly_accounts_book_based_reports22,name='monthly_accounts_book_based_reports22'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months22/', accounts22.monthly_reports_choose_months22, name='monthly_reports_choose_months22'),
    path('monthly_detailed_daily_in_exp_items_report22/<mo>',accounts22.monthly_detailed_daily_in_exp_items_report22,name='monthly_detailed_daily_in_exp_items_report22'),

    path('single_monthly_reports_choose_months22/', accounts22.single_monthly_reports_choose_months22,name='single_monthly_reports_choose_months22'),
    path('single_monthly_daily_in_exp_items_report22/<mo>',accounts22.single_monthly_daily_in_exp_items_report22,name='single_monthly_daily_in_exp_items_report22'),

    path('accounts_dash_board_ob_ch22/',accounts22.accounts_dash_board_ob_ch22,name='accounts_dash_board_ob_ch22'),
    path('accounts_dash_board22/',accounts22.accounts_dash_board22,name='accounts_dash_board22'),

    path('profit_sharing_choose_months22', accounts22.profit_sharing_choose_months22,name='profit_sharing_choose_months22'),
    path('profit_sharing22/<mo>', accounts22.profit_sharing22, name='profit_sharing22'),
    path('view_share_holders22', accounts22.view_share_holders22, name='view_share_holders22'),
    path('create_share_holders22', accounts22.create_share_holders22, name='create_share_holders22'),
    path('regi_share_holders22', accounts22.regi_share_holders22, name='regi_share_holders22'),
    path('update_share_holders22/<id>', accounts22.update_share_holders22, name='update_share_holders22'),
    path('delete_share_holders22/<id>', accounts22.delete_share_holders22, name='delete_share_holders22'),
    path('view_deleted_share_holders22', accounts22.view_deleted_share_holders22, name='view_deleted_share_holders22'),

    path('regi_multiple_share_holders22', accounts22.regi_multiple_share_holders22, name='regi_multiple_share_holders22'),

    #############BRANCH SETTINGS START HERE ########################

    path('guest_rent_update_ob_ch22/', branch_settings22.guest_rent_update_ob_ch22, name='guest_rent_update_ob_ch22'),

    ############BRANCH SETTINGS END HERE ############################

]

