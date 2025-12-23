from django.urls import path, include

from . import admin_branch51
from . import branch51
from . import reports51
from . import payment51
from . import admin_dashboard_calculations_br51
from . import accounts51

urlpatterns = [

    path('branch1_dashboard_ob_ch51/', branch51.branch1_dashboard_ob_ch51, name='branch1_dashboard_ob_ch51'),
    path('branch1_dashboard51/',branch51.branch1_dashboard51,name='branch1_dashboard51'),
    path('user_dashboard_calculations_ob_ch51/',branch51.user_dashboard_calculations_ob_ch51,name='user_dashboard_calculations_ob_ch51'),

    path('background_ob_ch51',branch51.background_ob_ch51,name='background_ob_ch51'),
    path('background_regi_ob_ch51',branch51.background_regi_ob_ch51,name='background_regi_ob_ch51'),
    path('custom_background_regi_ob_ch51',branch51.custom_background_regi_ob_ch51,name='custom_background_regi_ob_ch51'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch51/',admin_branch51.branch1_room_create_regi_ob_ch51,name='branch1_room_create_regi_ob_ch51'),
    path('view_all_room_ob_ch51/',admin_branch51.view_all_room_ob_ch51,name='view_all_room_ob_ch51'),
    path('delete_room_ob_ch51/<id>',admin_branch51.delete_room_ob_ch51,name='delete_room_ob_ch51'),

    path('branch1_room_create_ob_ch51/',admin_branch51.branch1_room_create_ob_ch51,name='branch1_room_create_ob_ch51'),

    path('multiple_branch1_room_create_regi51/',admin_branch51.multiple_branch1_room_create_regi51,name='multiple_branch1_room_create_regi51'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch51/', admin_branch51.pg1_bed_create_regi_ob_ch51, name='pg1_bed_create_regi_ob_ch51'),
    path('pg1_view_all_beds_ob_ch51/', admin_branch51.pg1_view_all_beds_ob_ch51, name='pg1_view_all_beds_ob_ch51'),
    path('delete_bed_ob_ch51/<id>', admin_branch51.delete_bed_ob_ch51, name='delete_bed_ob_ch51'),

    path('pg1_bed_create_ob_ch51/', admin_branch51.pg1_bed_create_ob_ch51, name='pg1_bed_create_ob_ch51'),

    path('single_pg1_bed_create_regi_ob_ch51/',admin_branch51.single_pg1_bed_create_regi_ob_ch51,name='single_pg1_bed_create_regi_ob_ch51'),
    path('update_bed_basic_details_ob_ch51/<id>',admin_branch51.update_bed_basic_details_ob_ch51, name='update_bed_basic_details_ob_ch51'),

    path('multiple_single_pg1_bed_create_regi51/',admin_branch51.multiple_single_pg1_bed_create_regi51,name='multiple_single_pg1_bed_create_regi51'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch51/<id>',branch51.br1_admit_guest_ob_ch51,name='br1_admit_guest_ob_ch51'),
    path('view_all_new_guest_ob_ch51/',branch51.view_all_new_guest_ob_ch51,name='view_all_new_guest_ob_ch51'),
    path('update_br1_admit_guest_ob_ch51/<id>',branch51.update_br1_admit_guest_ob_ch51,name='update_br1_admit_guest_ob_ch51'),
    path('vacate_br1_guest_ob_ch51/<id>',branch51.vacate_br1_guest_ob_ch51,name='vacate_br1_guest_ob_ch51'),

    path('active_guest_details_ob_ch51/<guest_code>',branch51.active_guest_details_ob_ch51,name='active_guest_details_ob_ch51'),
    path('view_all_guest_ob_ch51/',branch51.view_all_guest_ob_ch51,name='view_all_guest_ob_ch51'),
    path('shift_guest_ob_ch51/<id>',branch51.shift_guest_ob_ch51,name='shift_guest_ob_ch51'),
    path('shift_guest_regi_ob_ch51/',branch51.shift_guest_regi_ob_ch51,name='shift_guest_regi_ob_ch51'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch51/',branch51.update_all_rent_ob_ch51,name='update_all_rent_ob_ch51'),

    path('multiple_br1_admit_guest51/<id>',branch51.multiple_br1_admit_guest51,name='multiple_br1_admit_guest51'),

#guest end here


##################################
#_ADVANCE_ob_ch51 START HERE
################################


    path('choose_months_advance_ob_ch51/',branch51.choose_months_advance_ob_ch51,name='choose_months_advance_ob_ch51'),

    path('jan_advance_ob_ch51/', branch51.jan_advance_ob_ch51, name='jan_advance_ob_ch51'),
    path('jan_make_payments_advance_ob_ch51/<id>', branch51.jan_make_payments_advance_ob_ch51,name='jan_make_payments_advance_ob_ch51'),
    path('feb_advance_ob_ch51/', branch51.feb_advance_ob_ch51, name='feb_advance_ob_ch51'),
    path('feb_make_payments_advance_ob_ch51/<id>', branch51.feb_make_payments_advance_ob_ch51,name='feb_make_payments_advance_ob_ch51'),
    path('march_advance_ob_ch51/', branch51.march_advance_ob_ch51, name='march_advance_ob_ch51'),
    path('march_make_payments_advance_ob_ch51/<id>', branch51.march_make_payments_advance_ob_ch51,name='march_make_payments_advance_ob_ch51'),
    path('april_advance_ob_ch51/', branch51.april_advance_ob_ch51, name='april_advance_ob_ch51'),
    path('april_make_payments_advance_ob_ch51/<id>', branch51.april_make_payments_advance_ob_ch51, name='april_make_payments_advance_ob_ch51'),

    path('may_advance_ob_ch51/',branch51.may_advance_ob_ch51,name='may_advance_ob_ch51'),
    path('may_make_payments_advance_ob_ch51/<id>', branch51.may_make_payments_advance_ob_ch51, name='may_make_payments_advance_ob_ch51'),
    path('june_advance_ob_ch51/',branch51.june_advance_ob_ch51,name='june_advance_ob_ch51'),
    path('june_make_payments_advance_ob_ch51/<id>', branch51.june_make_payments_advance_ob_ch51, name='june_make_payments_advance_ob_ch51'),
    path('july_advance_ob_ch51/',branch51.july_advance_ob_ch51,name='july_advance_ob_ch51'),
    path('july_make_payments_advance_ob_ch51/<id>', branch51.july_make_payments_advance_ob_ch51, name='july_make_payments_advance_ob_ch51'),
    path('auguest_advance_ob_ch51/', branch51.auguest_advance_ob_ch51, name='auguest_advance_ob_ch51'),
    path('auguest_make_payments_advance_ob_ch51/<id>', branch51.auguest_make_payments_advance_ob_ch51, name='auguest_make_payments_advance_ob_ch51'),

    path('sept_advance_ob_ch51/', branch51.sept_advance_ob_ch51, name='sept_advance_ob_ch51'),
    path('sept_make_payments_advance_ob_ch51/<id>', branch51.sept_make_payments_advance_ob_ch51,name='sept_make_payments_advance_ob_ch51'),
    path('october_advance_ob_ch51/', branch51.october_advance_ob_ch51, name='october_advance_ob_ch51'),
    path('october_make_payments_advance_ob_ch51/<id>', branch51.october_make_payments_advance_ob_ch51, name='october_make_payments_advance_ob_ch51'),
    path('nov_advance_ob_ch51/', branch51.nov_advance_ob_ch51, name='nov_advance_ob_ch51'),
    path('nov_make_payments_advance_ob_ch51/<id>', branch51.nov_make_payments_advance_ob_ch51,name='nov_make_payments_advance_ob_ch51'),
    path('dec_advance_ob_ch51/', branch51.dec_advance_ob_ch51, name='dec_advance_ob_ch51'),
    path('dec_make_payments_advance_ob_ch51/<id>', branch51.dec_make_payments_advance_ob_ch51, name='dec_make_payments_advance_ob_ch51'),



##################################
#_ADVANCE_ob_ch51 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch51/',branch51.choose_months_ob_ch51,name='choose_months_ob_ch51'),

    path('jan_ob_ch51/',branch51.jan_ob_ch51,name='jan_ob_ch51'),
    path('jan_manke_payments_ob_ch51/<id>',branch51.jan_manke_payments_ob_ch51,name='jan_manke_payments_ob_ch51'),

    path('feb_ob_ch51/',branch51.feb_ob_ch51,name='feb_ob_ch51'),
    path('feb_manke_payments_ob_ch51/<id>',branch51.feb_manke_payments_ob_ch51,name='feb_manke_payments_ob_ch51'),

    path('march_ob_ch51/',branch51.march_ob_ch51,name='march_ob_ch51'),
    path('march_manke_payments_ob_ch51/<id>',branch51.march_manke_payments_ob_ch51,name='march_manke_payments_ob_ch51'),

    path('april_ob_ch51/',branch51.april_ob_ch51,name='april_ob_ch51'),
    path('april_make_payments_ob_ch51/<id>',branch51.april_make_payments_ob_ch51,name='april_make_payments_ob_ch51'),

    path('may_ob_ch51/',branch51.may_ob_ch51,name='may_ob_ch51'),
    path('may_make_payments_ob_ch51/<id>',branch51.may_make_payments_ob_ch51,name='may_make_payments_ob_ch51'),

    path('june_ob_ch51/',branch51.june_ob_ch51,name='june_ob_ch51'),
    path('june_make_payments_ob_ch51/<id>',branch51.june_make_payments_ob_ch51,name='june_make_payments_ob_ch51'),

    path('july_ob_ch51/',branch51.july_ob_ch51,name='july_ob_ch51'),
    path('july_make_payments_ob_ch51/<id>',branch51.july_make_payments_ob_ch51,name='july_make_payments_ob_ch51'),

    path('aug_ob_ch51/',branch51.aug_ob_ch51,name='aug_ob_ch51'),
    path('aug_make_payments_ob_ch51/<id>',branch51.aug_make_payments_ob_ch51,name='aug_make_payments_ob_ch51'),

    path('sept_ob_ch51/',branch51.sept_ob_ch51,name='sept_ob_ch51'),
    path('sept_make_payments_ob_ch51/<id>',branch51.sept_make_payments_ob_ch51,name='sept_make_payments_ob_ch51'),

    path('oct_ob_ch51/',branch51.oct_ob_ch51,name='oct_ob_ch51'),
    path('oct_make_payments_ob_ch51/<id>',branch51.oct_make_payments_ob_ch51,name='oct_make_payments_ob_ch51'),

    path('nov_ob_ch51/',branch51.nov_ob_ch51,name='nov_ob_ch51'),
    path('nov_make_payments_ob_ch51/<id>',branch51.nov_make_payments_ob_ch51,name='nov_make_payments_ob_ch51'),

    path('dec_ob_ch51/',branch51.dec_ob_ch51,name='dec_ob_ch51'),
    path('dec_make_payments_ob_ch51/<id>',branch51.dec_make_payments_ob_ch51,name='dec_make_payments_ob_ch51'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch51/', payment51.choose_user_ob_ch51, name='choose_user_ob_ch51'),
    path('payment_user_details_ob_ch51/<id>', payment51.payment_user_details_ob_ch51, name='payment_user_details_ob_ch51'),
    path('close_choose_user_ob_ch51/<id>',payment51.close_choose_user_ob_ch51,name='close_choose_user_ob_ch51'),

    path('monthly_jan_make_payments_ob_ch51/<id>', payment51.monthly_jan_make_payments_ob_ch51, name='monthly_jan_make_payments_ob_ch51'),
    path('monthly_feb_make_payments_ob_ch51/<id>', payment51.monthly_feb_make_payments_ob_ch51, name='monthly_feb_make_payments_ob_ch51'),
    path('monthly_march_make_payments_ob_ch51/<id>', payment51.monthly_march_make_payments_ob_ch51, name='monthly_march_make_payments_ob_ch51'),
    path('monthly_april_make_payments_ob_ch51/<id>', payment51.monthly_april_make_payments_ob_ch51, name='monthly_april_make_payments_ob_ch51'),
    path('monthly_may_make_payments_ob_ch51/<id>', payment51.monthly_may_make_payments_ob_ch51, name='monthly_may_make_payments_ob_ch51'),
    path('monthly_june_make_payments_ob_ch51/<id>', payment51.monthly_june_make_payments_ob_ch51, name='monthly_june_make_payments_ob_ch51'),

    path('monthly_july_make_payments_ob_ch51/<id>', payment51.monthly_july_make_payments_ob_ch51, name='monthly_july_make_payments_ob_ch51'),
    path('monthly_aug_make_payments_ob_ch51/<id>', payment51.monthly_aug_make_payments_ob_ch51, name='monthly_aug_make_payments_ob_ch51'),
    path('monthly_sept_make_payments_ob_ch51/<id>', payment51.monthly_sept_make_payments_ob_ch51, name='monthly_sept_make_payments_ob_ch51'),
    path('monthly_oct_make_payments_ob_ch51/<id>', payment51.monthly_oct_make_payments_ob_ch51, name='monthly_oct_make_payments_ob_ch51'),
    path('monthly_nov_make_payments_ob_ch51/<id>', payment51.monthly_nov_make_payments_ob_ch51, name='monthly_nov_make_payments_ob_ch51'),
    path('monthly_dec_make_payments_ob_ch51/<id>', payment51.monthly_dec_make_payments_ob_ch51, name='monthly_dec_make_payments_ob_ch51'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch51/',branch51.unpaid_rent_choose_months_ob_ch51,name='unpaid_rent_choose_months_ob_ch51'),

    path('jan_unpaid_rent_ob_ch51/', branch51.jan_unpaid_rent_ob_ch51, name='jan_unpaid_rent_ob_ch51'),
    path('table_jan_unpaid_rent_ob_ch51/', branch51.table_jan_unpaid_rent_ob_ch51, name='table_jan_unpaid_rent_ob_ch51'),
    path('feb_unpaid_rent_ob_ch51/', branch51.feb_unpaid_rent_ob_ch51, name='feb_unpaid_rent_ob_ch51'),
    path('table_feb_unpaid_rent_ob_ch51/', branch51.table_feb_unpaid_rent_ob_ch51, name='table_feb_unpaid_rent_ob_ch51'),
    path('mar_unpaid_rent_ob_ch51/', branch51.mar_unpaid_rent_ob_ch51, name='mar_unpaid_rent_ob_ch51'),
    path('table_mar_unpaid_rent_ob_ch51/', branch51.table_mar_unpaid_rent_ob_ch51, name='table_mar_unpaid_rent_ob_ch51'),
    path('april_unpaid_rent_ob_ch51/', branch51.april_unpaid_rent_ob_ch51, name='april_unpaid_rent_ob_ch51'),
    path('table_april_unpaid_rent_ob_ch51/', branch51.table_april_unpaid_rent_ob_ch51, name='table_april_unpaid_rent_ob_ch51'),

    path('may_unpaid_rent_ob_ch51/', branch51.may_unpaid_rent_ob_ch51, name='may_unpaid_rent_ob_ch51'),
    path('table_may_unpaid_rent_ob_ch51/', branch51.table_may_unpaid_rent_ob_ch51, name='table_may_unpaid_rent_ob_ch51'),
    path('june_unpaid_rent_ob_ch51/', branch51.june_unpaid_rent_ob_ch51, name='june_unpaid_rent_ob_ch51'),
    path('table_june_unpaid_rent_ob_ch51/', branch51.table_june_unpaid_rent_ob_ch51, name='table_june_unpaid_rent_ob_ch51'),
    path('july_unpaid_rent_ob_ch51/', branch51.july_unpaid_rent_ob_ch51, name='july_unpaid_rent_ob_ch51'),
    path('table_july_unpaid_rent_ob_ch51',branch51.table_july_unpaid_rent_ob_ch51,name='table_july_unpaid_rent_ob_ch51'),
    path('aug_unpaid_rent_ob_ch51/', branch51.aug_unpaid_rent_ob_ch51, name='aug_unpaid_rent_ob_ch51'),
    path('table_aug_unpaid_rent_ob_ch51/',branch51.table_aug_unpaid_rent_ob_ch51,name='table_aug_unpaid_rent_ob_ch51'),

    path('sept_unpaid_rent_ob_ch51/', branch51.sept_unpaid_rent_ob_ch51, name='sept_unpaid_rent_ob_ch51'),
    path('table_sept_unpaid_rent_ob_ch51/', branch51.table_sept_unpaid_rent_ob_ch51, name='table_sept_unpaid_rent_ob_ch51'),
    path('oct_unpaid_rent_ob_ch51/', branch51.oct_unpaid_rent_ob_ch51, name='oct_unpaid_rent_ob_ch51'),
    path('table_oct_unpaid_rent_ob_ch51/', branch51.table_oct_unpaid_rent_ob_ch51, name='table_oct_unpaid_rent_ob_ch51'),
    path('nov_unpaid_rent_ob_ch51/', branch51.nov_unpaid_rent_ob_ch51, name='nov_unpaid_rent_ob_ch51'),
    path('table_nov_unpaid_rent_ob_ch51/', branch51.table_nov_unpaid_rent_ob_ch51, name='table_nov_unpaid_rent_ob_ch51'),
    path('dec_unpaid_rent_ob_ch51/', branch51.dec_unpaid_rent_ob_ch51, name='dec_unpaid_rent_ob_ch51'),
    path('table_dec_unpaid_rent_ob_ch51/', branch51.table_dec_unpaid_rent_ob_ch51, name='table_dec_unpaid_rent_ob_ch51'),

    path('details_of_unpaid_guests_ob_ch51/<id>',branch51.details_of_unpaid_guests_ob_ch51,name='details_of_unpaid_guests_ob_ch51'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch51/',branch51.paid_rent_choose_months_ob_ch51,name='paid_rent_choose_months_ob_ch51'),
    path('partially_paid_guest_choose_months_ob_ch51/',reports51.partially_paid_guest_choose_months_ob_ch51,name='partially_paid_guest_choose_months_ob_ch51'),

    path('jan_paid_rent_ob_ch51/', branch51.jan_paid_rent_ob_ch51, name='jan_paid_rent_ob_ch51'),
    path('table_jan_paid_rent_ob_ch51/', branch51.table_jan_paid_rent_ob_ch51, name='table_jan_paid_rent_ob_ch51'),
    path('jan_full_paid_guest_ob_ch51/', reports51.jan_full_paid_guest_ob_ch51, name='jan_full_paid_guest_ob_ch51'),
    path('jan_partially_paid_guest_ob_ch51/', reports51.jan_partially_paid_guest_ob_ch51, name='jan_partially_paid_guest_ob_ch51'),
    path('table_jan_partially_paid_guest_ob_ch51/', reports51.table_jan_partially_paid_guest_ob_ch51,name='table_jan_partially_paid_guest_ob_ch51'),

    path('feb_paid_rent_ob_ch51/', branch51.feb_paid_rent_ob_ch51, name='feb_paid_rent_ob_ch51'),
    path('table_feb_paid_rent_ob_ch51/', branch51.table_feb_paid_rent_ob_ch51, name='table_feb_paid_rent_ob_ch51'),
    path('feb_full_paid_guest_ob_ch51/', reports51.feb_full_paid_guest_ob_ch51, name='feb_full_paid_guest_ob_ch51'),
    path('feb_partially_paid_guest_ob_ch51/', reports51.feb_partially_paid_guest_ob_ch51, name='feb_partially_paid_guest_ob_ch51'),
    path('table_feb_partially_paid_guest_ob_ch51/', reports51.table_feb_partially_paid_guest_ob_ch51,name='table_feb_partially_paid_guest_ob_ch51'),

    path('mar_paid_rent_ob_ch51/', branch51.mar_paid_rent_ob_ch51, name='mar_paid_rent_ob_ch51'),
    path('table_mar_paid_rent_ob_ch51/', branch51.table_mar_paid_rent_ob_ch51, name='table_mar_paid_rent_ob_ch51'),
    path('march_full_paid_guest_ob_ch51/', reports51.march_full_paid_guest_ob_ch51, name='march_full_paid_guest_ob_ch51'),
    path('march_partially_paid_guest_ob_ch51/', reports51.march_partially_paid_guest_ob_ch51, name='march_partially_paid_guest_ob_ch51'),
    path('table_march_partially_paid_guest_ob_ch51/', reports51.table_march_partially_paid_guest_ob_ch51,name='table_march_partially_paid_guest_ob_ch51'),

    path('april_paid_rent_ob_ch51/', branch51.april_paid_rent_ob_ch51, name='april_paid_rent_ob_ch51'),
    path('table_april_paid_rent_ob_ch51/', branch51.table_april_paid_rent_ob_ch51, name='table_april_paid_rent_ob_ch51'),
    path('april_full_paid_guest_ob_ch51/', reports51.april_full_paid_guest_ob_ch51, name='april_full_paid_guest_ob_ch51'),
    path('april_partially_paid_guest_ob_ch51/', reports51.april_partially_paid_guest_ob_ch51, name='april_partially_paid_guest_ob_ch51'),
    path('table_april_partially_paid_guest_ob_ch51/', reports51.table_april_partially_paid_guest_ob_ch51,name='table_april_partially_paid_guest_ob_ch51'),

    path('may_paid_rent_ob_ch51/', branch51.may_paid_rent_ob_ch51, name='may_paid_rent_ob_ch51'),
    path('table_may_paid_rent_ob_ch51/', branch51.table_may_paid_rent_ob_ch51, name='table_may_paid_rent_ob_ch51'),
    path('may_full_paid_guest_ob_ch51/', reports51.may_full_paid_guest_ob_ch51, name='may_full_paid_guest_ob_ch51'),
    path('may_partially_paid_guest_ob_ch51/', reports51.may_partially_paid_guest_ob_ch51, name='may_partially_paid_guest_ob_ch51'),
    path('table_may_partially_paid_guest_ob_ch51/', reports51.table_may_partially_paid_guest_ob_ch51, name='table_may_partially_paid_guest_ob_ch51'),

    path('june_paid_rent_ob_ch51/', branch51.june_paid_rent_ob_ch51, name='june_paid_rent_ob_ch51'),
    path('table_june_paid_rent_ob_ch51/', branch51.table_june_paid_rent_ob_ch51, name='table_june_paid_rent_ob_ch51'),
    path('june_full_paid_guest_ob_ch51/', reports51.june_full_paid_guest_ob_ch51, name='june_full_paid_guest_ob_ch51'),
    path('june_partially_paid_guest_ob_ch51/', reports51.june_partially_paid_guest_ob_ch51, name='june_partially_paid_guest_ob_ch51'),
    path('table_june_partially_paid_guest_ob_ch51/', reports51.table_june_partially_paid_guest_ob_ch51, name='table_june_partially_paid_guest_ob_ch51'),

    path('july_paid_rent_ob_ch51/', branch51.july_paid_rent_ob_ch51, name='july_paid_rent_ob_ch51'),
    path('table_july_paid_rent_ob_ch51/', branch51.table_july_paid_rent_ob_ch51, name='table_july_paid_rent_ob_ch51'),
    path('july_full_paid_guest_ob_ch51/', reports51.july_full_paid_guest_ob_ch51, name='july_full_paid_guest_ob_ch51'),
    path('july_partially_paid_guest_ob_ch51/', reports51.july_partially_paid_guest_ob_ch51, name='july_partially_paid_guest_ob_ch51'),
    path('table_july_partially_paid_guest_ob_ch51/', reports51.table_july_partially_paid_guest_ob_ch51, name='table_july_partially_paid_guest_ob_ch51'),

    path('aug_paid_rent_ob_ch51/', branch51.aug_paid_rent_ob_ch51, name='aug_paid_rent_ob_ch51'),
    path('table_aug_paid_rent_ob_ch51/', branch51.table_aug_paid_rent_ob_ch51, name='table_aug_paid_rent_ob_ch51'),
    path('auguest_full_paid_guest_ob_ch51/', reports51.auguest_full_paid_guest_ob_ch51, name='auguest_full_paid_guest_ob_ch51'),
    path('auguest_partially_paid_guest_ob_ch51/', reports51.auguest_partially_paid_guest_ob_ch51,name='auguest_partially_paid_guest_ob_ch51'),
    path('table_auguest_partially_paid_guest_ob_ch51/', reports51.table_auguest_partially_paid_guest_ob_ch51,name='table_auguest_partially_paid_guest_ob_ch51'),

    path('sept_paid_rent_ob_ch51/', branch51.sept_paid_rent_ob_ch51, name='sept_paid_rent_ob_ch51'),
    path('table_sept_paid_rent_ob_ch51/', branch51.table_sept_paid_rent_ob_ch51, name='table_sept_paid_rent_ob_ch51'),
    path('sept_full_paid_guest_ob_ch51/', reports51.sept_full_paid_guest_ob_ch51, name='sept_full_paid_guest_ob_ch51'),
    path('sept_partially_paid_guest_ob_ch51/', reports51.sept_partially_paid_guest_ob_ch51, name='sept_partially_paid_guest_ob_ch51'),
    path('table_sept_partially_paid_guest_ob_ch51/', reports51.table_sept_partially_paid_guest_ob_ch51,name='table_sept_partially_paid_guest_ob_ch51'),

    path('oct_paid_rent_ob_ch51/', branch51.oct_paid_rent_ob_ch51, name='oct_paid_rent_ob_ch51'),
    path('table_oct_paid_rent_ob_ch51/', branch51.table_oct_paid_rent_ob_ch51, name='table_oct_paid_rent_ob_ch51'),
    path('october_full_paid_guest_ob_ch51/', reports51.october_full_paid_guest_ob_ch51, name='october_full_paid_guest_ob_ch51'),
    path('october_partially_paid_guest_ob_ch51/', reports51.october_partially_paid_guest_ob_ch51,name='october_partially_paid_guest_ob_ch51'),
    path('table_october_partially_paid_guest_ob_ch51/', reports51.table_october_partially_paid_guest_ob_ch51,name='table_october_partially_paid_guest_ob_ch51'),

    path('nov_paid_rent_ob_ch51/', branch51.nov_paid_rent_ob_ch51, name='nov_paid_rent_ob_ch51'),
    path('table_nov_paid_rent_ob_ch51/', branch51.table_nov_paid_rent_ob_ch51, name='table_nov_paid_rent_ob_ch51'),
    path('nov_full_paid_guest_ob_ch51/', reports51.nov_full_paid_guest_ob_ch51, name='nov_full_paid_guest_ob_ch51'),
    path('nov_partially_paid_guest_ob_ch51/', reports51.nov_partially_paid_guest_ob_ch51, name='nov_partially_paid_guest_ob_ch51'),
    path('table_nov_partially_paid_guest_ob_ch51/', reports51.table_nov_partially_paid_guest_ob_ch51,name='table_nov_partially_paid_guest_ob_ch51'),

    path('dec_paid_rent_ob_ch51/', branch51.dec_paid_rent_ob_ch51, name='dec_paid_rent_ob_ch51'),
    path('table_dec_paid_rent_ob_ch51/', branch51.table_dec_paid_rent_ob_ch51, name='table_dec_paid_rent_ob_ch51'),
    path('dec_full_paid_guest_ob_ch51/', reports51.dec_full_paid_guest_ob_ch51, name='dec_full_paid_guest_ob_ch51'),
    path('dec_partially_paid_guest_ob_ch51/', reports51.dec_partially_paid_guest_ob_ch51, name='dec_partially_paid_guest_ob_ch51'),
    path('table_dec_partially_paid_guest_ob_ch51/', reports51.table_dec_partially_paid_guest_ob_ch51,name='table_dec_partially_paid_guest_ob_ch51'),

    path('details_of_paid_guests_ob_ch51/<id>',branch51.details_of_paid_guests_ob_ch51,name='details_of_paid_guests_ob_ch51'),
    path('full_paid_guest_ob_ch51/',reports51.full_paid_guest_ob_ch51,name='full_paid_guest_ob_ch51'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch51/',branch51.viewall_vacate_guest_ob_ch51,name='viewall_vacate_guest_ob_ch51'),
    path('details_of_vacate_guest_ob_ch51/<id>',branch51.details_of_vacate_guest_ob_ch51,name='details_of_vacate_guest_ob_ch51'),
    path('full_vacated_guest_details_ob_ch51',branch51.full_vacated_guest_details_ob_ch51,name='full_vacated_guest_details_ob_ch51'),
    path('full_vacated_guest_table_ob_ch51',branch51.full_vacated_guest_table_ob_ch51,name='full_vacated_guest_table_ob_ch51'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch51/<id>', branch51.jan_manke_payments_vacate_ob_ch51, name='jan_manke_payments_vacate_ob_ch51'),
    path('feb_manke_payments_vacate_ob_ch51/<id>', branch51.feb_manke_payments_vacate_ob_ch51, name='feb_manke_payments_vacate_ob_ch51'),
    path('march_manke_payments_vacate_ob_ch51/<id>', branch51.march_manke_payments_vacate_ob_ch51, name='march_manke_payments_vacate_ob_ch51'),
    path('april_make_payments_vacate_ob_ch51/<id>', branch51.april_make_payments_vacate_ob_ch51, name='april_make_payments_vacate_ob_ch51'),

    path('may_make_payments_vacate_ob_ch51/<id>', branch51.may_make_payments_vacate_ob_ch51, name='may_make_payments_vacate_ob_ch51'),
    path('june_make_payments_vacate_ob_ch51/<id>', branch51.june_make_payments_vacate_ob_ch51, name='june_make_payments_vacate_ob_ch51'),
    path('july_make_payments_vacate_ob_ch51/<id>', branch51.july_make_payments_vacate_ob_ch51, name='july_make_payments_vacate_ob_ch51'),
    path('aug_make_payments_vacate_ob_ch51/<id>', branch51.aug_make_payments_vacate_ob_ch51, name='aug_make_payments_vacate_ob_ch51'),

    path('sept_make_payments_vacate_ob_ch51/<id>', branch51.sept_make_payments_vacate_ob_ch51, name='sept_make_payments_vacate_ob_ch51'),
    path('oct_make_payments_vacate_ob_ch51/<id>', branch51.oct_make_payments_vacate_ob_ch51, name='oct_make_payments_vacate_ob_ch51'),
    path('nov_make_payments_vacate_ob_ch51/<id>', branch51.nov_make_payments_vacate_ob_ch51, name='nov_make_payments_vacate_ob_ch51'),
    path('dec_make_payments_vacate_ob_ch51/<id>', branch51.dec_make_payments_vacate_ob_ch51, name='dec_make_payments_vacate_ob_ch51'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch51/',branch51.detail_guest_general_ob_ch51,name='detail_guest_general_ob_ch51'),

    path('jan_print_ob_ch51/',branch51.jan_print_ob_ch51,name='jan_print_ob_ch51'),
    path('feb_print_ob_ch51/',branch51.feb_print_ob_ch51,name='feb_print_ob_ch51'),
    path('march_print_ob_ch51/',branch51.march_print_ob_ch51,name='march_print_ob_ch51'),
    path('april_print_ob_ch51/',branch51.april_print_ob_ch51,name='april_print_ob_ch51'),

    path('may_print_ob_ch51/',branch51.may_print_ob_ch51,name='may_print_ob_ch51'),
    path('june_print_ob_ch51/',branch51.june_print_ob_ch51,name='june_print_ob_ch51'),
    path('july_print_ob_ch51/', branch51.july_print_ob_ch51, name='july_print_ob_ch51'),
    path('aug_print_ob_ch51/', branch51.aug_print_ob_ch51, name='aug_print_ob_ch51'),

    path('sept_print_ob_ch51/', branch51.sept_print_ob_ch51, name='sept_print_ob_ch51'),
    path('oct_print_ob_ch51/', branch51.oct_print_ob_ch51, name='oct_print_ob_ch51'),
    path('nov_print_ob_ch51/', branch51.nov_print_ob_ch51, name='nov_print_ob_ch51'),
    path('dec_print_ob_ch51/', branch51.dec_print_ob_ch51, name='dec_print_ob_ch51'),

    path('new_year_jan_print_ob_ch51/', branch51.new_year_jan_print_ob_ch51, name='new_year_jan_print_ob_ch51'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch51/', branch51.jan_close_ob_ch51, name='jan_close_ob_ch51'),
    path('jan_close_decision_page_ob_ch51/', branch51.jan_close_decision_page_ob_ch51, name='jan_close_decision_page_ob_ch51'),
    path('feb_close/', branch51.feb_close_ob_ch51, name='feb_close_ob_ch51'),
    path('feb_close_decision_page_ob_ch51/', branch51.feb_close_decision_page_ob_ch51, name='feb_close_decision_page_ob_ch51'),
    path('mar_close_ob_ch51/', branch51.mar_close_ob_ch51, name='mar_close_ob_ch51'),
    path('mar_close_decision_page/', branch51.mar_close_decision_page_ob_ch51, name='mar_close_decision_page_ob_ch51'),
    path('apr_close_ob_ch51/', branch51.apr_close_ob_ch51, name='apr_close_ob_ch51'),
    path('apr_close_decision_page_ob_ch51/', branch51.apr_close_decision_page_ob_ch51, name='apr_close_decision_page_ob_ch51'),

    path('may_close_ob_ch51/', branch51.may_close_ob_ch51, name='may_close_ob_ch51'),
    path('may_close_decision_page_ob_ch51/', branch51.may_close_decision_page_ob_ch51, name='may_close_decision_page_ob_ch51'),
    path('jun_close_ob_ch51/', branch51.jun_close_ob_ch51, name='jun_close_ob_ch51'),
    path('jun_close_decision_page_ob_ch51/', branch51.jun_close_decision_page_ob_ch51, name='jun_close_decision_page_ob_ch51'),
    path('jul_close_ob_ch51/', branch51.jul_close_ob_ch51, name='jul_close_ob_ch51'),
    path('jul_close_decision_page_ob_ch51/', branch51.jul_close_decision_page_ob_ch51, name='jul_close_decision_page_ob_ch51'),
    path('aug_close_ob_ch51/', branch51.aug_close_ob_ch51, name='aug_close_ob_ch51'),
    path('aug_close_decision_page_ob_ch51/', branch51.aug_close_decision_page_ob_ch51, name='aug_close_decision_page_ob_ch51'),

    path('sep_close_ob_ch51/', branch51.sep_close_ob_ch51, name='sep_close_ob_ch51'),
    path('sep_close_decision_page_ob_ch51/', branch51.sep_close_decision_page_ob_ch51, name='sep_close_decision_page_ob_ch51'),
    path('oct_close_ob_ch51/', branch51.oct_close_ob_ch51, name='oct_close_ob_ch51'),
    path('oct_close_decision_page_ob_ch51/', branch51.oct_close_decision_page_ob_ch51, name='oct_close_decision_page_ob_ch51'),
    path('nov_close_ob_ch51/', branch51.nov_close_ob_ch51, name='nov_close_ob_ch51'),
    path('nov_close_decision_page_ob_ch51/', branch51.nov_close_decision_page_ob_ch51, name='nov_close_decision_page_ob_ch51'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch51/',reports51.detailed_report_choose_months_ob_ch51,name='detailed_report_choose_months_ob_ch51'),

    path('jan_details_live_ob_ch51/', reports51.jan_details_live_ob_ch51, name='jan_details_live_ob_ch51'),
    path('jan_print_live_ob_ch51/', reports51.jan_print_live_ob_ch51, name='jan_print_live_ob_ch51'),
    path('feb_details_live_ob_ch51/', reports51.feb_details_live_ob_ch51, name='feb_details_live_ob_ch51'),
    path('feb_print_live_ob_ch51/', reports51.feb_print_live_ob_ch51, name='feb_print_live_ob_ch51'),
    path('march_details_live_ob_ch51/', reports51.march_details_live_ob_ch51, name='march_details_live_ob_ch51'),
    path('march_print_live_ob_ch51/', reports51.march_print_live_ob_ch51, name='march_print_live_ob_ch51'),

    path('april_details_live_ob_ch51/', reports51.april_details_live_ob_ch51, name='april_details_live_ob_ch51'),
    path('april_print_live_ob_ch51/', reports51.april_print_live_ob_ch51, name='april_print_live_ob_ch51'),
    path('may_details_live_ob_ch51/', reports51.may_details_live_ob_ch51, name='may_details_live_ob_ch51'),
    path('may_print_live_ob_ch51/', reports51.may_print_live_ob_ch51, name='may_print_live_ob_ch51'),
    path('june_details_live_ob_ch51/',reports51.june_details_live_ob_ch51,name='june_details_live_ob_ch51'),
    path('june_print_live_ob_ch51/', reports51.june_print_live_ob_ch51, name='june_print_live_ob_ch51'),

    path('july_details_live_ob_ch51/', reports51.july_details_live_ob_ch51, name='july_details_live_ob_ch51'),
    path('july_print_live_ob_ch51/', reports51.july_print_live_ob_ch51, name='july_print_live_ob_ch51'),
    path('auguest_details_live_ob_ch51/', reports51.auguest_details_live_ob_ch51, name='auguest_details_live_ob_ch51'),
    path('auguest_print_live_ob_ch51/', reports51.auguest_print_live_ob_ch51, name='auguest_print_live_ob_ch51'),
    path('sept_details_live_ob_ch51/', reports51.sept_details_live_ob_ch51, name='sept_details_live_ob_ch51'),
    path('sept_print_live_ob_ch51/', reports51.sept_print_live_ob_ch51, name='sept_print_live_ob_ch51'),

    path('october_details_live_ob_ch51/', reports51.october_details_live_ob_ch51, name='october_details_live_ob_ch51'),
    path('october_print_live_ob_ch51/', reports51.october_print_live_ob_ch51, name='october_print_live_ob_ch51'),
    path('nov_details_live_ob_ch51/', reports51.nov_details_live_ob_ch51, name='nov_details_live_ob_ch51'),
    path('nov_print_live_ob_ch51/', reports51.nov_print_live_ob_ch51, name='nov_print_live_ob_ch51'),
    path('dec_details_live_ob_ch51/', reports51.dec_details_live_ob_ch51, name='dec_details_live_ob_ch51'),
    path('dec_print_live_ob_ch51/', reports51.dec_print_live_ob_ch51, name='dec_print_live_ob_ch51'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch51/', reports51.viewall_vaccant_room_ob_ch51, name='viewall_vaccant_room_ob_ch51'),

    path('d_ob_ch51/', branch51.dynamic, name='dynamic'),

    path('manage_bed_ob_ch51/', branch51.manage_bed_ob_ch51, name='manage_bed_ob_ch51'),
    path('manage_new_guest_ob_ch51/', branch51.manage_new_guest_ob_ch51, name='manage_new_guest_ob_ch51'),
    path('manage_update_new_guest_ob_ch51/<id>', branch51.manage_update_new_guest_ob_ch51, name='manage_update_new_guest_ob_ch51'),
    path('manage_update_beds_ob_ch51/<id>', branch51.manage_update_beds_ob_ch51, name='manage_update_beds_ob_ch51'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch51/', branch51.view_all_due_amt_ob_ch51, name='view_all_due_amt_ob_ch51'),
    path('due_amt_mgt_choose_months_ob_ch51/', branch51.due_amt_mgt_choose_months_ob_ch51, name='due_amt_mgt_choose_months_ob_ch51'),

    path('view_jan_account_details_ob_ch51/', branch51.view_jan_account_details_ob_ch51, name='view_jan_account_details_ob_ch51'),
    path('jan_account_mgt_ob_ch51/<id>',branch51.jan_account_mgt_ob_ch51,name='jan_account_mgt_ob_ch51'),
    path('view_feb_account_details_ob_ch51/', branch51.view_feb_account_details_ob_ch51, name='view_feb_account_details_ob_ch51'),
    path('feb_account_mgt_ob_ch51/<id>',branch51.feb_account_mgt_ob_ch51,name='feb_account_mgt_ob_ch51'),
    path('view_march_account_details_ob_ch51/', branch51.view_march_account_details_ob_ch51, name='view_march_account_details_ob_ch51'),
    path('march_account_mgt_ob_ch51/<id>',branch51.march_account_mgt_ob_ch51,name='march_account_mgt_ob_ch51'),
    path('view_april_account_details_ob_ch51/', branch51.view_april_account_details_ob_ch51, name='view_april_account_details_ob_ch51'),
    path('april_account_mgt_ob_ch51/<id>',branch51.april_account_mgt_ob_ch51,name='april_account_mgt_ob_ch51'),

    path('view_may_account_details_ob_ch51/',branch51.view_may_account_details_ob_ch51,name='view_may_account_details_ob_ch51'),
    path('may_account_mgt_ob_ch51/<id>', branch51.may_account_mgt_ob_ch51, name='may_account_mgt_ob_ch51'),
    path('view_june_account_details_ob_ch51/', branch51.view_june_account_details_ob_ch51, name='view_june_account_details_ob_ch51'),
    path('june_account_mgt_ob_ch51/<id>',branch51.june_account_mgt_ob_ch51,name='june_account_mgt_ob_ch51'),
    path('view_july_account_details_ob_ch51/', branch51.view_july_account_details_ob_ch51, name='view_july_account_details_ob_ch51'),
    path('july_account_mgt_ob_ch51/<id>',branch51.july_account_mgt_ob_ch51,name='july_account_mgt_ob_ch51'),
    path('view_auguest_account_details_ob_ch51/', branch51.view_auguest_account_details_ob_ch51, name='view_auguest_account_details_ob_ch51'),
    path('auguest_account_mgt_ob_ch51/<id>',branch51.auguest_account_mgt_ob_ch51,name='auguest_account_mgt_ob_ch51'),

    path('view_sept_account_details_ob_ch51/', branch51.view_sept_account_details_ob_ch51, name='view_sept_account_details_ob_ch51'),
    path('sept_account_mgt_ob_ch51/<id>',branch51.sept_account_mgt_ob_ch51,name='sept_account_mgt_ob_ch51'),
    path('view_october_account_details_ob_ch51/', branch51.view_october_account_details_ob_ch51, name='view_october_account_details_ob_ch51'),
    path('october_account_mgt_ob_ch51/<id>',branch51.october_account_mgt_ob_ch51,name='october_account_mgt_ob_ch51'),
    path('view_nov_account_details_ob_ch51/', branch51.view_nov_account_details_ob_ch51, name='view_nov_account_details_ob_ch51'),
    path('nov_account_mgt_ob_ch51/<id>',branch51.nov_account_mgt_ob_ch51,name='nov_account_mgt_ob_ch51'),
    path('view_dec_account_details_ob_ch51/', branch51.view_dec_account_details_ob_ch51, name='view_dec_account_details_ob_ch51'),
    path('dec_account_mgt_ob_ch51/<id>',branch51.dec_account_mgt_ob_ch51,name='dec_account_mgt_ob_ch51'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch51', admin_dashboard_calculations_br51.monthly_details_due_ob_ch51, name='monthly_details_due_ob_ch51'),
    path('monthly_collection_details_ob_ch51/', admin_dashboard_calculations_br51.monthly_collection_details_ob_ch51, name='monthly_collection_details_ob_ch51'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch51/',branch51.guest_all_ob_ch51,name='guest_all_ob_ch51'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category51/', accounts51.view_all_category51, name='view_all_category51'),
    path('create_new_category51/', accounts51.create_new_category51, name='create_new_category51'),
    path('regi_new_category51/', accounts51.regi_new_category51, name='regi_new_category51'),
    path('update_category51/<id>',accounts51.update_category51,name='update_category51'),

    path('delete_category51/<id>', accounts51.delete_category51, name='delete_category51'),
    path('view_all_category_delete51/', accounts51.view_all_category_delete51, name='view_all_category_delete51'),

    path('regi_multiple_new_category51/', accounts51.regi_multiple_new_category51, name='regi_multiple_new_category51'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items51/', accounts51.view_all_items51, name='view_all_items51'),
    path('create_new_item51/', accounts51.create_new_item51, name='create_new_item51'),
    path('regi_new_item51/', accounts51.regi_new_item51, name='regi_new_item51'),
    path('delete_item51/<id>',accounts51.delete_item51,name='delete_item51'),
    path('update_item51/<id>', accounts51.update_item51, name='update_item51'),
    path('view_all_items_delete51/',accounts51.view_all_items_delete51,name='view_all_items_delete51'),

    path('regi_multiple_new_item51/', accounts51.regi_multiple_new_item51, name='regi_multiple_new_item51'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger51/', accounts51.view_all_ledger51, name='view_all_ledger51'),
    path('create_new_ledger51/', accounts51.create_new_ledger51, name='create_new_ledger51'),
    path('regi_new_ledger51/', accounts51.regi_new_ledger51, name='regi_new_ledger51'),
    path('delete_ledger51/<id>',accounts51.delete_ledger51,name='delete_ledger51'),
    path('update_ledger51/<id>',accounts51.update_ledger51,name='update_ledger51'),
    path('view_all_ledger_delete51/',accounts51.view_all_ledger_delete51,name='view_all_ledger_delete51'),

    path('regi_multiple_new_ledger51/', accounts51.regi_multiple_new_ledger51, name='regi_multiple_new_ledger51'),

    ##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book51/', accounts51.view_all_accounts_book51, name='view_all_accounts_book51'),
    path('create_new_accounts_book51/', accounts51.create_new_accounts_book51, name='create_new_accounts_book51'),
    path('regi_new_accounts_book51/', accounts51.regi_new_accounts_book51, name='regi_new_accounts_book51'),
    path('update_accounts_book51/<id>',accounts51.update_accounts_book51,name='update_accounts_book51'),
    path('delete_accounts_book51/<id>',accounts51.delete_accounts_book51,name='delete_accounts_book51'),
    path('view_all_accounts_book_delete51/',accounts51.view_all_accounts_book_delete51,name='view_all_accounts_book_delete51'),

    path('regi_multiple_new_accounts_book51/', accounts51.regi_multiple_new_accounts_book51,name='regi_multiple_new_accounts_book51'),

    ##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries51/', accounts51.get_countries51, name='get_countries51'),

    path('in_exp_items_entry51/', accounts51.in_exp_items_entry51, name='in_exp_items_entry51'),
    path('reg_in_exp_items_entry51/', accounts51.reg_in_exp_items_entry51, name='reg_in_exp_items_entry51'),
    path('delete_journal51/<id>',accounts51.delete_journal51,name='delete_journal51'),
    path('update_in_exp_items_entry51/<id>',accounts51.update_in_exp_items_entry51,name='update_in_exp_items_entry51'),
    path('detailed_journal_report51/',accounts51.detailed_journal_report51,name='detailed_journal_report51'),
    path('journal_report_deleted51/',accounts51.journal_report_deleted51,name='journal_report_deleted51'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise51/', accounts51.daily_category_wise51, name='daily_category_wise51'),
    path('monthly_category_based_reports51/',accounts51.monthly_category_based_reports51,name='monthly_category_based_reports51'),
    path('yearly_category_based_reports51/', accounts51.yearly_category_based_reports51,name='yearly_category_based_reports51'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed51/', accounts51.daily_detailed51, name='daily_detailed51'),
    path('monthly_detailed51/',accounts51.monthly_detailed51,name='monthly_detailed51'),
    path('yearly_detailed51/',accounts51.yearly_detailed51,name='yearly_detailed51'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports51/', accounts51.item_based_reports51, name='item_based_reports51'),
    path('daily_item_based_reports51/',accounts51.daily_item_based_reports51,name='daily_item_based_reports51'),
    path('monthly_item_based_reports51/',accounts51.monthly_item_based_reports51,name='monthly_item_based_reports51'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports51/', accounts51.ledger_based_reports51, name='ledger_based_reports51'),
    path('monthly_ledger_based_reports51/', accounts51.monthly_ledger_based_reports51, name='monthly_ledger_based_reports51'),
    path('daily_ledger_based_reports51/',accounts51.daily_ledger_based_reports51,name='daily_ledger_based_reports51'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports51/', accounts51.accounts_book_based_reports51, name='accounts_book_based_reports51'),
    path('daily_accounts_book_based_reports51/',accounts51.daily_accounts_book_based_reports51,name='daily_accounts_book_based_reports51'),
    path('monthly_accounts_book_based_reports51/',accounts51.monthly_accounts_book_based_reports51,name='monthly_accounts_book_based_reports51'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months51/', accounts51.monthly_reports_choose_months51, name='monthly_reports_choose_months51'),
    path('monthly_detailed_daily_in_exp_items_report51/<mo>',accounts51.monthly_detailed_daily_in_exp_items_report51,name='monthly_detailed_daily_in_exp_items_report51'),

    path('single_monthly_reports_choose_months51/', accounts51.single_monthly_reports_choose_months51,name='single_monthly_reports_choose_months51'),
    path('single_monthly_daily_in_exp_items_report51/<mo>',accounts51.single_monthly_daily_in_exp_items_report51,name='single_monthly_daily_in_exp_items_report51'),

    path('accounts_dash_board_ob_ch51/',accounts51.accounts_dash_board_ob_ch51,name='accounts_dash_board_ob_ch51'),
    path('accounts_dash_board51/',accounts51.accounts_dash_board51,name='accounts_dash_board51'),

    path('profit_sharing_choose_months51', accounts51.profit_sharing_choose_months51,name='profit_sharing_choose_months51'),
    path('profit_sharing51/<mo>', accounts51.profit_sharing51, name='profit_sharing51'),
    path('view_share_holders51', accounts51.view_share_holders51, name='view_share_holders51'),
    path('create_share_holders51', accounts51.create_share_holders51, name='create_share_holders51'),
    path('regi_share_holders51', accounts51.regi_share_holders51, name='regi_share_holders51'),
    path('update_share_holders51/<id>', accounts51.update_share_holders51, name='update_share_holders51'),
    path('delete_share_holders51/<id>', accounts51.delete_share_holders51, name='delete_share_holders51'),
    path('view_deleted_share_holders51', accounts51.view_deleted_share_holders51, name='view_deleted_share_holders51'),

    path('regi_multiple_share_holders51', accounts51.regi_multiple_share_holders51, name='regi_multiple_share_holders51'),

]

