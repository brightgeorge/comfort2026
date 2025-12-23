from django.urls import path, include

from . import admin_branch52
from . import admin_branch52
from . import branch52
from . import reports52
from . import payment52
from . import admin_dashboard_calculations_br52
from . import accounts52

urlpatterns = [

    path('branch1_dashboard_ob_ch52/', branch52.branch1_dashboard_ob_ch52, name='branch1_dashboard_ob_ch52'),
    path('branch1_dashboard52/',branch52.branch1_dashboard52,name='branch1_dashboard52'),
    path('user_dashboard_calculations_ob_ch52/',branch52.user_dashboard_calculations_ob_ch52,name='user_dashboard_calculations_ob_ch52'),

    path('background_ob_ch52',branch52.background_ob_ch52,name='background_ob_ch52'),
    path('background_regi_ob_ch52',branch52.background_regi_ob_ch52,name='background_regi_ob_ch52'),
    path('custom_background_regi_ob_ch52',branch52.custom_background_regi_ob_ch52,name='custom_background_regi_ob_ch52'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch52/',admin_branch52.branch1_room_create_regi_ob_ch52,name='branch1_room_create_regi_ob_ch52'),
    path('view_all_room_ob_ch52/',admin_branch52.view_all_room_ob_ch52,name='view_all_room_ob_ch52'),
    path('delete_room_ob_ch52/<id>',admin_branch52.delete_room_ob_ch52,name='delete_room_ob_ch52'),

    path('branch1_room_create_ob_ch52/',admin_branch52.branch1_room_create_ob_ch52,name='branch1_room_create_ob_ch52'),

    path('multiple_branch1_room_create_regi52/',admin_branch52.multiple_branch1_room_create_regi52,name='multiple_branch1_room_create_regi52'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch52/', admin_branch52.pg1_bed_create_regi_ob_ch52, name='pg1_bed_create_regi_ob_ch52'),
    path('pg1_view_all_beds_ob_ch52/', admin_branch52.pg1_view_all_beds_ob_ch52, name='pg1_view_all_beds_ob_ch52'),
    path('delete_bed_ob_ch52/<id>', admin_branch52.delete_bed_ob_ch52, name='delete_bed_ob_ch52'),

    path('pg1_bed_create_ob_ch52/', admin_branch52.pg1_bed_create_ob_ch52, name='pg1_bed_create_ob_ch52'),

    path('single_pg1_bed_create_regi_ob_ch52/',admin_branch52.single_pg1_bed_create_regi_ob_ch52,name='single_pg1_bed_create_regi_ob_ch52'),
    path('update_bed_basic_details_ob_ch52/<id>',admin_branch52.update_bed_basic_details_ob_ch52, name='update_bed_basic_details_ob_ch52'),

    path('multiple_single_pg1_bed_create_regi52/',admin_branch52.multiple_single_pg1_bed_create_regi52,name='multiple_single_pg1_bed_create_regi52'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch52/<id>',branch52.br1_admit_guest_ob_ch52,name='br1_admit_guest_ob_ch52'),
    path('view_all_new_guest_ob_ch52/',branch52.view_all_new_guest_ob_ch52,name='view_all_new_guest_ob_ch52'),
    path('update_br1_admit_guest_ob_ch52/<id>',branch52.update_br1_admit_guest_ob_ch52,name='update_br1_admit_guest_ob_ch52'),
    path('vacate_br1_guest_ob_ch52/<id>',branch52.vacate_br1_guest_ob_ch52,name='vacate_br1_guest_ob_ch52'),

    path('active_guest_details_ob_ch52/<guest_code>',branch52.active_guest_details_ob_ch52,name='active_guest_details_ob_ch52'),
    path('view_all_guest_ob_ch52/',branch52.view_all_guest_ob_ch52,name='view_all_guest_ob_ch52'),
    path('shift_guest_ob_ch52/<id>',branch52.shift_guest_ob_ch52,name='shift_guest_ob_ch52'),
    path('shift_guest_regi_ob_ch52/',branch52.shift_guest_regi_ob_ch52,name='shift_guest_regi_ob_ch52'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch52/',branch52.update_all_rent_ob_ch52,name='update_all_rent_ob_ch52'),

    path('multiple_br1_admit_guest52/<id>',branch52.multiple_br1_admit_guest52,name='multiple_br1_admit_guest52'),

#guest end here


##################################
#_ADVANCE_ob_ch52 START HERE
################################


    path('choose_months_advance_ob_ch52/',branch52.choose_months_advance_ob_ch52,name='choose_months_advance_ob_ch52'),

    path('jan_advance_ob_ch52/', branch52.jan_advance_ob_ch52, name='jan_advance_ob_ch52'),
    path('jan_make_payments_advance_ob_ch52/<id>', branch52.jan_make_payments_advance_ob_ch52,name='jan_make_payments_advance_ob_ch52'),
    path('feb_advance_ob_ch52/', branch52.feb_advance_ob_ch52, name='feb_advance_ob_ch52'),
    path('feb_make_payments_advance_ob_ch52/<id>', branch52.feb_make_payments_advance_ob_ch52,name='feb_make_payments_advance_ob_ch52'),
    path('march_advance_ob_ch52/', branch52.march_advance_ob_ch52, name='march_advance_ob_ch52'),
    path('march_make_payments_advance_ob_ch52/<id>', branch52.march_make_payments_advance_ob_ch52,name='march_make_payments_advance_ob_ch52'),
    path('april_advance_ob_ch52/', branch52.april_advance_ob_ch52, name='april_advance_ob_ch52'),
    path('april_make_payments_advance_ob_ch52/<id>', branch52.april_make_payments_advance_ob_ch52, name='april_make_payments_advance_ob_ch52'),

    path('may_advance_ob_ch52/',branch52.may_advance_ob_ch52,name='may_advance_ob_ch52'),
    path('may_make_payments_advance_ob_ch52/<id>', branch52.may_make_payments_advance_ob_ch52, name='may_make_payments_advance_ob_ch52'),
    path('june_advance_ob_ch52/',branch52.june_advance_ob_ch52,name='june_advance_ob_ch52'),
    path('june_make_payments_advance_ob_ch52/<id>', branch52.june_make_payments_advance_ob_ch52, name='june_make_payments_advance_ob_ch52'),
    path('july_advance_ob_ch52/',branch52.july_advance_ob_ch52,name='july_advance_ob_ch52'),
    path('july_make_payments_advance_ob_ch52/<id>', branch52.july_make_payments_advance_ob_ch52, name='july_make_payments_advance_ob_ch52'),
    path('auguest_advance_ob_ch52/', branch52.auguest_advance_ob_ch52, name='auguest_advance_ob_ch52'),
    path('auguest_make_payments_advance_ob_ch52/<id>', branch52.auguest_make_payments_advance_ob_ch52, name='auguest_make_payments_advance_ob_ch52'),

    path('sept_advance_ob_ch52/', branch52.sept_advance_ob_ch52, name='sept_advance_ob_ch52'),
    path('sept_make_payments_advance_ob_ch52/<id>', branch52.sept_make_payments_advance_ob_ch52,name='sept_make_payments_advance_ob_ch52'),
    path('october_advance_ob_ch52/', branch52.october_advance_ob_ch52, name='october_advance_ob_ch52'),
    path('october_make_payments_advance_ob_ch52/<id>', branch52.october_make_payments_advance_ob_ch52, name='october_make_payments_advance_ob_ch52'),
    path('nov_advance_ob_ch52/', branch52.nov_advance_ob_ch52, name='nov_advance_ob_ch52'),
    path('nov_make_payments_advance_ob_ch52/<id>', branch52.nov_make_payments_advance_ob_ch52,name='nov_make_payments_advance_ob_ch52'),
    path('dec_advance_ob_ch52/', branch52.dec_advance_ob_ch52, name='dec_advance_ob_ch52'),
    path('dec_make_payments_advance_ob_ch52/<id>', branch52.dec_make_payments_advance_ob_ch52, name='dec_make_payments_advance_ob_ch52'),



##################################
#_ADVANCE_ob_ch52 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch52/',branch52.choose_months_ob_ch52,name='choose_months_ob_ch52'),

    path('jan_ob_ch52/',branch52.jan_ob_ch52,name='jan_ob_ch52'),
    path('jan_manke_payments_ob_ch52/<id>',branch52.jan_manke_payments_ob_ch52,name='jan_manke_payments_ob_ch52'),

    path('feb_ob_ch52/',branch52.feb_ob_ch52,name='feb_ob_ch52'),
    path('feb_manke_payments_ob_ch52/<id>',branch52.feb_manke_payments_ob_ch52,name='feb_manke_payments_ob_ch52'),

    path('march_ob_ch52/',branch52.march_ob_ch52,name='march_ob_ch52'),
    path('march_manke_payments_ob_ch52/<id>',branch52.march_manke_payments_ob_ch52,name='march_manke_payments_ob_ch52'),

    path('april_ob_ch52/',branch52.april_ob_ch52,name='april_ob_ch52'),
    path('april_make_payments_ob_ch52/<id>',branch52.april_make_payments_ob_ch52,name='april_make_payments_ob_ch52'),

    path('may_ob_ch52/',branch52.may_ob_ch52,name='may_ob_ch52'),
    path('may_make_payments_ob_ch52/<id>',branch52.may_make_payments_ob_ch52,name='may_make_payments_ob_ch52'),

    path('june_ob_ch52/',branch52.june_ob_ch52,name='june_ob_ch52'),
    path('june_make_payments_ob_ch52/<id>',branch52.june_make_payments_ob_ch52,name='june_make_payments_ob_ch52'),

    path('july_ob_ch52/',branch52.july_ob_ch52,name='july_ob_ch52'),
    path('july_make_payments_ob_ch52/<id>',branch52.july_make_payments_ob_ch52,name='july_make_payments_ob_ch52'),

    path('aug_ob_ch52/',branch52.aug_ob_ch52,name='aug_ob_ch52'),
    path('aug_make_payments_ob_ch52/<id>',branch52.aug_make_payments_ob_ch52,name='aug_make_payments_ob_ch52'),

    path('sept_ob_ch52/',branch52.sept_ob_ch52,name='sept_ob_ch52'),
    path('sept_make_payments_ob_ch52/<id>',branch52.sept_make_payments_ob_ch52,name='sept_make_payments_ob_ch52'),

    path('oct_ob_ch52/',branch52.oct_ob_ch52,name='oct_ob_ch52'),
    path('oct_make_payments_ob_ch52/<id>',branch52.oct_make_payments_ob_ch52,name='oct_make_payments_ob_ch52'),

    path('nov_ob_ch52/',branch52.nov_ob_ch52,name='nov_ob_ch52'),
    path('nov_make_payments_ob_ch52/<id>',branch52.nov_make_payments_ob_ch52,name='nov_make_payments_ob_ch52'),

    path('dec_ob_ch52/',branch52.dec_ob_ch52,name='dec_ob_ch52'),
    path('dec_make_payments_ob_ch52/<id>',branch52.dec_make_payments_ob_ch52,name='dec_make_payments_ob_ch52'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch52/', payment52.choose_user_ob_ch52, name='choose_user_ob_ch52'),
    path('payment_user_details_ob_ch52/<id>', payment52.payment_user_details_ob_ch52, name='payment_user_details_ob_ch52'),
    path('close_choose_user_ob_ch52/<id>',payment52.close_choose_user_ob_ch52,name='close_choose_user_ob_ch52'),

    path('monthly_jan_make_payments_ob_ch52/<id>', payment52.monthly_jan_make_payments_ob_ch52, name='monthly_jan_make_payments_ob_ch52'),
    path('monthly_feb_make_payments_ob_ch52/<id>', payment52.monthly_feb_make_payments_ob_ch52, name='monthly_feb_make_payments_ob_ch52'),
    path('monthly_march_make_payments_ob_ch52/<id>', payment52.monthly_march_make_payments_ob_ch52, name='monthly_march_make_payments_ob_ch52'),
    path('monthly_april_make_payments_ob_ch52/<id>', payment52.monthly_april_make_payments_ob_ch52, name='monthly_april_make_payments_ob_ch52'),
    path('monthly_may_make_payments_ob_ch52/<id>', payment52.monthly_may_make_payments_ob_ch52, name='monthly_may_make_payments_ob_ch52'),
    path('monthly_june_make_payments_ob_ch52/<id>', payment52.monthly_june_make_payments_ob_ch52, name='monthly_june_make_payments_ob_ch52'),

    path('monthly_july_make_payments_ob_ch52/<id>', payment52.monthly_july_make_payments_ob_ch52, name='monthly_july_make_payments_ob_ch52'),
    path('monthly_aug_make_payments_ob_ch52/<id>', payment52.monthly_aug_make_payments_ob_ch52, name='monthly_aug_make_payments_ob_ch52'),
    path('monthly_sept_make_payments_ob_ch52/<id>', payment52.monthly_sept_make_payments_ob_ch52, name='monthly_sept_make_payments_ob_ch52'),
    path('monthly_oct_make_payments_ob_ch52/<id>', payment52.monthly_oct_make_payments_ob_ch52, name='monthly_oct_make_payments_ob_ch52'),
    path('monthly_nov_make_payments_ob_ch52/<id>', payment52.monthly_nov_make_payments_ob_ch52, name='monthly_nov_make_payments_ob_ch52'),
    path('monthly_dec_make_payments_ob_ch52/<id>', payment52.monthly_dec_make_payments_ob_ch52, name='monthly_dec_make_payments_ob_ch52'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch52/',branch52.unpaid_rent_choose_months_ob_ch52,name='unpaid_rent_choose_months_ob_ch52'),

    path('jan_unpaid_rent_ob_ch52/', branch52.jan_unpaid_rent_ob_ch52, name='jan_unpaid_rent_ob_ch52'),
    path('table_jan_unpaid_rent_ob_ch52/', branch52.table_jan_unpaid_rent_ob_ch52, name='table_jan_unpaid_rent_ob_ch52'),
    path('feb_unpaid_rent_ob_ch52/', branch52.feb_unpaid_rent_ob_ch52, name='feb_unpaid_rent_ob_ch52'),
    path('table_feb_unpaid_rent_ob_ch52/', branch52.table_feb_unpaid_rent_ob_ch52, name='table_feb_unpaid_rent_ob_ch52'),
    path('mar_unpaid_rent_ob_ch52/', branch52.mar_unpaid_rent_ob_ch52, name='mar_unpaid_rent_ob_ch52'),
    path('table_mar_unpaid_rent_ob_ch52/', branch52.table_mar_unpaid_rent_ob_ch52, name='table_mar_unpaid_rent_ob_ch52'),
    path('april_unpaid_rent_ob_ch52/', branch52.april_unpaid_rent_ob_ch52, name='april_unpaid_rent_ob_ch52'),
    path('table_april_unpaid_rent_ob_ch52/', branch52.table_april_unpaid_rent_ob_ch52, name='table_april_unpaid_rent_ob_ch52'),

    path('may_unpaid_rent_ob_ch52/', branch52.may_unpaid_rent_ob_ch52, name='may_unpaid_rent_ob_ch52'),
    path('table_may_unpaid_rent_ob_ch52/', branch52.table_may_unpaid_rent_ob_ch52, name='table_may_unpaid_rent_ob_ch52'),
    path('june_unpaid_rent_ob_ch52/', branch52.june_unpaid_rent_ob_ch52, name='june_unpaid_rent_ob_ch52'),
    path('table_june_unpaid_rent_ob_ch52/', branch52.table_june_unpaid_rent_ob_ch52, name='table_june_unpaid_rent_ob_ch52'),
    path('july_unpaid_rent_ob_ch52/', branch52.july_unpaid_rent_ob_ch52, name='july_unpaid_rent_ob_ch52'),
    path('table_july_unpaid_rent_ob_ch52',branch52.table_july_unpaid_rent_ob_ch52,name='table_july_unpaid_rent_ob_ch52'),
    path('aug_unpaid_rent_ob_ch52/', branch52.aug_unpaid_rent_ob_ch52, name='aug_unpaid_rent_ob_ch52'),
    path('table_aug_unpaid_rent_ob_ch52/',branch52.table_aug_unpaid_rent_ob_ch52,name='table_aug_unpaid_rent_ob_ch52'),

    path('sept_unpaid_rent_ob_ch52/', branch52.sept_unpaid_rent_ob_ch52, name='sept_unpaid_rent_ob_ch52'),
    path('table_sept_unpaid_rent_ob_ch52/', branch52.table_sept_unpaid_rent_ob_ch52, name='table_sept_unpaid_rent_ob_ch52'),
    path('oct_unpaid_rent_ob_ch52/', branch52.oct_unpaid_rent_ob_ch52, name='oct_unpaid_rent_ob_ch52'),
    path('table_oct_unpaid_rent_ob_ch52/', branch52.table_oct_unpaid_rent_ob_ch52, name='table_oct_unpaid_rent_ob_ch52'),
    path('nov_unpaid_rent_ob_ch52/', branch52.nov_unpaid_rent_ob_ch52, name='nov_unpaid_rent_ob_ch52'),
    path('table_nov_unpaid_rent_ob_ch52/', branch52.table_nov_unpaid_rent_ob_ch52, name='table_nov_unpaid_rent_ob_ch52'),
    path('dec_unpaid_rent_ob_ch52/', branch52.dec_unpaid_rent_ob_ch52, name='dec_unpaid_rent_ob_ch52'),
    path('table_dec_unpaid_rent_ob_ch52/', branch52.table_dec_unpaid_rent_ob_ch52, name='table_dec_unpaid_rent_ob_ch52'),

    path('details_of_unpaid_guests_ob_ch52/<id>',branch52.details_of_unpaid_guests_ob_ch52,name='details_of_unpaid_guests_ob_ch52'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch52/',branch52.paid_rent_choose_months_ob_ch52,name='paid_rent_choose_months_ob_ch52'),
    path('partially_paid_guest_choose_months_ob_ch52/',reports52.partially_paid_guest_choose_months_ob_ch52,name='partially_paid_guest_choose_months_ob_ch52'),

    path('jan_paid_rent_ob_ch52/', branch52.jan_paid_rent_ob_ch52, name='jan_paid_rent_ob_ch52'),
    path('table_jan_paid_rent_ob_ch52/', branch52.table_jan_paid_rent_ob_ch52, name='table_jan_paid_rent_ob_ch52'),
    path('jan_full_paid_guest_ob_ch52/', reports52.jan_full_paid_guest_ob_ch52, name='jan_full_paid_guest_ob_ch52'),
    path('jan_partially_paid_guest_ob_ch52/', reports52.jan_partially_paid_guest_ob_ch52, name='jan_partially_paid_guest_ob_ch52'),
    path('table_jan_partially_paid_guest_ob_ch52/', reports52.table_jan_partially_paid_guest_ob_ch52,name='table_jan_partially_paid_guest_ob_ch52'),

    path('feb_paid_rent_ob_ch52/', branch52.feb_paid_rent_ob_ch52, name='feb_paid_rent_ob_ch52'),
    path('table_feb_paid_rent_ob_ch52/', branch52.table_feb_paid_rent_ob_ch52, name='table_feb_paid_rent_ob_ch52'),
    path('feb_full_paid_guest_ob_ch52/', reports52.feb_full_paid_guest_ob_ch52, name='feb_full_paid_guest_ob_ch52'),
    path('feb_partially_paid_guest_ob_ch52/', reports52.feb_partially_paid_guest_ob_ch52, name='feb_partially_paid_guest_ob_ch52'),
    path('table_feb_partially_paid_guest_ob_ch52/', reports52.table_feb_partially_paid_guest_ob_ch52,name='table_feb_partially_paid_guest_ob_ch52'),

    path('mar_paid_rent_ob_ch52/', branch52.mar_paid_rent_ob_ch52, name='mar_paid_rent_ob_ch52'),
    path('table_mar_paid_rent_ob_ch52/', branch52.table_mar_paid_rent_ob_ch52, name='table_mar_paid_rent_ob_ch52'),
    path('march_full_paid_guest_ob_ch52/', reports52.march_full_paid_guest_ob_ch52, name='march_full_paid_guest_ob_ch52'),
    path('march_partially_paid_guest_ob_ch52/', reports52.march_partially_paid_guest_ob_ch52, name='march_partially_paid_guest_ob_ch52'),
    path('table_march_partially_paid_guest_ob_ch52/', reports52.table_march_partially_paid_guest_ob_ch52,name='table_march_partially_paid_guest_ob_ch52'),

    path('april_paid_rent_ob_ch52/', branch52.april_paid_rent_ob_ch52, name='april_paid_rent_ob_ch52'),
    path('table_april_paid_rent_ob_ch52/', branch52.table_april_paid_rent_ob_ch52, name='table_april_paid_rent_ob_ch52'),
    path('april_full_paid_guest_ob_ch52/', reports52.april_full_paid_guest_ob_ch52, name='april_full_paid_guest_ob_ch52'),
    path('april_partially_paid_guest_ob_ch52/', reports52.april_partially_paid_guest_ob_ch52, name='april_partially_paid_guest_ob_ch52'),
    path('table_april_partially_paid_guest_ob_ch52/', reports52.table_april_partially_paid_guest_ob_ch52,name='table_april_partially_paid_guest_ob_ch52'),

    path('may_paid_rent_ob_ch52/', branch52.may_paid_rent_ob_ch52, name='may_paid_rent_ob_ch52'),
    path('table_may_paid_rent_ob_ch52/', branch52.table_may_paid_rent_ob_ch52, name='table_may_paid_rent_ob_ch52'),
    path('may_full_paid_guest_ob_ch52/', reports52.may_full_paid_guest_ob_ch52, name='may_full_paid_guest_ob_ch52'),
    path('may_partially_paid_guest_ob_ch52/', reports52.may_partially_paid_guest_ob_ch52, name='may_partially_paid_guest_ob_ch52'),
    path('table_may_partially_paid_guest_ob_ch52/', reports52.table_may_partially_paid_guest_ob_ch52, name='table_may_partially_paid_guest_ob_ch52'),

    path('june_paid_rent_ob_ch52/', branch52.june_paid_rent_ob_ch52, name='june_paid_rent_ob_ch52'),
    path('table_june_paid_rent_ob_ch52/', branch52.table_june_paid_rent_ob_ch52, name='table_june_paid_rent_ob_ch52'),
    path('june_full_paid_guest_ob_ch52/', reports52.june_full_paid_guest_ob_ch52, name='june_full_paid_guest_ob_ch52'),
    path('june_partially_paid_guest_ob_ch52/', reports52.june_partially_paid_guest_ob_ch52, name='june_partially_paid_guest_ob_ch52'),
    path('table_june_partially_paid_guest_ob_ch52/', reports52.table_june_partially_paid_guest_ob_ch52, name='table_june_partially_paid_guest_ob_ch52'),

    path('july_paid_rent_ob_ch52/', branch52.july_paid_rent_ob_ch52, name='july_paid_rent_ob_ch52'),
    path('table_july_paid_rent_ob_ch52/', branch52.table_july_paid_rent_ob_ch52, name='table_july_paid_rent_ob_ch52'),
    path('july_full_paid_guest_ob_ch52/', reports52.july_full_paid_guest_ob_ch52, name='july_full_paid_guest_ob_ch52'),
    path('july_partially_paid_guest_ob_ch52/', reports52.july_partially_paid_guest_ob_ch52, name='july_partially_paid_guest_ob_ch52'),
    path('table_july_partially_paid_guest_ob_ch52/', reports52.table_july_partially_paid_guest_ob_ch52, name='table_july_partially_paid_guest_ob_ch52'),

    path('aug_paid_rent_ob_ch52/', branch52.aug_paid_rent_ob_ch52, name='aug_paid_rent_ob_ch52'),
    path('table_aug_paid_rent_ob_ch52/', branch52.table_aug_paid_rent_ob_ch52, name='table_aug_paid_rent_ob_ch52'),
    path('auguest_full_paid_guest_ob_ch52/', reports52.auguest_full_paid_guest_ob_ch52, name='auguest_full_paid_guest_ob_ch52'),
    path('auguest_partially_paid_guest_ob_ch52/', reports52.auguest_partially_paid_guest_ob_ch52,name='auguest_partially_paid_guest_ob_ch52'),
    path('table_auguest_partially_paid_guest_ob_ch52/', reports52.table_auguest_partially_paid_guest_ob_ch52,name='table_auguest_partially_paid_guest_ob_ch52'),

    path('sept_paid_rent_ob_ch52/', branch52.sept_paid_rent_ob_ch52, name='sept_paid_rent_ob_ch52'),
    path('table_sept_paid_rent_ob_ch52/', branch52.table_sept_paid_rent_ob_ch52, name='table_sept_paid_rent_ob_ch52'),
    path('sept_full_paid_guest_ob_ch52/', reports52.sept_full_paid_guest_ob_ch52, name='sept_full_paid_guest_ob_ch52'),
    path('sept_partially_paid_guest_ob_ch52/', reports52.sept_partially_paid_guest_ob_ch52, name='sept_partially_paid_guest_ob_ch52'),
    path('table_sept_partially_paid_guest_ob_ch52/', reports52.table_sept_partially_paid_guest_ob_ch52,name='table_sept_partially_paid_guest_ob_ch52'),

    path('oct_paid_rent_ob_ch52/', branch52.oct_paid_rent_ob_ch52, name='oct_paid_rent_ob_ch52'),
    path('table_oct_paid_rent_ob_ch52/', branch52.table_oct_paid_rent_ob_ch52, name='table_oct_paid_rent_ob_ch52'),
    path('october_full_paid_guest_ob_ch52/', reports52.october_full_paid_guest_ob_ch52, name='october_full_paid_guest_ob_ch52'),
    path('october_partially_paid_guest_ob_ch52/', reports52.october_partially_paid_guest_ob_ch52,name='october_partially_paid_guest_ob_ch52'),
    path('table_october_partially_paid_guest_ob_ch52/', reports52.table_october_partially_paid_guest_ob_ch52,name='table_october_partially_paid_guest_ob_ch52'),

    path('nov_paid_rent_ob_ch52/', branch52.nov_paid_rent_ob_ch52, name='nov_paid_rent_ob_ch52'),
    path('table_nov_paid_rent_ob_ch52/', branch52.table_nov_paid_rent_ob_ch52, name='table_nov_paid_rent_ob_ch52'),
    path('nov_full_paid_guest_ob_ch52/', reports52.nov_full_paid_guest_ob_ch52, name='nov_full_paid_guest_ob_ch52'),
    path('nov_partially_paid_guest_ob_ch52/', reports52.nov_partially_paid_guest_ob_ch52, name='nov_partially_paid_guest_ob_ch52'),
    path('table_nov_partially_paid_guest_ob_ch52/', reports52.table_nov_partially_paid_guest_ob_ch52,name='table_nov_partially_paid_guest_ob_ch52'),

    path('dec_paid_rent_ob_ch52/', branch52.dec_paid_rent_ob_ch52, name='dec_paid_rent_ob_ch52'),
    path('table_dec_paid_rent_ob_ch52/', branch52.table_dec_paid_rent_ob_ch52, name='table_dec_paid_rent_ob_ch52'),
    path('dec_full_paid_guest_ob_ch52/', reports52.dec_full_paid_guest_ob_ch52, name='dec_full_paid_guest_ob_ch52'),
    path('dec_partially_paid_guest_ob_ch52/', reports52.dec_partially_paid_guest_ob_ch52, name='dec_partially_paid_guest_ob_ch52'),
    path('table_dec_partially_paid_guest_ob_ch52/', reports52.table_dec_partially_paid_guest_ob_ch52,name='table_dec_partially_paid_guest_ob_ch52'),

    path('details_of_paid_guests_ob_ch52/<id>',branch52.details_of_paid_guests_ob_ch52,name='details_of_paid_guests_ob_ch52'),
    path('full_paid_guest_ob_ch52/',reports52.full_paid_guest_ob_ch52,name='full_paid_guest_ob_ch52'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch52/',branch52.viewall_vacate_guest_ob_ch52,name='viewall_vacate_guest_ob_ch52'),
    path('details_of_vacate_guest_ob_ch52/<id>',branch52.details_of_vacate_guest_ob_ch52,name='details_of_vacate_guest_ob_ch52'),
    path('full_vacated_guest_details_ob_ch52',branch52.full_vacated_guest_details_ob_ch52,name='full_vacated_guest_details_ob_ch52'),
    path('full_vacated_guest_table_ob_ch52',branch52.full_vacated_guest_table_ob_ch52,name='full_vacated_guest_table_ob_ch52'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch52/<id>', branch52.jan_manke_payments_vacate_ob_ch52, name='jan_manke_payments_vacate_ob_ch52'),
    path('feb_manke_payments_vacate_ob_ch52/<id>', branch52.feb_manke_payments_vacate_ob_ch52, name='feb_manke_payments_vacate_ob_ch52'),
    path('march_manke_payments_vacate_ob_ch52/<id>', branch52.march_manke_payments_vacate_ob_ch52, name='march_manke_payments_vacate_ob_ch52'),
    path('april_make_payments_vacate_ob_ch52/<id>', branch52.april_make_payments_vacate_ob_ch52, name='april_make_payments_vacate_ob_ch52'),

    path('may_make_payments_vacate_ob_ch52/<id>', branch52.may_make_payments_vacate_ob_ch52, name='may_make_payments_vacate_ob_ch52'),
    path('june_make_payments_vacate_ob_ch52/<id>', branch52.june_make_payments_vacate_ob_ch52, name='june_make_payments_vacate_ob_ch52'),
    path('july_make_payments_vacate_ob_ch52/<id>', branch52.july_make_payments_vacate_ob_ch52, name='july_make_payments_vacate_ob_ch52'),
    path('aug_make_payments_vacate_ob_ch52/<id>', branch52.aug_make_payments_vacate_ob_ch52, name='aug_make_payments_vacate_ob_ch52'),

    path('sept_make_payments_vacate_ob_ch52/<id>', branch52.sept_make_payments_vacate_ob_ch52, name='sept_make_payments_vacate_ob_ch52'),
    path('oct_make_payments_vacate_ob_ch52/<id>', branch52.oct_make_payments_vacate_ob_ch52, name='oct_make_payments_vacate_ob_ch52'),
    path('nov_make_payments_vacate_ob_ch52/<id>', branch52.nov_make_payments_vacate_ob_ch52, name='nov_make_payments_vacate_ob_ch52'),
    path('dec_make_payments_vacate_ob_ch52/<id>', branch52.dec_make_payments_vacate_ob_ch52, name='dec_make_payments_vacate_ob_ch52'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch52/',branch52.detail_guest_general_ob_ch52,name='detail_guest_general_ob_ch52'),

    path('jan_print_ob_ch52/',branch52.jan_print_ob_ch52,name='jan_print_ob_ch52'),
    path('feb_print_ob_ch52/',branch52.feb_print_ob_ch52,name='feb_print_ob_ch52'),
    path('march_print_ob_ch52/',branch52.march_print_ob_ch52,name='march_print_ob_ch52'),
    path('april_print_ob_ch52/',branch52.april_print_ob_ch52,name='april_print_ob_ch52'),

    path('may_print_ob_ch52/',branch52.may_print_ob_ch52,name='may_print_ob_ch52'),
    path('june_print_ob_ch52/',branch52.june_print_ob_ch52,name='june_print_ob_ch52'),
    path('july_print_ob_ch52/', branch52.july_print_ob_ch52, name='july_print_ob_ch52'),
    path('aug_print_ob_ch52/', branch52.aug_print_ob_ch52, name='aug_print_ob_ch52'),

    path('sept_print_ob_ch52/', branch52.sept_print_ob_ch52, name='sept_print_ob_ch52'),
    path('oct_print_ob_ch52/', branch52.oct_print_ob_ch52, name='oct_print_ob_ch52'),
    path('nov_print_ob_ch52/', branch52.nov_print_ob_ch52, name='nov_print_ob_ch52'),
    path('dec_print_ob_ch52/', branch52.dec_print_ob_ch52, name='dec_print_ob_ch52'),

    path('new_year_jan_print_ob_ch52/', branch52.new_year_jan_print_ob_ch52, name='new_year_jan_print_ob_ch52'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch52/', branch52.jan_close_ob_ch52, name='jan_close_ob_ch52'),
    path('jan_close_decision_page_ob_ch52/', branch52.jan_close_decision_page_ob_ch52, name='jan_close_decision_page_ob_ch52'),
    path('feb_close/', branch52.feb_close_ob_ch52, name='feb_close_ob_ch52'),
    path('feb_close_decision_page_ob_ch52/', branch52.feb_close_decision_page_ob_ch52, name='feb_close_decision_page_ob_ch52'),
    path('mar_close_ob_ch52/', branch52.mar_close_ob_ch52, name='mar_close_ob_ch52'),
    path('mar_close_decision_page/', branch52.mar_close_decision_page_ob_ch52, name='mar_close_decision_page_ob_ch52'),
    path('apr_close_ob_ch52/', branch52.apr_close_ob_ch52, name='apr_close_ob_ch52'),
    path('apr_close_decision_page_ob_ch52/', branch52.apr_close_decision_page_ob_ch52, name='apr_close_decision_page_ob_ch52'),

    path('may_close_ob_ch52/', branch52.may_close_ob_ch52, name='may_close_ob_ch52'),
    path('may_close_decision_page_ob_ch52/', branch52.may_close_decision_page_ob_ch52, name='may_close_decision_page_ob_ch52'),
    path('jun_close_ob_ch52/', branch52.jun_close_ob_ch52, name='jun_close_ob_ch52'),
    path('jun_close_decision_page_ob_ch52/', branch52.jun_close_decision_page_ob_ch52, name='jun_close_decision_page_ob_ch52'),
    path('jul_close_ob_ch52/', branch52.jul_close_ob_ch52, name='jul_close_ob_ch52'),
    path('jul_close_decision_page_ob_ch52/', branch52.jul_close_decision_page_ob_ch52, name='jul_close_decision_page_ob_ch52'),
    path('aug_close_ob_ch52/', branch52.aug_close_ob_ch52, name='aug_close_ob_ch52'),
    path('aug_close_decision_page_ob_ch52/', branch52.aug_close_decision_page_ob_ch52, name='aug_close_decision_page_ob_ch52'),

    path('sep_close_ob_ch52/', branch52.sep_close_ob_ch52, name='sep_close_ob_ch52'),
    path('sep_close_decision_page_ob_ch52/', branch52.sep_close_decision_page_ob_ch52, name='sep_close_decision_page_ob_ch52'),
    path('oct_close_ob_ch52/', branch52.oct_close_ob_ch52, name='oct_close_ob_ch52'),
    path('oct_close_decision_page_ob_ch52/', branch52.oct_close_decision_page_ob_ch52, name='oct_close_decision_page_ob_ch52'),
    path('nov_close_ob_ch52/', branch52.nov_close_ob_ch52, name='nov_close_ob_ch52'),
    path('nov_close_decision_page_ob_ch52/', branch52.nov_close_decision_page_ob_ch52, name='nov_close_decision_page_ob_ch52'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch52/',reports52.detailed_report_choose_months_ob_ch52,name='detailed_report_choose_months_ob_ch52'),

    path('jan_details_live_ob_ch52/', reports52.jan_details_live_ob_ch52, name='jan_details_live_ob_ch52'),
    path('jan_print_live_ob_ch52/', reports52.jan_print_live_ob_ch52, name='jan_print_live_ob_ch52'),
    path('feb_details_live_ob_ch52/', reports52.feb_details_live_ob_ch52, name='feb_details_live_ob_ch52'),
    path('feb_print_live_ob_ch52/', reports52.feb_print_live_ob_ch52, name='feb_print_live_ob_ch52'),
    path('march_details_live_ob_ch52/', reports52.march_details_live_ob_ch52, name='march_details_live_ob_ch52'),
    path('march_print_live_ob_ch52/', reports52.march_print_live_ob_ch52, name='march_print_live_ob_ch52'),

    path('april_details_live_ob_ch52/', reports52.april_details_live_ob_ch52, name='april_details_live_ob_ch52'),
    path('april_print_live_ob_ch52/', reports52.april_print_live_ob_ch52, name='april_print_live_ob_ch52'),
    path('may_details_live_ob_ch52/', reports52.may_details_live_ob_ch52, name='may_details_live_ob_ch52'),
    path('may_print_live_ob_ch52/', reports52.may_print_live_ob_ch52, name='may_print_live_ob_ch52'),
    path('june_details_live_ob_ch52/',reports52.june_details_live_ob_ch52,name='june_details_live_ob_ch52'),
    path('june_print_live_ob_ch52/', reports52.june_print_live_ob_ch52, name='june_print_live_ob_ch52'),

    path('july_details_live_ob_ch52/', reports52.july_details_live_ob_ch52, name='july_details_live_ob_ch52'),
    path('july_print_live_ob_ch52/', reports52.july_print_live_ob_ch52, name='july_print_live_ob_ch52'),
    path('auguest_details_live_ob_ch52/', reports52.auguest_details_live_ob_ch52, name='auguest_details_live_ob_ch52'),
    path('auguest_print_live_ob_ch52/', reports52.auguest_print_live_ob_ch52, name='auguest_print_live_ob_ch52'),
    path('sept_details_live_ob_ch52/', reports52.sept_details_live_ob_ch52, name='sept_details_live_ob_ch52'),
    path('sept_print_live_ob_ch52/', reports52.sept_print_live_ob_ch52, name='sept_print_live_ob_ch52'),

    path('october_details_live_ob_ch52/', reports52.october_details_live_ob_ch52, name='october_details_live_ob_ch52'),
    path('october_print_live_ob_ch52/', reports52.october_print_live_ob_ch52, name='october_print_live_ob_ch52'),
    path('nov_details_live_ob_ch52/', reports52.nov_details_live_ob_ch52, name='nov_details_live_ob_ch52'),
    path('nov_print_live_ob_ch52/', reports52.nov_print_live_ob_ch52, name='nov_print_live_ob_ch52'),
    path('dec_details_live_ob_ch52/', reports52.dec_details_live_ob_ch52, name='dec_details_live_ob_ch52'),
    path('dec_print_live_ob_ch52/', reports52.dec_print_live_ob_ch52, name='dec_print_live_ob_ch52'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch52/', reports52.viewall_vaccant_room_ob_ch52, name='viewall_vaccant_room_ob_ch52'),

    path('d_ob_ch52/', branch52.dynamic, name='dynamic'),

    path('manage_bed_ob_ch52/', branch52.manage_bed_ob_ch52, name='manage_bed_ob_ch52'),
    path('manage_new_guest_ob_ch52/', branch52.manage_new_guest_ob_ch52, name='manage_new_guest_ob_ch52'),
    path('manage_update_new_guest_ob_ch52/<id>', branch52.manage_update_new_guest_ob_ch52, name='manage_update_new_guest_ob_ch52'),
    path('manage_update_beds_ob_ch52/<id>', branch52.manage_update_beds_ob_ch52, name='manage_update_beds_ob_ch52'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch52/', branch52.view_all_due_amt_ob_ch52, name='view_all_due_amt_ob_ch52'),
    path('due_amt_mgt_choose_months_ob_ch52/', branch52.due_amt_mgt_choose_months_ob_ch52, name='due_amt_mgt_choose_months_ob_ch52'),

    path('view_jan_account_details_ob_ch52/', branch52.view_jan_account_details_ob_ch52, name='view_jan_account_details_ob_ch52'),
    path('jan_account_mgt_ob_ch52/<id>',branch52.jan_account_mgt_ob_ch52,name='jan_account_mgt_ob_ch52'),
    path('view_feb_account_details_ob_ch52/', branch52.view_feb_account_details_ob_ch52, name='view_feb_account_details_ob_ch52'),
    path('feb_account_mgt_ob_ch52/<id>',branch52.feb_account_mgt_ob_ch52,name='feb_account_mgt_ob_ch52'),
    path('view_march_account_details_ob_ch52/', branch52.view_march_account_details_ob_ch52, name='view_march_account_details_ob_ch52'),
    path('march_account_mgt_ob_ch52/<id>',branch52.march_account_mgt_ob_ch52,name='march_account_mgt_ob_ch52'),
    path('view_april_account_details_ob_ch52/', branch52.view_april_account_details_ob_ch52, name='view_april_account_details_ob_ch52'),
    path('april_account_mgt_ob_ch52/<id>',branch52.april_account_mgt_ob_ch52,name='april_account_mgt_ob_ch52'),

    path('view_may_account_details_ob_ch52/',branch52.view_may_account_details_ob_ch52,name='view_may_account_details_ob_ch52'),
    path('may_account_mgt_ob_ch52/<id>', branch52.may_account_mgt_ob_ch52, name='may_account_mgt_ob_ch52'),
    path('view_june_account_details_ob_ch52/', branch52.view_june_account_details_ob_ch52, name='view_june_account_details_ob_ch52'),
    path('june_account_mgt_ob_ch52/<id>',branch52.june_account_mgt_ob_ch52,name='june_account_mgt_ob_ch52'),
    path('view_july_account_details_ob_ch52/', branch52.view_july_account_details_ob_ch52, name='view_july_account_details_ob_ch52'),
    path('july_account_mgt_ob_ch52/<id>',branch52.july_account_mgt_ob_ch52,name='july_account_mgt_ob_ch52'),
    path('view_auguest_account_details_ob_ch52/', branch52.view_auguest_account_details_ob_ch52, name='view_auguest_account_details_ob_ch52'),
    path('auguest_account_mgt_ob_ch52/<id>',branch52.auguest_account_mgt_ob_ch52,name='auguest_account_mgt_ob_ch52'),

    path('view_sept_account_details_ob_ch52/', branch52.view_sept_account_details_ob_ch52, name='view_sept_account_details_ob_ch52'),
    path('sept_account_mgt_ob_ch52/<id>',branch52.sept_account_mgt_ob_ch52,name='sept_account_mgt_ob_ch52'),
    path('view_october_account_details_ob_ch52/', branch52.view_october_account_details_ob_ch52, name='view_october_account_details_ob_ch52'),
    path('october_account_mgt_ob_ch52/<id>',branch52.october_account_mgt_ob_ch52,name='october_account_mgt_ob_ch52'),
    path('view_nov_account_details_ob_ch52/', branch52.view_nov_account_details_ob_ch52, name='view_nov_account_details_ob_ch52'),
    path('nov_account_mgt_ob_ch52/<id>',branch52.nov_account_mgt_ob_ch52,name='nov_account_mgt_ob_ch52'),
    path('view_dec_account_details_ob_ch52/', branch52.view_dec_account_details_ob_ch52, name='view_dec_account_details_ob_ch52'),
    path('dec_account_mgt_ob_ch52/<id>',branch52.dec_account_mgt_ob_ch52,name='dec_account_mgt_ob_ch52'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch52', admin_dashboard_calculations_br52.monthly_details_due_ob_ch52, name='monthly_details_due_ob_ch52'),
    path('monthly_collection_details_ob_ch52/', admin_dashboard_calculations_br52.monthly_collection_details_ob_ch52, name='monthly_collection_details_ob_ch52'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch52/',branch52.guest_all_ob_ch52,name='guest_all_ob_ch52'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category52/', accounts52.view_all_category52, name='view_all_category52'),
    path('create_new_category52/', accounts52.create_new_category52, name='create_new_category52'),
    path('regi_new_category52/', accounts52.regi_new_category52, name='regi_new_category52'),
    path('update_category52/<id>',accounts52.update_category52,name='update_category52'),

    path('delete_category52/<id>', accounts52.delete_category52, name='delete_category52'),
    path('view_all_category_delete52/', accounts52.view_all_category_delete52, name='view_all_category_delete52'),

    path('regi_multiple_new_category52/', accounts52.regi_multiple_new_category52, name='regi_multiple_new_category52'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items52/', accounts52.view_all_items52, name='view_all_items52'),
    path('create_new_item52/', accounts52.create_new_item52, name='create_new_item52'),
    path('regi_new_item52/', accounts52.regi_new_item52, name='regi_new_item52'),
    path('delete_item52/<id>',accounts52.delete_item52,name='delete_item52'),
    path('update_item52/<id>', accounts52.update_item52, name='update_item52'),
    path('view_all_items_delete52/',accounts52.view_all_items_delete52,name='view_all_items_delete52'),

    path('regi_multiple_new_item52/', accounts52.regi_multiple_new_item52, name='regi_multiple_new_item52'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger52/', accounts52.view_all_ledger52, name='view_all_ledger52'),
    path('create_new_ledger52/', accounts52.create_new_ledger52, name='create_new_ledger52'),
    path('regi_new_ledger52/', accounts52.regi_new_ledger52, name='regi_new_ledger52'),
    path('delete_ledger52/<id>',accounts52.delete_ledger52,name='delete_ledger52'),
    path('update_ledger52/<id>',accounts52.update_ledger52,name='update_ledger52'),
    path('view_all_ledger_delete52/',accounts52.view_all_ledger_delete52,name='view_all_ledger_delete52'),

    path('regi_multiple_new_ledger52/', accounts52.regi_multiple_new_ledger52, name='regi_multiple_new_ledger52'),

    ##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book52/', accounts52.view_all_accounts_book52, name='view_all_accounts_book52'),
    path('create_new_accounts_book52/', accounts52.create_new_accounts_book52, name='create_new_accounts_book52'),
    path('regi_new_accounts_book52/', accounts52.regi_new_accounts_book52, name='regi_new_accounts_book52'),
    path('update_accounts_book52/<id>',accounts52.update_accounts_book52,name='update_accounts_book52'),
    path('delete_accounts_book52/<id>',accounts52.delete_accounts_book52,name='delete_accounts_book52'),
    path('view_all_accounts_book_delete52/',accounts52.view_all_accounts_book_delete52,name='view_all_accounts_book_delete52'),

    path('regi_multiple_new_accounts_book52/', accounts52.regi_multiple_new_accounts_book52,name='regi_multiple_new_accounts_book52'),

    ##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries52/', accounts52.get_countries52, name='get_countries52'),

    path('in_exp_items_entry52/', accounts52.in_exp_items_entry52, name='in_exp_items_entry52'),
    path('reg_in_exp_items_entry52/', accounts52.reg_in_exp_items_entry52, name='reg_in_exp_items_entry52'),
    path('delete_journal52/<id>',accounts52.delete_journal52,name='delete_journal52'),
    path('update_in_exp_items_entry52/<id>',accounts52.update_in_exp_items_entry52,name='update_in_exp_items_entry52'),
    path('detailed_journal_report52/',accounts52.detailed_journal_report52,name='detailed_journal_report52'),
    path('journal_report_deleted52/',accounts52.journal_report_deleted52,name='journal_report_deleted52'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise52/', accounts52.daily_category_wise52, name='daily_category_wise52'),
    path('monthly_category_based_reports52/',accounts52.monthly_category_based_reports52,name='monthly_category_based_reports52'),
    path('yearly_category_based_reports52/', accounts52.yearly_category_based_reports52,name='yearly_category_based_reports52'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed52/', accounts52.daily_detailed52, name='daily_detailed52'),
    path('monthly_detailed52/',accounts52.monthly_detailed52,name='monthly_detailed52'),
    path('yearly_detailed52/',accounts52.yearly_detailed52,name='yearly_detailed52'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports52/', accounts52.item_based_reports52, name='item_based_reports52'),
    path('daily_item_based_reports52/',accounts52.daily_item_based_reports52,name='daily_item_based_reports52'),
    path('monthly_item_based_reports52/',accounts52.monthly_item_based_reports52,name='monthly_item_based_reports52'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports52/', accounts52.ledger_based_reports52, name='ledger_based_reports52'),
    path('monthly_ledger_based_reports52/', accounts52.monthly_ledger_based_reports52, name='monthly_ledger_based_reports52'),
    path('daily_ledger_based_reports52/',accounts52.daily_ledger_based_reports52,name='daily_ledger_based_reports52'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports52/', accounts52.accounts_book_based_reports52, name='accounts_book_based_reports52'),
    path('daily_accounts_book_based_reports52/',accounts52.daily_accounts_book_based_reports52,name='daily_accounts_book_based_reports52'),
    path('monthly_accounts_book_based_reports52/',accounts52.monthly_accounts_book_based_reports52,name='monthly_accounts_book_based_reports52'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months52/', accounts52.monthly_reports_choose_months52, name='monthly_reports_choose_months52'),
    path('monthly_detailed_daily_in_exp_items_report52/<mo>',accounts52.monthly_detailed_daily_in_exp_items_report52,name='monthly_detailed_daily_in_exp_items_report52'),

    path('single_monthly_reports_choose_months52/', accounts52.single_monthly_reports_choose_months52,name='single_monthly_reports_choose_months52'),
    path('single_monthly_daily_in_exp_items_report52/<mo>',accounts52.single_monthly_daily_in_exp_items_report52,name='single_monthly_daily_in_exp_items_report52'),

    path('accounts_dash_board_ob_ch52/',accounts52.accounts_dash_board_ob_ch52,name='accounts_dash_board_ob_ch52'),
    path('accounts_dash_board52/',accounts52.accounts_dash_board52,name='accounts_dash_board52'),

    path('profit_sharing_choose_months52', accounts52.profit_sharing_choose_months52,name='profit_sharing_choose_months52'),
    path('profit_sharing52/<mo>', accounts52.profit_sharing52, name='profit_sharing52'),
    path('view_share_holders52', accounts52.view_share_holders52, name='view_share_holders52'),
    path('create_share_holders52', accounts52.create_share_holders52, name='create_share_holders52'),
    path('regi_share_holders52', accounts52.regi_share_holders52, name='regi_share_holders52'),
    path('update_share_holders52/<id>', accounts52.update_share_holders52, name='update_share_holders52'),
    path('delete_share_holders52/<id>', accounts52.delete_share_holders52, name='delete_share_holders52'),
    path('view_deleted_share_holders52', accounts52.view_deleted_share_holders52, name='view_deleted_share_holders52'),

    path('regi_multiple_share_holders52', accounts52.regi_multiple_share_holders52, name='regi_multiple_share_holders52'),

]

