from django.urls import path, include

from . import admin_branch25
from . import admin_branch25
from . import branch25
from . import reports25
from . import payment25
from . import admin_dashboard_calculations_br25
from . import accounts25
from . import branch_settings25

urlpatterns = [

    path('branch1_dashboard_ob_ch25/', branch25.branch1_dashboard_ob_ch25, name='branch1_dashboard_ob_ch25'),
    path('branch1_dashboard25/',branch25.branch1_dashboard25,name='branch1_dashboard25'),
    path('user_dashboard_calculations_ob_ch25/',branch25.user_dashboard_calculations_ob_ch25,name='user_dashboard_calculations_ob_ch25'),

    path('background_ob_ch25',branch25.background_ob_ch25,name='background_ob_ch25'),
    path('background_regi_ob_ch25',branch25.background_regi_ob_ch25,name='background_regi_ob_ch25'),
    path('custom_background_regi_ob_ch25',branch25.custom_background_regi_ob_ch25,name='custom_background_regi_ob_ch25'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch25/',admin_branch25.branch1_room_create_regi_ob_ch25,name='branch1_room_create_regi_ob_ch25'),
    path('view_all_room_ob_ch25/',admin_branch25.view_all_room_ob_ch25,name='view_all_room_ob_ch25'),
    path('delete_room_ob_ch25/<id>',admin_branch25.delete_room_ob_ch25,name='delete_room_ob_ch25'),

    path('branch1_room_create_ob_ch25/',admin_branch25.branch1_room_create_ob_ch25,name='branch1_room_create_ob_ch25'),

    path('multiple_branch1_room_create_regi25/',admin_branch25.multiple_branch1_room_create_regi25,name='multiple_branch1_room_create_regi25'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch25/', admin_branch25.pg1_bed_create_regi_ob_ch25, name='pg1_bed_create_regi_ob_ch25'),
    path('pg1_view_all_beds_ob_ch25/', admin_branch25.pg1_view_all_beds_ob_ch25, name='pg1_view_all_beds_ob_ch25'),
    path('delete_bed_ob_ch25/<id>', admin_branch25.delete_bed_ob_ch25, name='delete_bed_ob_ch25'),

    path('pg1_bed_create_ob_ch25/', admin_branch25.pg1_bed_create_ob_ch25, name='pg1_bed_create_ob_ch25'),

    path('single_pg1_bed_create_regi_ob_ch25/',admin_branch25.single_pg1_bed_create_regi_ob_ch25,name='single_pg1_bed_create_regi_ob_ch25'),
    path('update_bed_basic_details_ob_ch25/<id>',admin_branch25.update_bed_basic_details_ob_ch25, name='update_bed_basic_details_ob_ch25'),

    path('multiple_single_pg1_bed_create_regi25/',admin_branch25.multiple_single_pg1_bed_create_regi25,name='multiple_single_pg1_bed_create_regi25'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch25/<id>',branch25.br1_admit_guest_ob_ch25,name='br1_admit_guest_ob_ch25'),
    path('view_all_new_guest_ob_ch25/',branch25.view_all_new_guest_ob_ch25,name='view_all_new_guest_ob_ch25'),
    path('update_br1_admit_guest_ob_ch25/<id>',branch25.update_br1_admit_guest_ob_ch25,name='update_br1_admit_guest_ob_ch25'),
    path('vacate_br1_guest_ob_ch25/<id>',branch25.vacate_br1_guest_ob_ch25,name='vacate_br1_guest_ob_ch25'),

    path('active_guest_details_ob_ch25/<guest_code>',branch25.active_guest_details_ob_ch25,name='active_guest_details_ob_ch25'),
    path('view_all_guest_ob_ch25/',branch25.view_all_guest_ob_ch25,name='view_all_guest_ob_ch25'),
    path('shift_guest_ob_ch25/<id>',branch25.shift_guest_ob_ch25,name='shift_guest_ob_ch25'),
    path('shift_guest_regi_ob_ch25/',branch25.shift_guest_regi_ob_ch25,name='shift_guest_regi_ob_ch25'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch25/',branch25.update_all_rent_ob_ch25,name='update_all_rent_ob_ch25'),

    path('multiple_br1_admit_guest25/<id>',branch25.multiple_br1_admit_guest25,name='multiple_br1_admit_guest25'),

#guest end here


##################################
#_ADVANCE_ob_ch25 START HERE
################################


    path('choose_months_advance_ob_ch25/',branch25.choose_months_advance_ob_ch25,name='choose_months_advance_ob_ch25'),

    path('jan_advance_ob_ch25/', branch25.jan_advance_ob_ch25, name='jan_advance_ob_ch25'),
    path('jan_make_payments_advance_ob_ch25/<id>', branch25.jan_make_payments_advance_ob_ch25,name='jan_make_payments_advance_ob_ch25'),
    path('feb_advance_ob_ch25/', branch25.feb_advance_ob_ch25, name='feb_advance_ob_ch25'),
    path('feb_make_payments_advance_ob_ch25/<id>', branch25.feb_make_payments_advance_ob_ch25,name='feb_make_payments_advance_ob_ch25'),
    path('march_advance_ob_ch25/', branch25.march_advance_ob_ch25, name='march_advance_ob_ch25'),
    path('march_make_payments_advance_ob_ch25/<id>', branch25.march_make_payments_advance_ob_ch25,name='march_make_payments_advance_ob_ch25'),
    path('april_advance_ob_ch25/', branch25.april_advance_ob_ch25, name='april_advance_ob_ch25'),
    path('april_make_payments_advance_ob_ch25/<id>', branch25.april_make_payments_advance_ob_ch25, name='april_make_payments_advance_ob_ch25'),

    path('may_advance_ob_ch25/',branch25.may_advance_ob_ch25,name='may_advance_ob_ch25'),
    path('may_make_payments_advance_ob_ch25/<id>', branch25.may_make_payments_advance_ob_ch25, name='may_make_payments_advance_ob_ch25'),
    path('june_advance_ob_ch25/',branch25.june_advance_ob_ch25,name='june_advance_ob_ch25'),
    path('june_make_payments_advance_ob_ch25/<id>', branch25.june_make_payments_advance_ob_ch25, name='june_make_payments_advance_ob_ch25'),
    path('july_advance_ob_ch25/',branch25.july_advance_ob_ch25,name='july_advance_ob_ch25'),
    path('july_make_payments_advance_ob_ch25/<id>', branch25.july_make_payments_advance_ob_ch25, name='july_make_payments_advance_ob_ch25'),
    path('auguest_advance_ob_ch25/', branch25.auguest_advance_ob_ch25, name='auguest_advance_ob_ch25'),
    path('auguest_make_payments_advance_ob_ch25/<id>', branch25.auguest_make_payments_advance_ob_ch25, name='auguest_make_payments_advance_ob_ch25'),

    path('sept_advance_ob_ch25/', branch25.sept_advance_ob_ch25, name='sept_advance_ob_ch25'),
    path('sept_make_payments_advance_ob_ch25/<id>', branch25.sept_make_payments_advance_ob_ch25,name='sept_make_payments_advance_ob_ch25'),
    path('october_advance_ob_ch25/', branch25.october_advance_ob_ch25, name='october_advance_ob_ch25'),
    path('october_make_payments_advance_ob_ch25/<id>', branch25.october_make_payments_advance_ob_ch25, name='october_make_payments_advance_ob_ch25'),
    path('nov_advance_ob_ch25/', branch25.nov_advance_ob_ch25, name='nov_advance_ob_ch25'),
    path('nov_make_payments_advance_ob_ch25/<id>', branch25.nov_make_payments_advance_ob_ch25,name='nov_make_payments_advance_ob_ch25'),
    path('dec_advance_ob_ch25/', branch25.dec_advance_ob_ch25, name='dec_advance_ob_ch25'),
    path('dec_make_payments_advance_ob_ch25/<id>', branch25.dec_make_payments_advance_ob_ch25, name='dec_make_payments_advance_ob_ch25'),



##################################
#_ADVANCE_ob_ch25 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch25/',branch25.choose_months_ob_ch25,name='choose_months_ob_ch25'),

    path('jan_ob_ch25/',branch25.jan_ob_ch25,name='jan_ob_ch25'),
    path('jan_manke_payments_ob_ch25/<id>',branch25.jan_manke_payments_ob_ch25,name='jan_manke_payments_ob_ch25'),

    path('feb_ob_ch25/',branch25.feb_ob_ch25,name='feb_ob_ch25'),
    path('feb_manke_payments_ob_ch25/<id>',branch25.feb_manke_payments_ob_ch25,name='feb_manke_payments_ob_ch25'),

    path('march_ob_ch25/',branch25.march_ob_ch25,name='march_ob_ch25'),
    path('march_manke_payments_ob_ch25/<id>',branch25.march_manke_payments_ob_ch25,name='march_manke_payments_ob_ch25'),

    path('april_ob_ch25/',branch25.april_ob_ch25,name='april_ob_ch25'),
    path('april_make_payments_ob_ch25/<id>',branch25.april_make_payments_ob_ch25,name='april_make_payments_ob_ch25'),

    path('may_ob_ch25/',branch25.may_ob_ch25,name='may_ob_ch25'),
    path('may_make_payments_ob_ch25/<id>',branch25.may_make_payments_ob_ch25,name='may_make_payments_ob_ch25'),

    path('june_ob_ch25/',branch25.june_ob_ch25,name='june_ob_ch25'),
    path('june_make_payments_ob_ch25/<id>',branch25.june_make_payments_ob_ch25,name='june_make_payments_ob_ch25'),

    path('july_ob_ch25/',branch25.july_ob_ch25,name='july_ob_ch25'),
    path('july_make_payments_ob_ch25/<id>',branch25.july_make_payments_ob_ch25,name='july_make_payments_ob_ch25'),

    path('aug_ob_ch25/',branch25.aug_ob_ch25,name='aug_ob_ch25'),
    path('aug_make_payments_ob_ch25/<id>',branch25.aug_make_payments_ob_ch25,name='aug_make_payments_ob_ch25'),

    path('sept_ob_ch25/',branch25.sept_ob_ch25,name='sept_ob_ch25'),
    path('sept_make_payments_ob_ch25/<id>',branch25.sept_make_payments_ob_ch25,name='sept_make_payments_ob_ch25'),

    path('oct_ob_ch25/',branch25.oct_ob_ch25,name='oct_ob_ch25'),
    path('oct_make_payments_ob_ch25/<id>',branch25.oct_make_payments_ob_ch25,name='oct_make_payments_ob_ch25'),

    path('nov_ob_ch25/',branch25.nov_ob_ch25,name='nov_ob_ch25'),
    path('nov_make_payments_ob_ch25/<id>',branch25.nov_make_payments_ob_ch25,name='nov_make_payments_ob_ch25'),

    path('dec_ob_ch25/',branch25.dec_ob_ch25,name='dec_ob_ch25'),
    path('dec_make_payments_ob_ch25/<id>',branch25.dec_make_payments_ob_ch25,name='dec_make_payments_ob_ch25'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch25/', payment25.choose_user_ob_ch25, name='choose_user_ob_ch25'),
    path('payment_user_details_ob_ch25/<id>', payment25.payment_user_details_ob_ch25, name='payment_user_details_ob_ch25'),
    path('close_choose_user_ob_ch25/<id>',payment25.close_choose_user_ob_ch25,name='close_choose_user_ob_ch25'),

    path('monthly_jan_make_payments_ob_ch25/<id>', payment25.monthly_jan_make_payments_ob_ch25, name='monthly_jan_make_payments_ob_ch25'),
    path('monthly_feb_make_payments_ob_ch25/<id>', payment25.monthly_feb_make_payments_ob_ch25, name='monthly_feb_make_payments_ob_ch25'),
    path('monthly_march_make_payments_ob_ch25/<id>', payment25.monthly_march_make_payments_ob_ch25, name='monthly_march_make_payments_ob_ch25'),
    path('monthly_april_make_payments_ob_ch25/<id>', payment25.monthly_april_make_payments_ob_ch25, name='monthly_april_make_payments_ob_ch25'),
    path('monthly_may_make_payments_ob_ch25/<id>', payment25.monthly_may_make_payments_ob_ch25, name='monthly_may_make_payments_ob_ch25'),
    path('monthly_june_make_payments_ob_ch25/<id>', payment25.monthly_june_make_payments_ob_ch25, name='monthly_june_make_payments_ob_ch25'),

    path('monthly_july_make_payments_ob_ch25/<id>', payment25.monthly_july_make_payments_ob_ch25, name='monthly_july_make_payments_ob_ch25'),
    path('monthly_aug_make_payments_ob_ch25/<id>', payment25.monthly_aug_make_payments_ob_ch25, name='monthly_aug_make_payments_ob_ch25'),
    path('monthly_sept_make_payments_ob_ch25/<id>', payment25.monthly_sept_make_payments_ob_ch25, name='monthly_sept_make_payments_ob_ch25'),
    path('monthly_oct_make_payments_ob_ch25/<id>', payment25.monthly_oct_make_payments_ob_ch25, name='monthly_oct_make_payments_ob_ch25'),
    path('monthly_nov_make_payments_ob_ch25/<id>', payment25.monthly_nov_make_payments_ob_ch25, name='monthly_nov_make_payments_ob_ch25'),
    path('monthly_dec_make_payments_ob_ch25/<id>', payment25.monthly_dec_make_payments_ob_ch25, name='monthly_dec_make_payments_ob_ch25'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch25/',branch25.unpaid_rent_choose_months_ob_ch25,name='unpaid_rent_choose_months_ob_ch25'),

    path('jan_unpaid_rent_ob_ch25/', branch25.jan_unpaid_rent_ob_ch25, name='jan_unpaid_rent_ob_ch25'),
    path('table_jan_unpaid_rent_ob_ch25/', branch25.table_jan_unpaid_rent_ob_ch25, name='table_jan_unpaid_rent_ob_ch25'),
    path('feb_unpaid_rent_ob_ch25/', branch25.feb_unpaid_rent_ob_ch25, name='feb_unpaid_rent_ob_ch25'),
    path('table_feb_unpaid_rent_ob_ch25/', branch25.table_feb_unpaid_rent_ob_ch25, name='table_feb_unpaid_rent_ob_ch25'),
    path('mar_unpaid_rent_ob_ch25/', branch25.mar_unpaid_rent_ob_ch25, name='mar_unpaid_rent_ob_ch25'),
    path('table_mar_unpaid_rent_ob_ch25/', branch25.table_mar_unpaid_rent_ob_ch25, name='table_mar_unpaid_rent_ob_ch25'),
    path('april_unpaid_rent_ob_ch25/', branch25.april_unpaid_rent_ob_ch25, name='april_unpaid_rent_ob_ch25'),
    path('table_april_unpaid_rent_ob_ch25/', branch25.table_april_unpaid_rent_ob_ch25, name='table_april_unpaid_rent_ob_ch25'),

    path('may_unpaid_rent_ob_ch25/', branch25.may_unpaid_rent_ob_ch25, name='may_unpaid_rent_ob_ch25'),
    path('table_may_unpaid_rent_ob_ch25/', branch25.table_may_unpaid_rent_ob_ch25, name='table_may_unpaid_rent_ob_ch25'),
    path('june_unpaid_rent_ob_ch25/', branch25.june_unpaid_rent_ob_ch25, name='june_unpaid_rent_ob_ch25'),
    path('table_june_unpaid_rent_ob_ch25/', branch25.table_june_unpaid_rent_ob_ch25, name='table_june_unpaid_rent_ob_ch25'),
    path('july_unpaid_rent_ob_ch25/', branch25.july_unpaid_rent_ob_ch25, name='july_unpaid_rent_ob_ch25'),
    path('table_july_unpaid_rent_ob_ch25',branch25.table_july_unpaid_rent_ob_ch25,name='table_july_unpaid_rent_ob_ch25'),
    path('aug_unpaid_rent_ob_ch25/', branch25.aug_unpaid_rent_ob_ch25, name='aug_unpaid_rent_ob_ch25'),
    path('table_aug_unpaid_rent_ob_ch25/',branch25.table_aug_unpaid_rent_ob_ch25,name='table_aug_unpaid_rent_ob_ch25'),

    path('sept_unpaid_rent_ob_ch25/', branch25.sept_unpaid_rent_ob_ch25, name='sept_unpaid_rent_ob_ch25'),
    path('table_sept_unpaid_rent_ob_ch25/', branch25.table_sept_unpaid_rent_ob_ch25, name='table_sept_unpaid_rent_ob_ch25'),
    path('oct_unpaid_rent_ob_ch25/', branch25.oct_unpaid_rent_ob_ch25, name='oct_unpaid_rent_ob_ch25'),
    path('table_oct_unpaid_rent_ob_ch25/', branch25.table_oct_unpaid_rent_ob_ch25, name='table_oct_unpaid_rent_ob_ch25'),
    path('nov_unpaid_rent_ob_ch25/', branch25.nov_unpaid_rent_ob_ch25, name='nov_unpaid_rent_ob_ch25'),
    path('table_nov_unpaid_rent_ob_ch25/', branch25.table_nov_unpaid_rent_ob_ch25, name='table_nov_unpaid_rent_ob_ch25'),
    path('dec_unpaid_rent_ob_ch25/', branch25.dec_unpaid_rent_ob_ch25, name='dec_unpaid_rent_ob_ch25'),
    path('table_dec_unpaid_rent_ob_ch25/', branch25.table_dec_unpaid_rent_ob_ch25, name='table_dec_unpaid_rent_ob_ch25'),

    path('details_of_unpaid_guests_ob_ch25/<id>',branch25.details_of_unpaid_guests_ob_ch25,name='details_of_unpaid_guests_ob_ch25'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch25/',branch25.paid_rent_choose_months_ob_ch25,name='paid_rent_choose_months_ob_ch25'),
    path('partially_paid_guest_choose_months_ob_ch25/',reports25.partially_paid_guest_choose_months_ob_ch25,name='partially_paid_guest_choose_months_ob_ch25'),

    path('jan_paid_rent_ob_ch25/', branch25.jan_paid_rent_ob_ch25, name='jan_paid_rent_ob_ch25'),
    path('table_jan_paid_rent_ob_ch25/', branch25.table_jan_paid_rent_ob_ch25, name='table_jan_paid_rent_ob_ch25'),
    path('jan_full_paid_guest_ob_ch25/', reports25.jan_full_paid_guest_ob_ch25, name='jan_full_paid_guest_ob_ch25'),
    path('jan_partially_paid_guest_ob_ch25/', reports25.jan_partially_paid_guest_ob_ch25, name='jan_partially_paid_guest_ob_ch25'),
    path('table_jan_partially_paid_guest_ob_ch25/', reports25.table_jan_partially_paid_guest_ob_ch25,name='table_jan_partially_paid_guest_ob_ch25'),

    path('feb_paid_rent_ob_ch25/', branch25.feb_paid_rent_ob_ch25, name='feb_paid_rent_ob_ch25'),
    path('table_feb_paid_rent_ob_ch25/', branch25.table_feb_paid_rent_ob_ch25, name='table_feb_paid_rent_ob_ch25'),
    path('feb_full_paid_guest_ob_ch25/', reports25.feb_full_paid_guest_ob_ch25, name='feb_full_paid_guest_ob_ch25'),
    path('feb_partially_paid_guest_ob_ch25/', reports25.feb_partially_paid_guest_ob_ch25, name='feb_partially_paid_guest_ob_ch25'),
    path('table_feb_partially_paid_guest_ob_ch25/', reports25.table_feb_partially_paid_guest_ob_ch25,name='table_feb_partially_paid_guest_ob_ch25'),

    path('mar_paid_rent_ob_ch25/', branch25.mar_paid_rent_ob_ch25, name='mar_paid_rent_ob_ch25'),
    path('table_mar_paid_rent_ob_ch25/', branch25.table_mar_paid_rent_ob_ch25, name='table_mar_paid_rent_ob_ch25'),
    path('march_full_paid_guest_ob_ch25/', reports25.march_full_paid_guest_ob_ch25, name='march_full_paid_guest_ob_ch25'),
    path('march_partially_paid_guest_ob_ch25/', reports25.march_partially_paid_guest_ob_ch25, name='march_partially_paid_guest_ob_ch25'),
    path('table_march_partially_paid_guest_ob_ch25/', reports25.table_march_partially_paid_guest_ob_ch25,name='table_march_partially_paid_guest_ob_ch25'),

    path('april_paid_rent_ob_ch25/', branch25.april_paid_rent_ob_ch25, name='april_paid_rent_ob_ch25'),
    path('table_april_paid_rent_ob_ch25/', branch25.table_april_paid_rent_ob_ch25, name='table_april_paid_rent_ob_ch25'),
    path('april_full_paid_guest_ob_ch25/', reports25.april_full_paid_guest_ob_ch25, name='april_full_paid_guest_ob_ch25'),
    path('april_partially_paid_guest_ob_ch25/', reports25.april_partially_paid_guest_ob_ch25, name='april_partially_paid_guest_ob_ch25'),
    path('table_april_partially_paid_guest_ob_ch25/', reports25.table_april_partially_paid_guest_ob_ch25,name='table_april_partially_paid_guest_ob_ch25'),

    path('may_paid_rent_ob_ch25/', branch25.may_paid_rent_ob_ch25, name='may_paid_rent_ob_ch25'),
    path('table_may_paid_rent_ob_ch25/', branch25.table_may_paid_rent_ob_ch25, name='table_may_paid_rent_ob_ch25'),
    path('may_full_paid_guest_ob_ch25/', reports25.may_full_paid_guest_ob_ch25, name='may_full_paid_guest_ob_ch25'),
    path('may_partially_paid_guest_ob_ch25/', reports25.may_partially_paid_guest_ob_ch25, name='may_partially_paid_guest_ob_ch25'),
    path('table_may_partially_paid_guest_ob_ch25/', reports25.table_may_partially_paid_guest_ob_ch25, name='table_may_partially_paid_guest_ob_ch25'),

    path('june_paid_rent_ob_ch25/', branch25.june_paid_rent_ob_ch25, name='june_paid_rent_ob_ch25'),
    path('table_june_paid_rent_ob_ch25/', branch25.table_june_paid_rent_ob_ch25, name='table_june_paid_rent_ob_ch25'),
    path('june_full_paid_guest_ob_ch25/', reports25.june_full_paid_guest_ob_ch25, name='june_full_paid_guest_ob_ch25'),
    path('june_partially_paid_guest_ob_ch25/', reports25.june_partially_paid_guest_ob_ch25, name='june_partially_paid_guest_ob_ch25'),
    path('table_june_partially_paid_guest_ob_ch25/', reports25.table_june_partially_paid_guest_ob_ch25, name='table_june_partially_paid_guest_ob_ch25'),

    path('july_paid_rent_ob_ch25/', branch25.july_paid_rent_ob_ch25, name='july_paid_rent_ob_ch25'),
    path('table_july_paid_rent_ob_ch25/', branch25.table_july_paid_rent_ob_ch25, name='table_july_paid_rent_ob_ch25'),
    path('july_full_paid_guest_ob_ch25/', reports25.july_full_paid_guest_ob_ch25, name='july_full_paid_guest_ob_ch25'),
    path('july_partially_paid_guest_ob_ch25/', reports25.july_partially_paid_guest_ob_ch25, name='july_partially_paid_guest_ob_ch25'),
    path('table_july_partially_paid_guest_ob_ch25/', reports25.table_july_partially_paid_guest_ob_ch25, name='table_july_partially_paid_guest_ob_ch25'),

    path('aug_paid_rent_ob_ch25/', branch25.aug_paid_rent_ob_ch25, name='aug_paid_rent_ob_ch25'),
    path('table_aug_paid_rent_ob_ch25/', branch25.table_aug_paid_rent_ob_ch25, name='table_aug_paid_rent_ob_ch25'),
    path('auguest_full_paid_guest_ob_ch25/', reports25.auguest_full_paid_guest_ob_ch25, name='auguest_full_paid_guest_ob_ch25'),
    path('auguest_partially_paid_guest_ob_ch25/', reports25.auguest_partially_paid_guest_ob_ch25,name='auguest_partially_paid_guest_ob_ch25'),
    path('table_auguest_partially_paid_guest_ob_ch25/', reports25.table_auguest_partially_paid_guest_ob_ch25,name='table_auguest_partially_paid_guest_ob_ch25'),

    path('sept_paid_rent_ob_ch25/', branch25.sept_paid_rent_ob_ch25, name='sept_paid_rent_ob_ch25'),
    path('table_sept_paid_rent_ob_ch25/', branch25.table_sept_paid_rent_ob_ch25, name='table_sept_paid_rent_ob_ch25'),
    path('sept_full_paid_guest_ob_ch25/', reports25.sept_full_paid_guest_ob_ch25, name='sept_full_paid_guest_ob_ch25'),
    path('sept_partially_paid_guest_ob_ch25/', reports25.sept_partially_paid_guest_ob_ch25, name='sept_partially_paid_guest_ob_ch25'),
    path('table_sept_partially_paid_guest_ob_ch25/', reports25.table_sept_partially_paid_guest_ob_ch25,name='table_sept_partially_paid_guest_ob_ch25'),

    path('oct_paid_rent_ob_ch25/', branch25.oct_paid_rent_ob_ch25, name='oct_paid_rent_ob_ch25'),
    path('table_oct_paid_rent_ob_ch25/', branch25.table_oct_paid_rent_ob_ch25, name='table_oct_paid_rent_ob_ch25'),
    path('october_full_paid_guest_ob_ch25/', reports25.october_full_paid_guest_ob_ch25, name='october_full_paid_guest_ob_ch25'),
    path('october_partially_paid_guest_ob_ch25/', reports25.october_partially_paid_guest_ob_ch25,name='october_partially_paid_guest_ob_ch25'),
    path('table_october_partially_paid_guest_ob_ch25/', reports25.table_october_partially_paid_guest_ob_ch25,name='table_october_partially_paid_guest_ob_ch25'),

    path('nov_paid_rent_ob_ch25/', branch25.nov_paid_rent_ob_ch25, name='nov_paid_rent_ob_ch25'),
    path('table_nov_paid_rent_ob_ch25/', branch25.table_nov_paid_rent_ob_ch25, name='table_nov_paid_rent_ob_ch25'),
    path('nov_full_paid_guest_ob_ch25/', reports25.nov_full_paid_guest_ob_ch25, name='nov_full_paid_guest_ob_ch25'),
    path('nov_partially_paid_guest_ob_ch25/', reports25.nov_partially_paid_guest_ob_ch25, name='nov_partially_paid_guest_ob_ch25'),
    path('table_nov_partially_paid_guest_ob_ch25/', reports25.table_nov_partially_paid_guest_ob_ch25,name='table_nov_partially_paid_guest_ob_ch25'),

    path('dec_paid_rent_ob_ch25/', branch25.dec_paid_rent_ob_ch25, name='dec_paid_rent_ob_ch25'),
    path('table_dec_paid_rent_ob_ch25/', branch25.table_dec_paid_rent_ob_ch25, name='table_dec_paid_rent_ob_ch25'),
    path('dec_full_paid_guest_ob_ch25/', reports25.dec_full_paid_guest_ob_ch25, name='dec_full_paid_guest_ob_ch25'),
    path('dec_partially_paid_guest_ob_ch25/', reports25.dec_partially_paid_guest_ob_ch25, name='dec_partially_paid_guest_ob_ch25'),
    path('table_dec_partially_paid_guest_ob_ch25/', reports25.table_dec_partially_paid_guest_ob_ch25,name='table_dec_partially_paid_guest_ob_ch25'),

    path('details_of_paid_guests_ob_ch25/<id>',branch25.details_of_paid_guests_ob_ch25,name='details_of_paid_guests_ob_ch25'),
    path('full_paid_guest_ob_ch25/',reports25.full_paid_guest_ob_ch25,name='full_paid_guest_ob_ch25'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch25/',branch25.viewall_vacate_guest_ob_ch25,name='viewall_vacate_guest_ob_ch25'),
    path('details_of_vacate_guest_ob_ch25/<id>',branch25.details_of_vacate_guest_ob_ch25,name='details_of_vacate_guest_ob_ch25'),
    path('full_vacated_guest_details_ob_ch25',branch25.full_vacated_guest_details_ob_ch25,name='full_vacated_guest_details_ob_ch25'),
    path('full_vacated_guest_table_ob_ch25',branch25.full_vacated_guest_table_ob_ch25,name='full_vacated_guest_table_ob_ch25'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch25/<id>', branch25.jan_manke_payments_vacate_ob_ch25, name='jan_manke_payments_vacate_ob_ch25'),
    path('feb_manke_payments_vacate_ob_ch25/<id>', branch25.feb_manke_payments_vacate_ob_ch25, name='feb_manke_payments_vacate_ob_ch25'),
    path('march_manke_payments_vacate_ob_ch25/<id>', branch25.march_manke_payments_vacate_ob_ch25, name='march_manke_payments_vacate_ob_ch25'),
    path('april_make_payments_vacate_ob_ch25/<id>', branch25.april_make_payments_vacate_ob_ch25, name='april_make_payments_vacate_ob_ch25'),

    path('may_make_payments_vacate_ob_ch25/<id>', branch25.may_make_payments_vacate_ob_ch25, name='may_make_payments_vacate_ob_ch25'),
    path('june_make_payments_vacate_ob_ch25/<id>', branch25.june_make_payments_vacate_ob_ch25, name='june_make_payments_vacate_ob_ch25'),
    path('july_make_payments_vacate_ob_ch25/<id>', branch25.july_make_payments_vacate_ob_ch25, name='july_make_payments_vacate_ob_ch25'),
    path('aug_make_payments_vacate_ob_ch25/<id>', branch25.aug_make_payments_vacate_ob_ch25, name='aug_make_payments_vacate_ob_ch25'),

    path('sept_make_payments_vacate_ob_ch25/<id>', branch25.sept_make_payments_vacate_ob_ch25, name='sept_make_payments_vacate_ob_ch25'),
    path('oct_make_payments_vacate_ob_ch25/<id>', branch25.oct_make_payments_vacate_ob_ch25, name='oct_make_payments_vacate_ob_ch25'),
    path('nov_make_payments_vacate_ob_ch25/<id>', branch25.nov_make_payments_vacate_ob_ch25, name='nov_make_payments_vacate_ob_ch25'),
    path('dec_make_payments_vacate_ob_ch25/<id>', branch25.dec_make_payments_vacate_ob_ch25, name='dec_make_payments_vacate_ob_ch25'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch25/',branch25.detail_guest_general_ob_ch25,name='detail_guest_general_ob_ch25'),

    path('jan_print_ob_ch25/',branch25.jan_print_ob_ch25,name='jan_print_ob_ch25'),
    path('feb_print_ob_ch25/',branch25.feb_print_ob_ch25,name='feb_print_ob_ch25'),
    path('march_print_ob_ch25/',branch25.march_print_ob_ch25,name='march_print_ob_ch25'),
    path('april_print_ob_ch25/',branch25.april_print_ob_ch25,name='april_print_ob_ch25'),

    path('may_print_ob_ch25/',branch25.may_print_ob_ch25,name='may_print_ob_ch25'),
    path('june_print_ob_ch25/',branch25.june_print_ob_ch25,name='june_print_ob_ch25'),
    path('july_print_ob_ch25/', branch25.july_print_ob_ch25, name='july_print_ob_ch25'),
    path('aug_print_ob_ch25/', branch25.aug_print_ob_ch25, name='aug_print_ob_ch25'),

    path('sept_print_ob_ch25/', branch25.sept_print_ob_ch25, name='sept_print_ob_ch25'),
    path('oct_print_ob_ch25/', branch25.oct_print_ob_ch25, name='oct_print_ob_ch25'),
    path('nov_print_ob_ch25/', branch25.nov_print_ob_ch25, name='nov_print_ob_ch25'),
    path('dec_print_ob_ch25/', branch25.dec_print_ob_ch25, name='dec_print_ob_ch25'),

    path('new_year_jan_print_ob_ch25/', branch25.new_year_jan_print_ob_ch25, name='new_year_jan_print_ob_ch25'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch25/', branch25.jan_close_ob_ch25, name='jan_close_ob_ch25'),
    path('jan_close_decision_page_ob_ch25/', branch25.jan_close_decision_page_ob_ch25, name='jan_close_decision_page_ob_ch25'),
    path('feb_close/', branch25.feb_close_ob_ch25, name='feb_close_ob_ch25'),
    path('feb_close_decision_page_ob_ch25/', branch25.feb_close_decision_page_ob_ch25, name='feb_close_decision_page_ob_ch25'),
    path('mar_close_ob_ch25/', branch25.mar_close_ob_ch25, name='mar_close_ob_ch25'),
    path('mar_close_decision_page/', branch25.mar_close_decision_page_ob_ch25, name='mar_close_decision_page_ob_ch25'),
    path('apr_close_ob_ch25/', branch25.apr_close_ob_ch25, name='apr_close_ob_ch25'),
    path('apr_close_decision_page_ob_ch25/', branch25.apr_close_decision_page_ob_ch25, name='apr_close_decision_page_ob_ch25'),

    path('may_close_ob_ch25/', branch25.may_close_ob_ch25, name='may_close_ob_ch25'),
    path('may_close_decision_page_ob_ch25/', branch25.may_close_decision_page_ob_ch25, name='may_close_decision_page_ob_ch25'),
    path('jun_close_ob_ch25/', branch25.jun_close_ob_ch25, name='jun_close_ob_ch25'),
    path('jun_close_decision_page_ob_ch25/', branch25.jun_close_decision_page_ob_ch25, name='jun_close_decision_page_ob_ch25'),
    path('jul_close_ob_ch25/', branch25.jul_close_ob_ch25, name='jul_close_ob_ch25'),
    path('jul_close_decision_page_ob_ch25/', branch25.jul_close_decision_page_ob_ch25, name='jul_close_decision_page_ob_ch25'),
    path('aug_close_ob_ch25/', branch25.aug_close_ob_ch25, name='aug_close_ob_ch25'),
    path('aug_close_decision_page_ob_ch25/', branch25.aug_close_decision_page_ob_ch25, name='aug_close_decision_page_ob_ch25'),

    path('sep_close_ob_ch25/', branch25.sep_close_ob_ch25, name='sep_close_ob_ch25'),
    path('sep_close_decision_page_ob_ch25/', branch25.sep_close_decision_page_ob_ch25, name='sep_close_decision_page_ob_ch25'),
    path('oct_close_ob_ch25/', branch25.oct_close_ob_ch25, name='oct_close_ob_ch25'),
    path('oct_close_decision_page_ob_ch25/', branch25.oct_close_decision_page_ob_ch25, name='oct_close_decision_page_ob_ch25'),
    path('nov_close_ob_ch25/', branch25.nov_close_ob_ch25, name='nov_close_ob_ch25'),
    path('nov_close_decision_page_ob_ch25/', branch25.nov_close_decision_page_ob_ch25, name='nov_close_decision_page_ob_ch25'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch25/',reports25.detailed_report_choose_months_ob_ch25,name='detailed_report_choose_months_ob_ch25'),

    path('jan_details_live_ob_ch25/', reports25.jan_details_live_ob_ch25, name='jan_details_live_ob_ch25'),
    path('jan_print_live_ob_ch25/', reports25.jan_print_live_ob_ch25, name='jan_print_live_ob_ch25'),
    path('feb_details_live_ob_ch25/', reports25.feb_details_live_ob_ch25, name='feb_details_live_ob_ch25'),
    path('feb_print_live_ob_ch25/', reports25.feb_print_live_ob_ch25, name='feb_print_live_ob_ch25'),
    path('march_details_live_ob_ch25/', reports25.march_details_live_ob_ch25, name='march_details_live_ob_ch25'),
    path('march_print_live_ob_ch25/', reports25.march_print_live_ob_ch25, name='march_print_live_ob_ch25'),

    path('april_details_live_ob_ch25/', reports25.april_details_live_ob_ch25, name='april_details_live_ob_ch25'),
    path('april_print_live_ob_ch25/', reports25.april_print_live_ob_ch25, name='april_print_live_ob_ch25'),
    path('may_details_live_ob_ch25/', reports25.may_details_live_ob_ch25, name='may_details_live_ob_ch25'),
    path('may_print_live_ob_ch25/', reports25.may_print_live_ob_ch25, name='may_print_live_ob_ch25'),
    path('june_details_live_ob_ch25/',reports25.june_details_live_ob_ch25,name='june_details_live_ob_ch25'),
    path('june_print_live_ob_ch25/', reports25.june_print_live_ob_ch25, name='june_print_live_ob_ch25'),

    path('july_details_live_ob_ch25/', reports25.july_details_live_ob_ch25, name='july_details_live_ob_ch25'),
    path('july_print_live_ob_ch25/', reports25.july_print_live_ob_ch25, name='july_print_live_ob_ch25'),
    path('auguest_details_live_ob_ch25/', reports25.auguest_details_live_ob_ch25, name='auguest_details_live_ob_ch25'),
    path('auguest_print_live_ob_ch25/', reports25.auguest_print_live_ob_ch25, name='auguest_print_live_ob_ch25'),
    path('sept_details_live_ob_ch25/', reports25.sept_details_live_ob_ch25, name='sept_details_live_ob_ch25'),
    path('sept_print_live_ob_ch25/', reports25.sept_print_live_ob_ch25, name='sept_print_live_ob_ch25'),

    path('october_details_live_ob_ch25/', reports25.october_details_live_ob_ch25, name='october_details_live_ob_ch25'),
    path('october_print_live_ob_ch25/', reports25.october_print_live_ob_ch25, name='october_print_live_ob_ch25'),
    path('nov_details_live_ob_ch25/', reports25.nov_details_live_ob_ch25, name='nov_details_live_ob_ch25'),
    path('nov_print_live_ob_ch25/', reports25.nov_print_live_ob_ch25, name='nov_print_live_ob_ch25'),
    path('dec_details_live_ob_ch25/', reports25.dec_details_live_ob_ch25, name='dec_details_live_ob_ch25'),
    path('dec_print_live_ob_ch25/', reports25.dec_print_live_ob_ch25, name='dec_print_live_ob_ch25'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch25/', reports25.viewall_vaccant_room_ob_ch25, name='viewall_vaccant_room_ob_ch25'),

    path('d_ob_ch25/', branch25.dynamic, name='dynamic'),

    path('manage_bed_ob_ch25/', branch25.manage_bed_ob_ch25, name='manage_bed_ob_ch25'),
    path('manage_new_guest_ob_ch25/', branch25.manage_new_guest_ob_ch25, name='manage_new_guest_ob_ch25'),
    path('manage_update_new_guest_ob_ch25/<id>', branch25.manage_update_new_guest_ob_ch25, name='manage_update_new_guest_ob_ch25'),
    path('manage_update_beds_ob_ch25/<id>', branch25.manage_update_beds_ob_ch25, name='manage_update_beds_ob_ch25'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch25/', branch25.view_all_due_amt_ob_ch25, name='view_all_due_amt_ob_ch25'),
    path('due_amt_mgt_choose_months_ob_ch25/', branch25.due_amt_mgt_choose_months_ob_ch25, name='due_amt_mgt_choose_months_ob_ch25'),

    path('view_jan_account_details_ob_ch25/', branch25.view_jan_account_details_ob_ch25, name='view_jan_account_details_ob_ch25'),
    path('jan_account_mgt_ob_ch25/<id>',branch25.jan_account_mgt_ob_ch25,name='jan_account_mgt_ob_ch25'),
    path('view_feb_account_details_ob_ch25/', branch25.view_feb_account_details_ob_ch25, name='view_feb_account_details_ob_ch25'),
    path('feb_account_mgt_ob_ch25/<id>',branch25.feb_account_mgt_ob_ch25,name='feb_account_mgt_ob_ch25'),
    path('view_march_account_details_ob_ch25/', branch25.view_march_account_details_ob_ch25, name='view_march_account_details_ob_ch25'),
    path('march_account_mgt_ob_ch25/<id>',branch25.march_account_mgt_ob_ch25,name='march_account_mgt_ob_ch25'),
    path('view_april_account_details_ob_ch25/', branch25.view_april_account_details_ob_ch25, name='view_april_account_details_ob_ch25'),
    path('april_account_mgt_ob_ch25/<id>',branch25.april_account_mgt_ob_ch25,name='april_account_mgt_ob_ch25'),

    path('view_may_account_details_ob_ch25/',branch25.view_may_account_details_ob_ch25,name='view_may_account_details_ob_ch25'),
    path('may_account_mgt_ob_ch25/<id>', branch25.may_account_mgt_ob_ch25, name='may_account_mgt_ob_ch25'),
    path('view_june_account_details_ob_ch25/', branch25.view_june_account_details_ob_ch25, name='view_june_account_details_ob_ch25'),
    path('june_account_mgt_ob_ch25/<id>',branch25.june_account_mgt_ob_ch25,name='june_account_mgt_ob_ch25'),
    path('view_july_account_details_ob_ch25/', branch25.view_july_account_details_ob_ch25, name='view_july_account_details_ob_ch25'),
    path('july_account_mgt_ob_ch25/<id>',branch25.july_account_mgt_ob_ch25,name='july_account_mgt_ob_ch25'),
    path('view_auguest_account_details_ob_ch25/', branch25.view_auguest_account_details_ob_ch25, name='view_auguest_account_details_ob_ch25'),
    path('auguest_account_mgt_ob_ch25/<id>',branch25.auguest_account_mgt_ob_ch25,name='auguest_account_mgt_ob_ch25'),

    path('view_sept_account_details_ob_ch25/', branch25.view_sept_account_details_ob_ch25, name='view_sept_account_details_ob_ch25'),
    path('sept_account_mgt_ob_ch25/<id>',branch25.sept_account_mgt_ob_ch25,name='sept_account_mgt_ob_ch25'),
    path('view_october_account_details_ob_ch25/', branch25.view_october_account_details_ob_ch25, name='view_october_account_details_ob_ch25'),
    path('october_account_mgt_ob_ch25/<id>',branch25.october_account_mgt_ob_ch25,name='october_account_mgt_ob_ch25'),
    path('view_nov_account_details_ob_ch25/', branch25.view_nov_account_details_ob_ch25, name='view_nov_account_details_ob_ch25'),
    path('nov_account_mgt_ob_ch25/<id>',branch25.nov_account_mgt_ob_ch25,name='nov_account_mgt_ob_ch25'),
    path('view_dec_account_details_ob_ch25/', branch25.view_dec_account_details_ob_ch25, name='view_dec_account_details_ob_ch25'),
    path('dec_account_mgt_ob_ch25/<id>',branch25.dec_account_mgt_ob_ch25,name='dec_account_mgt_ob_ch25'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch25', admin_dashboard_calculations_br25.monthly_details_due_ob_ch25, name='monthly_details_due_ob_ch25'),
    path('monthly_collection_details_ob_ch25/', admin_dashboard_calculations_br25.monthly_collection_details_ob_ch25, name='monthly_collection_details_ob_ch25'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch25/',branch25.guest_all_ob_ch25,name='guest_all_ob_ch25'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category25/', accounts25.view_all_category25, name='view_all_category25'),
    path('create_new_category25/', accounts25.create_new_category25, name='create_new_category25'),
    path('regi_new_category25/', accounts25.regi_new_category25, name='regi_new_category25'),
    path('update_category25/<id>',accounts25.update_category25,name='update_category25'),

    path('delete_category25/<id>', accounts25.delete_category25, name='delete_category25'),
    path('view_all_category_delete25/', accounts25.view_all_category_delete25, name='view_all_category_delete25'),

    path('regi_multiple_new_category25/', accounts25.regi_multiple_new_category25, name='regi_multiple_new_category25'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items25/', accounts25.view_all_items25, name='view_all_items25'),
    path('create_new_item25/', accounts25.create_new_item25, name='create_new_item25'),
    path('regi_new_item25/', accounts25.regi_new_item25, name='regi_new_item25'),
    path('delete_item25/<id>',accounts25.delete_item25,name='delete_item25'),
    path('update_item25/<id>', accounts25.update_item25, name='update_item25'),
    path('view_all_items_delete25/',accounts25.view_all_items_delete25,name='view_all_items_delete25'),

    path('regi_multiple_new_item25/', accounts25.regi_multiple_new_item25, name='regi_multiple_new_item25'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger25/', accounts25.view_all_ledger25, name='view_all_ledger25'),
    path('create_new_ledger25/', accounts25.create_new_ledger25, name='create_new_ledger25'),
    path('regi_new_ledger25/', accounts25.regi_new_ledger25, name='regi_new_ledger25'),
    path('delete_ledger25/<id>',accounts25.delete_ledger25,name='delete_ledger25'),
    path('update_ledger25/<id>',accounts25.update_ledger25,name='update_ledger25'),
    path('view_all_ledger_delete25/',accounts25.view_all_ledger_delete25,name='view_all_ledger_delete25'),

    path('regi_multiple_new_ledger25/', accounts25.regi_multiple_new_ledger25, name='regi_multiple_new_ledger25'),

    ##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book25/', accounts25.view_all_accounts_book25, name='view_all_accounts_book25'),
    path('create_new_accounts_book25/', accounts25.create_new_accounts_book25, name='create_new_accounts_book25'),
    path('regi_new_accounts_book25/', accounts25.regi_new_accounts_book25, name='regi_new_accounts_book25'),
    path('update_accounts_book25/<id>',accounts25.update_accounts_book25,name='update_accounts_book25'),
    path('delete_accounts_book25/<id>',accounts25.delete_accounts_book25,name='delete_accounts_book25'),
    path('view_all_accounts_book_delete25/',accounts25.view_all_accounts_book_delete25,name='view_all_accounts_book_delete25'),

    path('regi_multiple_new_accounts_book25/', accounts25.regi_multiple_new_accounts_book25,name='regi_multiple_new_accounts_book25'),

    ##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries25/', accounts25.get_countries25, name='get_countries25'),

    path('in_exp_items_entry25/', accounts25.in_exp_items_entry25, name='in_exp_items_entry25'),
    path('reg_in_exp_items_entry25/', accounts25.reg_in_exp_items_entry25, name='reg_in_exp_items_entry25'),
    path('delete_journal25/<id>',accounts25.delete_journal25,name='delete_journal25'),
    path('update_in_exp_items_entry25/<id>',accounts25.update_in_exp_items_entry25,name='update_in_exp_items_entry25'),
    path('detailed_journal_report25/',accounts25.detailed_journal_report25,name='detailed_journal_report25'),
    path('journal_report_deleted25/',accounts25.journal_report_deleted25,name='journal_report_deleted25'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise25/', accounts25.daily_category_wise25, name='daily_category_wise25'),
    path('monthly_category_based_reports25/',accounts25.monthly_category_based_reports25,name='monthly_category_based_reports25'),
    path('yearly_category_based_reports25/', accounts25.yearly_category_based_reports25,name='yearly_category_based_reports25'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed25/', accounts25.daily_detailed25, name='daily_detailed25'),
    path('monthly_detailed25/',accounts25.monthly_detailed25,name='monthly_detailed25'),
    path('yearly_detailed25/',accounts25.yearly_detailed25,name='yearly_detailed25'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports25/', accounts25.item_based_reports25, name='item_based_reports25'),
    path('daily_item_based_reports25/',accounts25.daily_item_based_reports25,name='daily_item_based_reports25'),
    path('monthly_item_based_reports25/',accounts25.monthly_item_based_reports25,name='monthly_item_based_reports25'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports25/', accounts25.ledger_based_reports25, name='ledger_based_reports25'),
    path('monthly_ledger_based_reports25/', accounts25.monthly_ledger_based_reports25, name='monthly_ledger_based_reports25'),
    path('daily_ledger_based_reports25/',accounts25.daily_ledger_based_reports25,name='daily_ledger_based_reports25'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports25/', accounts25.accounts_book_based_reports25, name='accounts_book_based_reports25'),
    path('daily_accounts_book_based_reports25/',accounts25.daily_accounts_book_based_reports25,name='daily_accounts_book_based_reports25'),
    path('monthly_accounts_book_based_reports25/',accounts25.monthly_accounts_book_based_reports25,name='monthly_accounts_book_based_reports25'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months25/', accounts25.monthly_reports_choose_months25, name='monthly_reports_choose_months25'),
    path('monthly_detailed_daily_in_exp_items_report25/<mo>',accounts25.monthly_detailed_daily_in_exp_items_report25,name='monthly_detailed_daily_in_exp_items_report25'),

    path('single_monthly_reports_choose_months25/', accounts25.single_monthly_reports_choose_months25,name='single_monthly_reports_choose_months25'),
    path('single_monthly_daily_in_exp_items_report25/<mo>',accounts25.single_monthly_daily_in_exp_items_report25,name='single_monthly_daily_in_exp_items_report25'),

    path('accounts_dash_board_ob_ch25/',accounts25.accounts_dash_board_ob_ch25,name='accounts_dash_board_ob_ch25'),
    path('accounts_dash_board25/',accounts25.accounts_dash_board25,name='accounts_dash_board25'),

    path('profit_sharing_choose_months25', accounts25.profit_sharing_choose_months25,name='profit_sharing_choose_months25'),
    path('profit_sharing25/<mo>', accounts25.profit_sharing25, name='profit_sharing25'),
    path('view_share_holders25', accounts25.view_share_holders25, name='view_share_holders25'),
    path('create_share_holders25', accounts25.create_share_holders25, name='create_share_holders25'),
    path('regi_share_holders25', accounts25.regi_share_holders25, name='regi_share_holders25'),
    path('update_share_holders25/<id>', accounts25.update_share_holders25, name='update_share_holders25'),
    path('delete_share_holders25/<id>', accounts25.delete_share_holders25, name='delete_share_holders25'),
    path('view_deleted_share_holders25', accounts25.view_deleted_share_holders25, name='view_deleted_share_holders25'),

    path('regi_multiple_share_holders25', accounts25.regi_multiple_share_holders25, name='regi_multiple_share_holders25'),

    #############BRANCH SETTINGS START HERE ########################

    path('guest_rent_update_ob_ch25/', branch_settings25.guest_rent_update_ob_ch25, name='guest_rent_update_ob_ch25'),

    ############BRANCH SETTINGS END HERE ############################

]

