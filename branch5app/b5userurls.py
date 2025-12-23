from django.urls import path, include

from . import admin_branch5
from . import admin_branch5
from . import branch5
from . import reports5
from . import payment5
from . import admin_dashboard_calculations_br5
from . import accounts5
from . import branch_settings5

urlpatterns = [

    path('branch1_dashboard_ob_ch5/', branch5.branch1_dashboard_ob_ch5, name='branch1_dashboard_ob_ch5'),
    path('branch1_dashboard5/',branch5.branch1_dashboard5,name='branch1_dashboard5'),
    path('user_dashboard_calculations_ob_ch5/',branch5.user_dashboard_calculations_ob_ch5,name='user_dashboard_calculations_ob_ch5'),

    path('background_ob_ch5',branch5.background_ob_ch5,name='background_ob_ch5'),
    path('background_regi_ob_ch5',branch5.background_regi_ob_ch5,name='background_regi_ob_ch5'),
    path('custom_background_regi_ob_ch5',branch5.custom_background_regi_ob_ch5,name='custom_background_regi_ob_ch5'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch5/',admin_branch5.branch1_room_create_regi_ob_ch5,name='branch1_room_create_regi_ob_ch5'),
    path('view_all_room_ob_ch5/',admin_branch5.view_all_room_ob_ch5,name='view_all_room_ob_ch5'),
    path('delete_room_ob_ch5/<id>',admin_branch5.delete_room_ob_ch5,name='delete_room_ob_ch5'),

    path('branch1_room_create_ob_ch5/',admin_branch5.branch1_room_create_ob_ch5,name='branch1_room_create_ob_ch5'),

    path('multiple_branch1_room_create_regi5/',admin_branch5.multiple_branch1_room_create_regi5,name='multiple_branch1_room_create_regi5'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch5/', admin_branch5.pg1_bed_create_regi_ob_ch5, name='pg1_bed_create_regi_ob_ch5'),
    path('pg1_view_all_beds_ob_ch5/', admin_branch5.pg1_view_all_beds_ob_ch5, name='pg1_view_all_beds_ob_ch5'),
    path('delete_bed_ob_ch5/<id>', admin_branch5.delete_bed_ob_ch5, name='delete_bed_ob_ch5'),

    path('pg1_bed_create_ob_ch5/', admin_branch5.pg1_bed_create_ob_ch5, name='pg1_bed_create_ob_ch5'),

    path('single_pg1_bed_create_regi_ob_ch5/',admin_branch5.single_pg1_bed_create_regi_ob_ch5,name='single_pg1_bed_create_regi_ob_ch5'),
    path('update_bed_basic_details_ob_ch5/<id>',admin_branch5.update_bed_basic_details_ob_ch5, name='update_bed_basic_details_ob_ch5'),

    path('multiple_single_pg1_bed_create_regi5/',admin_branch5.multiple_single_pg1_bed_create_regi5,name='multiple_single_pg1_bed_create_regi5'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch5/<id>',branch5.br1_admit_guest_ob_ch5,name='br1_admit_guest_ob_ch5'),
    path('view_all_new_guest_ob_ch5/',branch5.view_all_new_guest_ob_ch5,name='view_all_new_guest_ob_ch5'),
    path('update_br1_admit_guest_ob_ch5/<id>',branch5.update_br1_admit_guest_ob_ch5,name='update_br1_admit_guest_ob_ch5'),
    path('vacate_br1_guest_ob_ch5/<id>',branch5.vacate_br1_guest_ob_ch5,name='vacate_br1_guest_ob_ch5'),

    path('active_guest_details_ob_ch5/<guest_code>',branch5.active_guest_details_ob_ch5,name='active_guest_details_ob_ch5'),
    path('view_all_guest_ob_ch5/',branch5.view_all_guest_ob_ch5,name='view_all_guest_ob_ch5'),
    path('shift_guest_ob_ch5/<id>',branch5.shift_guest_ob_ch5,name='shift_guest_ob_ch5'),
    path('shift_guest_regi_ob_ch5/',branch5.shift_guest_regi_ob_ch5,name='shift_guest_regi_ob_ch5'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch5/',branch5.update_all_rent_ob_ch5,name='update_all_rent_ob_ch5'),

    path('multiple_br1_admit_guest5/<id>',branch5.multiple_br1_admit_guest5,name='multiple_br1_admit_guest5'),

#guest end here


##################################
#_ADVANCE_ob_ch5 START HERE
################################


    path('choose_months_advance_ob_ch5/',branch5.choose_months_advance_ob_ch5,name='choose_months_advance_ob_ch5'),

    path('jan_advance_ob_ch5/', branch5.jan_advance_ob_ch5, name='jan_advance_ob_ch5'),
    path('jan_make_payments_advance_ob_ch5/<id>', branch5.jan_make_payments_advance_ob_ch5,name='jan_make_payments_advance_ob_ch5'),
    path('feb_advance_ob_ch5/', branch5.feb_advance_ob_ch5, name='feb_advance_ob_ch5'),
    path('feb_make_payments_advance_ob_ch5/<id>', branch5.feb_make_payments_advance_ob_ch5,name='feb_make_payments_advance_ob_ch5'),
    path('march_advance_ob_ch5/', branch5.march_advance_ob_ch5, name='march_advance_ob_ch5'),
    path('march_make_payments_advance_ob_ch5/<id>', branch5.march_make_payments_advance_ob_ch5,name='march_make_payments_advance_ob_ch5'),
    path('april_advance_ob_ch5/', branch5.april_advance_ob_ch5, name='april_advance_ob_ch5'),
    path('april_make_payments_advance_ob_ch5/<id>', branch5.april_make_payments_advance_ob_ch5, name='april_make_payments_advance_ob_ch5'),

    path('may_advance_ob_ch5/',branch5.may_advance_ob_ch5,name='may_advance_ob_ch5'),
    path('may_make_payments_advance_ob_ch5/<id>', branch5.may_make_payments_advance_ob_ch5, name='may_make_payments_advance_ob_ch5'),
    path('june_advance_ob_ch5/',branch5.june_advance_ob_ch5,name='june_advance_ob_ch5'),
    path('june_make_payments_advance_ob_ch5/<id>', branch5.june_make_payments_advance_ob_ch5, name='june_make_payments_advance_ob_ch5'),
    path('july_advance_ob_ch5/',branch5.july_advance_ob_ch5,name='july_advance_ob_ch5'),
    path('july_make_payments_advance_ob_ch5/<id>', branch5.july_make_payments_advance_ob_ch5, name='july_make_payments_advance_ob_ch5'),
    path('auguest_advance_ob_ch5/', branch5.auguest_advance_ob_ch5, name='auguest_advance_ob_ch5'),
    path('auguest_make_payments_advance_ob_ch5/<id>', branch5.auguest_make_payments_advance_ob_ch5, name='auguest_make_payments_advance_ob_ch5'),

    path('sept_advance_ob_ch5/', branch5.sept_advance_ob_ch5, name='sept_advance_ob_ch5'),
    path('sept_make_payments_advance_ob_ch5/<id>', branch5.sept_make_payments_advance_ob_ch5,name='sept_make_payments_advance_ob_ch5'),
    path('october_advance_ob_ch5/', branch5.october_advance_ob_ch5, name='october_advance_ob_ch5'),
    path('october_make_payments_advance_ob_ch5/<id>', branch5.october_make_payments_advance_ob_ch5, name='october_make_payments_advance_ob_ch5'),
    path('nov_advance_ob_ch5/', branch5.nov_advance_ob_ch5, name='nov_advance_ob_ch5'),
    path('nov_make_payments_advance_ob_ch5/<id>', branch5.nov_make_payments_advance_ob_ch5,name='nov_make_payments_advance_ob_ch5'),
    path('dec_advance_ob_ch5/', branch5.dec_advance_ob_ch5, name='dec_advance_ob_ch5'),
    path('dec_make_payments_advance_ob_ch5/<id>', branch5.dec_make_payments_advance_ob_ch5, name='dec_make_payments_advance_ob_ch5'),



##################################
#_ADVANCE_ob_ch5 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch5/',branch5.choose_months_ob_ch5,name='choose_months_ob_ch5'),

    path('jan_ob_ch5/',branch5.jan_ob_ch5,name='jan_ob_ch5'),
    path('jan_manke_payments_ob_ch5/<id>',branch5.jan_manke_payments_ob_ch5,name='jan_manke_payments_ob_ch5'),

    path('feb_ob_ch5/',branch5.feb_ob_ch5,name='feb_ob_ch5'),
    path('feb_manke_payments_ob_ch5/<id>',branch5.feb_manke_payments_ob_ch5,name='feb_manke_payments_ob_ch5'),

    path('march_ob_ch5/',branch5.march_ob_ch5,name='march_ob_ch5'),
    path('march_manke_payments_ob_ch5/<id>',branch5.march_manke_payments_ob_ch5,name='march_manke_payments_ob_ch5'),

    path('april_ob_ch5/',branch5.april_ob_ch5,name='april_ob_ch5'),
    path('april_make_payments_ob_ch5/<id>',branch5.april_make_payments_ob_ch5,name='april_make_payments_ob_ch5'),

    path('may_ob_ch5/',branch5.may_ob_ch5,name='may_ob_ch5'),
    path('may_make_payments_ob_ch5/<id>',branch5.may_make_payments_ob_ch5,name='may_make_payments_ob_ch5'),

    path('june_ob_ch5/',branch5.june_ob_ch5,name='june_ob_ch5'),
    path('june_make_payments_ob_ch5/<id>',branch5.june_make_payments_ob_ch5,name='june_make_payments_ob_ch5'),

    path('july_ob_ch5/',branch5.july_ob_ch5,name='july_ob_ch5'),
    path('july_make_payments_ob_ch5/<id>',branch5.july_make_payments_ob_ch5,name='july_make_payments_ob_ch5'),

    path('aug_ob_ch5/',branch5.aug_ob_ch5,name='aug_ob_ch5'),
    path('aug_make_payments_ob_ch5/<id>',branch5.aug_make_payments_ob_ch5,name='aug_make_payments_ob_ch5'),

    path('sept_ob_ch5/',branch5.sept_ob_ch5,name='sept_ob_ch5'),
    path('sept_make_payments_ob_ch5/<id>',branch5.sept_make_payments_ob_ch5,name='sept_make_payments_ob_ch5'),

    path('oct_ob_ch5/',branch5.oct_ob_ch5,name='oct_ob_ch5'),
    path('oct_make_payments_ob_ch5/<id>',branch5.oct_make_payments_ob_ch5,name='oct_make_payments_ob_ch5'),

    path('nov_ob_ch5/',branch5.nov_ob_ch5,name='nov_ob_ch5'),
    path('nov_make_payments_ob_ch5/<id>',branch5.nov_make_payments_ob_ch5,name='nov_make_payments_ob_ch5'),

    path('dec_ob_ch5/',branch5.dec_ob_ch5,name='dec_ob_ch5'),
    path('dec_make_payments_ob_ch5/<id>',branch5.dec_make_payments_ob_ch5,name='dec_make_payments_ob_ch5'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch5/', payment5.choose_user_ob_ch5, name='choose_user_ob_ch5'),
    path('payment_user_details_ob_ch5/<id>', payment5.payment_user_details_ob_ch5, name='payment_user_details_ob_ch5'),
    path('close_choose_user_ob_ch5/<id>',payment5.close_choose_user_ob_ch5,name='close_choose_user_ob_ch5'),

    path('monthly_jan_make_payments_ob_ch5/<id>', payment5.monthly_jan_make_payments_ob_ch5, name='monthly_jan_make_payments_ob_ch5'),
    path('monthly_feb_make_payments_ob_ch5/<id>', payment5.monthly_feb_make_payments_ob_ch5, name='monthly_feb_make_payments_ob_ch5'),
    path('monthly_march_make_payments_ob_ch5/<id>', payment5.monthly_march_make_payments_ob_ch5, name='monthly_march_make_payments_ob_ch5'),
    path('monthly_april_make_payments_ob_ch5/<id>', payment5.monthly_april_make_payments_ob_ch5, name='monthly_april_make_payments_ob_ch5'),
    path('monthly_may_make_payments_ob_ch5/<id>', payment5.monthly_may_make_payments_ob_ch5, name='monthly_may_make_payments_ob_ch5'),
    path('monthly_june_make_payments_ob_ch5/<id>', payment5.monthly_june_make_payments_ob_ch5, name='monthly_june_make_payments_ob_ch5'),

    path('monthly_july_make_payments_ob_ch5/<id>', payment5.monthly_july_make_payments_ob_ch5, name='monthly_july_make_payments_ob_ch5'),
    path('monthly_aug_make_payments_ob_ch5/<id>', payment5.monthly_aug_make_payments_ob_ch5, name='monthly_aug_make_payments_ob_ch5'),
    path('monthly_sept_make_payments_ob_ch5/<id>', payment5.monthly_sept_make_payments_ob_ch5, name='monthly_sept_make_payments_ob_ch5'),
    path('monthly_oct_make_payments_ob_ch5/<id>', payment5.monthly_oct_make_payments_ob_ch5, name='monthly_oct_make_payments_ob_ch5'),
    path('monthly_nov_make_payments_ob_ch5/<id>', payment5.monthly_nov_make_payments_ob_ch5, name='monthly_nov_make_payments_ob_ch5'),
    path('monthly_dec_make_payments_ob_ch5/<id>', payment5.monthly_dec_make_payments_ob_ch5, name='monthly_dec_make_payments_ob_ch5'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch5/',branch5.unpaid_rent_choose_months_ob_ch5,name='unpaid_rent_choose_months_ob_ch5'),

    path('jan_unpaid_rent_ob_ch5/', branch5.jan_unpaid_rent_ob_ch5, name='jan_unpaid_rent_ob_ch5'),
    path('table_jan_unpaid_rent_ob_ch5/', branch5.table_jan_unpaid_rent_ob_ch5, name='table_jan_unpaid_rent_ob_ch5'),
    path('feb_unpaid_rent_ob_ch5/', branch5.feb_unpaid_rent_ob_ch5, name='feb_unpaid_rent_ob_ch5'),
    path('table_feb_unpaid_rent_ob_ch5/', branch5.table_feb_unpaid_rent_ob_ch5, name='table_feb_unpaid_rent_ob_ch5'),
    path('mar_unpaid_rent_ob_ch5/', branch5.mar_unpaid_rent_ob_ch5, name='mar_unpaid_rent_ob_ch5'),
    path('table_mar_unpaid_rent_ob_ch5/', branch5.table_mar_unpaid_rent_ob_ch5, name='table_mar_unpaid_rent_ob_ch5'),
    path('april_unpaid_rent_ob_ch5/', branch5.april_unpaid_rent_ob_ch5, name='april_unpaid_rent_ob_ch5'),
    path('table_april_unpaid_rent_ob_ch5/', branch5.table_april_unpaid_rent_ob_ch5, name='table_april_unpaid_rent_ob_ch5'),

    path('may_unpaid_rent_ob_ch5/', branch5.may_unpaid_rent_ob_ch5, name='may_unpaid_rent_ob_ch5'),
    path('table_may_unpaid_rent_ob_ch5/', branch5.table_may_unpaid_rent_ob_ch5, name='table_may_unpaid_rent_ob_ch5'),
    path('june_unpaid_rent_ob_ch5/', branch5.june_unpaid_rent_ob_ch5, name='june_unpaid_rent_ob_ch5'),
    path('table_june_unpaid_rent_ob_ch5/', branch5.table_june_unpaid_rent_ob_ch5, name='table_june_unpaid_rent_ob_ch5'),
    path('july_unpaid_rent_ob_ch5/', branch5.july_unpaid_rent_ob_ch5, name='july_unpaid_rent_ob_ch5'),
    path('table_july_unpaid_rent_ob_ch5',branch5.table_july_unpaid_rent_ob_ch5,name='table_july_unpaid_rent_ob_ch5'),
    path('aug_unpaid_rent_ob_ch5/', branch5.aug_unpaid_rent_ob_ch5, name='aug_unpaid_rent_ob_ch5'),
    path('table_aug_unpaid_rent_ob_ch5/',branch5.table_aug_unpaid_rent_ob_ch5,name='table_aug_unpaid_rent_ob_ch5'),

    path('sept_unpaid_rent_ob_ch5/', branch5.sept_unpaid_rent_ob_ch5, name='sept_unpaid_rent_ob_ch5'),
    path('table_sept_unpaid_rent_ob_ch5/', branch5.table_sept_unpaid_rent_ob_ch5, name='table_sept_unpaid_rent_ob_ch5'),
    path('oct_unpaid_rent_ob_ch5/', branch5.oct_unpaid_rent_ob_ch5, name='oct_unpaid_rent_ob_ch5'),
    path('table_oct_unpaid_rent_ob_ch5/', branch5.table_oct_unpaid_rent_ob_ch5, name='table_oct_unpaid_rent_ob_ch5'),
    path('nov_unpaid_rent_ob_ch5/', branch5.nov_unpaid_rent_ob_ch5, name='nov_unpaid_rent_ob_ch5'),
    path('table_nov_unpaid_rent_ob_ch5/', branch5.table_nov_unpaid_rent_ob_ch5, name='table_nov_unpaid_rent_ob_ch5'),
    path('dec_unpaid_rent_ob_ch5/', branch5.dec_unpaid_rent_ob_ch5, name='dec_unpaid_rent_ob_ch5'),
    path('table_dec_unpaid_rent_ob_ch5/', branch5.table_dec_unpaid_rent_ob_ch5, name='table_dec_unpaid_rent_ob_ch5'),

    path('details_of_unpaid_guests_ob_ch5/<id>',branch5.details_of_unpaid_guests_ob_ch5,name='details_of_unpaid_guests_ob_ch5'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch5/',branch5.paid_rent_choose_months_ob_ch5,name='paid_rent_choose_months_ob_ch5'),
    path('partially_paid_guest_choose_months_ob_ch5/',reports5.partially_paid_guest_choose_months_ob_ch5,name='partially_paid_guest_choose_months_ob_ch5'),

    path('jan_paid_rent_ob_ch5/', branch5.jan_paid_rent_ob_ch5, name='jan_paid_rent_ob_ch5'),
    path('table_jan_paid_rent_ob_ch5/', branch5.table_jan_paid_rent_ob_ch5, name='table_jan_paid_rent_ob_ch5'),
    path('jan_full_paid_guest_ob_ch5/', reports5.jan_full_paid_guest_ob_ch5, name='jan_full_paid_guest_ob_ch5'),
    path('jan_partially_paid_guest_ob_ch5/', reports5.jan_partially_paid_guest_ob_ch5, name='jan_partially_paid_guest_ob_ch5'),
    path('table_jan_partially_paid_guest_ob_ch5/', reports5.table_jan_partially_paid_guest_ob_ch5,name='table_jan_partially_paid_guest_ob_ch5'),

    path('feb_paid_rent_ob_ch5/', branch5.feb_paid_rent_ob_ch5, name='feb_paid_rent_ob_ch5'),
    path('table_feb_paid_rent_ob_ch5/', branch5.table_feb_paid_rent_ob_ch5, name='table_feb_paid_rent_ob_ch5'),
    path('feb_full_paid_guest_ob_ch5/', reports5.feb_full_paid_guest_ob_ch5, name='feb_full_paid_guest_ob_ch5'),
    path('feb_partially_paid_guest_ob_ch5/', reports5.feb_partially_paid_guest_ob_ch5, name='feb_partially_paid_guest_ob_ch5'),
    path('table_feb_partially_paid_guest_ob_ch5/', reports5.table_feb_partially_paid_guest_ob_ch5,name='table_feb_partially_paid_guest_ob_ch5'),

    path('mar_paid_rent_ob_ch5/', branch5.mar_paid_rent_ob_ch5, name='mar_paid_rent_ob_ch5'),
    path('table_mar_paid_rent_ob_ch5/', branch5.table_mar_paid_rent_ob_ch5, name='table_mar_paid_rent_ob_ch5'),
    path('march_full_paid_guest_ob_ch5/', reports5.march_full_paid_guest_ob_ch5, name='march_full_paid_guest_ob_ch5'),
    path('march_partially_paid_guest_ob_ch5/', reports5.march_partially_paid_guest_ob_ch5, name='march_partially_paid_guest_ob_ch5'),
    path('table_march_partially_paid_guest_ob_ch5/', reports5.table_march_partially_paid_guest_ob_ch5,name='table_march_partially_paid_guest_ob_ch5'),

    path('april_paid_rent_ob_ch5/', branch5.april_paid_rent_ob_ch5, name='april_paid_rent_ob_ch5'),
    path('table_april_paid_rent_ob_ch5/', branch5.table_april_paid_rent_ob_ch5, name='table_april_paid_rent_ob_ch5'),
    path('april_full_paid_guest_ob_ch5/', reports5.april_full_paid_guest_ob_ch5, name='april_full_paid_guest_ob_ch5'),
    path('april_partially_paid_guest_ob_ch5/', reports5.april_partially_paid_guest_ob_ch5, name='april_partially_paid_guest_ob_ch5'),
    path('table_april_partially_paid_guest_ob_ch5/', reports5.table_april_partially_paid_guest_ob_ch5,name='table_april_partially_paid_guest_ob_ch5'),

    path('may_paid_rent_ob_ch5/', branch5.may_paid_rent_ob_ch5, name='may_paid_rent_ob_ch5'),
    path('table_may_paid_rent_ob_ch5/', branch5.table_may_paid_rent_ob_ch5, name='table_may_paid_rent_ob_ch5'),
    path('may_full_paid_guest_ob_ch5/', reports5.may_full_paid_guest_ob_ch5, name='may_full_paid_guest_ob_ch5'),
    path('may_partially_paid_guest_ob_ch5/', reports5.may_partially_paid_guest_ob_ch5, name='may_partially_paid_guest_ob_ch5'),
    path('table_may_partially_paid_guest_ob_ch5/', reports5.table_may_partially_paid_guest_ob_ch5, name='table_may_partially_paid_guest_ob_ch5'),

    path('june_paid_rent_ob_ch5/', branch5.june_paid_rent_ob_ch5, name='june_paid_rent_ob_ch5'),
    path('table_june_paid_rent_ob_ch5/', branch5.table_june_paid_rent_ob_ch5, name='table_june_paid_rent_ob_ch5'),
    path('june_full_paid_guest_ob_ch5/', reports5.june_full_paid_guest_ob_ch5, name='june_full_paid_guest_ob_ch5'),
    path('june_partially_paid_guest_ob_ch5/', reports5.june_partially_paid_guest_ob_ch5, name='june_partially_paid_guest_ob_ch5'),
    path('table_june_partially_paid_guest_ob_ch5/', reports5.table_june_partially_paid_guest_ob_ch5, name='table_june_partially_paid_guest_ob_ch5'),

    path('july_paid_rent_ob_ch5/', branch5.july_paid_rent_ob_ch5, name='july_paid_rent_ob_ch5'),
    path('table_july_paid_rent_ob_ch5/', branch5.table_july_paid_rent_ob_ch5, name='table_july_paid_rent_ob_ch5'),
    path('july_full_paid_guest_ob_ch5/', reports5.july_full_paid_guest_ob_ch5, name='july_full_paid_guest_ob_ch5'),
    path('july_partially_paid_guest_ob_ch5/', reports5.july_partially_paid_guest_ob_ch5, name='july_partially_paid_guest_ob_ch5'),
    path('table_july_partially_paid_guest_ob_ch5/', reports5.table_july_partially_paid_guest_ob_ch5, name='table_july_partially_paid_guest_ob_ch5'),

    path('aug_paid_rent_ob_ch5/', branch5.aug_paid_rent_ob_ch5, name='aug_paid_rent_ob_ch5'),
    path('table_aug_paid_rent_ob_ch5/', branch5.table_aug_paid_rent_ob_ch5, name='table_aug_paid_rent_ob_ch5'),
    path('auguest_full_paid_guest_ob_ch5/', reports5.auguest_full_paid_guest_ob_ch5, name='auguest_full_paid_guest_ob_ch5'),
    path('auguest_partially_paid_guest_ob_ch5/', reports5.auguest_partially_paid_guest_ob_ch5,name='auguest_partially_paid_guest_ob_ch5'),
    path('table_auguest_partially_paid_guest_ob_ch5/', reports5.table_auguest_partially_paid_guest_ob_ch5,name='table_auguest_partially_paid_guest_ob_ch5'),

    path('sept_paid_rent_ob_ch5/', branch5.sept_paid_rent_ob_ch5, name='sept_paid_rent_ob_ch5'),
    path('table_sept_paid_rent_ob_ch5/', branch5.table_sept_paid_rent_ob_ch5, name='table_sept_paid_rent_ob_ch5'),
    path('sept_full_paid_guest_ob_ch5/', reports5.sept_full_paid_guest_ob_ch5, name='sept_full_paid_guest_ob_ch5'),
    path('sept_partially_paid_guest_ob_ch5/', reports5.sept_partially_paid_guest_ob_ch5, name='sept_partially_paid_guest_ob_ch5'),
    path('table_sept_partially_paid_guest_ob_ch5/', reports5.table_sept_partially_paid_guest_ob_ch5,name='table_sept_partially_paid_guest_ob_ch5'),

    path('oct_paid_rent_ob_ch5/', branch5.oct_paid_rent_ob_ch5, name='oct_paid_rent_ob_ch5'),
    path('table_oct_paid_rent_ob_ch5/', branch5.table_oct_paid_rent_ob_ch5, name='table_oct_paid_rent_ob_ch5'),
    path('october_full_paid_guest_ob_ch5/', reports5.october_full_paid_guest_ob_ch5, name='october_full_paid_guest_ob_ch5'),
    path('october_partially_paid_guest_ob_ch5/', reports5.october_partially_paid_guest_ob_ch5,name='october_partially_paid_guest_ob_ch5'),
    path('table_october_partially_paid_guest_ob_ch5/', reports5.table_october_partially_paid_guest_ob_ch5,name='table_october_partially_paid_guest_ob_ch5'),

    path('nov_paid_rent_ob_ch5/', branch5.nov_paid_rent_ob_ch5, name='nov_paid_rent_ob_ch5'),
    path('table_nov_paid_rent_ob_ch5/', branch5.table_nov_paid_rent_ob_ch5, name='table_nov_paid_rent_ob_ch5'),
    path('nov_full_paid_guest_ob_ch5/', reports5.nov_full_paid_guest_ob_ch5, name='nov_full_paid_guest_ob_ch5'),
    path('nov_partially_paid_guest_ob_ch5/', reports5.nov_partially_paid_guest_ob_ch5, name='nov_partially_paid_guest_ob_ch5'),
    path('table_nov_partially_paid_guest_ob_ch5/', reports5.table_nov_partially_paid_guest_ob_ch5,name='table_nov_partially_paid_guest_ob_ch5'),

    path('dec_paid_rent_ob_ch5/', branch5.dec_paid_rent_ob_ch5, name='dec_paid_rent_ob_ch5'),
    path('table_dec_paid_rent_ob_ch5/', branch5.table_dec_paid_rent_ob_ch5, name='table_dec_paid_rent_ob_ch5'),
    path('dec_full_paid_guest_ob_ch5/', reports5.dec_full_paid_guest_ob_ch5, name='dec_full_paid_guest_ob_ch5'),
    path('dec_partially_paid_guest_ob_ch5/', reports5.dec_partially_paid_guest_ob_ch5, name='dec_partially_paid_guest_ob_ch5'),
    path('table_dec_partially_paid_guest_ob_ch5/', reports5.table_dec_partially_paid_guest_ob_ch5,name='table_dec_partially_paid_guest_ob_ch5'),

    path('details_of_paid_guests_ob_ch5/<id>',branch5.details_of_paid_guests_ob_ch5,name='details_of_paid_guests_ob_ch5'),
    path('full_paid_guest_ob_ch5/',reports5.full_paid_guest_ob_ch5,name='full_paid_guest_ob_ch5'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch5/',branch5.viewall_vacate_guest_ob_ch5,name='viewall_vacate_guest_ob_ch5'),
    path('details_of_vacate_guest_ob_ch5/<id>',branch5.details_of_vacate_guest_ob_ch5,name='details_of_vacate_guest_ob_ch5'),
    path('full_vacated_guest_details_ob_ch5',branch5.full_vacated_guest_details_ob_ch5,name='full_vacated_guest_details_ob_ch5'),
    path('full_vacated_guest_table_ob_ch5',branch5.full_vacated_guest_table_ob_ch5,name='full_vacated_guest_table_ob_ch5'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch5/<id>', branch5.jan_manke_payments_vacate_ob_ch5, name='jan_manke_payments_vacate_ob_ch5'),
    path('feb_manke_payments_vacate_ob_ch5/<id>', branch5.feb_manke_payments_vacate_ob_ch5, name='feb_manke_payments_vacate_ob_ch5'),
    path('march_manke_payments_vacate_ob_ch5/<id>', branch5.march_manke_payments_vacate_ob_ch5, name='march_manke_payments_vacate_ob_ch5'),
    path('april_make_payments_vacate_ob_ch5/<id>', branch5.april_make_payments_vacate_ob_ch5, name='april_make_payments_vacate_ob_ch5'),

    path('may_make_payments_vacate_ob_ch5/<id>', branch5.may_make_payments_vacate_ob_ch5, name='may_make_payments_vacate_ob_ch5'),
    path('june_make_payments_vacate_ob_ch5/<id>', branch5.june_make_payments_vacate_ob_ch5, name='june_make_payments_vacate_ob_ch5'),
    path('july_make_payments_vacate_ob_ch5/<id>', branch5.july_make_payments_vacate_ob_ch5, name='july_make_payments_vacate_ob_ch5'),
    path('aug_make_payments_vacate_ob_ch5/<id>', branch5.aug_make_payments_vacate_ob_ch5, name='aug_make_payments_vacate_ob_ch5'),

    path('sept_make_payments_vacate_ob_ch5/<id>', branch5.sept_make_payments_vacate_ob_ch5, name='sept_make_payments_vacate_ob_ch5'),
    path('oct_make_payments_vacate_ob_ch5/<id>', branch5.oct_make_payments_vacate_ob_ch5, name='oct_make_payments_vacate_ob_ch5'),
    path('nov_make_payments_vacate_ob_ch5/<id>', branch5.nov_make_payments_vacate_ob_ch5, name='nov_make_payments_vacate_ob_ch5'),
    path('dec_make_payments_vacate_ob_ch5/<id>', branch5.dec_make_payments_vacate_ob_ch5, name='dec_make_payments_vacate_ob_ch5'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch5/',branch5.detail_guest_general_ob_ch5,name='detail_guest_general_ob_ch5'),

    path('jan_print_ob_ch5/',branch5.jan_print_ob_ch5,name='jan_print_ob_ch5'),
    path('feb_print_ob_ch5/',branch5.feb_print_ob_ch5,name='feb_print_ob_ch5'),
    path('march_print_ob_ch5/',branch5.march_print_ob_ch5,name='march_print_ob_ch5'),
    path('april_print_ob_ch5/',branch5.april_print_ob_ch5,name='april_print_ob_ch5'),

    path('may_print_ob_ch5/',branch5.may_print_ob_ch5,name='may_print_ob_ch5'),
    path('june_print_ob_ch5/',branch5.june_print_ob_ch5,name='june_print_ob_ch5'),
    path('july_print_ob_ch5/', branch5.july_print_ob_ch5, name='july_print_ob_ch5'),
    path('aug_print_ob_ch5/', branch5.aug_print_ob_ch5, name='aug_print_ob_ch5'),

    path('sept_print_ob_ch5/', branch5.sept_print_ob_ch5, name='sept_print_ob_ch5'),
    path('oct_print_ob_ch5/', branch5.oct_print_ob_ch5, name='oct_print_ob_ch5'),
    path('nov_print_ob_ch5/', branch5.nov_print_ob_ch5, name='nov_print_ob_ch5'),
    path('dec_print_ob_ch5/', branch5.dec_print_ob_ch5, name='dec_print_ob_ch5'),

    path('new_year_jan_print_ob_ch5/', branch5.new_year_jan_print_ob_ch5, name='new_year_jan_print_ob_ch5'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch5/', branch5.jan_close_ob_ch5, name='jan_close_ob_ch5'),
    path('jan_close_decision_page_ob_ch5/', branch5.jan_close_decision_page_ob_ch5, name='jan_close_decision_page_ob_ch5'),
    path('feb_close/', branch5.feb_close_ob_ch5, name='feb_close_ob_ch5'),
    path('feb_close_decision_page_ob_ch5/', branch5.feb_close_decision_page_ob_ch5, name='feb_close_decision_page_ob_ch5'),
    path('mar_close_ob_ch5/', branch5.mar_close_ob_ch5, name='mar_close_ob_ch5'),
    path('mar_close_decision_page/', branch5.mar_close_decision_page_ob_ch5, name='mar_close_decision_page_ob_ch5'),
    path('apr_close_ob_ch5/', branch5.apr_close_ob_ch5, name='apr_close_ob_ch5'),
    path('apr_close_decision_page_ob_ch5/', branch5.apr_close_decision_page_ob_ch5, name='apr_close_decision_page_ob_ch5'),

    path('may_close_ob_ch5/', branch5.may_close_ob_ch5, name='may_close_ob_ch5'),
    path('may_close_decision_page_ob_ch5/', branch5.may_close_decision_page_ob_ch5, name='may_close_decision_page_ob_ch5'),
    path('jun_close_ob_ch5/', branch5.jun_close_ob_ch5, name='jun_close_ob_ch5'),
    path('jun_close_decision_page_ob_ch5/', branch5.jun_close_decision_page_ob_ch5, name='jun_close_decision_page_ob_ch5'),
    path('jul_close_ob_ch5/', branch5.jul_close_ob_ch5, name='jul_close_ob_ch5'),
    path('jul_close_decision_page_ob_ch5/', branch5.jul_close_decision_page_ob_ch5, name='jul_close_decision_page_ob_ch5'),
    path('aug_close_ob_ch5/', branch5.aug_close_ob_ch5, name='aug_close_ob_ch5'),
    path('aug_close_decision_page_ob_ch5/', branch5.aug_close_decision_page_ob_ch5, name='aug_close_decision_page_ob_ch5'),

    path('sep_close_ob_ch5/', branch5.sep_close_ob_ch5, name='sep_close_ob_ch5'),
    path('sep_close_decision_page_ob_ch5/', branch5.sep_close_decision_page_ob_ch5, name='sep_close_decision_page_ob_ch5'),
    path('oct_close_ob_ch5/', branch5.oct_close_ob_ch5, name='oct_close_ob_ch5'),
    path('oct_close_decision_page_ob_ch5/', branch5.oct_close_decision_page_ob_ch5, name='oct_close_decision_page_ob_ch5'),
    path('nov_close_ob_ch5/', branch5.nov_close_ob_ch5, name='nov_close_ob_ch5'),
    path('nov_close_decision_page_ob_ch5/', branch5.nov_close_decision_page_ob_ch5, name='nov_close_decision_page_ob_ch5'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch5/',reports5.detailed_report_choose_months_ob_ch5,name='detailed_report_choose_months_ob_ch5'),

    path('jan_details_live_ob_ch5/', reports5.jan_details_live_ob_ch5, name='jan_details_live_ob_ch5'),
    path('jan_print_live_ob_ch5/', reports5.jan_print_live_ob_ch5, name='jan_print_live_ob_ch5'),
    path('feb_details_live_ob_ch5/', reports5.feb_details_live_ob_ch5, name='feb_details_live_ob_ch5'),
    path('feb_print_live_ob_ch5/', reports5.feb_print_live_ob_ch5, name='feb_print_live_ob_ch5'),
    path('march_details_live_ob_ch5/', reports5.march_details_live_ob_ch5, name='march_details_live_ob_ch5'),
    path('march_print_live_ob_ch5/', reports5.march_print_live_ob_ch5, name='march_print_live_ob_ch5'),

    path('april_details_live_ob_ch5/', reports5.april_details_live_ob_ch5, name='april_details_live_ob_ch5'),
    path('april_print_live_ob_ch5/', reports5.april_print_live_ob_ch5, name='april_print_live_ob_ch5'),
    path('may_details_live_ob_ch5/', reports5.may_details_live_ob_ch5, name='may_details_live_ob_ch5'),
    path('may_print_live_ob_ch5/', reports5.may_print_live_ob_ch5, name='may_print_live_ob_ch5'),
    path('june_details_live_ob_ch5/',reports5.june_details_live_ob_ch5,name='june_details_live_ob_ch5'),
    path('june_print_live_ob_ch5/', reports5.june_print_live_ob_ch5, name='june_print_live_ob_ch5'),

    path('july_details_live_ob_ch5/', reports5.july_details_live_ob_ch5, name='july_details_live_ob_ch5'),
    path('july_print_live_ob_ch5/', reports5.july_print_live_ob_ch5, name='july_print_live_ob_ch5'),
    path('auguest_details_live_ob_ch5/', reports5.auguest_details_live_ob_ch5, name='auguest_details_live_ob_ch5'),
    path('auguest_print_live_ob_ch5/', reports5.auguest_print_live_ob_ch5, name='auguest_print_live_ob_ch5'),
    path('sept_details_live_ob_ch5/', reports5.sept_details_live_ob_ch5, name='sept_details_live_ob_ch5'),
    path('sept_print_live_ob_ch5/', reports5.sept_print_live_ob_ch5, name='sept_print_live_ob_ch5'),

    path('october_details_live_ob_ch5/', reports5.october_details_live_ob_ch5, name='october_details_live_ob_ch5'),
    path('october_print_live_ob_ch5/', reports5.october_print_live_ob_ch5, name='october_print_live_ob_ch5'),
    path('nov_details_live_ob_ch5/', reports5.nov_details_live_ob_ch5, name='nov_details_live_ob_ch5'),
    path('nov_print_live_ob_ch5/', reports5.nov_print_live_ob_ch5, name='nov_print_live_ob_ch5'),
    path('dec_details_live_ob_ch5/', reports5.dec_details_live_ob_ch5, name='dec_details_live_ob_ch5'),
    path('dec_print_live_ob_ch5/', reports5.dec_print_live_ob_ch5, name='dec_print_live_ob_ch5'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch5/', reports5.viewall_vaccant_room_ob_ch5, name='viewall_vaccant_room_ob_ch5'),

    path('d_ob_ch5/', branch5.dynamic, name='dynamic'),

    path('manage_bed_ob_ch5/', branch5.manage_bed_ob_ch5, name='manage_bed_ob_ch5'),
    path('manage_new_guest_ob_ch5/', branch5.manage_new_guest_ob_ch5, name='manage_new_guest_ob_ch5'),
    path('manage_update_new_guest_ob_ch5/<id>', branch5.manage_update_new_guest_ob_ch5, name='manage_update_new_guest_ob_ch5'),
    path('manage_update_beds_ob_ch5/<id>', branch5.manage_update_beds_ob_ch5, name='manage_update_beds_ob_ch5'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch5/', branch5.view_all_due_amt_ob_ch5, name='view_all_due_amt_ob_ch5'),
    path('due_amt_mgt_choose_months_ob_ch5/', branch5.due_amt_mgt_choose_months_ob_ch5, name='due_amt_mgt_choose_months_ob_ch5'),

    path('view_jan_account_details_ob_ch5/', branch5.view_jan_account_details_ob_ch5, name='view_jan_account_details_ob_ch5'),
    path('jan_account_mgt_ob_ch5/<id>',branch5.jan_account_mgt_ob_ch5,name='jan_account_mgt_ob_ch5'),
    path('view_feb_account_details_ob_ch5/', branch5.view_feb_account_details_ob_ch5, name='view_feb_account_details_ob_ch5'),
    path('feb_account_mgt_ob_ch5/<id>',branch5.feb_account_mgt_ob_ch5,name='feb_account_mgt_ob_ch5'),
    path('view_march_account_details_ob_ch5/', branch5.view_march_account_details_ob_ch5, name='view_march_account_details_ob_ch5'),
    path('march_account_mgt_ob_ch5/<id>',branch5.march_account_mgt_ob_ch5,name='march_account_mgt_ob_ch5'),
    path('view_april_account_details_ob_ch5/', branch5.view_april_account_details_ob_ch5, name='view_april_account_details_ob_ch5'),
    path('april_account_mgt_ob_ch5/<id>',branch5.april_account_mgt_ob_ch5,name='april_account_mgt_ob_ch5'),

    path('view_may_account_details_ob_ch5/',branch5.view_may_account_details_ob_ch5,name='view_may_account_details_ob_ch5'),
    path('may_account_mgt_ob_ch5/<id>', branch5.may_account_mgt_ob_ch5, name='may_account_mgt_ob_ch5'),
    path('view_june_account_details_ob_ch5/', branch5.view_june_account_details_ob_ch5, name='view_june_account_details_ob_ch5'),
    path('june_account_mgt_ob_ch5/<id>',branch5.june_account_mgt_ob_ch5,name='june_account_mgt_ob_ch5'),
    path('view_july_account_details_ob_ch5/', branch5.view_july_account_details_ob_ch5, name='view_july_account_details_ob_ch5'),
    path('july_account_mgt_ob_ch5/<id>',branch5.july_account_mgt_ob_ch5,name='july_account_mgt_ob_ch5'),
    path('view_auguest_account_details_ob_ch5/', branch5.view_auguest_account_details_ob_ch5, name='view_auguest_account_details_ob_ch5'),
    path('auguest_account_mgt_ob_ch5/<id>',branch5.auguest_account_mgt_ob_ch5,name='auguest_account_mgt_ob_ch5'),

    path('view_sept_account_details_ob_ch5/', branch5.view_sept_account_details_ob_ch5, name='view_sept_account_details_ob_ch5'),
    path('sept_account_mgt_ob_ch5/<id>',branch5.sept_account_mgt_ob_ch5,name='sept_account_mgt_ob_ch5'),
    path('view_october_account_details_ob_ch5/', branch5.view_october_account_details_ob_ch5, name='view_october_account_details_ob_ch5'),
    path('october_account_mgt_ob_ch5/<id>',branch5.october_account_mgt_ob_ch5,name='october_account_mgt_ob_ch5'),
    path('view_nov_account_details_ob_ch5/', branch5.view_nov_account_details_ob_ch5, name='view_nov_account_details_ob_ch5'),
    path('nov_account_mgt_ob_ch5/<id>',branch5.nov_account_mgt_ob_ch5,name='nov_account_mgt_ob_ch5'),
    path('view_dec_account_details_ob_ch5/', branch5.view_dec_account_details_ob_ch5, name='view_dec_account_details_ob_ch5'),
    path('dec_account_mgt_ob_ch5/<id>',branch5.dec_account_mgt_ob_ch5,name='dec_account_mgt_ob_ch5'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch5', admin_dashboard_calculations_br5.monthly_details_due_ob_ch5, name='monthly_details_due_ob_ch5'),
    path('monthly_collection_details_ob_ch5/', admin_dashboard_calculations_br5.monthly_collection_details_ob_ch5, name='monthly_collection_details_ob_ch5'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch5/',branch5.guest_all_ob_ch5,name='guest_all_ob_ch5'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category5/', accounts5.view_all_category5, name='view_all_category5'),
    path('create_new_category5/', accounts5.create_new_category5, name='create_new_category5'),
    path('regi_new_category5/', accounts5.regi_new_category5, name='regi_new_category5'),
    path('update_category5/<id>',accounts5.update_category5,name='update_category5'),

    path('delete_category5/<id>', accounts5.delete_category5, name='delete_category5'),
    path('view_all_category_delete5/', accounts5.view_all_category_delete5, name='view_all_category_delete5'),

    path('regi_multiple_new_category5/', accounts5.regi_multiple_new_category5, name='regi_multiple_new_category5'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items5/', accounts5.view_all_items5, name='view_all_items5'),
    path('create_new_item5/', accounts5.create_new_item5, name='create_new_item5'),
    path('regi_new_item5/', accounts5.regi_new_item5, name='regi_new_item5'),
    path('delete_item5/<id>',accounts5.delete_item5,name='delete_item5'),
    path('update_item5/<id>', accounts5.update_item5, name='update_item5'),
    path('view_all_items_delete5/',accounts5.view_all_items_delete5,name='view_all_items_delete5'),

    path('regi_multiple_new_item5/', accounts5.regi_multiple_new_item5, name='regi_multiple_new_item5'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger5/', accounts5.view_all_ledger5, name='view_all_ledger5'),
    path('create_new_ledger5/', accounts5.create_new_ledger5, name='create_new_ledger5'),
    path('regi_new_ledger5/', accounts5.regi_new_ledger5, name='regi_new_ledger5'),
    path('delete_ledger5/<id>',accounts5.delete_ledger5,name='delete_ledger5'),
    path('update_ledger5/<id>',accounts5.update_ledger5,name='update_ledger5'),
    path('view_all_ledger_delete5/',accounts5.view_all_ledger_delete5,name='view_all_ledger_delete5'),

    path('regi_multiple_new_ledger5/', accounts5.regi_multiple_new_ledger5, name='regi_multiple_new_ledger5'),

    ##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book5/', accounts5.view_all_accounts_book5, name='view_all_accounts_book5'),
    path('create_new_accounts_book5/', accounts5.create_new_accounts_book5, name='create_new_accounts_book5'),
    path('regi_new_accounts_book5/', accounts5.regi_new_accounts_book5, name='regi_new_accounts_book5'),
    path('update_accounts_book5/<id>',accounts5.update_accounts_book5,name='update_accounts_book5'),
    path('delete_accounts_book5/<id>',accounts5.delete_accounts_book5,name='delete_accounts_book5'),
    path('view_all_accounts_book_delete5/',accounts5.view_all_accounts_book_delete5,name='view_all_accounts_book_delete5'),

    path('regi_multiple_new_accounts_book5/', accounts5.regi_multiple_new_accounts_book5,name='regi_multiple_new_accounts_book5'),

    ##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries5/', accounts5.get_countries5, name='get_countries5'),

    path('in_exp_items_entry5/', accounts5.in_exp_items_entry5, name='in_exp_items_entry5'),
    path('reg_in_exp_items_entry5/', accounts5.reg_in_exp_items_entry5, name='reg_in_exp_items_entry5'),
    path('delete_journal5/<id>',accounts5.delete_journal5,name='delete_journal5'),
    path('update_in_exp_items_entry5/<id>',accounts5.update_in_exp_items_entry5,name='update_in_exp_items_entry5'),
    path('detailed_journal_report5/',accounts5.detailed_journal_report5,name='detailed_journal_report5'),
    path('journal_report_deleted5/',accounts5.journal_report_deleted5,name='journal_report_deleted5'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise5/', accounts5.daily_category_wise5, name='daily_category_wise5'),
    path('monthly_category_based_reports5/',accounts5.monthly_category_based_reports5,name='monthly_category_based_reports5'),
    path('yearly_category_based_reports5/', accounts5.yearly_category_based_reports5,name='yearly_category_based_reports5'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed5/', accounts5.daily_detailed5, name='daily_detailed5'),
    path('monthly_detailed5/',accounts5.monthly_detailed5,name='monthly_detailed5'),
    path('yearly_detailed5/',accounts5.yearly_detailed5,name='yearly_detailed5'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports5/', accounts5.item_based_reports5, name='item_based_reports5'),
    path('daily_item_based_reports5/',accounts5.daily_item_based_reports5,name='daily_item_based_reports5'),
    path('monthly_item_based_reports5/',accounts5.monthly_item_based_reports5,name='monthly_item_based_reports5'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports5/', accounts5.ledger_based_reports5, name='ledger_based_reports5'),
    path('monthly_ledger_based_reports5/', accounts5.monthly_ledger_based_reports5, name='monthly_ledger_based_reports5'),
    path('daily_ledger_based_reports5/',accounts5.daily_ledger_based_reports5,name='daily_ledger_based_reports5'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports5/', accounts5.accounts_book_based_reports5, name='accounts_book_based_reports5'),
    path('daily_accounts_book_based_reports5/',accounts5.daily_accounts_book_based_reports5,name='daily_accounts_book_based_reports5'),
    path('monthly_accounts_book_based_reports5/',accounts5.monthly_accounts_book_based_reports5,name='monthly_accounts_book_based_reports5'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months5/', accounts5.monthly_reports_choose_months5, name='monthly_reports_choose_months5'),
    path('monthly_detailed_daily_in_exp_items_report5/<mo>',accounts5.monthly_detailed_daily_in_exp_items_report5,name='monthly_detailed_daily_in_exp_items_report5'),

    path('single_monthly_reports_choose_months5/', accounts5.single_monthly_reports_choose_months5,name='single_monthly_reports_choose_months5'),
    path('single_monthly_daily_in_exp_items_report5/<mo>',accounts5.single_monthly_daily_in_exp_items_report5,name='single_monthly_daily_in_exp_items_report5'),

    path('accounts_dash_board_ob_ch5/',accounts5.accounts_dash_board_ob_ch5,name='accounts_dash_board_ob_ch5'),
    path('accounts_dash_board5/',accounts5.accounts_dash_board5,name='accounts_dash_board5'),

    path('profit_sharing_choose_months5', accounts5.profit_sharing_choose_months5,name='profit_sharing_choose_months5'),
    path('profit_sharing5/<mo>', accounts5.profit_sharing5, name='profit_sharing5'),
    path('view_share_holders5', accounts5.view_share_holders5, name='view_share_holders5'),
    path('create_share_holders5', accounts5.create_share_holders5, name='create_share_holders5'),
    path('regi_share_holders5', accounts5.regi_share_holders5, name='regi_share_holders5'),
    path('update_share_holders5/<id>', accounts5.update_share_holders5, name='update_share_holders5'),
    path('delete_share_holders5/<id>', accounts5.delete_share_holders5, name='delete_share_holders5'),
    path('view_deleted_share_holders5', accounts5.view_deleted_share_holders5, name='view_deleted_share_holders5'),

    path('regi_multiple_share_holders5', accounts5.regi_multiple_share_holders5, name='regi_multiple_share_holders5'),

    #############BRANCH SETTINGS START HERE ########################

    path('guest_rent_update_ob_ch5/', branch_settings5.guest_rent_update_ob_ch5, name='guest_rent_update_ob_ch5'),

    ############BRANCH SETTINGS END HERE ############################

]

