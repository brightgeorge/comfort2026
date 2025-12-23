from django.urls import path, include

from . import admin_branch42
from . import admin_branch42
from . import branch42
from . import reports42
from . import payment42
from . import admin_dashboard_calculations_br42
from . import accounts42
from . import branch_settings42

urlpatterns = [

    path('branch1_dashboard_ob_ch42/', branch42.branch1_dashboard_ob_ch42, name='branch1_dashboard_ob_ch42'),
    path('branch1_dashboard42/',branch42.branch1_dashboard42,name='branch1_dashboard42'),
    path('user_dashboard_calculations_ob_ch42/',branch42.user_dashboard_calculations_ob_ch42,name='user_dashboard_calculations_ob_ch42'),

    path('background_ob_ch42',branch42.background_ob_ch42,name='background_ob_ch42'),
    path('background_regi_ob_ch42',branch42.background_regi_ob_ch42,name='background_regi_ob_ch42'),
    path('custom_background_regi_ob_ch42',branch42.custom_background_regi_ob_ch42,name='custom_background_regi_ob_ch42'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch42/',admin_branch42.branch1_room_create_regi_ob_ch42,name='branch1_room_create_regi_ob_ch42'),
    path('view_all_room_ob_ch42/',admin_branch42.view_all_room_ob_ch42,name='view_all_room_ob_ch42'),
    path('delete_room_ob_ch42/<id>',admin_branch42.delete_room_ob_ch42,name='delete_room_ob_ch42'),

    path('branch1_room_create_ob_ch42/',admin_branch42.branch1_room_create_ob_ch42,name='branch1_room_create_ob_ch42'),

    path('multiple_branch1_room_create_regi42/',admin_branch42.multiple_branch1_room_create_regi42,name='multiple_branch1_room_create_regi42'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch42/', admin_branch42.pg1_bed_create_regi_ob_ch42, name='pg1_bed_create_regi_ob_ch42'),
    path('pg1_view_all_beds_ob_ch42/', admin_branch42.pg1_view_all_beds_ob_ch42, name='pg1_view_all_beds_ob_ch42'),
    path('delete_bed_ob_ch42/<id>', admin_branch42.delete_bed_ob_ch42, name='delete_bed_ob_ch42'),

    path('pg1_bed_create_ob_ch42/', admin_branch42.pg1_bed_create_ob_ch42, name='pg1_bed_create_ob_ch42'),

    path('single_pg1_bed_create_regi_ob_ch42/',admin_branch42.single_pg1_bed_create_regi_ob_ch42,name='single_pg1_bed_create_regi_ob_ch42'),
    path('update_bed_basic_details_ob_ch42/<id>',admin_branch42.update_bed_basic_details_ob_ch42, name='update_bed_basic_details_ob_ch42'),

    path('multiple_single_pg1_bed_create_regi42/',admin_branch42.multiple_single_pg1_bed_create_regi42,name='multiple_single_pg1_bed_create_regi42'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch42/<id>',branch42.br1_admit_guest_ob_ch42,name='br1_admit_guest_ob_ch42'),
    path('view_all_new_guest_ob_ch42/',branch42.view_all_new_guest_ob_ch42,name='view_all_new_guest_ob_ch42'),
    path('update_br1_admit_guest_ob_ch42/<id>',branch42.update_br1_admit_guest_ob_ch42,name='update_br1_admit_guest_ob_ch42'),
    path('vacate_br1_guest_ob_ch42/<id>',branch42.vacate_br1_guest_ob_ch42,name='vacate_br1_guest_ob_ch42'),

    path('active_guest_details_ob_ch42/<guest_code>',branch42.active_guest_details_ob_ch42,name='active_guest_details_ob_ch42'),
    path('view_all_guest_ob_ch42/',branch42.view_all_guest_ob_ch42,name='view_all_guest_ob_ch42'),
    path('shift_guest_ob_ch42/<id>',branch42.shift_guest_ob_ch42,name='shift_guest_ob_ch42'),
    path('shift_guest_regi_ob_ch42/',branch42.shift_guest_regi_ob_ch42,name='shift_guest_regi_ob_ch42'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch42/',branch42.update_all_rent_ob_ch42,name='update_all_rent_ob_ch42'),

    path('multiple_br1_admit_guest42/<id>',branch42.multiple_br1_admit_guest42,name='multiple_br1_admit_guest42'),

#guest end here


##################################
#_ADVANCE_ob_ch42 START HERE
################################


    path('choose_months_advance_ob_ch42/',branch42.choose_months_advance_ob_ch42,name='choose_months_advance_ob_ch42'),

    path('jan_advance_ob_ch42/', branch42.jan_advance_ob_ch42, name='jan_advance_ob_ch42'),
    path('jan_make_payments_advance_ob_ch42/<id>', branch42.jan_make_payments_advance_ob_ch42,name='jan_make_payments_advance_ob_ch42'),
    path('feb_advance_ob_ch42/', branch42.feb_advance_ob_ch42, name='feb_advance_ob_ch42'),
    path('feb_make_payments_advance_ob_ch42/<id>', branch42.feb_make_payments_advance_ob_ch42,name='feb_make_payments_advance_ob_ch42'),
    path('march_advance_ob_ch42/', branch42.march_advance_ob_ch42, name='march_advance_ob_ch42'),
    path('march_make_payments_advance_ob_ch42/<id>', branch42.march_make_payments_advance_ob_ch42,name='march_make_payments_advance_ob_ch42'),
    path('april_advance_ob_ch42/', branch42.april_advance_ob_ch42, name='april_advance_ob_ch42'),
    path('april_make_payments_advance_ob_ch42/<id>', branch42.april_make_payments_advance_ob_ch42, name='april_make_payments_advance_ob_ch42'),

    path('may_advance_ob_ch42/',branch42.may_advance_ob_ch42,name='may_advance_ob_ch42'),
    path('may_make_payments_advance_ob_ch42/<id>', branch42.may_make_payments_advance_ob_ch42, name='may_make_payments_advance_ob_ch42'),
    path('june_advance_ob_ch42/',branch42.june_advance_ob_ch42,name='june_advance_ob_ch42'),
    path('june_make_payments_advance_ob_ch42/<id>', branch42.june_make_payments_advance_ob_ch42, name='june_make_payments_advance_ob_ch42'),
    path('july_advance_ob_ch42/',branch42.july_advance_ob_ch42,name='july_advance_ob_ch42'),
    path('july_make_payments_advance_ob_ch42/<id>', branch42.july_make_payments_advance_ob_ch42, name='july_make_payments_advance_ob_ch42'),
    path('auguest_advance_ob_ch42/', branch42.auguest_advance_ob_ch42, name='auguest_advance_ob_ch42'),
    path('auguest_make_payments_advance_ob_ch42/<id>', branch42.auguest_make_payments_advance_ob_ch42, name='auguest_make_payments_advance_ob_ch42'),

    path('sept_advance_ob_ch42/', branch42.sept_advance_ob_ch42, name='sept_advance_ob_ch42'),
    path('sept_make_payments_advance_ob_ch42/<id>', branch42.sept_make_payments_advance_ob_ch42,name='sept_make_payments_advance_ob_ch42'),
    path('october_advance_ob_ch42/', branch42.october_advance_ob_ch42, name='october_advance_ob_ch42'),
    path('october_make_payments_advance_ob_ch42/<id>', branch42.october_make_payments_advance_ob_ch42, name='october_make_payments_advance_ob_ch42'),
    path('nov_advance_ob_ch42/', branch42.nov_advance_ob_ch42, name='nov_advance_ob_ch42'),
    path('nov_make_payments_advance_ob_ch42/<id>', branch42.nov_make_payments_advance_ob_ch42,name='nov_make_payments_advance_ob_ch42'),
    path('dec_advance_ob_ch42/', branch42.dec_advance_ob_ch42, name='dec_advance_ob_ch42'),
    path('dec_make_payments_advance_ob_ch42/<id>', branch42.dec_make_payments_advance_ob_ch42, name='dec_make_payments_advance_ob_ch42'),



##################################
#_ADVANCE_ob_ch42 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch42/',branch42.choose_months_ob_ch42,name='choose_months_ob_ch42'),

    path('jan_ob_ch42/',branch42.jan_ob_ch42,name='jan_ob_ch42'),
    path('jan_manke_payments_ob_ch42/<id>',branch42.jan_manke_payments_ob_ch42,name='jan_manke_payments_ob_ch42'),

    path('feb_ob_ch42/',branch42.feb_ob_ch42,name='feb_ob_ch42'),
    path('feb_manke_payments_ob_ch42/<id>',branch42.feb_manke_payments_ob_ch42,name='feb_manke_payments_ob_ch42'),

    path('march_ob_ch42/',branch42.march_ob_ch42,name='march_ob_ch42'),
    path('march_manke_payments_ob_ch42/<id>',branch42.march_manke_payments_ob_ch42,name='march_manke_payments_ob_ch42'),

    path('april_ob_ch42/',branch42.april_ob_ch42,name='april_ob_ch42'),
    path('april_make_payments_ob_ch42/<id>',branch42.april_make_payments_ob_ch42,name='april_make_payments_ob_ch42'),

    path('may_ob_ch42/',branch42.may_ob_ch42,name='may_ob_ch42'),
    path('may_make_payments_ob_ch42/<id>',branch42.may_make_payments_ob_ch42,name='may_make_payments_ob_ch42'),

    path('june_ob_ch42/',branch42.june_ob_ch42,name='june_ob_ch42'),
    path('june_make_payments_ob_ch42/<id>',branch42.june_make_payments_ob_ch42,name='june_make_payments_ob_ch42'),

    path('july_ob_ch42/',branch42.july_ob_ch42,name='july_ob_ch42'),
    path('july_make_payments_ob_ch42/<id>',branch42.july_make_payments_ob_ch42,name='july_make_payments_ob_ch42'),

    path('aug_ob_ch42/',branch42.aug_ob_ch42,name='aug_ob_ch42'),
    path('aug_make_payments_ob_ch42/<id>',branch42.aug_make_payments_ob_ch42,name='aug_make_payments_ob_ch42'),

    path('sept_ob_ch42/',branch42.sept_ob_ch42,name='sept_ob_ch42'),
    path('sept_make_payments_ob_ch42/<id>',branch42.sept_make_payments_ob_ch42,name='sept_make_payments_ob_ch42'),

    path('oct_ob_ch42/',branch42.oct_ob_ch42,name='oct_ob_ch42'),
    path('oct_make_payments_ob_ch42/<id>',branch42.oct_make_payments_ob_ch42,name='oct_make_payments_ob_ch42'),

    path('nov_ob_ch42/',branch42.nov_ob_ch42,name='nov_ob_ch42'),
    path('nov_make_payments_ob_ch42/<id>',branch42.nov_make_payments_ob_ch42,name='nov_make_payments_ob_ch42'),

    path('dec_ob_ch42/',branch42.dec_ob_ch42,name='dec_ob_ch42'),
    path('dec_make_payments_ob_ch42/<id>',branch42.dec_make_payments_ob_ch42,name='dec_make_payments_ob_ch42'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch42/', payment42.choose_user_ob_ch42, name='choose_user_ob_ch42'),
    path('payment_user_details_ob_ch42/<id>', payment42.payment_user_details_ob_ch42, name='payment_user_details_ob_ch42'),
    path('close_choose_user_ob_ch42/<id>',payment42.close_choose_user_ob_ch42,name='close_choose_user_ob_ch42'),

    path('monthly_jan_make_payments_ob_ch42/<id>', payment42.monthly_jan_make_payments_ob_ch42, name='monthly_jan_make_payments_ob_ch42'),
    path('monthly_feb_make_payments_ob_ch42/<id>', payment42.monthly_feb_make_payments_ob_ch42, name='monthly_feb_make_payments_ob_ch42'),
    path('monthly_march_make_payments_ob_ch42/<id>', payment42.monthly_march_make_payments_ob_ch42, name='monthly_march_make_payments_ob_ch42'),
    path('monthly_april_make_payments_ob_ch42/<id>', payment42.monthly_april_make_payments_ob_ch42, name='monthly_april_make_payments_ob_ch42'),
    path('monthly_may_make_payments_ob_ch42/<id>', payment42.monthly_may_make_payments_ob_ch42, name='monthly_may_make_payments_ob_ch42'),
    path('monthly_june_make_payments_ob_ch42/<id>', payment42.monthly_june_make_payments_ob_ch42, name='monthly_june_make_payments_ob_ch42'),

    path('monthly_july_make_payments_ob_ch42/<id>', payment42.monthly_july_make_payments_ob_ch42, name='monthly_july_make_payments_ob_ch42'),
    path('monthly_aug_make_payments_ob_ch42/<id>', payment42.monthly_aug_make_payments_ob_ch42, name='monthly_aug_make_payments_ob_ch42'),
    path('monthly_sept_make_payments_ob_ch42/<id>', payment42.monthly_sept_make_payments_ob_ch42, name='monthly_sept_make_payments_ob_ch42'),
    path('monthly_oct_make_payments_ob_ch42/<id>', payment42.monthly_oct_make_payments_ob_ch42, name='monthly_oct_make_payments_ob_ch42'),
    path('monthly_nov_make_payments_ob_ch42/<id>', payment42.monthly_nov_make_payments_ob_ch42, name='monthly_nov_make_payments_ob_ch42'),
    path('monthly_dec_make_payments_ob_ch42/<id>', payment42.monthly_dec_make_payments_ob_ch42, name='monthly_dec_make_payments_ob_ch42'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch42/',branch42.unpaid_rent_choose_months_ob_ch42,name='unpaid_rent_choose_months_ob_ch42'),

    path('jan_unpaid_rent_ob_ch42/', branch42.jan_unpaid_rent_ob_ch42, name='jan_unpaid_rent_ob_ch42'),
    path('table_jan_unpaid_rent_ob_ch42/', branch42.table_jan_unpaid_rent_ob_ch42, name='table_jan_unpaid_rent_ob_ch42'),
    path('feb_unpaid_rent_ob_ch42/', branch42.feb_unpaid_rent_ob_ch42, name='feb_unpaid_rent_ob_ch42'),
    path('table_feb_unpaid_rent_ob_ch42/', branch42.table_feb_unpaid_rent_ob_ch42, name='table_feb_unpaid_rent_ob_ch42'),
    path('mar_unpaid_rent_ob_ch42/', branch42.mar_unpaid_rent_ob_ch42, name='mar_unpaid_rent_ob_ch42'),
    path('table_mar_unpaid_rent_ob_ch42/', branch42.table_mar_unpaid_rent_ob_ch42, name='table_mar_unpaid_rent_ob_ch42'),
    path('april_unpaid_rent_ob_ch42/', branch42.april_unpaid_rent_ob_ch42, name='april_unpaid_rent_ob_ch42'),
    path('table_april_unpaid_rent_ob_ch42/', branch42.table_april_unpaid_rent_ob_ch42, name='table_april_unpaid_rent_ob_ch42'),

    path('may_unpaid_rent_ob_ch42/', branch42.may_unpaid_rent_ob_ch42, name='may_unpaid_rent_ob_ch42'),
    path('table_may_unpaid_rent_ob_ch42/', branch42.table_may_unpaid_rent_ob_ch42, name='table_may_unpaid_rent_ob_ch42'),
    path('june_unpaid_rent_ob_ch42/', branch42.june_unpaid_rent_ob_ch42, name='june_unpaid_rent_ob_ch42'),
    path('table_june_unpaid_rent_ob_ch42/', branch42.table_june_unpaid_rent_ob_ch42, name='table_june_unpaid_rent_ob_ch42'),
    path('july_unpaid_rent_ob_ch42/', branch42.july_unpaid_rent_ob_ch42, name='july_unpaid_rent_ob_ch42'),
    path('table_july_unpaid_rent_ob_ch42',branch42.table_july_unpaid_rent_ob_ch42,name='table_july_unpaid_rent_ob_ch42'),
    path('aug_unpaid_rent_ob_ch42/', branch42.aug_unpaid_rent_ob_ch42, name='aug_unpaid_rent_ob_ch42'),
    path('table_aug_unpaid_rent_ob_ch42/',branch42.table_aug_unpaid_rent_ob_ch42,name='table_aug_unpaid_rent_ob_ch42'),

    path('sept_unpaid_rent_ob_ch42/', branch42.sept_unpaid_rent_ob_ch42, name='sept_unpaid_rent_ob_ch42'),
    path('table_sept_unpaid_rent_ob_ch42/', branch42.table_sept_unpaid_rent_ob_ch42, name='table_sept_unpaid_rent_ob_ch42'),
    path('oct_unpaid_rent_ob_ch42/', branch42.oct_unpaid_rent_ob_ch42, name='oct_unpaid_rent_ob_ch42'),
    path('table_oct_unpaid_rent_ob_ch42/', branch42.table_oct_unpaid_rent_ob_ch42, name='table_oct_unpaid_rent_ob_ch42'),
    path('nov_unpaid_rent_ob_ch42/', branch42.nov_unpaid_rent_ob_ch42, name='nov_unpaid_rent_ob_ch42'),
    path('table_nov_unpaid_rent_ob_ch42/', branch42.table_nov_unpaid_rent_ob_ch42, name='table_nov_unpaid_rent_ob_ch42'),
    path('dec_unpaid_rent_ob_ch42/', branch42.dec_unpaid_rent_ob_ch42, name='dec_unpaid_rent_ob_ch42'),
    path('table_dec_unpaid_rent_ob_ch42/', branch42.table_dec_unpaid_rent_ob_ch42, name='table_dec_unpaid_rent_ob_ch42'),

    path('details_of_unpaid_guests_ob_ch42/<id>',branch42.details_of_unpaid_guests_ob_ch42,name='details_of_unpaid_guests_ob_ch42'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch42/',branch42.paid_rent_choose_months_ob_ch42,name='paid_rent_choose_months_ob_ch42'),
    path('partially_paid_guest_choose_months_ob_ch42/',reports42.partially_paid_guest_choose_months_ob_ch42,name='partially_paid_guest_choose_months_ob_ch42'),

    path('jan_paid_rent_ob_ch42/', branch42.jan_paid_rent_ob_ch42, name='jan_paid_rent_ob_ch42'),
    path('table_jan_paid_rent_ob_ch42/', branch42.table_jan_paid_rent_ob_ch42, name='table_jan_paid_rent_ob_ch42'),
    path('jan_full_paid_guest_ob_ch42/', reports42.jan_full_paid_guest_ob_ch42, name='jan_full_paid_guest_ob_ch42'),
    path('jan_partially_paid_guest_ob_ch42/', reports42.jan_partially_paid_guest_ob_ch42, name='jan_partially_paid_guest_ob_ch42'),
    path('table_jan_partially_paid_guest_ob_ch42/', reports42.table_jan_partially_paid_guest_ob_ch42,name='table_jan_partially_paid_guest_ob_ch42'),

    path('feb_paid_rent_ob_ch42/', branch42.feb_paid_rent_ob_ch42, name='feb_paid_rent_ob_ch42'),
    path('table_feb_paid_rent_ob_ch42/', branch42.table_feb_paid_rent_ob_ch42, name='table_feb_paid_rent_ob_ch42'),
    path('feb_full_paid_guest_ob_ch42/', reports42.feb_full_paid_guest_ob_ch42, name='feb_full_paid_guest_ob_ch42'),
    path('feb_partially_paid_guest_ob_ch42/', reports42.feb_partially_paid_guest_ob_ch42, name='feb_partially_paid_guest_ob_ch42'),
    path('table_feb_partially_paid_guest_ob_ch42/', reports42.table_feb_partially_paid_guest_ob_ch42,name='table_feb_partially_paid_guest_ob_ch42'),

    path('mar_paid_rent_ob_ch42/', branch42.mar_paid_rent_ob_ch42, name='mar_paid_rent_ob_ch42'),
    path('table_mar_paid_rent_ob_ch42/', branch42.table_mar_paid_rent_ob_ch42, name='table_mar_paid_rent_ob_ch42'),
    path('march_full_paid_guest_ob_ch42/', reports42.march_full_paid_guest_ob_ch42, name='march_full_paid_guest_ob_ch42'),
    path('march_partially_paid_guest_ob_ch42/', reports42.march_partially_paid_guest_ob_ch42, name='march_partially_paid_guest_ob_ch42'),
    path('table_march_partially_paid_guest_ob_ch42/', reports42.table_march_partially_paid_guest_ob_ch42,name='table_march_partially_paid_guest_ob_ch42'),

    path('april_paid_rent_ob_ch42/', branch42.april_paid_rent_ob_ch42, name='april_paid_rent_ob_ch42'),
    path('table_april_paid_rent_ob_ch42/', branch42.table_april_paid_rent_ob_ch42, name='table_april_paid_rent_ob_ch42'),
    path('april_full_paid_guest_ob_ch42/', reports42.april_full_paid_guest_ob_ch42, name='april_full_paid_guest_ob_ch42'),
    path('april_partially_paid_guest_ob_ch42/', reports42.april_partially_paid_guest_ob_ch42, name='april_partially_paid_guest_ob_ch42'),
    path('table_april_partially_paid_guest_ob_ch42/', reports42.table_april_partially_paid_guest_ob_ch42,name='table_april_partially_paid_guest_ob_ch42'),

    path('may_paid_rent_ob_ch42/', branch42.may_paid_rent_ob_ch42, name='may_paid_rent_ob_ch42'),
    path('table_may_paid_rent_ob_ch42/', branch42.table_may_paid_rent_ob_ch42, name='table_may_paid_rent_ob_ch42'),
    path('may_full_paid_guest_ob_ch42/', reports42.may_full_paid_guest_ob_ch42, name='may_full_paid_guest_ob_ch42'),
    path('may_partially_paid_guest_ob_ch42/', reports42.may_partially_paid_guest_ob_ch42, name='may_partially_paid_guest_ob_ch42'),
    path('table_may_partially_paid_guest_ob_ch42/', reports42.table_may_partially_paid_guest_ob_ch42, name='table_may_partially_paid_guest_ob_ch42'),

    path('june_paid_rent_ob_ch42/', branch42.june_paid_rent_ob_ch42, name='june_paid_rent_ob_ch42'),
    path('table_june_paid_rent_ob_ch42/', branch42.table_june_paid_rent_ob_ch42, name='table_june_paid_rent_ob_ch42'),
    path('june_full_paid_guest_ob_ch42/', reports42.june_full_paid_guest_ob_ch42, name='june_full_paid_guest_ob_ch42'),
    path('june_partially_paid_guest_ob_ch42/', reports42.june_partially_paid_guest_ob_ch42, name='june_partially_paid_guest_ob_ch42'),
    path('table_june_partially_paid_guest_ob_ch42/', reports42.table_june_partially_paid_guest_ob_ch42, name='table_june_partially_paid_guest_ob_ch42'),

    path('july_paid_rent_ob_ch42/', branch42.july_paid_rent_ob_ch42, name='july_paid_rent_ob_ch42'),
    path('table_july_paid_rent_ob_ch42/', branch42.table_july_paid_rent_ob_ch42, name='table_july_paid_rent_ob_ch42'),
    path('july_full_paid_guest_ob_ch42/', reports42.july_full_paid_guest_ob_ch42, name='july_full_paid_guest_ob_ch42'),
    path('july_partially_paid_guest_ob_ch42/', reports42.july_partially_paid_guest_ob_ch42, name='july_partially_paid_guest_ob_ch42'),
    path('table_july_partially_paid_guest_ob_ch42/', reports42.table_july_partially_paid_guest_ob_ch42, name='table_july_partially_paid_guest_ob_ch42'),

    path('aug_paid_rent_ob_ch42/', branch42.aug_paid_rent_ob_ch42, name='aug_paid_rent_ob_ch42'),
    path('table_aug_paid_rent_ob_ch42/', branch42.table_aug_paid_rent_ob_ch42, name='table_aug_paid_rent_ob_ch42'),
    path('auguest_full_paid_guest_ob_ch42/', reports42.auguest_full_paid_guest_ob_ch42, name='auguest_full_paid_guest_ob_ch42'),
    path('auguest_partially_paid_guest_ob_ch42/', reports42.auguest_partially_paid_guest_ob_ch42,name='auguest_partially_paid_guest_ob_ch42'),
    path('table_auguest_partially_paid_guest_ob_ch42/', reports42.table_auguest_partially_paid_guest_ob_ch42,name='table_auguest_partially_paid_guest_ob_ch42'),

    path('sept_paid_rent_ob_ch42/', branch42.sept_paid_rent_ob_ch42, name='sept_paid_rent_ob_ch42'),
    path('table_sept_paid_rent_ob_ch42/', branch42.table_sept_paid_rent_ob_ch42, name='table_sept_paid_rent_ob_ch42'),
    path('sept_full_paid_guest_ob_ch42/', reports42.sept_full_paid_guest_ob_ch42, name='sept_full_paid_guest_ob_ch42'),
    path('sept_partially_paid_guest_ob_ch42/', reports42.sept_partially_paid_guest_ob_ch42, name='sept_partially_paid_guest_ob_ch42'),
    path('table_sept_partially_paid_guest_ob_ch42/', reports42.table_sept_partially_paid_guest_ob_ch42,name='table_sept_partially_paid_guest_ob_ch42'),

    path('oct_paid_rent_ob_ch42/', branch42.oct_paid_rent_ob_ch42, name='oct_paid_rent_ob_ch42'),
    path('table_oct_paid_rent_ob_ch42/', branch42.table_oct_paid_rent_ob_ch42, name='table_oct_paid_rent_ob_ch42'),
    path('october_full_paid_guest_ob_ch42/', reports42.october_full_paid_guest_ob_ch42, name='october_full_paid_guest_ob_ch42'),
    path('october_partially_paid_guest_ob_ch42/', reports42.october_partially_paid_guest_ob_ch42,name='october_partially_paid_guest_ob_ch42'),
    path('table_october_partially_paid_guest_ob_ch42/', reports42.table_october_partially_paid_guest_ob_ch42,name='table_october_partially_paid_guest_ob_ch42'),

    path('nov_paid_rent_ob_ch42/', branch42.nov_paid_rent_ob_ch42, name='nov_paid_rent_ob_ch42'),
    path('table_nov_paid_rent_ob_ch42/', branch42.table_nov_paid_rent_ob_ch42, name='table_nov_paid_rent_ob_ch42'),
    path('nov_full_paid_guest_ob_ch42/', reports42.nov_full_paid_guest_ob_ch42, name='nov_full_paid_guest_ob_ch42'),
    path('nov_partially_paid_guest_ob_ch42/', reports42.nov_partially_paid_guest_ob_ch42, name='nov_partially_paid_guest_ob_ch42'),
    path('table_nov_partially_paid_guest_ob_ch42/', reports42.table_nov_partially_paid_guest_ob_ch42,name='table_nov_partially_paid_guest_ob_ch42'),

    path('dec_paid_rent_ob_ch42/', branch42.dec_paid_rent_ob_ch42, name='dec_paid_rent_ob_ch42'),
    path('table_dec_paid_rent_ob_ch42/', branch42.table_dec_paid_rent_ob_ch42, name='table_dec_paid_rent_ob_ch42'),
    path('dec_full_paid_guest_ob_ch42/', reports42.dec_full_paid_guest_ob_ch42, name='dec_full_paid_guest_ob_ch42'),
    path('dec_partially_paid_guest_ob_ch42/', reports42.dec_partially_paid_guest_ob_ch42, name='dec_partially_paid_guest_ob_ch42'),
    path('table_dec_partially_paid_guest_ob_ch42/', reports42.table_dec_partially_paid_guest_ob_ch42,name='table_dec_partially_paid_guest_ob_ch42'),

    path('details_of_paid_guests_ob_ch42/<id>',branch42.details_of_paid_guests_ob_ch42,name='details_of_paid_guests_ob_ch42'),
    path('full_paid_guest_ob_ch42/',reports42.full_paid_guest_ob_ch42,name='full_paid_guest_ob_ch42'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch42/',branch42.viewall_vacate_guest_ob_ch42,name='viewall_vacate_guest_ob_ch42'),
    path('details_of_vacate_guest_ob_ch42/<id>',branch42.details_of_vacate_guest_ob_ch42,name='details_of_vacate_guest_ob_ch42'),
    path('full_vacated_guest_details_ob_ch42',branch42.full_vacated_guest_details_ob_ch42,name='full_vacated_guest_details_ob_ch42'),
    path('full_vacated_guest_table_ob_ch42',branch42.full_vacated_guest_table_ob_ch42,name='full_vacated_guest_table_ob_ch42'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch42/<id>', branch42.jan_manke_payments_vacate_ob_ch42, name='jan_manke_payments_vacate_ob_ch42'),
    path('feb_manke_payments_vacate_ob_ch42/<id>', branch42.feb_manke_payments_vacate_ob_ch42, name='feb_manke_payments_vacate_ob_ch42'),
    path('march_manke_payments_vacate_ob_ch42/<id>', branch42.march_manke_payments_vacate_ob_ch42, name='march_manke_payments_vacate_ob_ch42'),
    path('april_make_payments_vacate_ob_ch42/<id>', branch42.april_make_payments_vacate_ob_ch42, name='april_make_payments_vacate_ob_ch42'),

    path('may_make_payments_vacate_ob_ch42/<id>', branch42.may_make_payments_vacate_ob_ch42, name='may_make_payments_vacate_ob_ch42'),
    path('june_make_payments_vacate_ob_ch42/<id>', branch42.june_make_payments_vacate_ob_ch42, name='june_make_payments_vacate_ob_ch42'),
    path('july_make_payments_vacate_ob_ch42/<id>', branch42.july_make_payments_vacate_ob_ch42, name='july_make_payments_vacate_ob_ch42'),
    path('aug_make_payments_vacate_ob_ch42/<id>', branch42.aug_make_payments_vacate_ob_ch42, name='aug_make_payments_vacate_ob_ch42'),

    path('sept_make_payments_vacate_ob_ch42/<id>', branch42.sept_make_payments_vacate_ob_ch42, name='sept_make_payments_vacate_ob_ch42'),
    path('oct_make_payments_vacate_ob_ch42/<id>', branch42.oct_make_payments_vacate_ob_ch42, name='oct_make_payments_vacate_ob_ch42'),
    path('nov_make_payments_vacate_ob_ch42/<id>', branch42.nov_make_payments_vacate_ob_ch42, name='nov_make_payments_vacate_ob_ch42'),
    path('dec_make_payments_vacate_ob_ch42/<id>', branch42.dec_make_payments_vacate_ob_ch42, name='dec_make_payments_vacate_ob_ch42'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch42/',branch42.detail_guest_general_ob_ch42,name='detail_guest_general_ob_ch42'),

    path('jan_print_ob_ch42/',branch42.jan_print_ob_ch42,name='jan_print_ob_ch42'),
    path('feb_print_ob_ch42/',branch42.feb_print_ob_ch42,name='feb_print_ob_ch42'),
    path('march_print_ob_ch42/',branch42.march_print_ob_ch42,name='march_print_ob_ch42'),
    path('april_print_ob_ch42/',branch42.april_print_ob_ch42,name='april_print_ob_ch42'),

    path('may_print_ob_ch42/',branch42.may_print_ob_ch42,name='may_print_ob_ch42'),
    path('june_print_ob_ch42/',branch42.june_print_ob_ch42,name='june_print_ob_ch42'),
    path('july_print_ob_ch42/', branch42.july_print_ob_ch42, name='july_print_ob_ch42'),
    path('aug_print_ob_ch42/', branch42.aug_print_ob_ch42, name='aug_print_ob_ch42'),

    path('sept_print_ob_ch42/', branch42.sept_print_ob_ch42, name='sept_print_ob_ch42'),
    path('oct_print_ob_ch42/', branch42.oct_print_ob_ch42, name='oct_print_ob_ch42'),
    path('nov_print_ob_ch42/', branch42.nov_print_ob_ch42, name='nov_print_ob_ch42'),
    path('dec_print_ob_ch42/', branch42.dec_print_ob_ch42, name='dec_print_ob_ch42'),

    path('new_year_jan_print_ob_ch42/', branch42.new_year_jan_print_ob_ch42, name='new_year_jan_print_ob_ch42'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch42/', branch42.jan_close_ob_ch42, name='jan_close_ob_ch42'),
    path('jan_close_decision_page_ob_ch42/', branch42.jan_close_decision_page_ob_ch42, name='jan_close_decision_page_ob_ch42'),
    path('feb_close/', branch42.feb_close_ob_ch42, name='feb_close_ob_ch42'),
    path('feb_close_decision_page_ob_ch42/', branch42.feb_close_decision_page_ob_ch42, name='feb_close_decision_page_ob_ch42'),
    path('mar_close_ob_ch42/', branch42.mar_close_ob_ch42, name='mar_close_ob_ch42'),
    path('mar_close_decision_page/', branch42.mar_close_decision_page_ob_ch42, name='mar_close_decision_page_ob_ch42'),
    path('apr_close_ob_ch42/', branch42.apr_close_ob_ch42, name='apr_close_ob_ch42'),
    path('apr_close_decision_page_ob_ch42/', branch42.apr_close_decision_page_ob_ch42, name='apr_close_decision_page_ob_ch42'),

    path('may_close_ob_ch42/', branch42.may_close_ob_ch42, name='may_close_ob_ch42'),
    path('may_close_decision_page_ob_ch42/', branch42.may_close_decision_page_ob_ch42, name='may_close_decision_page_ob_ch42'),
    path('jun_close_ob_ch42/', branch42.jun_close_ob_ch42, name='jun_close_ob_ch42'),
    path('jun_close_decision_page_ob_ch42/', branch42.jun_close_decision_page_ob_ch42, name='jun_close_decision_page_ob_ch42'),
    path('jul_close_ob_ch42/', branch42.jul_close_ob_ch42, name='jul_close_ob_ch42'),
    path('jul_close_decision_page_ob_ch42/', branch42.jul_close_decision_page_ob_ch42, name='jul_close_decision_page_ob_ch42'),
    path('aug_close_ob_ch42/', branch42.aug_close_ob_ch42, name='aug_close_ob_ch42'),
    path('aug_close_decision_page_ob_ch42/', branch42.aug_close_decision_page_ob_ch42, name='aug_close_decision_page_ob_ch42'),

    path('sep_close_ob_ch42/', branch42.sep_close_ob_ch42, name='sep_close_ob_ch42'),
    path('sep_close_decision_page_ob_ch42/', branch42.sep_close_decision_page_ob_ch42, name='sep_close_decision_page_ob_ch42'),
    path('oct_close_ob_ch42/', branch42.oct_close_ob_ch42, name='oct_close_ob_ch42'),
    path('oct_close_decision_page_ob_ch42/', branch42.oct_close_decision_page_ob_ch42, name='oct_close_decision_page_ob_ch42'),
    path('nov_close_ob_ch42/', branch42.nov_close_ob_ch42, name='nov_close_ob_ch42'),
    path('nov_close_decision_page_ob_ch42/', branch42.nov_close_decision_page_ob_ch42, name='nov_close_decision_page_ob_ch42'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch42/',reports42.detailed_report_choose_months_ob_ch42,name='detailed_report_choose_months_ob_ch42'),

    path('jan_details_live_ob_ch42/', reports42.jan_details_live_ob_ch42, name='jan_details_live_ob_ch42'),
    path('jan_print_live_ob_ch42/', reports42.jan_print_live_ob_ch42, name='jan_print_live_ob_ch42'),
    path('feb_details_live_ob_ch42/', reports42.feb_details_live_ob_ch42, name='feb_details_live_ob_ch42'),
    path('feb_print_live_ob_ch42/', reports42.feb_print_live_ob_ch42, name='feb_print_live_ob_ch42'),
    path('march_details_live_ob_ch42/', reports42.march_details_live_ob_ch42, name='march_details_live_ob_ch42'),
    path('march_print_live_ob_ch42/', reports42.march_print_live_ob_ch42, name='march_print_live_ob_ch42'),

    path('april_details_live_ob_ch42/', reports42.april_details_live_ob_ch42, name='april_details_live_ob_ch42'),
    path('april_print_live_ob_ch42/', reports42.april_print_live_ob_ch42, name='april_print_live_ob_ch42'),
    path('may_details_live_ob_ch42/', reports42.may_details_live_ob_ch42, name='may_details_live_ob_ch42'),
    path('may_print_live_ob_ch42/', reports42.may_print_live_ob_ch42, name='may_print_live_ob_ch42'),
    path('june_details_live_ob_ch42/',reports42.june_details_live_ob_ch42,name='june_details_live_ob_ch42'),
    path('june_print_live_ob_ch42/', reports42.june_print_live_ob_ch42, name='june_print_live_ob_ch42'),

    path('july_details_live_ob_ch42/', reports42.july_details_live_ob_ch42, name='july_details_live_ob_ch42'),
    path('july_print_live_ob_ch42/', reports42.july_print_live_ob_ch42, name='july_print_live_ob_ch42'),
    path('auguest_details_live_ob_ch42/', reports42.auguest_details_live_ob_ch42, name='auguest_details_live_ob_ch42'),
    path('auguest_print_live_ob_ch42/', reports42.auguest_print_live_ob_ch42, name='auguest_print_live_ob_ch42'),
    path('sept_details_live_ob_ch42/', reports42.sept_details_live_ob_ch42, name='sept_details_live_ob_ch42'),
    path('sept_print_live_ob_ch42/', reports42.sept_print_live_ob_ch42, name='sept_print_live_ob_ch42'),

    path('october_details_live_ob_ch42/', reports42.october_details_live_ob_ch42, name='october_details_live_ob_ch42'),
    path('october_print_live_ob_ch42/', reports42.october_print_live_ob_ch42, name='october_print_live_ob_ch42'),
    path('nov_details_live_ob_ch42/', reports42.nov_details_live_ob_ch42, name='nov_details_live_ob_ch42'),
    path('nov_print_live_ob_ch42/', reports42.nov_print_live_ob_ch42, name='nov_print_live_ob_ch42'),
    path('dec_details_live_ob_ch42/', reports42.dec_details_live_ob_ch42, name='dec_details_live_ob_ch42'),
    path('dec_print_live_ob_ch42/', reports42.dec_print_live_ob_ch42, name='dec_print_live_ob_ch42'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch42/', reports42.viewall_vaccant_room_ob_ch42, name='viewall_vaccant_room_ob_ch42'),

    path('d_ob_ch42/', branch42.dynamic, name='dynamic'),

    path('manage_bed_ob_ch42/', branch42.manage_bed_ob_ch42, name='manage_bed_ob_ch42'),
    path('manage_new_guest_ob_ch42/', branch42.manage_new_guest_ob_ch42, name='manage_new_guest_ob_ch42'),
    path('manage_update_new_guest_ob_ch42/<id>', branch42.manage_update_new_guest_ob_ch42, name='manage_update_new_guest_ob_ch42'),
    path('manage_update_beds_ob_ch42/<id>', branch42.manage_update_beds_ob_ch42, name='manage_update_beds_ob_ch42'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch42/', branch42.view_all_due_amt_ob_ch42, name='view_all_due_amt_ob_ch42'),
    path('due_amt_mgt_choose_months_ob_ch42/', branch42.due_amt_mgt_choose_months_ob_ch42, name='due_amt_mgt_choose_months_ob_ch42'),

    path('view_jan_account_details_ob_ch42/', branch42.view_jan_account_details_ob_ch42, name='view_jan_account_details_ob_ch42'),
    path('jan_account_mgt_ob_ch42/<id>',branch42.jan_account_mgt_ob_ch42,name='jan_account_mgt_ob_ch42'),
    path('view_feb_account_details_ob_ch42/', branch42.view_feb_account_details_ob_ch42, name='view_feb_account_details_ob_ch42'),
    path('feb_account_mgt_ob_ch42/<id>',branch42.feb_account_mgt_ob_ch42,name='feb_account_mgt_ob_ch42'),
    path('view_march_account_details_ob_ch42/', branch42.view_march_account_details_ob_ch42, name='view_march_account_details_ob_ch42'),
    path('march_account_mgt_ob_ch42/<id>',branch42.march_account_mgt_ob_ch42,name='march_account_mgt_ob_ch42'),
    path('view_april_account_details_ob_ch42/', branch42.view_april_account_details_ob_ch42, name='view_april_account_details_ob_ch42'),
    path('april_account_mgt_ob_ch42/<id>',branch42.april_account_mgt_ob_ch42,name='april_account_mgt_ob_ch42'),

    path('view_may_account_details_ob_ch42/',branch42.view_may_account_details_ob_ch42,name='view_may_account_details_ob_ch42'),
    path('may_account_mgt_ob_ch42/<id>', branch42.may_account_mgt_ob_ch42, name='may_account_mgt_ob_ch42'),
    path('view_june_account_details_ob_ch42/', branch42.view_june_account_details_ob_ch42, name='view_june_account_details_ob_ch42'),
    path('june_account_mgt_ob_ch42/<id>',branch42.june_account_mgt_ob_ch42,name='june_account_mgt_ob_ch42'),
    path('view_july_account_details_ob_ch42/', branch42.view_july_account_details_ob_ch42, name='view_july_account_details_ob_ch42'),
    path('july_account_mgt_ob_ch42/<id>',branch42.july_account_mgt_ob_ch42,name='july_account_mgt_ob_ch42'),
    path('view_auguest_account_details_ob_ch42/', branch42.view_auguest_account_details_ob_ch42, name='view_auguest_account_details_ob_ch42'),
    path('auguest_account_mgt_ob_ch42/<id>',branch42.auguest_account_mgt_ob_ch42,name='auguest_account_mgt_ob_ch42'),

    path('view_sept_account_details_ob_ch42/', branch42.view_sept_account_details_ob_ch42, name='view_sept_account_details_ob_ch42'),
    path('sept_account_mgt_ob_ch42/<id>',branch42.sept_account_mgt_ob_ch42,name='sept_account_mgt_ob_ch42'),
    path('view_october_account_details_ob_ch42/', branch42.view_october_account_details_ob_ch42, name='view_october_account_details_ob_ch42'),
    path('october_account_mgt_ob_ch42/<id>',branch42.october_account_mgt_ob_ch42,name='october_account_mgt_ob_ch42'),
    path('view_nov_account_details_ob_ch42/', branch42.view_nov_account_details_ob_ch42, name='view_nov_account_details_ob_ch42'),
    path('nov_account_mgt_ob_ch42/<id>',branch42.nov_account_mgt_ob_ch42,name='nov_account_mgt_ob_ch42'),
    path('view_dec_account_details_ob_ch42/', branch42.view_dec_account_details_ob_ch42, name='view_dec_account_details_ob_ch42'),
    path('dec_account_mgt_ob_ch42/<id>',branch42.dec_account_mgt_ob_ch42,name='dec_account_mgt_ob_ch42'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch42', admin_dashboard_calculations_br42.monthly_details_due_ob_ch42, name='monthly_details_due_ob_ch42'),
    path('monthly_collection_details_ob_ch42/', admin_dashboard_calculations_br42.monthly_collection_details_ob_ch42, name='monthly_collection_details_ob_ch42'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch42/',branch42.guest_all_ob_ch42,name='guest_all_ob_ch42'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category42/', accounts42.view_all_category42, name='view_all_category42'),
    path('create_new_category42/', accounts42.create_new_category42, name='create_new_category42'),
    path('regi_new_category42/', accounts42.regi_new_category42, name='regi_new_category42'),
    path('update_category42/<id>',accounts42.update_category42,name='update_category42'),

    path('delete_category42/<id>', accounts42.delete_category42, name='delete_category42'),
    path('view_all_category_delete42/', accounts42.view_all_category_delete42, name='view_all_category_delete42'),

    path('regi_multiple_new_category42/', accounts42.regi_multiple_new_category42, name='regi_multiple_new_category42'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items42/', accounts42.view_all_items42, name='view_all_items42'),
    path('create_new_item42/', accounts42.create_new_item42, name='create_new_item42'),
    path('regi_new_item42/', accounts42.regi_new_item42, name='regi_new_item42'),
    path('delete_item42/<id>',accounts42.delete_item42,name='delete_item42'),
    path('update_item42/<id>', accounts42.update_item42, name='update_item42'),
    path('view_all_items_delete42/',accounts42.view_all_items_delete42,name='view_all_items_delete42'),

    path('regi_multiple_new_item42/', accounts42.regi_multiple_new_item42, name='regi_multiple_new_item42'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger42/', accounts42.view_all_ledger42, name='view_all_ledger42'),
    path('create_new_ledger42/', accounts42.create_new_ledger42, name='create_new_ledger42'),
    path('regi_new_ledger42/', accounts42.regi_new_ledger42, name='regi_new_ledger42'),
    path('delete_ledger42/<id>',accounts42.delete_ledger42,name='delete_ledger42'),
    path('update_ledger42/<id>',accounts42.update_ledger42,name='update_ledger42'),
    path('view_all_ledger_delete42/',accounts42.view_all_ledger_delete42,name='view_all_ledger_delete42'),

    path('regi_multiple_new_ledger42/', accounts42.regi_multiple_new_ledger42, name='regi_multiple_new_ledger42'),

    ##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book42/', accounts42.view_all_accounts_book42, name='view_all_accounts_book42'),
    path('create_new_accounts_book42/', accounts42.create_new_accounts_book42, name='create_new_accounts_book42'),
    path('regi_new_accounts_book42/', accounts42.regi_new_accounts_book42, name='regi_new_accounts_book42'),
    path('update_accounts_book42/<id>',accounts42.update_accounts_book42,name='update_accounts_book42'),
    path('delete_accounts_book42/<id>',accounts42.delete_accounts_book42,name='delete_accounts_book42'),
    path('view_all_accounts_book_delete42/',accounts42.view_all_accounts_book_delete42,name='view_all_accounts_book_delete42'),

    path('regi_multiple_new_accounts_book42/', accounts42.regi_multiple_new_accounts_book42,name='regi_multiple_new_accounts_book42'),

    ##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries42/', accounts42.get_countries42, name='get_countries42'),

    path('in_exp_items_entry42/', accounts42.in_exp_items_entry42, name='in_exp_items_entry42'),
    path('reg_in_exp_items_entry42/', accounts42.reg_in_exp_items_entry42, name='reg_in_exp_items_entry42'),
    path('delete_journal42/<id>',accounts42.delete_journal42,name='delete_journal42'),
    path('update_in_exp_items_entry42/<id>',accounts42.update_in_exp_items_entry42,name='update_in_exp_items_entry42'),
    path('detailed_journal_report42/',accounts42.detailed_journal_report42,name='detailed_journal_report42'),
    path('journal_report_deleted42/',accounts42.journal_report_deleted42,name='journal_report_deleted42'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise42/', accounts42.daily_category_wise42, name='daily_category_wise42'),
    path('monthly_category_based_reports42/',accounts42.monthly_category_based_reports42,name='monthly_category_based_reports42'),
    path('yearly_category_based_reports42/', accounts42.yearly_category_based_reports42,name='yearly_category_based_reports42'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed42/', accounts42.daily_detailed42, name='daily_detailed42'),
    path('monthly_detailed42/',accounts42.monthly_detailed42,name='monthly_detailed42'),
    path('yearly_detailed42/',accounts42.yearly_detailed42,name='yearly_detailed42'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports42/', accounts42.item_based_reports42, name='item_based_reports42'),
    path('daily_item_based_reports42/',accounts42.daily_item_based_reports42,name='daily_item_based_reports42'),
    path('monthly_item_based_reports42/',accounts42.monthly_item_based_reports42,name='monthly_item_based_reports42'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports42/', accounts42.ledger_based_reports42, name='ledger_based_reports42'),
    path('monthly_ledger_based_reports42/', accounts42.monthly_ledger_based_reports42, name='monthly_ledger_based_reports42'),
    path('daily_ledger_based_reports42/',accounts42.daily_ledger_based_reports42,name='daily_ledger_based_reports42'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports42/', accounts42.accounts_book_based_reports42, name='accounts_book_based_reports42'),
    path('daily_accounts_book_based_reports42/',accounts42.daily_accounts_book_based_reports42,name='daily_accounts_book_based_reports42'),
    path('monthly_accounts_book_based_reports42/',accounts42.monthly_accounts_book_based_reports42,name='monthly_accounts_book_based_reports42'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months42/', accounts42.monthly_reports_choose_months42, name='monthly_reports_choose_months42'),
    path('monthly_detailed_daily_in_exp_items_report42/<mo>',accounts42.monthly_detailed_daily_in_exp_items_report42,name='monthly_detailed_daily_in_exp_items_report42'),

    path('single_monthly_reports_choose_months42/', accounts42.single_monthly_reports_choose_months42,name='single_monthly_reports_choose_months42'),
    path('single_monthly_daily_in_exp_items_report42/<mo>',accounts42.single_monthly_daily_in_exp_items_report42,name='single_monthly_daily_in_exp_items_report42'),

    path('accounts_dash_board_ob_ch42/',accounts42.accounts_dash_board_ob_ch42,name='accounts_dash_board_ob_ch42'),
    path('accounts_dash_board42/',accounts42.accounts_dash_board42,name='accounts_dash_board42'),

    path('profit_sharing_choose_months42', accounts42.profit_sharing_choose_months42,name='profit_sharing_choose_months42'),
    path('profit_sharing42/<mo>', accounts42.profit_sharing42, name='profit_sharing42'),
    path('view_share_holders42', accounts42.view_share_holders42, name='view_share_holders42'),
    path('create_share_holders42', accounts42.create_share_holders42, name='create_share_holders42'),
    path('regi_share_holders42', accounts42.regi_share_holders42, name='regi_share_holders42'),
    path('update_share_holders42/<id>', accounts42.update_share_holders42, name='update_share_holders42'),
    path('delete_share_holders42/<id>', accounts42.delete_share_holders42, name='delete_share_holders42'),
    path('view_deleted_share_holders42', accounts42.view_deleted_share_holders42, name='view_deleted_share_holders42'),

    path('regi_multiple_share_holders42', accounts42.regi_multiple_share_holders42, name='regi_multiple_share_holders42'),

    #############BRANCH SETTINGS START HERE ########################

    path('guest_rent_update_ob_ch42/', branch_settings42.guest_rent_update_ob_ch42, name='guest_rent_update_ob_ch42'),

    ############BRANCH SETTINGS END HERE ############################

]

