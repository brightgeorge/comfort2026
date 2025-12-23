from django.urls import path, include

from . import admin_branch32
from . import admin_branch32
from . import branch32
from . import reports32
from . import payment32
from . import admin_dashboard_calculations_br32
from . import accounts32
from . import branch_settings32

urlpatterns = [

    path('branch1_dashboard_ob_ch32/', branch32.branch1_dashboard_ob_ch32, name='branch1_dashboard_ob_ch32'),
    path('branch1_dashboard32/',branch32.branch1_dashboard32,name='branch1_dashboard32'),
    path('user_dashboard_calculations_ob_ch32/',branch32.user_dashboard_calculations_ob_ch32,name='user_dashboard_calculations_ob_ch32'),

    path('background_ob_ch32',branch32.background_ob_ch32,name='background_ob_ch32'),
    path('background_regi_ob_ch32',branch32.background_regi_ob_ch32,name='background_regi_ob_ch32'),
    path('custom_background_regi_ob_ch32',branch32.custom_background_regi_ob_ch32,name='custom_background_regi_ob_ch32'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch32/',admin_branch32.branch1_room_create_regi_ob_ch32,name='branch1_room_create_regi_ob_ch32'),
    path('view_all_room_ob_ch32/',admin_branch32.view_all_room_ob_ch32,name='view_all_room_ob_ch32'),
    path('delete_room_ob_ch32/<id>',admin_branch32.delete_room_ob_ch32,name='delete_room_ob_ch32'),

    path('branch1_room_create_ob_ch32/',admin_branch32.branch1_room_create_ob_ch32,name='branch1_room_create_ob_ch32'),

    path('multiple_branch1_room_create_regi32/',admin_branch32.multiple_branch1_room_create_regi32,name='multiple_branch1_room_create_regi32'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch32/', admin_branch32.pg1_bed_create_regi_ob_ch32, name='pg1_bed_create_regi_ob_ch32'),
    path('pg1_view_all_beds_ob_ch32/', admin_branch32.pg1_view_all_beds_ob_ch32, name='pg1_view_all_beds_ob_ch32'),
    path('delete_bed_ob_ch32/<id>', admin_branch32.delete_bed_ob_ch32, name='delete_bed_ob_ch32'),

    path('pg1_bed_create_ob_ch32/', admin_branch32.pg1_bed_create_ob_ch32, name='pg1_bed_create_ob_ch32'),

    path('single_pg1_bed_create_regi_ob_ch32/',admin_branch32.single_pg1_bed_create_regi_ob_ch32,name='single_pg1_bed_create_regi_ob_ch32'),
    path('update_bed_basic_details_ob_ch32/<id>',admin_branch32.update_bed_basic_details_ob_ch32, name='update_bed_basic_details_ob_ch32'),

    path('multiple_single_pg1_bed_create_regi32/',admin_branch32.multiple_single_pg1_bed_create_regi32,name='multiple_single_pg1_bed_create_regi32'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch32/<id>',branch32.br1_admit_guest_ob_ch32,name='br1_admit_guest_ob_ch32'),
    path('view_all_new_guest_ob_ch32/',branch32.view_all_new_guest_ob_ch32,name='view_all_new_guest_ob_ch32'),
    path('update_br1_admit_guest_ob_ch32/<id>',branch32.update_br1_admit_guest_ob_ch32,name='update_br1_admit_guest_ob_ch32'),
    path('vacate_br1_guest_ob_ch32/<id>',branch32.vacate_br1_guest_ob_ch32,name='vacate_br1_guest_ob_ch32'),

    path('active_guest_details_ob_ch32/<guest_code>',branch32.active_guest_details_ob_ch32,name='active_guest_details_ob_ch32'),
    path('view_all_guest_ob_ch32/',branch32.view_all_guest_ob_ch32,name='view_all_guest_ob_ch32'),
    path('shift_guest_ob_ch32/<id>',branch32.shift_guest_ob_ch32,name='shift_guest_ob_ch32'),
    path('shift_guest_regi_ob_ch32/',branch32.shift_guest_regi_ob_ch32,name='shift_guest_regi_ob_ch32'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch32/',branch32.update_all_rent_ob_ch32,name='update_all_rent_ob_ch32'),

    path('multiple_br1_admit_guest32/<id>',branch32.multiple_br1_admit_guest32,name='multiple_br1_admit_guest32'),

#guest end here


##################################
#_ADVANCE_ob_ch32 START HERE
################################


    path('choose_months_advance_ob_ch32/',branch32.choose_months_advance_ob_ch32,name='choose_months_advance_ob_ch32'),

    path('jan_advance_ob_ch32/', branch32.jan_advance_ob_ch32, name='jan_advance_ob_ch32'),
    path('jan_make_payments_advance_ob_ch32/<id>', branch32.jan_make_payments_advance_ob_ch32,name='jan_make_payments_advance_ob_ch32'),
    path('feb_advance_ob_ch32/', branch32.feb_advance_ob_ch32, name='feb_advance_ob_ch32'),
    path('feb_make_payments_advance_ob_ch32/<id>', branch32.feb_make_payments_advance_ob_ch32,name='feb_make_payments_advance_ob_ch32'),
    path('march_advance_ob_ch32/', branch32.march_advance_ob_ch32, name='march_advance_ob_ch32'),
    path('march_make_payments_advance_ob_ch32/<id>', branch32.march_make_payments_advance_ob_ch32,name='march_make_payments_advance_ob_ch32'),
    path('april_advance_ob_ch32/', branch32.april_advance_ob_ch32, name='april_advance_ob_ch32'),
    path('april_make_payments_advance_ob_ch32/<id>', branch32.april_make_payments_advance_ob_ch32, name='april_make_payments_advance_ob_ch32'),

    path('may_advance_ob_ch32/',branch32.may_advance_ob_ch32,name='may_advance_ob_ch32'),
    path('may_make_payments_advance_ob_ch32/<id>', branch32.may_make_payments_advance_ob_ch32, name='may_make_payments_advance_ob_ch32'),
    path('june_advance_ob_ch32/',branch32.june_advance_ob_ch32,name='june_advance_ob_ch32'),
    path('june_make_payments_advance_ob_ch32/<id>', branch32.june_make_payments_advance_ob_ch32, name='june_make_payments_advance_ob_ch32'),
    path('july_advance_ob_ch32/',branch32.july_advance_ob_ch32,name='july_advance_ob_ch32'),
    path('july_make_payments_advance_ob_ch32/<id>', branch32.july_make_payments_advance_ob_ch32, name='july_make_payments_advance_ob_ch32'),
    path('auguest_advance_ob_ch32/', branch32.auguest_advance_ob_ch32, name='auguest_advance_ob_ch32'),
    path('auguest_make_payments_advance_ob_ch32/<id>', branch32.auguest_make_payments_advance_ob_ch32, name='auguest_make_payments_advance_ob_ch32'),

    path('sept_advance_ob_ch32/', branch32.sept_advance_ob_ch32, name='sept_advance_ob_ch32'),
    path('sept_make_payments_advance_ob_ch32/<id>', branch32.sept_make_payments_advance_ob_ch32,name='sept_make_payments_advance_ob_ch32'),
    path('october_advance_ob_ch32/', branch32.october_advance_ob_ch32, name='october_advance_ob_ch32'),
    path('october_make_payments_advance_ob_ch32/<id>', branch32.october_make_payments_advance_ob_ch32, name='october_make_payments_advance_ob_ch32'),
    path('nov_advance_ob_ch32/', branch32.nov_advance_ob_ch32, name='nov_advance_ob_ch32'),
    path('nov_make_payments_advance_ob_ch32/<id>', branch32.nov_make_payments_advance_ob_ch32,name='nov_make_payments_advance_ob_ch32'),
    path('dec_advance_ob_ch32/', branch32.dec_advance_ob_ch32, name='dec_advance_ob_ch32'),
    path('dec_make_payments_advance_ob_ch32/<id>', branch32.dec_make_payments_advance_ob_ch32, name='dec_make_payments_advance_ob_ch32'),



##################################
#_ADVANCE_ob_ch32 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch32/',branch32.choose_months_ob_ch32,name='choose_months_ob_ch32'),

    path('jan_ob_ch32/',branch32.jan_ob_ch32,name='jan_ob_ch32'),
    path('jan_manke_payments_ob_ch32/<id>',branch32.jan_manke_payments_ob_ch32,name='jan_manke_payments_ob_ch32'),

    path('feb_ob_ch32/',branch32.feb_ob_ch32,name='feb_ob_ch32'),
    path('feb_manke_payments_ob_ch32/<id>',branch32.feb_manke_payments_ob_ch32,name='feb_manke_payments_ob_ch32'),

    path('march_ob_ch32/',branch32.march_ob_ch32,name='march_ob_ch32'),
    path('march_manke_payments_ob_ch32/<id>',branch32.march_manke_payments_ob_ch32,name='march_manke_payments_ob_ch32'),

    path('april_ob_ch32/',branch32.april_ob_ch32,name='april_ob_ch32'),
    path('april_make_payments_ob_ch32/<id>',branch32.april_make_payments_ob_ch32,name='april_make_payments_ob_ch32'),

    path('may_ob_ch32/',branch32.may_ob_ch32,name='may_ob_ch32'),
    path('may_make_payments_ob_ch32/<id>',branch32.may_make_payments_ob_ch32,name='may_make_payments_ob_ch32'),

    path('june_ob_ch32/',branch32.june_ob_ch32,name='june_ob_ch32'),
    path('june_make_payments_ob_ch32/<id>',branch32.june_make_payments_ob_ch32,name='june_make_payments_ob_ch32'),

    path('july_ob_ch32/',branch32.july_ob_ch32,name='july_ob_ch32'),
    path('july_make_payments_ob_ch32/<id>',branch32.july_make_payments_ob_ch32,name='july_make_payments_ob_ch32'),

    path('aug_ob_ch32/',branch32.aug_ob_ch32,name='aug_ob_ch32'),
    path('aug_make_payments_ob_ch32/<id>',branch32.aug_make_payments_ob_ch32,name='aug_make_payments_ob_ch32'),

    path('sept_ob_ch32/',branch32.sept_ob_ch32,name='sept_ob_ch32'),
    path('sept_make_payments_ob_ch32/<id>',branch32.sept_make_payments_ob_ch32,name='sept_make_payments_ob_ch32'),

    path('oct_ob_ch32/',branch32.oct_ob_ch32,name='oct_ob_ch32'),
    path('oct_make_payments_ob_ch32/<id>',branch32.oct_make_payments_ob_ch32,name='oct_make_payments_ob_ch32'),

    path('nov_ob_ch32/',branch32.nov_ob_ch32,name='nov_ob_ch32'),
    path('nov_make_payments_ob_ch32/<id>',branch32.nov_make_payments_ob_ch32,name='nov_make_payments_ob_ch32'),

    path('dec_ob_ch32/',branch32.dec_ob_ch32,name='dec_ob_ch32'),
    path('dec_make_payments_ob_ch32/<id>',branch32.dec_make_payments_ob_ch32,name='dec_make_payments_ob_ch32'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch32/', payment32.choose_user_ob_ch32, name='choose_user_ob_ch32'),
    path('payment_user_details_ob_ch32/<id>', payment32.payment_user_details_ob_ch32, name='payment_user_details_ob_ch32'),
    path('close_choose_user_ob_ch32/<id>',payment32.close_choose_user_ob_ch32,name='close_choose_user_ob_ch32'),

    path('monthly_jan_make_payments_ob_ch32/<id>', payment32.monthly_jan_make_payments_ob_ch32, name='monthly_jan_make_payments_ob_ch32'),
    path('monthly_feb_make_payments_ob_ch32/<id>', payment32.monthly_feb_make_payments_ob_ch32, name='monthly_feb_make_payments_ob_ch32'),
    path('monthly_march_make_payments_ob_ch32/<id>', payment32.monthly_march_make_payments_ob_ch32, name='monthly_march_make_payments_ob_ch32'),
    path('monthly_april_make_payments_ob_ch32/<id>', payment32.monthly_april_make_payments_ob_ch32, name='monthly_april_make_payments_ob_ch32'),
    path('monthly_may_make_payments_ob_ch32/<id>', payment32.monthly_may_make_payments_ob_ch32, name='monthly_may_make_payments_ob_ch32'),
    path('monthly_june_make_payments_ob_ch32/<id>', payment32.monthly_june_make_payments_ob_ch32, name='monthly_june_make_payments_ob_ch32'),

    path('monthly_july_make_payments_ob_ch32/<id>', payment32.monthly_july_make_payments_ob_ch32, name='monthly_july_make_payments_ob_ch32'),
    path('monthly_aug_make_payments_ob_ch32/<id>', payment32.monthly_aug_make_payments_ob_ch32, name='monthly_aug_make_payments_ob_ch32'),
    path('monthly_sept_make_payments_ob_ch32/<id>', payment32.monthly_sept_make_payments_ob_ch32, name='monthly_sept_make_payments_ob_ch32'),
    path('monthly_oct_make_payments_ob_ch32/<id>', payment32.monthly_oct_make_payments_ob_ch32, name='monthly_oct_make_payments_ob_ch32'),
    path('monthly_nov_make_payments_ob_ch32/<id>', payment32.monthly_nov_make_payments_ob_ch32, name='monthly_nov_make_payments_ob_ch32'),
    path('monthly_dec_make_payments_ob_ch32/<id>', payment32.monthly_dec_make_payments_ob_ch32, name='monthly_dec_make_payments_ob_ch32'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch32/',branch32.unpaid_rent_choose_months_ob_ch32,name='unpaid_rent_choose_months_ob_ch32'),

    path('jan_unpaid_rent_ob_ch32/', branch32.jan_unpaid_rent_ob_ch32, name='jan_unpaid_rent_ob_ch32'),
    path('table_jan_unpaid_rent_ob_ch32/', branch32.table_jan_unpaid_rent_ob_ch32, name='table_jan_unpaid_rent_ob_ch32'),
    path('feb_unpaid_rent_ob_ch32/', branch32.feb_unpaid_rent_ob_ch32, name='feb_unpaid_rent_ob_ch32'),
    path('table_feb_unpaid_rent_ob_ch32/', branch32.table_feb_unpaid_rent_ob_ch32, name='table_feb_unpaid_rent_ob_ch32'),
    path('mar_unpaid_rent_ob_ch32/', branch32.mar_unpaid_rent_ob_ch32, name='mar_unpaid_rent_ob_ch32'),
    path('table_mar_unpaid_rent_ob_ch32/', branch32.table_mar_unpaid_rent_ob_ch32, name='table_mar_unpaid_rent_ob_ch32'),
    path('april_unpaid_rent_ob_ch32/', branch32.april_unpaid_rent_ob_ch32, name='april_unpaid_rent_ob_ch32'),
    path('table_april_unpaid_rent_ob_ch32/', branch32.table_april_unpaid_rent_ob_ch32, name='table_april_unpaid_rent_ob_ch32'),

    path('may_unpaid_rent_ob_ch32/', branch32.may_unpaid_rent_ob_ch32, name='may_unpaid_rent_ob_ch32'),
    path('table_may_unpaid_rent_ob_ch32/', branch32.table_may_unpaid_rent_ob_ch32, name='table_may_unpaid_rent_ob_ch32'),
    path('june_unpaid_rent_ob_ch32/', branch32.june_unpaid_rent_ob_ch32, name='june_unpaid_rent_ob_ch32'),
    path('table_june_unpaid_rent_ob_ch32/', branch32.table_june_unpaid_rent_ob_ch32, name='table_june_unpaid_rent_ob_ch32'),
    path('july_unpaid_rent_ob_ch32/', branch32.july_unpaid_rent_ob_ch32, name='july_unpaid_rent_ob_ch32'),
    path('table_july_unpaid_rent_ob_ch32',branch32.table_july_unpaid_rent_ob_ch32,name='table_july_unpaid_rent_ob_ch32'),
    path('aug_unpaid_rent_ob_ch32/', branch32.aug_unpaid_rent_ob_ch32, name='aug_unpaid_rent_ob_ch32'),
    path('table_aug_unpaid_rent_ob_ch32/',branch32.table_aug_unpaid_rent_ob_ch32,name='table_aug_unpaid_rent_ob_ch32'),

    path('sept_unpaid_rent_ob_ch32/', branch32.sept_unpaid_rent_ob_ch32, name='sept_unpaid_rent_ob_ch32'),
    path('table_sept_unpaid_rent_ob_ch32/', branch32.table_sept_unpaid_rent_ob_ch32, name='table_sept_unpaid_rent_ob_ch32'),
    path('oct_unpaid_rent_ob_ch32/', branch32.oct_unpaid_rent_ob_ch32, name='oct_unpaid_rent_ob_ch32'),
    path('table_oct_unpaid_rent_ob_ch32/', branch32.table_oct_unpaid_rent_ob_ch32, name='table_oct_unpaid_rent_ob_ch32'),
    path('nov_unpaid_rent_ob_ch32/', branch32.nov_unpaid_rent_ob_ch32, name='nov_unpaid_rent_ob_ch32'),
    path('table_nov_unpaid_rent_ob_ch32/', branch32.table_nov_unpaid_rent_ob_ch32, name='table_nov_unpaid_rent_ob_ch32'),
    path('dec_unpaid_rent_ob_ch32/', branch32.dec_unpaid_rent_ob_ch32, name='dec_unpaid_rent_ob_ch32'),
    path('table_dec_unpaid_rent_ob_ch32/', branch32.table_dec_unpaid_rent_ob_ch32, name='table_dec_unpaid_rent_ob_ch32'),

    path('details_of_unpaid_guests_ob_ch32/<id>',branch32.details_of_unpaid_guests_ob_ch32,name='details_of_unpaid_guests_ob_ch32'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch32/',branch32.paid_rent_choose_months_ob_ch32,name='paid_rent_choose_months_ob_ch32'),
    path('partially_paid_guest_choose_months_ob_ch32/',reports32.partially_paid_guest_choose_months_ob_ch32,name='partially_paid_guest_choose_months_ob_ch32'),

    path('jan_paid_rent_ob_ch32/', branch32.jan_paid_rent_ob_ch32, name='jan_paid_rent_ob_ch32'),
    path('table_jan_paid_rent_ob_ch32/', branch32.table_jan_paid_rent_ob_ch32, name='table_jan_paid_rent_ob_ch32'),
    path('jan_full_paid_guest_ob_ch32/', reports32.jan_full_paid_guest_ob_ch32, name='jan_full_paid_guest_ob_ch32'),
    path('jan_partially_paid_guest_ob_ch32/', reports32.jan_partially_paid_guest_ob_ch32, name='jan_partially_paid_guest_ob_ch32'),
    path('table_jan_partially_paid_guest_ob_ch32/', reports32.table_jan_partially_paid_guest_ob_ch32,name='table_jan_partially_paid_guest_ob_ch32'),

    path('feb_paid_rent_ob_ch32/', branch32.feb_paid_rent_ob_ch32, name='feb_paid_rent_ob_ch32'),
    path('table_feb_paid_rent_ob_ch32/', branch32.table_feb_paid_rent_ob_ch32, name='table_feb_paid_rent_ob_ch32'),
    path('feb_full_paid_guest_ob_ch32/', reports32.feb_full_paid_guest_ob_ch32, name='feb_full_paid_guest_ob_ch32'),
    path('feb_partially_paid_guest_ob_ch32/', reports32.feb_partially_paid_guest_ob_ch32, name='feb_partially_paid_guest_ob_ch32'),
    path('table_feb_partially_paid_guest_ob_ch32/', reports32.table_feb_partially_paid_guest_ob_ch32,name='table_feb_partially_paid_guest_ob_ch32'),

    path('mar_paid_rent_ob_ch32/', branch32.mar_paid_rent_ob_ch32, name='mar_paid_rent_ob_ch32'),
    path('table_mar_paid_rent_ob_ch32/', branch32.table_mar_paid_rent_ob_ch32, name='table_mar_paid_rent_ob_ch32'),
    path('march_full_paid_guest_ob_ch32/', reports32.march_full_paid_guest_ob_ch32, name='march_full_paid_guest_ob_ch32'),
    path('march_partially_paid_guest_ob_ch32/', reports32.march_partially_paid_guest_ob_ch32, name='march_partially_paid_guest_ob_ch32'),
    path('table_march_partially_paid_guest_ob_ch32/', reports32.table_march_partially_paid_guest_ob_ch32,name='table_march_partially_paid_guest_ob_ch32'),

    path('april_paid_rent_ob_ch32/', branch32.april_paid_rent_ob_ch32, name='april_paid_rent_ob_ch32'),
    path('table_april_paid_rent_ob_ch32/', branch32.table_april_paid_rent_ob_ch32, name='table_april_paid_rent_ob_ch32'),
    path('april_full_paid_guest_ob_ch32/', reports32.april_full_paid_guest_ob_ch32, name='april_full_paid_guest_ob_ch32'),
    path('april_partially_paid_guest_ob_ch32/', reports32.april_partially_paid_guest_ob_ch32, name='april_partially_paid_guest_ob_ch32'),
    path('table_april_partially_paid_guest_ob_ch32/', reports32.table_april_partially_paid_guest_ob_ch32,name='table_april_partially_paid_guest_ob_ch32'),

    path('may_paid_rent_ob_ch32/', branch32.may_paid_rent_ob_ch32, name='may_paid_rent_ob_ch32'),
    path('table_may_paid_rent_ob_ch32/', branch32.table_may_paid_rent_ob_ch32, name='table_may_paid_rent_ob_ch32'),
    path('may_full_paid_guest_ob_ch32/', reports32.may_full_paid_guest_ob_ch32, name='may_full_paid_guest_ob_ch32'),
    path('may_partially_paid_guest_ob_ch32/', reports32.may_partially_paid_guest_ob_ch32, name='may_partially_paid_guest_ob_ch32'),
    path('table_may_partially_paid_guest_ob_ch32/', reports32.table_may_partially_paid_guest_ob_ch32, name='table_may_partially_paid_guest_ob_ch32'),

    path('june_paid_rent_ob_ch32/', branch32.june_paid_rent_ob_ch32, name='june_paid_rent_ob_ch32'),
    path('table_june_paid_rent_ob_ch32/', branch32.table_june_paid_rent_ob_ch32, name='table_june_paid_rent_ob_ch32'),
    path('june_full_paid_guest_ob_ch32/', reports32.june_full_paid_guest_ob_ch32, name='june_full_paid_guest_ob_ch32'),
    path('june_partially_paid_guest_ob_ch32/', reports32.june_partially_paid_guest_ob_ch32, name='june_partially_paid_guest_ob_ch32'),
    path('table_june_partially_paid_guest_ob_ch32/', reports32.table_june_partially_paid_guest_ob_ch32, name='table_june_partially_paid_guest_ob_ch32'),

    path('july_paid_rent_ob_ch32/', branch32.july_paid_rent_ob_ch32, name='july_paid_rent_ob_ch32'),
    path('table_july_paid_rent_ob_ch32/', branch32.table_july_paid_rent_ob_ch32, name='table_july_paid_rent_ob_ch32'),
    path('july_full_paid_guest_ob_ch32/', reports32.july_full_paid_guest_ob_ch32, name='july_full_paid_guest_ob_ch32'),
    path('july_partially_paid_guest_ob_ch32/', reports32.july_partially_paid_guest_ob_ch32, name='july_partially_paid_guest_ob_ch32'),
    path('table_july_partially_paid_guest_ob_ch32/', reports32.table_july_partially_paid_guest_ob_ch32, name='table_july_partially_paid_guest_ob_ch32'),

    path('aug_paid_rent_ob_ch32/', branch32.aug_paid_rent_ob_ch32, name='aug_paid_rent_ob_ch32'),
    path('table_aug_paid_rent_ob_ch32/', branch32.table_aug_paid_rent_ob_ch32, name='table_aug_paid_rent_ob_ch32'),
    path('auguest_full_paid_guest_ob_ch32/', reports32.auguest_full_paid_guest_ob_ch32, name='auguest_full_paid_guest_ob_ch32'),
    path('auguest_partially_paid_guest_ob_ch32/', reports32.auguest_partially_paid_guest_ob_ch32,name='auguest_partially_paid_guest_ob_ch32'),
    path('table_auguest_partially_paid_guest_ob_ch32/', reports32.table_auguest_partially_paid_guest_ob_ch32,name='table_auguest_partially_paid_guest_ob_ch32'),

    path('sept_paid_rent_ob_ch32/', branch32.sept_paid_rent_ob_ch32, name='sept_paid_rent_ob_ch32'),
    path('table_sept_paid_rent_ob_ch32/', branch32.table_sept_paid_rent_ob_ch32, name='table_sept_paid_rent_ob_ch32'),
    path('sept_full_paid_guest_ob_ch32/', reports32.sept_full_paid_guest_ob_ch32, name='sept_full_paid_guest_ob_ch32'),
    path('sept_partially_paid_guest_ob_ch32/', reports32.sept_partially_paid_guest_ob_ch32, name='sept_partially_paid_guest_ob_ch32'),
    path('table_sept_partially_paid_guest_ob_ch32/', reports32.table_sept_partially_paid_guest_ob_ch32,name='table_sept_partially_paid_guest_ob_ch32'),

    path('oct_paid_rent_ob_ch32/', branch32.oct_paid_rent_ob_ch32, name='oct_paid_rent_ob_ch32'),
    path('table_oct_paid_rent_ob_ch32/', branch32.table_oct_paid_rent_ob_ch32, name='table_oct_paid_rent_ob_ch32'),
    path('october_full_paid_guest_ob_ch32/', reports32.october_full_paid_guest_ob_ch32, name='october_full_paid_guest_ob_ch32'),
    path('october_partially_paid_guest_ob_ch32/', reports32.october_partially_paid_guest_ob_ch32,name='october_partially_paid_guest_ob_ch32'),
    path('table_october_partially_paid_guest_ob_ch32/', reports32.table_october_partially_paid_guest_ob_ch32,name='table_october_partially_paid_guest_ob_ch32'),

    path('nov_paid_rent_ob_ch32/', branch32.nov_paid_rent_ob_ch32, name='nov_paid_rent_ob_ch32'),
    path('table_nov_paid_rent_ob_ch32/', branch32.table_nov_paid_rent_ob_ch32, name='table_nov_paid_rent_ob_ch32'),
    path('nov_full_paid_guest_ob_ch32/', reports32.nov_full_paid_guest_ob_ch32, name='nov_full_paid_guest_ob_ch32'),
    path('nov_partially_paid_guest_ob_ch32/', reports32.nov_partially_paid_guest_ob_ch32, name='nov_partially_paid_guest_ob_ch32'),
    path('table_nov_partially_paid_guest_ob_ch32/', reports32.table_nov_partially_paid_guest_ob_ch32,name='table_nov_partially_paid_guest_ob_ch32'),

    path('dec_paid_rent_ob_ch32/', branch32.dec_paid_rent_ob_ch32, name='dec_paid_rent_ob_ch32'),
    path('table_dec_paid_rent_ob_ch32/', branch32.table_dec_paid_rent_ob_ch32, name='table_dec_paid_rent_ob_ch32'),
    path('dec_full_paid_guest_ob_ch32/', reports32.dec_full_paid_guest_ob_ch32, name='dec_full_paid_guest_ob_ch32'),
    path('dec_partially_paid_guest_ob_ch32/', reports32.dec_partially_paid_guest_ob_ch32, name='dec_partially_paid_guest_ob_ch32'),
    path('table_dec_partially_paid_guest_ob_ch32/', reports32.table_dec_partially_paid_guest_ob_ch32,name='table_dec_partially_paid_guest_ob_ch32'),

    path('details_of_paid_guests_ob_ch32/<id>',branch32.details_of_paid_guests_ob_ch32,name='details_of_paid_guests_ob_ch32'),
    path('full_paid_guest_ob_ch32/',reports32.full_paid_guest_ob_ch32,name='full_paid_guest_ob_ch32'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch32/',branch32.viewall_vacate_guest_ob_ch32,name='viewall_vacate_guest_ob_ch32'),
    path('details_of_vacate_guest_ob_ch32/<id>',branch32.details_of_vacate_guest_ob_ch32,name='details_of_vacate_guest_ob_ch32'),
    path('full_vacated_guest_details_ob_ch32',branch32.full_vacated_guest_details_ob_ch32,name='full_vacated_guest_details_ob_ch32'),
    path('full_vacated_guest_table_ob_ch32',branch32.full_vacated_guest_table_ob_ch32,name='full_vacated_guest_table_ob_ch32'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch32/<id>', branch32.jan_manke_payments_vacate_ob_ch32, name='jan_manke_payments_vacate_ob_ch32'),
    path('feb_manke_payments_vacate_ob_ch32/<id>', branch32.feb_manke_payments_vacate_ob_ch32, name='feb_manke_payments_vacate_ob_ch32'),
    path('march_manke_payments_vacate_ob_ch32/<id>', branch32.march_manke_payments_vacate_ob_ch32, name='march_manke_payments_vacate_ob_ch32'),
    path('april_make_payments_vacate_ob_ch32/<id>', branch32.april_make_payments_vacate_ob_ch32, name='april_make_payments_vacate_ob_ch32'),

    path('may_make_payments_vacate_ob_ch32/<id>', branch32.may_make_payments_vacate_ob_ch32, name='may_make_payments_vacate_ob_ch32'),
    path('june_make_payments_vacate_ob_ch32/<id>', branch32.june_make_payments_vacate_ob_ch32, name='june_make_payments_vacate_ob_ch32'),
    path('july_make_payments_vacate_ob_ch32/<id>', branch32.july_make_payments_vacate_ob_ch32, name='july_make_payments_vacate_ob_ch32'),
    path('aug_make_payments_vacate_ob_ch32/<id>', branch32.aug_make_payments_vacate_ob_ch32, name='aug_make_payments_vacate_ob_ch32'),

    path('sept_make_payments_vacate_ob_ch32/<id>', branch32.sept_make_payments_vacate_ob_ch32, name='sept_make_payments_vacate_ob_ch32'),
    path('oct_make_payments_vacate_ob_ch32/<id>', branch32.oct_make_payments_vacate_ob_ch32, name='oct_make_payments_vacate_ob_ch32'),
    path('nov_make_payments_vacate_ob_ch32/<id>', branch32.nov_make_payments_vacate_ob_ch32, name='nov_make_payments_vacate_ob_ch32'),
    path('dec_make_payments_vacate_ob_ch32/<id>', branch32.dec_make_payments_vacate_ob_ch32, name='dec_make_payments_vacate_ob_ch32'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch32/',branch32.detail_guest_general_ob_ch32,name='detail_guest_general_ob_ch32'),

    path('jan_print_ob_ch32/',branch32.jan_print_ob_ch32,name='jan_print_ob_ch32'),
    path('feb_print_ob_ch32/',branch32.feb_print_ob_ch32,name='feb_print_ob_ch32'),
    path('march_print_ob_ch32/',branch32.march_print_ob_ch32,name='march_print_ob_ch32'),
    path('april_print_ob_ch32/',branch32.april_print_ob_ch32,name='april_print_ob_ch32'),

    path('may_print_ob_ch32/',branch32.may_print_ob_ch32,name='may_print_ob_ch32'),
    path('june_print_ob_ch32/',branch32.june_print_ob_ch32,name='june_print_ob_ch32'),
    path('july_print_ob_ch32/', branch32.july_print_ob_ch32, name='july_print_ob_ch32'),
    path('aug_print_ob_ch32/', branch32.aug_print_ob_ch32, name='aug_print_ob_ch32'),

    path('sept_print_ob_ch32/', branch32.sept_print_ob_ch32, name='sept_print_ob_ch32'),
    path('oct_print_ob_ch32/', branch32.oct_print_ob_ch32, name='oct_print_ob_ch32'),
    path('nov_print_ob_ch32/', branch32.nov_print_ob_ch32, name='nov_print_ob_ch32'),
    path('dec_print_ob_ch32/', branch32.dec_print_ob_ch32, name='dec_print_ob_ch32'),

    path('new_year_jan_print_ob_ch32/', branch32.new_year_jan_print_ob_ch32, name='new_year_jan_print_ob_ch32'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch32/', branch32.jan_close_ob_ch32, name='jan_close_ob_ch32'),
    path('jan_close_decision_page_ob_ch32/', branch32.jan_close_decision_page_ob_ch32, name='jan_close_decision_page_ob_ch32'),
    path('feb_close/', branch32.feb_close_ob_ch32, name='feb_close_ob_ch32'),
    path('feb_close_decision_page_ob_ch32/', branch32.feb_close_decision_page_ob_ch32, name='feb_close_decision_page_ob_ch32'),
    path('mar_close_ob_ch32/', branch32.mar_close_ob_ch32, name='mar_close_ob_ch32'),
    path('mar_close_decision_page/', branch32.mar_close_decision_page_ob_ch32, name='mar_close_decision_page_ob_ch32'),
    path('apr_close_ob_ch32/', branch32.apr_close_ob_ch32, name='apr_close_ob_ch32'),
    path('apr_close_decision_page_ob_ch32/', branch32.apr_close_decision_page_ob_ch32, name='apr_close_decision_page_ob_ch32'),

    path('may_close_ob_ch32/', branch32.may_close_ob_ch32, name='may_close_ob_ch32'),
    path('may_close_decision_page_ob_ch32/', branch32.may_close_decision_page_ob_ch32, name='may_close_decision_page_ob_ch32'),
    path('jun_close_ob_ch32/', branch32.jun_close_ob_ch32, name='jun_close_ob_ch32'),
    path('jun_close_decision_page_ob_ch32/', branch32.jun_close_decision_page_ob_ch32, name='jun_close_decision_page_ob_ch32'),
    path('jul_close_ob_ch32/', branch32.jul_close_ob_ch32, name='jul_close_ob_ch32'),
    path('jul_close_decision_page_ob_ch32/', branch32.jul_close_decision_page_ob_ch32, name='jul_close_decision_page_ob_ch32'),
    path('aug_close_ob_ch32/', branch32.aug_close_ob_ch32, name='aug_close_ob_ch32'),
    path('aug_close_decision_page_ob_ch32/', branch32.aug_close_decision_page_ob_ch32, name='aug_close_decision_page_ob_ch32'),

    path('sep_close_ob_ch32/', branch32.sep_close_ob_ch32, name='sep_close_ob_ch32'),
    path('sep_close_decision_page_ob_ch32/', branch32.sep_close_decision_page_ob_ch32, name='sep_close_decision_page_ob_ch32'),
    path('oct_close_ob_ch32/', branch32.oct_close_ob_ch32, name='oct_close_ob_ch32'),
    path('oct_close_decision_page_ob_ch32/', branch32.oct_close_decision_page_ob_ch32, name='oct_close_decision_page_ob_ch32'),
    path('nov_close_ob_ch32/', branch32.nov_close_ob_ch32, name='nov_close_ob_ch32'),
    path('nov_close_decision_page_ob_ch32/', branch32.nov_close_decision_page_ob_ch32, name='nov_close_decision_page_ob_ch32'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch32/',reports32.detailed_report_choose_months_ob_ch32,name='detailed_report_choose_months_ob_ch32'),

    path('jan_details_live_ob_ch32/', reports32.jan_details_live_ob_ch32, name='jan_details_live_ob_ch32'),
    path('jan_print_live_ob_ch32/', reports32.jan_print_live_ob_ch32, name='jan_print_live_ob_ch32'),
    path('feb_details_live_ob_ch32/', reports32.feb_details_live_ob_ch32, name='feb_details_live_ob_ch32'),
    path('feb_print_live_ob_ch32/', reports32.feb_print_live_ob_ch32, name='feb_print_live_ob_ch32'),
    path('march_details_live_ob_ch32/', reports32.march_details_live_ob_ch32, name='march_details_live_ob_ch32'),
    path('march_print_live_ob_ch32/', reports32.march_print_live_ob_ch32, name='march_print_live_ob_ch32'),

    path('april_details_live_ob_ch32/', reports32.april_details_live_ob_ch32, name='april_details_live_ob_ch32'),
    path('april_print_live_ob_ch32/', reports32.april_print_live_ob_ch32, name='april_print_live_ob_ch32'),
    path('may_details_live_ob_ch32/', reports32.may_details_live_ob_ch32, name='may_details_live_ob_ch32'),
    path('may_print_live_ob_ch32/', reports32.may_print_live_ob_ch32, name='may_print_live_ob_ch32'),
    path('june_details_live_ob_ch32/',reports32.june_details_live_ob_ch32,name='june_details_live_ob_ch32'),
    path('june_print_live_ob_ch32/', reports32.june_print_live_ob_ch32, name='june_print_live_ob_ch32'),

    path('july_details_live_ob_ch32/', reports32.july_details_live_ob_ch32, name='july_details_live_ob_ch32'),
    path('july_print_live_ob_ch32/', reports32.july_print_live_ob_ch32, name='july_print_live_ob_ch32'),
    path('auguest_details_live_ob_ch32/', reports32.auguest_details_live_ob_ch32, name='auguest_details_live_ob_ch32'),
    path('auguest_print_live_ob_ch32/', reports32.auguest_print_live_ob_ch32, name='auguest_print_live_ob_ch32'),
    path('sept_details_live_ob_ch32/', reports32.sept_details_live_ob_ch32, name='sept_details_live_ob_ch32'),
    path('sept_print_live_ob_ch32/', reports32.sept_print_live_ob_ch32, name='sept_print_live_ob_ch32'),

    path('october_details_live_ob_ch32/', reports32.october_details_live_ob_ch32, name='october_details_live_ob_ch32'),
    path('october_print_live_ob_ch32/', reports32.october_print_live_ob_ch32, name='october_print_live_ob_ch32'),
    path('nov_details_live_ob_ch32/', reports32.nov_details_live_ob_ch32, name='nov_details_live_ob_ch32'),
    path('nov_print_live_ob_ch32/', reports32.nov_print_live_ob_ch32, name='nov_print_live_ob_ch32'),
    path('dec_details_live_ob_ch32/', reports32.dec_details_live_ob_ch32, name='dec_details_live_ob_ch32'),
    path('dec_print_live_ob_ch32/', reports32.dec_print_live_ob_ch32, name='dec_print_live_ob_ch32'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch32/', reports32.viewall_vaccant_room_ob_ch32, name='viewall_vaccant_room_ob_ch32'),

    path('d_ob_ch32/', branch32.dynamic, name='dynamic'),

    path('manage_bed_ob_ch32/', branch32.manage_bed_ob_ch32, name='manage_bed_ob_ch32'),
    path('manage_new_guest_ob_ch32/', branch32.manage_new_guest_ob_ch32, name='manage_new_guest_ob_ch32'),
    path('manage_update_new_guest_ob_ch32/<id>', branch32.manage_update_new_guest_ob_ch32, name='manage_update_new_guest_ob_ch32'),
    path('manage_update_beds_ob_ch32/<id>', branch32.manage_update_beds_ob_ch32, name='manage_update_beds_ob_ch32'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch32/', branch32.view_all_due_amt_ob_ch32, name='view_all_due_amt_ob_ch32'),
    path('due_amt_mgt_choose_months_ob_ch32/', branch32.due_amt_mgt_choose_months_ob_ch32, name='due_amt_mgt_choose_months_ob_ch32'),

    path('view_jan_account_details_ob_ch32/', branch32.view_jan_account_details_ob_ch32, name='view_jan_account_details_ob_ch32'),
    path('jan_account_mgt_ob_ch32/<id>',branch32.jan_account_mgt_ob_ch32,name='jan_account_mgt_ob_ch32'),
    path('view_feb_account_details_ob_ch32/', branch32.view_feb_account_details_ob_ch32, name='view_feb_account_details_ob_ch32'),
    path('feb_account_mgt_ob_ch32/<id>',branch32.feb_account_mgt_ob_ch32,name='feb_account_mgt_ob_ch32'),
    path('view_march_account_details_ob_ch32/', branch32.view_march_account_details_ob_ch32, name='view_march_account_details_ob_ch32'),
    path('march_account_mgt_ob_ch32/<id>',branch32.march_account_mgt_ob_ch32,name='march_account_mgt_ob_ch32'),
    path('view_april_account_details_ob_ch32/', branch32.view_april_account_details_ob_ch32, name='view_april_account_details_ob_ch32'),
    path('april_account_mgt_ob_ch32/<id>',branch32.april_account_mgt_ob_ch32,name='april_account_mgt_ob_ch32'),

    path('view_may_account_details_ob_ch32/',branch32.view_may_account_details_ob_ch32,name='view_may_account_details_ob_ch32'),
    path('may_account_mgt_ob_ch32/<id>', branch32.may_account_mgt_ob_ch32, name='may_account_mgt_ob_ch32'),
    path('view_june_account_details_ob_ch32/', branch32.view_june_account_details_ob_ch32, name='view_june_account_details_ob_ch32'),
    path('june_account_mgt_ob_ch32/<id>',branch32.june_account_mgt_ob_ch32,name='june_account_mgt_ob_ch32'),
    path('view_july_account_details_ob_ch32/', branch32.view_july_account_details_ob_ch32, name='view_july_account_details_ob_ch32'),
    path('july_account_mgt_ob_ch32/<id>',branch32.july_account_mgt_ob_ch32,name='july_account_mgt_ob_ch32'),
    path('view_auguest_account_details_ob_ch32/', branch32.view_auguest_account_details_ob_ch32, name='view_auguest_account_details_ob_ch32'),
    path('auguest_account_mgt_ob_ch32/<id>',branch32.auguest_account_mgt_ob_ch32,name='auguest_account_mgt_ob_ch32'),

    path('view_sept_account_details_ob_ch32/', branch32.view_sept_account_details_ob_ch32, name='view_sept_account_details_ob_ch32'),
    path('sept_account_mgt_ob_ch32/<id>',branch32.sept_account_mgt_ob_ch32,name='sept_account_mgt_ob_ch32'),
    path('view_october_account_details_ob_ch32/', branch32.view_october_account_details_ob_ch32, name='view_october_account_details_ob_ch32'),
    path('october_account_mgt_ob_ch32/<id>',branch32.october_account_mgt_ob_ch32,name='october_account_mgt_ob_ch32'),
    path('view_nov_account_details_ob_ch32/', branch32.view_nov_account_details_ob_ch32, name='view_nov_account_details_ob_ch32'),
    path('nov_account_mgt_ob_ch32/<id>',branch32.nov_account_mgt_ob_ch32,name='nov_account_mgt_ob_ch32'),
    path('view_dec_account_details_ob_ch32/', branch32.view_dec_account_details_ob_ch32, name='view_dec_account_details_ob_ch32'),
    path('dec_account_mgt_ob_ch32/<id>',branch32.dec_account_mgt_ob_ch32,name='dec_account_mgt_ob_ch32'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch32', admin_dashboard_calculations_br32.monthly_details_due_ob_ch32, name='monthly_details_due_ob_ch32'),
    path('monthly_collection_details_ob_ch32/', admin_dashboard_calculations_br32.monthly_collection_details_ob_ch32, name='monthly_collection_details_ob_ch32'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch32/',branch32.guest_all_ob_ch32,name='guest_all_ob_ch32'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category32/', accounts32.view_all_category32, name='view_all_category32'),
    path('create_new_category32/', accounts32.create_new_category32, name='create_new_category32'),
    path('regi_new_category32/', accounts32.regi_new_category32, name='regi_new_category32'),
    path('update_category32/<id>',accounts32.update_category32,name='update_category32'),

    path('delete_category32/<id>', accounts32.delete_category32, name='delete_category32'),
    path('view_all_category_delete32/', accounts32.view_all_category_delete32, name='view_all_category_delete32'),

    path('regi_multiple_new_category32/', accounts32.regi_multiple_new_category32, name='regi_multiple_new_category32'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items32/', accounts32.view_all_items32, name='view_all_items32'),
    path('create_new_item32/', accounts32.create_new_item32, name='create_new_item32'),
    path('regi_new_item32/', accounts32.regi_new_item32, name='regi_new_item32'),
    path('delete_item32/<id>',accounts32.delete_item32,name='delete_item32'),
    path('update_item32/<id>', accounts32.update_item32, name='update_item32'),
    path('view_all_items_delete32/',accounts32.view_all_items_delete32,name='view_all_items_delete32'),

    path('regi_multiple_new_item32/', accounts32.regi_multiple_new_item32, name='regi_multiple_new_item32'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger32/', accounts32.view_all_ledger32, name='view_all_ledger32'),
    path('create_new_ledger32/', accounts32.create_new_ledger32, name='create_new_ledger32'),
    path('regi_new_ledger32/', accounts32.regi_new_ledger32, name='regi_new_ledger32'),
    path('delete_ledger32/<id>',accounts32.delete_ledger32,name='delete_ledger32'),
    path('update_ledger32/<id>',accounts32.update_ledger32,name='update_ledger32'),
    path('view_all_ledger_delete32/',accounts32.view_all_ledger_delete32,name='view_all_ledger_delete32'),

    path('regi_multiple_new_ledger32/', accounts32.regi_multiple_new_ledger32, name='regi_multiple_new_ledger32'),

    ##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book32/', accounts32.view_all_accounts_book32, name='view_all_accounts_book32'),
    path('create_new_accounts_book32/', accounts32.create_new_accounts_book32, name='create_new_accounts_book32'),
    path('regi_new_accounts_book32/', accounts32.regi_new_accounts_book32, name='regi_new_accounts_book32'),
    path('update_accounts_book32/<id>',accounts32.update_accounts_book32,name='update_accounts_book32'),
    path('delete_accounts_book32/<id>',accounts32.delete_accounts_book32,name='delete_accounts_book32'),
    path('view_all_accounts_book_delete32/',accounts32.view_all_accounts_book_delete32,name='view_all_accounts_book_delete32'),

    path('regi_multiple_new_accounts_book32/', accounts32.regi_multiple_new_accounts_book32,name='regi_multiple_new_accounts_book32'),

    ##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries32/', accounts32.get_countries32, name='get_countries32'),

    path('in_exp_items_entry32/', accounts32.in_exp_items_entry32, name='in_exp_items_entry32'),
    path('reg_in_exp_items_entry32/', accounts32.reg_in_exp_items_entry32, name='reg_in_exp_items_entry32'),
    path('delete_journal32/<id>',accounts32.delete_journal32,name='delete_journal32'),
    path('update_in_exp_items_entry32/<id>',accounts32.update_in_exp_items_entry32,name='update_in_exp_items_entry32'),
    path('detailed_journal_report32/',accounts32.detailed_journal_report32,name='detailed_journal_report32'),
    path('journal_report_deleted32/',accounts32.journal_report_deleted32,name='journal_report_deleted32'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise32/', accounts32.daily_category_wise32, name='daily_category_wise32'),
    path('monthly_category_based_reports32/',accounts32.monthly_category_based_reports32,name='monthly_category_based_reports32'),
    path('yearly_category_based_reports32/', accounts32.yearly_category_based_reports32,name='yearly_category_based_reports32'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed32/', accounts32.daily_detailed32, name='daily_detailed32'),
    path('monthly_detailed32/',accounts32.monthly_detailed32,name='monthly_detailed32'),
    path('yearly_detailed32/',accounts32.yearly_detailed32,name='yearly_detailed32'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports32/', accounts32.item_based_reports32, name='item_based_reports32'),
    path('daily_item_based_reports32/',accounts32.daily_item_based_reports32,name='daily_item_based_reports32'),
    path('monthly_item_based_reports32/',accounts32.monthly_item_based_reports32,name='monthly_item_based_reports32'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports32/', accounts32.ledger_based_reports32, name='ledger_based_reports32'),
    path('monthly_ledger_based_reports32/', accounts32.monthly_ledger_based_reports32, name='monthly_ledger_based_reports32'),
    path('daily_ledger_based_reports32/',accounts32.daily_ledger_based_reports32,name='daily_ledger_based_reports32'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports32/', accounts32.accounts_book_based_reports32, name='accounts_book_based_reports32'),
    path('daily_accounts_book_based_reports32/',accounts32.daily_accounts_book_based_reports32,name='daily_accounts_book_based_reports32'),
    path('monthly_accounts_book_based_reports32/',accounts32.monthly_accounts_book_based_reports32,name='monthly_accounts_book_based_reports32'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months32/', accounts32.monthly_reports_choose_months32, name='monthly_reports_choose_months32'),
    path('monthly_detailed_daily_in_exp_items_report32/<mo>',accounts32.monthly_detailed_daily_in_exp_items_report32,name='monthly_detailed_daily_in_exp_items_report32'),

    path('single_monthly_reports_choose_months32/', accounts32.single_monthly_reports_choose_months32,name='single_monthly_reports_choose_months32'),
    path('single_monthly_daily_in_exp_items_report32/<mo>',accounts32.single_monthly_daily_in_exp_items_report32,name='single_monthly_daily_in_exp_items_report32'),

    path('accounts_dash_board_ob_ch32/',accounts32.accounts_dash_board_ob_ch32,name='accounts_dash_board_ob_ch32'),
    path('accounts_dash_board32/',accounts32.accounts_dash_board32,name='accounts_dash_board32'),

    path('profit_sharing_choose_months32', accounts32.profit_sharing_choose_months32,name='profit_sharing_choose_months32'),
    path('profit_sharing32/<mo>', accounts32.profit_sharing32, name='profit_sharing32'),
    path('view_share_holders32', accounts32.view_share_holders32, name='view_share_holders32'),
    path('create_share_holders32', accounts32.create_share_holders32, name='create_share_holders32'),
    path('regi_share_holders32', accounts32.regi_share_holders32, name='regi_share_holders32'),
    path('update_share_holders32/<id>', accounts32.update_share_holders32, name='update_share_holders32'),
    path('delete_share_holders32/<id>', accounts32.delete_share_holders32, name='delete_share_holders32'),
    path('view_deleted_share_holders32', accounts32.view_deleted_share_holders32, name='view_deleted_share_holders32'),

    path('regi_multiple_share_holders32', accounts32.regi_multiple_share_holders32, name='regi_multiple_share_holders32'),

    #############BRANCH SETTINGS START HERE ########################

    path('guest_rent_update_ob_ch32/', branch_settings32.guest_rent_update_ob_ch32, name='guest_rent_update_ob_ch32'),

    ############BRANCH SETTINGS END HERE ############################

]

