from django.urls import path, include

from . import admin_branch26
from . import admin_branch26
from . import branch26
from . import reports26
from . import payment26
from . import admin_dashboard_calculations_br26
from . import accounts26
from . import branch_settings26

urlpatterns = [

    path('branch1_dashboard_ob_ch26/', branch26.branch1_dashboard_ob_ch26, name='branch1_dashboard_ob_ch26'),
    path('branch1_dashboard26/',branch26.branch1_dashboard26,name='branch1_dashboard26'),
    path('user_dashboard_calculations_ob_ch26/',branch26.user_dashboard_calculations_ob_ch26,name='user_dashboard_calculations_ob_ch26'),

    path('background_ob_ch26',branch26.background_ob_ch26,name='background_ob_ch26'),
    path('background_regi_ob_ch26',branch26.background_regi_ob_ch26,name='background_regi_ob_ch26'),
    path('custom_background_regi_ob_ch26',branch26.custom_background_regi_ob_ch26,name='custom_background_regi_ob_ch26'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch26/',admin_branch26.branch1_room_create_regi_ob_ch26,name='branch1_room_create_regi_ob_ch26'),
    path('view_all_room_ob_ch26/',admin_branch26.view_all_room_ob_ch26,name='view_all_room_ob_ch26'),
    path('delete_room_ob_ch26/<id>',admin_branch26.delete_room_ob_ch26,name='delete_room_ob_ch26'),

    path('branch1_room_create_ob_ch26/',admin_branch26.branch1_room_create_ob_ch26,name='branch1_room_create_ob_ch26'),

    path('multiple_branch1_room_create_regi26/',admin_branch26.multiple_branch1_room_create_regi26,name='multiple_branch1_room_create_regi26'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch26/', admin_branch26.pg1_bed_create_regi_ob_ch26, name='pg1_bed_create_regi_ob_ch26'),
    path('pg1_view_all_beds_ob_ch26/', admin_branch26.pg1_view_all_beds_ob_ch26, name='pg1_view_all_beds_ob_ch26'),
    path('delete_bed_ob_ch26/<id>', admin_branch26.delete_bed_ob_ch26, name='delete_bed_ob_ch26'),

    path('pg1_bed_create_ob_ch26/', admin_branch26.pg1_bed_create_ob_ch26, name='pg1_bed_create_ob_ch26'),

    path('single_pg1_bed_create_regi_ob_ch26/',admin_branch26.single_pg1_bed_create_regi_ob_ch26,name='single_pg1_bed_create_regi_ob_ch26'),
    path('update_bed_basic_details_ob_ch26/<id>',admin_branch26.update_bed_basic_details_ob_ch26, name='update_bed_basic_details_ob_ch26'),

    path('multiple_single_pg1_bed_create_regi26/',admin_branch26.multiple_single_pg1_bed_create_regi26,name='multiple_single_pg1_bed_create_regi26'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch26/<id>',branch26.br1_admit_guest_ob_ch26,name='br1_admit_guest_ob_ch26'),
    path('view_all_new_guest_ob_ch26/',branch26.view_all_new_guest_ob_ch26,name='view_all_new_guest_ob_ch26'),
    path('update_br1_admit_guest_ob_ch26/<id>',branch26.update_br1_admit_guest_ob_ch26,name='update_br1_admit_guest_ob_ch26'),
    path('vacate_br1_guest_ob_ch26/<id>',branch26.vacate_br1_guest_ob_ch26,name='vacate_br1_guest_ob_ch26'),

    path('active_guest_details_ob_ch26/<guest_code>',branch26.active_guest_details_ob_ch26,name='active_guest_details_ob_ch26'),
    path('view_all_guest_ob_ch26/',branch26.view_all_guest_ob_ch26,name='view_all_guest_ob_ch26'),
    path('shift_guest_ob_ch26/<id>',branch26.shift_guest_ob_ch26,name='shift_guest_ob_ch26'),
    path('shift_guest_regi_ob_ch26/',branch26.shift_guest_regi_ob_ch26,name='shift_guest_regi_ob_ch26'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch26/',branch26.update_all_rent_ob_ch26,name='update_all_rent_ob_ch26'),

    path('multiple_br1_admit_guest26/<id>',branch26.multiple_br1_admit_guest26,name='multiple_br1_admit_guest26'),

#guest end here


##################################
#_ADVANCE_ob_ch26 START HERE
################################


    path('choose_months_advance_ob_ch26/',branch26.choose_months_advance_ob_ch26,name='choose_months_advance_ob_ch26'),

    path('jan_advance_ob_ch26/', branch26.jan_advance_ob_ch26, name='jan_advance_ob_ch26'),
    path('jan_make_payments_advance_ob_ch26/<id>', branch26.jan_make_payments_advance_ob_ch26,name='jan_make_payments_advance_ob_ch26'),
    path('feb_advance_ob_ch26/', branch26.feb_advance_ob_ch26, name='feb_advance_ob_ch26'),
    path('feb_make_payments_advance_ob_ch26/<id>', branch26.feb_make_payments_advance_ob_ch26,name='feb_make_payments_advance_ob_ch26'),
    path('march_advance_ob_ch26/', branch26.march_advance_ob_ch26, name='march_advance_ob_ch26'),
    path('march_make_payments_advance_ob_ch26/<id>', branch26.march_make_payments_advance_ob_ch26,name='march_make_payments_advance_ob_ch26'),
    path('april_advance_ob_ch26/', branch26.april_advance_ob_ch26, name='april_advance_ob_ch26'),
    path('april_make_payments_advance_ob_ch26/<id>', branch26.april_make_payments_advance_ob_ch26, name='april_make_payments_advance_ob_ch26'),

    path('may_advance_ob_ch26/',branch26.may_advance_ob_ch26,name='may_advance_ob_ch26'),
    path('may_make_payments_advance_ob_ch26/<id>', branch26.may_make_payments_advance_ob_ch26, name='may_make_payments_advance_ob_ch26'),
    path('june_advance_ob_ch26/',branch26.june_advance_ob_ch26,name='june_advance_ob_ch26'),
    path('june_make_payments_advance_ob_ch26/<id>', branch26.june_make_payments_advance_ob_ch26, name='june_make_payments_advance_ob_ch26'),
    path('july_advance_ob_ch26/',branch26.july_advance_ob_ch26,name='july_advance_ob_ch26'),
    path('july_make_payments_advance_ob_ch26/<id>', branch26.july_make_payments_advance_ob_ch26, name='july_make_payments_advance_ob_ch26'),
    path('auguest_advance_ob_ch26/', branch26.auguest_advance_ob_ch26, name='auguest_advance_ob_ch26'),
    path('auguest_make_payments_advance_ob_ch26/<id>', branch26.auguest_make_payments_advance_ob_ch26, name='auguest_make_payments_advance_ob_ch26'),

    path('sept_advance_ob_ch26/', branch26.sept_advance_ob_ch26, name='sept_advance_ob_ch26'),
    path('sept_make_payments_advance_ob_ch26/<id>', branch26.sept_make_payments_advance_ob_ch26,name='sept_make_payments_advance_ob_ch26'),
    path('october_advance_ob_ch26/', branch26.october_advance_ob_ch26, name='october_advance_ob_ch26'),
    path('october_make_payments_advance_ob_ch26/<id>', branch26.october_make_payments_advance_ob_ch26, name='october_make_payments_advance_ob_ch26'),
    path('nov_advance_ob_ch26/', branch26.nov_advance_ob_ch26, name='nov_advance_ob_ch26'),
    path('nov_make_payments_advance_ob_ch26/<id>', branch26.nov_make_payments_advance_ob_ch26,name='nov_make_payments_advance_ob_ch26'),
    path('dec_advance_ob_ch26/', branch26.dec_advance_ob_ch26, name='dec_advance_ob_ch26'),
    path('dec_make_payments_advance_ob_ch26/<id>', branch26.dec_make_payments_advance_ob_ch26, name='dec_make_payments_advance_ob_ch26'),



##################################
#_ADVANCE_ob_ch26 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch26/',branch26.choose_months_ob_ch26,name='choose_months_ob_ch26'),

    path('jan_ob_ch26/',branch26.jan_ob_ch26,name='jan_ob_ch26'),
    path('jan_manke_payments_ob_ch26/<id>',branch26.jan_manke_payments_ob_ch26,name='jan_manke_payments_ob_ch26'),

    path('feb_ob_ch26/',branch26.feb_ob_ch26,name='feb_ob_ch26'),
    path('feb_manke_payments_ob_ch26/<id>',branch26.feb_manke_payments_ob_ch26,name='feb_manke_payments_ob_ch26'),

    path('march_ob_ch26/',branch26.march_ob_ch26,name='march_ob_ch26'),
    path('march_manke_payments_ob_ch26/<id>',branch26.march_manke_payments_ob_ch26,name='march_manke_payments_ob_ch26'),

    path('april_ob_ch26/',branch26.april_ob_ch26,name='april_ob_ch26'),
    path('april_make_payments_ob_ch26/<id>',branch26.april_make_payments_ob_ch26,name='april_make_payments_ob_ch26'),

    path('may_ob_ch26/',branch26.may_ob_ch26,name='may_ob_ch26'),
    path('may_make_payments_ob_ch26/<id>',branch26.may_make_payments_ob_ch26,name='may_make_payments_ob_ch26'),

    path('june_ob_ch26/',branch26.june_ob_ch26,name='june_ob_ch26'),
    path('june_make_payments_ob_ch26/<id>',branch26.june_make_payments_ob_ch26,name='june_make_payments_ob_ch26'),

    path('july_ob_ch26/',branch26.july_ob_ch26,name='july_ob_ch26'),
    path('july_make_payments_ob_ch26/<id>',branch26.july_make_payments_ob_ch26,name='july_make_payments_ob_ch26'),

    path('aug_ob_ch26/',branch26.aug_ob_ch26,name='aug_ob_ch26'),
    path('aug_make_payments_ob_ch26/<id>',branch26.aug_make_payments_ob_ch26,name='aug_make_payments_ob_ch26'),

    path('sept_ob_ch26/',branch26.sept_ob_ch26,name='sept_ob_ch26'),
    path('sept_make_payments_ob_ch26/<id>',branch26.sept_make_payments_ob_ch26,name='sept_make_payments_ob_ch26'),

    path('oct_ob_ch26/',branch26.oct_ob_ch26,name='oct_ob_ch26'),
    path('oct_make_payments_ob_ch26/<id>',branch26.oct_make_payments_ob_ch26,name='oct_make_payments_ob_ch26'),

    path('nov_ob_ch26/',branch26.nov_ob_ch26,name='nov_ob_ch26'),
    path('nov_make_payments_ob_ch26/<id>',branch26.nov_make_payments_ob_ch26,name='nov_make_payments_ob_ch26'),

    path('dec_ob_ch26/',branch26.dec_ob_ch26,name='dec_ob_ch26'),
    path('dec_make_payments_ob_ch26/<id>',branch26.dec_make_payments_ob_ch26,name='dec_make_payments_ob_ch26'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch26/', payment26.choose_user_ob_ch26, name='choose_user_ob_ch26'),
    path('payment_user_details_ob_ch26/<id>', payment26.payment_user_details_ob_ch26, name='payment_user_details_ob_ch26'),
    path('close_choose_user_ob_ch26/<id>',payment26.close_choose_user_ob_ch26,name='close_choose_user_ob_ch26'),

    path('monthly_jan_make_payments_ob_ch26/<id>', payment26.monthly_jan_make_payments_ob_ch26, name='monthly_jan_make_payments_ob_ch26'),
    path('monthly_feb_make_payments_ob_ch26/<id>', payment26.monthly_feb_make_payments_ob_ch26, name='monthly_feb_make_payments_ob_ch26'),
    path('monthly_march_make_payments_ob_ch26/<id>', payment26.monthly_march_make_payments_ob_ch26, name='monthly_march_make_payments_ob_ch26'),
    path('monthly_april_make_payments_ob_ch26/<id>', payment26.monthly_april_make_payments_ob_ch26, name='monthly_april_make_payments_ob_ch26'),
    path('monthly_may_make_payments_ob_ch26/<id>', payment26.monthly_may_make_payments_ob_ch26, name='monthly_may_make_payments_ob_ch26'),
    path('monthly_june_make_payments_ob_ch26/<id>', payment26.monthly_june_make_payments_ob_ch26, name='monthly_june_make_payments_ob_ch26'),

    path('monthly_july_make_payments_ob_ch26/<id>', payment26.monthly_july_make_payments_ob_ch26, name='monthly_july_make_payments_ob_ch26'),
    path('monthly_aug_make_payments_ob_ch26/<id>', payment26.monthly_aug_make_payments_ob_ch26, name='monthly_aug_make_payments_ob_ch26'),
    path('monthly_sept_make_payments_ob_ch26/<id>', payment26.monthly_sept_make_payments_ob_ch26, name='monthly_sept_make_payments_ob_ch26'),
    path('monthly_oct_make_payments_ob_ch26/<id>', payment26.monthly_oct_make_payments_ob_ch26, name='monthly_oct_make_payments_ob_ch26'),
    path('monthly_nov_make_payments_ob_ch26/<id>', payment26.monthly_nov_make_payments_ob_ch26, name='monthly_nov_make_payments_ob_ch26'),
    path('monthly_dec_make_payments_ob_ch26/<id>', payment26.monthly_dec_make_payments_ob_ch26, name='monthly_dec_make_payments_ob_ch26'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch26/',branch26.unpaid_rent_choose_months_ob_ch26,name='unpaid_rent_choose_months_ob_ch26'),

    path('jan_unpaid_rent_ob_ch26/', branch26.jan_unpaid_rent_ob_ch26, name='jan_unpaid_rent_ob_ch26'),
    path('table_jan_unpaid_rent_ob_ch26/', branch26.table_jan_unpaid_rent_ob_ch26, name='table_jan_unpaid_rent_ob_ch26'),
    path('feb_unpaid_rent_ob_ch26/', branch26.feb_unpaid_rent_ob_ch26, name='feb_unpaid_rent_ob_ch26'),
    path('table_feb_unpaid_rent_ob_ch26/', branch26.table_feb_unpaid_rent_ob_ch26, name='table_feb_unpaid_rent_ob_ch26'),
    path('mar_unpaid_rent_ob_ch26/', branch26.mar_unpaid_rent_ob_ch26, name='mar_unpaid_rent_ob_ch26'),
    path('table_mar_unpaid_rent_ob_ch26/', branch26.table_mar_unpaid_rent_ob_ch26, name='table_mar_unpaid_rent_ob_ch26'),
    path('april_unpaid_rent_ob_ch26/', branch26.april_unpaid_rent_ob_ch26, name='april_unpaid_rent_ob_ch26'),
    path('table_april_unpaid_rent_ob_ch26/', branch26.table_april_unpaid_rent_ob_ch26, name='table_april_unpaid_rent_ob_ch26'),

    path('may_unpaid_rent_ob_ch26/', branch26.may_unpaid_rent_ob_ch26, name='may_unpaid_rent_ob_ch26'),
    path('table_may_unpaid_rent_ob_ch26/', branch26.table_may_unpaid_rent_ob_ch26, name='table_may_unpaid_rent_ob_ch26'),
    path('june_unpaid_rent_ob_ch26/', branch26.june_unpaid_rent_ob_ch26, name='june_unpaid_rent_ob_ch26'),
    path('table_june_unpaid_rent_ob_ch26/', branch26.table_june_unpaid_rent_ob_ch26, name='table_june_unpaid_rent_ob_ch26'),
    path('july_unpaid_rent_ob_ch26/', branch26.july_unpaid_rent_ob_ch26, name='july_unpaid_rent_ob_ch26'),
    path('table_july_unpaid_rent_ob_ch26',branch26.table_july_unpaid_rent_ob_ch26,name='table_july_unpaid_rent_ob_ch26'),
    path('aug_unpaid_rent_ob_ch26/', branch26.aug_unpaid_rent_ob_ch26, name='aug_unpaid_rent_ob_ch26'),
    path('table_aug_unpaid_rent_ob_ch26/',branch26.table_aug_unpaid_rent_ob_ch26,name='table_aug_unpaid_rent_ob_ch26'),

    path('sept_unpaid_rent_ob_ch26/', branch26.sept_unpaid_rent_ob_ch26, name='sept_unpaid_rent_ob_ch26'),
    path('table_sept_unpaid_rent_ob_ch26/', branch26.table_sept_unpaid_rent_ob_ch26, name='table_sept_unpaid_rent_ob_ch26'),
    path('oct_unpaid_rent_ob_ch26/', branch26.oct_unpaid_rent_ob_ch26, name='oct_unpaid_rent_ob_ch26'),
    path('table_oct_unpaid_rent_ob_ch26/', branch26.table_oct_unpaid_rent_ob_ch26, name='table_oct_unpaid_rent_ob_ch26'),
    path('nov_unpaid_rent_ob_ch26/', branch26.nov_unpaid_rent_ob_ch26, name='nov_unpaid_rent_ob_ch26'),
    path('table_nov_unpaid_rent_ob_ch26/', branch26.table_nov_unpaid_rent_ob_ch26, name='table_nov_unpaid_rent_ob_ch26'),
    path('dec_unpaid_rent_ob_ch26/', branch26.dec_unpaid_rent_ob_ch26, name='dec_unpaid_rent_ob_ch26'),
    path('table_dec_unpaid_rent_ob_ch26/', branch26.table_dec_unpaid_rent_ob_ch26, name='table_dec_unpaid_rent_ob_ch26'),

    path('details_of_unpaid_guests_ob_ch26/<id>',branch26.details_of_unpaid_guests_ob_ch26,name='details_of_unpaid_guests_ob_ch26'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch26/',branch26.paid_rent_choose_months_ob_ch26,name='paid_rent_choose_months_ob_ch26'),
    path('partially_paid_guest_choose_months_ob_ch26/',reports26.partially_paid_guest_choose_months_ob_ch26,name='partially_paid_guest_choose_months_ob_ch26'),

    path('jan_paid_rent_ob_ch26/', branch26.jan_paid_rent_ob_ch26, name='jan_paid_rent_ob_ch26'),
    path('table_jan_paid_rent_ob_ch26/', branch26.table_jan_paid_rent_ob_ch26, name='table_jan_paid_rent_ob_ch26'),
    path('jan_full_paid_guest_ob_ch26/', reports26.jan_full_paid_guest_ob_ch26, name='jan_full_paid_guest_ob_ch26'),
    path('jan_partially_paid_guest_ob_ch26/', reports26.jan_partially_paid_guest_ob_ch26, name='jan_partially_paid_guest_ob_ch26'),
    path('table_jan_partially_paid_guest_ob_ch26/', reports26.table_jan_partially_paid_guest_ob_ch26,name='table_jan_partially_paid_guest_ob_ch26'),

    path('feb_paid_rent_ob_ch26/', branch26.feb_paid_rent_ob_ch26, name='feb_paid_rent_ob_ch26'),
    path('table_feb_paid_rent_ob_ch26/', branch26.table_feb_paid_rent_ob_ch26, name='table_feb_paid_rent_ob_ch26'),
    path('feb_full_paid_guest_ob_ch26/', reports26.feb_full_paid_guest_ob_ch26, name='feb_full_paid_guest_ob_ch26'),
    path('feb_partially_paid_guest_ob_ch26/', reports26.feb_partially_paid_guest_ob_ch26, name='feb_partially_paid_guest_ob_ch26'),
    path('table_feb_partially_paid_guest_ob_ch26/', reports26.table_feb_partially_paid_guest_ob_ch26,name='table_feb_partially_paid_guest_ob_ch26'),

    path('mar_paid_rent_ob_ch26/', branch26.mar_paid_rent_ob_ch26, name='mar_paid_rent_ob_ch26'),
    path('table_mar_paid_rent_ob_ch26/', branch26.table_mar_paid_rent_ob_ch26, name='table_mar_paid_rent_ob_ch26'),
    path('march_full_paid_guest_ob_ch26/', reports26.march_full_paid_guest_ob_ch26, name='march_full_paid_guest_ob_ch26'),
    path('march_partially_paid_guest_ob_ch26/', reports26.march_partially_paid_guest_ob_ch26, name='march_partially_paid_guest_ob_ch26'),
    path('table_march_partially_paid_guest_ob_ch26/', reports26.table_march_partially_paid_guest_ob_ch26,name='table_march_partially_paid_guest_ob_ch26'),

    path('april_paid_rent_ob_ch26/', branch26.april_paid_rent_ob_ch26, name='april_paid_rent_ob_ch26'),
    path('table_april_paid_rent_ob_ch26/', branch26.table_april_paid_rent_ob_ch26, name='table_april_paid_rent_ob_ch26'),
    path('april_full_paid_guest_ob_ch26/', reports26.april_full_paid_guest_ob_ch26, name='april_full_paid_guest_ob_ch26'),
    path('april_partially_paid_guest_ob_ch26/', reports26.april_partially_paid_guest_ob_ch26, name='april_partially_paid_guest_ob_ch26'),
    path('table_april_partially_paid_guest_ob_ch26/', reports26.table_april_partially_paid_guest_ob_ch26,name='table_april_partially_paid_guest_ob_ch26'),

    path('may_paid_rent_ob_ch26/', branch26.may_paid_rent_ob_ch26, name='may_paid_rent_ob_ch26'),
    path('table_may_paid_rent_ob_ch26/', branch26.table_may_paid_rent_ob_ch26, name='table_may_paid_rent_ob_ch26'),
    path('may_full_paid_guest_ob_ch26/', reports26.may_full_paid_guest_ob_ch26, name='may_full_paid_guest_ob_ch26'),
    path('may_partially_paid_guest_ob_ch26/', reports26.may_partially_paid_guest_ob_ch26, name='may_partially_paid_guest_ob_ch26'),
    path('table_may_partially_paid_guest_ob_ch26/', reports26.table_may_partially_paid_guest_ob_ch26, name='table_may_partially_paid_guest_ob_ch26'),

    path('june_paid_rent_ob_ch26/', branch26.june_paid_rent_ob_ch26, name='june_paid_rent_ob_ch26'),
    path('table_june_paid_rent_ob_ch26/', branch26.table_june_paid_rent_ob_ch26, name='table_june_paid_rent_ob_ch26'),
    path('june_full_paid_guest_ob_ch26/', reports26.june_full_paid_guest_ob_ch26, name='june_full_paid_guest_ob_ch26'),
    path('june_partially_paid_guest_ob_ch26/', reports26.june_partially_paid_guest_ob_ch26, name='june_partially_paid_guest_ob_ch26'),
    path('table_june_partially_paid_guest_ob_ch26/', reports26.table_june_partially_paid_guest_ob_ch26, name='table_june_partially_paid_guest_ob_ch26'),

    path('july_paid_rent_ob_ch26/', branch26.july_paid_rent_ob_ch26, name='july_paid_rent_ob_ch26'),
    path('table_july_paid_rent_ob_ch26/', branch26.table_july_paid_rent_ob_ch26, name='table_july_paid_rent_ob_ch26'),
    path('july_full_paid_guest_ob_ch26/', reports26.july_full_paid_guest_ob_ch26, name='july_full_paid_guest_ob_ch26'),
    path('july_partially_paid_guest_ob_ch26/', reports26.july_partially_paid_guest_ob_ch26, name='july_partially_paid_guest_ob_ch26'),
    path('table_july_partially_paid_guest_ob_ch26/', reports26.table_july_partially_paid_guest_ob_ch26, name='table_july_partially_paid_guest_ob_ch26'),

    path('aug_paid_rent_ob_ch26/', branch26.aug_paid_rent_ob_ch26, name='aug_paid_rent_ob_ch26'),
    path('table_aug_paid_rent_ob_ch26/', branch26.table_aug_paid_rent_ob_ch26, name='table_aug_paid_rent_ob_ch26'),
    path('auguest_full_paid_guest_ob_ch26/', reports26.auguest_full_paid_guest_ob_ch26, name='auguest_full_paid_guest_ob_ch26'),
    path('auguest_partially_paid_guest_ob_ch26/', reports26.auguest_partially_paid_guest_ob_ch26,name='auguest_partially_paid_guest_ob_ch26'),
    path('table_auguest_partially_paid_guest_ob_ch26/', reports26.table_auguest_partially_paid_guest_ob_ch26,name='table_auguest_partially_paid_guest_ob_ch26'),

    path('sept_paid_rent_ob_ch26/', branch26.sept_paid_rent_ob_ch26, name='sept_paid_rent_ob_ch26'),
    path('table_sept_paid_rent_ob_ch26/', branch26.table_sept_paid_rent_ob_ch26, name='table_sept_paid_rent_ob_ch26'),
    path('sept_full_paid_guest_ob_ch26/', reports26.sept_full_paid_guest_ob_ch26, name='sept_full_paid_guest_ob_ch26'),
    path('sept_partially_paid_guest_ob_ch26/', reports26.sept_partially_paid_guest_ob_ch26, name='sept_partially_paid_guest_ob_ch26'),
    path('table_sept_partially_paid_guest_ob_ch26/', reports26.table_sept_partially_paid_guest_ob_ch26,name='table_sept_partially_paid_guest_ob_ch26'),

    path('oct_paid_rent_ob_ch26/', branch26.oct_paid_rent_ob_ch26, name='oct_paid_rent_ob_ch26'),
    path('table_oct_paid_rent_ob_ch26/', branch26.table_oct_paid_rent_ob_ch26, name='table_oct_paid_rent_ob_ch26'),
    path('october_full_paid_guest_ob_ch26/', reports26.october_full_paid_guest_ob_ch26, name='october_full_paid_guest_ob_ch26'),
    path('october_partially_paid_guest_ob_ch26/', reports26.october_partially_paid_guest_ob_ch26,name='october_partially_paid_guest_ob_ch26'),
    path('table_october_partially_paid_guest_ob_ch26/', reports26.table_october_partially_paid_guest_ob_ch26,name='table_october_partially_paid_guest_ob_ch26'),

    path('nov_paid_rent_ob_ch26/', branch26.nov_paid_rent_ob_ch26, name='nov_paid_rent_ob_ch26'),
    path('table_nov_paid_rent_ob_ch26/', branch26.table_nov_paid_rent_ob_ch26, name='table_nov_paid_rent_ob_ch26'),
    path('nov_full_paid_guest_ob_ch26/', reports26.nov_full_paid_guest_ob_ch26, name='nov_full_paid_guest_ob_ch26'),
    path('nov_partially_paid_guest_ob_ch26/', reports26.nov_partially_paid_guest_ob_ch26, name='nov_partially_paid_guest_ob_ch26'),
    path('table_nov_partially_paid_guest_ob_ch26/', reports26.table_nov_partially_paid_guest_ob_ch26,name='table_nov_partially_paid_guest_ob_ch26'),

    path('dec_paid_rent_ob_ch26/', branch26.dec_paid_rent_ob_ch26, name='dec_paid_rent_ob_ch26'),
    path('table_dec_paid_rent_ob_ch26/', branch26.table_dec_paid_rent_ob_ch26, name='table_dec_paid_rent_ob_ch26'),
    path('dec_full_paid_guest_ob_ch26/', reports26.dec_full_paid_guest_ob_ch26, name='dec_full_paid_guest_ob_ch26'),
    path('dec_partially_paid_guest_ob_ch26/', reports26.dec_partially_paid_guest_ob_ch26, name='dec_partially_paid_guest_ob_ch26'),
    path('table_dec_partially_paid_guest_ob_ch26/', reports26.table_dec_partially_paid_guest_ob_ch26,name='table_dec_partially_paid_guest_ob_ch26'),

    path('details_of_paid_guests_ob_ch26/<id>',branch26.details_of_paid_guests_ob_ch26,name='details_of_paid_guests_ob_ch26'),
    path('full_paid_guest_ob_ch26/',reports26.full_paid_guest_ob_ch26,name='full_paid_guest_ob_ch26'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch26/',branch26.viewall_vacate_guest_ob_ch26,name='viewall_vacate_guest_ob_ch26'),
    path('details_of_vacate_guest_ob_ch26/<id>',branch26.details_of_vacate_guest_ob_ch26,name='details_of_vacate_guest_ob_ch26'),
    path('full_vacated_guest_details_ob_ch26',branch26.full_vacated_guest_details_ob_ch26,name='full_vacated_guest_details_ob_ch26'),
    path('full_vacated_guest_table_ob_ch26',branch26.full_vacated_guest_table_ob_ch26,name='full_vacated_guest_table_ob_ch26'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch26/<id>', branch26.jan_manke_payments_vacate_ob_ch26, name='jan_manke_payments_vacate_ob_ch26'),
    path('feb_manke_payments_vacate_ob_ch26/<id>', branch26.feb_manke_payments_vacate_ob_ch26, name='feb_manke_payments_vacate_ob_ch26'),
    path('march_manke_payments_vacate_ob_ch26/<id>', branch26.march_manke_payments_vacate_ob_ch26, name='march_manke_payments_vacate_ob_ch26'),
    path('april_make_payments_vacate_ob_ch26/<id>', branch26.april_make_payments_vacate_ob_ch26, name='april_make_payments_vacate_ob_ch26'),

    path('may_make_payments_vacate_ob_ch26/<id>', branch26.may_make_payments_vacate_ob_ch26, name='may_make_payments_vacate_ob_ch26'),
    path('june_make_payments_vacate_ob_ch26/<id>', branch26.june_make_payments_vacate_ob_ch26, name='june_make_payments_vacate_ob_ch26'),
    path('july_make_payments_vacate_ob_ch26/<id>', branch26.july_make_payments_vacate_ob_ch26, name='july_make_payments_vacate_ob_ch26'),
    path('aug_make_payments_vacate_ob_ch26/<id>', branch26.aug_make_payments_vacate_ob_ch26, name='aug_make_payments_vacate_ob_ch26'),

    path('sept_make_payments_vacate_ob_ch26/<id>', branch26.sept_make_payments_vacate_ob_ch26, name='sept_make_payments_vacate_ob_ch26'),
    path('oct_make_payments_vacate_ob_ch26/<id>', branch26.oct_make_payments_vacate_ob_ch26, name='oct_make_payments_vacate_ob_ch26'),
    path('nov_make_payments_vacate_ob_ch26/<id>', branch26.nov_make_payments_vacate_ob_ch26, name='nov_make_payments_vacate_ob_ch26'),
    path('dec_make_payments_vacate_ob_ch26/<id>', branch26.dec_make_payments_vacate_ob_ch26, name='dec_make_payments_vacate_ob_ch26'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch26/',branch26.detail_guest_general_ob_ch26,name='detail_guest_general_ob_ch26'),

    path('jan_print_ob_ch26/',branch26.jan_print_ob_ch26,name='jan_print_ob_ch26'),
    path('feb_print_ob_ch26/',branch26.feb_print_ob_ch26,name='feb_print_ob_ch26'),
    path('march_print_ob_ch26/',branch26.march_print_ob_ch26,name='march_print_ob_ch26'),
    path('april_print_ob_ch26/',branch26.april_print_ob_ch26,name='april_print_ob_ch26'),

    path('may_print_ob_ch26/',branch26.may_print_ob_ch26,name='may_print_ob_ch26'),
    path('june_print_ob_ch26/',branch26.june_print_ob_ch26,name='june_print_ob_ch26'),
    path('july_print_ob_ch26/', branch26.july_print_ob_ch26, name='july_print_ob_ch26'),
    path('aug_print_ob_ch26/', branch26.aug_print_ob_ch26, name='aug_print_ob_ch26'),

    path('sept_print_ob_ch26/', branch26.sept_print_ob_ch26, name='sept_print_ob_ch26'),
    path('oct_print_ob_ch26/', branch26.oct_print_ob_ch26, name='oct_print_ob_ch26'),
    path('nov_print_ob_ch26/', branch26.nov_print_ob_ch26, name='nov_print_ob_ch26'),
    path('dec_print_ob_ch26/', branch26.dec_print_ob_ch26, name='dec_print_ob_ch26'),

    path('new_year_jan_print_ob_ch26/', branch26.new_year_jan_print_ob_ch26, name='new_year_jan_print_ob_ch26'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch26/', branch26.jan_close_ob_ch26, name='jan_close_ob_ch26'),
    path('jan_close_decision_page_ob_ch26/', branch26.jan_close_decision_page_ob_ch26, name='jan_close_decision_page_ob_ch26'),
    path('feb_close/', branch26.feb_close_ob_ch26, name='feb_close_ob_ch26'),
    path('feb_close_decision_page_ob_ch26/', branch26.feb_close_decision_page_ob_ch26, name='feb_close_decision_page_ob_ch26'),
    path('mar_close_ob_ch26/', branch26.mar_close_ob_ch26, name='mar_close_ob_ch26'),
    path('mar_close_decision_page/', branch26.mar_close_decision_page_ob_ch26, name='mar_close_decision_page_ob_ch26'),
    path('apr_close_ob_ch26/', branch26.apr_close_ob_ch26, name='apr_close_ob_ch26'),
    path('apr_close_decision_page_ob_ch26/', branch26.apr_close_decision_page_ob_ch26, name='apr_close_decision_page_ob_ch26'),

    path('may_close_ob_ch26/', branch26.may_close_ob_ch26, name='may_close_ob_ch26'),
    path('may_close_decision_page_ob_ch26/', branch26.may_close_decision_page_ob_ch26, name='may_close_decision_page_ob_ch26'),
    path('jun_close_ob_ch26/', branch26.jun_close_ob_ch26, name='jun_close_ob_ch26'),
    path('jun_close_decision_page_ob_ch26/', branch26.jun_close_decision_page_ob_ch26, name='jun_close_decision_page_ob_ch26'),
    path('jul_close_ob_ch26/', branch26.jul_close_ob_ch26, name='jul_close_ob_ch26'),
    path('jul_close_decision_page_ob_ch26/', branch26.jul_close_decision_page_ob_ch26, name='jul_close_decision_page_ob_ch26'),
    path('aug_close_ob_ch26/', branch26.aug_close_ob_ch26, name='aug_close_ob_ch26'),
    path('aug_close_decision_page_ob_ch26/', branch26.aug_close_decision_page_ob_ch26, name='aug_close_decision_page_ob_ch26'),

    path('sep_close_ob_ch26/', branch26.sep_close_ob_ch26, name='sep_close_ob_ch26'),
    path('sep_close_decision_page_ob_ch26/', branch26.sep_close_decision_page_ob_ch26, name='sep_close_decision_page_ob_ch26'),
    path('oct_close_ob_ch26/', branch26.oct_close_ob_ch26, name='oct_close_ob_ch26'),
    path('oct_close_decision_page_ob_ch26/', branch26.oct_close_decision_page_ob_ch26, name='oct_close_decision_page_ob_ch26'),
    path('nov_close_ob_ch26/', branch26.nov_close_ob_ch26, name='nov_close_ob_ch26'),
    path('nov_close_decision_page_ob_ch26/', branch26.nov_close_decision_page_ob_ch26, name='nov_close_decision_page_ob_ch26'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch26/',reports26.detailed_report_choose_months_ob_ch26,name='detailed_report_choose_months_ob_ch26'),

    path('jan_details_live_ob_ch26/', reports26.jan_details_live_ob_ch26, name='jan_details_live_ob_ch26'),
    path('jan_print_live_ob_ch26/', reports26.jan_print_live_ob_ch26, name='jan_print_live_ob_ch26'),
    path('feb_details_live_ob_ch26/', reports26.feb_details_live_ob_ch26, name='feb_details_live_ob_ch26'),
    path('feb_print_live_ob_ch26/', reports26.feb_print_live_ob_ch26, name='feb_print_live_ob_ch26'),
    path('march_details_live_ob_ch26/', reports26.march_details_live_ob_ch26, name='march_details_live_ob_ch26'),
    path('march_print_live_ob_ch26/', reports26.march_print_live_ob_ch26, name='march_print_live_ob_ch26'),

    path('april_details_live_ob_ch26/', reports26.april_details_live_ob_ch26, name='april_details_live_ob_ch26'),
    path('april_print_live_ob_ch26/', reports26.april_print_live_ob_ch26, name='april_print_live_ob_ch26'),
    path('may_details_live_ob_ch26/', reports26.may_details_live_ob_ch26, name='may_details_live_ob_ch26'),
    path('may_print_live_ob_ch26/', reports26.may_print_live_ob_ch26, name='may_print_live_ob_ch26'),
    path('june_details_live_ob_ch26/',reports26.june_details_live_ob_ch26,name='june_details_live_ob_ch26'),
    path('june_print_live_ob_ch26/', reports26.june_print_live_ob_ch26, name='june_print_live_ob_ch26'),

    path('july_details_live_ob_ch26/', reports26.july_details_live_ob_ch26, name='july_details_live_ob_ch26'),
    path('july_print_live_ob_ch26/', reports26.july_print_live_ob_ch26, name='july_print_live_ob_ch26'),
    path('auguest_details_live_ob_ch26/', reports26.auguest_details_live_ob_ch26, name='auguest_details_live_ob_ch26'),
    path('auguest_print_live_ob_ch26/', reports26.auguest_print_live_ob_ch26, name='auguest_print_live_ob_ch26'),
    path('sept_details_live_ob_ch26/', reports26.sept_details_live_ob_ch26, name='sept_details_live_ob_ch26'),
    path('sept_print_live_ob_ch26/', reports26.sept_print_live_ob_ch26, name='sept_print_live_ob_ch26'),

    path('october_details_live_ob_ch26/', reports26.october_details_live_ob_ch26, name='october_details_live_ob_ch26'),
    path('october_print_live_ob_ch26/', reports26.october_print_live_ob_ch26, name='october_print_live_ob_ch26'),
    path('nov_details_live_ob_ch26/', reports26.nov_details_live_ob_ch26, name='nov_details_live_ob_ch26'),
    path('nov_print_live_ob_ch26/', reports26.nov_print_live_ob_ch26, name='nov_print_live_ob_ch26'),
    path('dec_details_live_ob_ch26/', reports26.dec_details_live_ob_ch26, name='dec_details_live_ob_ch26'),
    path('dec_print_live_ob_ch26/', reports26.dec_print_live_ob_ch26, name='dec_print_live_ob_ch26'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch26/', reports26.viewall_vaccant_room_ob_ch26, name='viewall_vaccant_room_ob_ch26'),

    path('d_ob_ch26/', branch26.dynamic, name='dynamic'),

    path('manage_bed_ob_ch26/', branch26.manage_bed_ob_ch26, name='manage_bed_ob_ch26'),
    path('manage_new_guest_ob_ch26/', branch26.manage_new_guest_ob_ch26, name='manage_new_guest_ob_ch26'),
    path('manage_update_new_guest_ob_ch26/<id>', branch26.manage_update_new_guest_ob_ch26, name='manage_update_new_guest_ob_ch26'),
    path('manage_update_beds_ob_ch26/<id>', branch26.manage_update_beds_ob_ch26, name='manage_update_beds_ob_ch26'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch26/', branch26.view_all_due_amt_ob_ch26, name='view_all_due_amt_ob_ch26'),
    path('due_amt_mgt_choose_months_ob_ch26/', branch26.due_amt_mgt_choose_months_ob_ch26, name='due_amt_mgt_choose_months_ob_ch26'),

    path('view_jan_account_details_ob_ch26/', branch26.view_jan_account_details_ob_ch26, name='view_jan_account_details_ob_ch26'),
    path('jan_account_mgt_ob_ch26/<id>',branch26.jan_account_mgt_ob_ch26,name='jan_account_mgt_ob_ch26'),
    path('view_feb_account_details_ob_ch26/', branch26.view_feb_account_details_ob_ch26, name='view_feb_account_details_ob_ch26'),
    path('feb_account_mgt_ob_ch26/<id>',branch26.feb_account_mgt_ob_ch26,name='feb_account_mgt_ob_ch26'),
    path('view_march_account_details_ob_ch26/', branch26.view_march_account_details_ob_ch26, name='view_march_account_details_ob_ch26'),
    path('march_account_mgt_ob_ch26/<id>',branch26.march_account_mgt_ob_ch26,name='march_account_mgt_ob_ch26'),
    path('view_april_account_details_ob_ch26/', branch26.view_april_account_details_ob_ch26, name='view_april_account_details_ob_ch26'),
    path('april_account_mgt_ob_ch26/<id>',branch26.april_account_mgt_ob_ch26,name='april_account_mgt_ob_ch26'),

    path('view_may_account_details_ob_ch26/',branch26.view_may_account_details_ob_ch26,name='view_may_account_details_ob_ch26'),
    path('may_account_mgt_ob_ch26/<id>', branch26.may_account_mgt_ob_ch26, name='may_account_mgt_ob_ch26'),
    path('view_june_account_details_ob_ch26/', branch26.view_june_account_details_ob_ch26, name='view_june_account_details_ob_ch26'),
    path('june_account_mgt_ob_ch26/<id>',branch26.june_account_mgt_ob_ch26,name='june_account_mgt_ob_ch26'),
    path('view_july_account_details_ob_ch26/', branch26.view_july_account_details_ob_ch26, name='view_july_account_details_ob_ch26'),
    path('july_account_mgt_ob_ch26/<id>',branch26.july_account_mgt_ob_ch26,name='july_account_mgt_ob_ch26'),
    path('view_auguest_account_details_ob_ch26/', branch26.view_auguest_account_details_ob_ch26, name='view_auguest_account_details_ob_ch26'),
    path('auguest_account_mgt_ob_ch26/<id>',branch26.auguest_account_mgt_ob_ch26,name='auguest_account_mgt_ob_ch26'),

    path('view_sept_account_details_ob_ch26/', branch26.view_sept_account_details_ob_ch26, name='view_sept_account_details_ob_ch26'),
    path('sept_account_mgt_ob_ch26/<id>',branch26.sept_account_mgt_ob_ch26,name='sept_account_mgt_ob_ch26'),
    path('view_october_account_details_ob_ch26/', branch26.view_october_account_details_ob_ch26, name='view_october_account_details_ob_ch26'),
    path('october_account_mgt_ob_ch26/<id>',branch26.october_account_mgt_ob_ch26,name='october_account_mgt_ob_ch26'),
    path('view_nov_account_details_ob_ch26/', branch26.view_nov_account_details_ob_ch26, name='view_nov_account_details_ob_ch26'),
    path('nov_account_mgt_ob_ch26/<id>',branch26.nov_account_mgt_ob_ch26,name='nov_account_mgt_ob_ch26'),
    path('view_dec_account_details_ob_ch26/', branch26.view_dec_account_details_ob_ch26, name='view_dec_account_details_ob_ch26'),
    path('dec_account_mgt_ob_ch26/<id>',branch26.dec_account_mgt_ob_ch26,name='dec_account_mgt_ob_ch26'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch26', admin_dashboard_calculations_br26.monthly_details_due_ob_ch26, name='monthly_details_due_ob_ch26'),
    path('monthly_collection_details_ob_ch26/', admin_dashboard_calculations_br26.monthly_collection_details_ob_ch26, name='monthly_collection_details_ob_ch26'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch26/',branch26.guest_all_ob_ch26,name='guest_all_ob_ch26'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category26/', accounts26.view_all_category26, name='view_all_category26'),
    path('create_new_category26/', accounts26.create_new_category26, name='create_new_category26'),
    path('regi_new_category26/', accounts26.regi_new_category26, name='regi_new_category26'),
    path('update_category26/<id>',accounts26.update_category26,name='update_category26'),

    path('delete_category26/<id>', accounts26.delete_category26, name='delete_category26'),
    path('view_all_category_delete26/', accounts26.view_all_category_delete26, name='view_all_category_delete26'),

    path('regi_multiple_new_category26/', accounts26.regi_multiple_new_category26, name='regi_multiple_new_category26'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items26/', accounts26.view_all_items26, name='view_all_items26'),
    path('create_new_item26/', accounts26.create_new_item26, name='create_new_item26'),
    path('regi_new_item26/', accounts26.regi_new_item26, name='regi_new_item26'),
    path('delete_item26/<id>',accounts26.delete_item26,name='delete_item26'),
    path('update_item26/<id>', accounts26.update_item26, name='update_item26'),
    path('view_all_items_delete26/',accounts26.view_all_items_delete26,name='view_all_items_delete26'),

    path('regi_multiple_new_item26/', accounts26.regi_multiple_new_item26, name='regi_multiple_new_item26'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger26/', accounts26.view_all_ledger26, name='view_all_ledger26'),
    path('create_new_ledger26/', accounts26.create_new_ledger26, name='create_new_ledger26'),
    path('regi_new_ledger26/', accounts26.regi_new_ledger26, name='regi_new_ledger26'),
    path('delete_ledger26/<id>',accounts26.delete_ledger26,name='delete_ledger26'),
    path('update_ledger26/<id>',accounts26.update_ledger26,name='update_ledger26'),
    path('view_all_ledger_delete26/',accounts26.view_all_ledger_delete26,name='view_all_ledger_delete26'),

    path('regi_multiple_new_ledger26/', accounts26.regi_multiple_new_ledger26, name='regi_multiple_new_ledger26'),

    ##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book26/', accounts26.view_all_accounts_book26, name='view_all_accounts_book26'),
    path('create_new_accounts_book26/', accounts26.create_new_accounts_book26, name='create_new_accounts_book26'),
    path('regi_new_accounts_book26/', accounts26.regi_new_accounts_book26, name='regi_new_accounts_book26'),
    path('update_accounts_book26/<id>',accounts26.update_accounts_book26,name='update_accounts_book26'),
    path('delete_accounts_book26/<id>',accounts26.delete_accounts_book26,name='delete_accounts_book26'),
    path('view_all_accounts_book_delete26/',accounts26.view_all_accounts_book_delete26,name='view_all_accounts_book_delete26'),

    path('regi_multiple_new_accounts_book26/', accounts26.regi_multiple_new_accounts_book26,name='regi_multiple_new_accounts_book26'),

    ##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries26/', accounts26.get_countries26, name='get_countries26'),

    path('in_exp_items_entry26/', accounts26.in_exp_items_entry26, name='in_exp_items_entry26'),
    path('reg_in_exp_items_entry26/', accounts26.reg_in_exp_items_entry26, name='reg_in_exp_items_entry26'),
    path('delete_journal26/<id>',accounts26.delete_journal26,name='delete_journal26'),
    path('update_in_exp_items_entry26/<id>',accounts26.update_in_exp_items_entry26,name='update_in_exp_items_entry26'),
    path('detailed_journal_report26/',accounts26.detailed_journal_report26,name='detailed_journal_report26'),
    path('journal_report_deleted26/',accounts26.journal_report_deleted26,name='journal_report_deleted26'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise26/', accounts26.daily_category_wise26, name='daily_category_wise26'),
    path('monthly_category_based_reports26/',accounts26.monthly_category_based_reports26,name='monthly_category_based_reports26'),
    path('yearly_category_based_reports26/', accounts26.yearly_category_based_reports26,name='yearly_category_based_reports26'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed26/', accounts26.daily_detailed26, name='daily_detailed26'),
    path('monthly_detailed26/',accounts26.monthly_detailed26,name='monthly_detailed26'),
    path('yearly_detailed26/',accounts26.yearly_detailed26,name='yearly_detailed26'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports26/', accounts26.item_based_reports26, name='item_based_reports26'),
    path('daily_item_based_reports26/',accounts26.daily_item_based_reports26,name='daily_item_based_reports26'),
    path('monthly_item_based_reports26/',accounts26.monthly_item_based_reports26,name='monthly_item_based_reports26'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports26/', accounts26.ledger_based_reports26, name='ledger_based_reports26'),
    path('monthly_ledger_based_reports26/', accounts26.monthly_ledger_based_reports26, name='monthly_ledger_based_reports26'),
    path('daily_ledger_based_reports26/',accounts26.daily_ledger_based_reports26,name='daily_ledger_based_reports26'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports26/', accounts26.accounts_book_based_reports26, name='accounts_book_based_reports26'),
    path('daily_accounts_book_based_reports26/',accounts26.daily_accounts_book_based_reports26,name='daily_accounts_book_based_reports26'),
    path('monthly_accounts_book_based_reports26/',accounts26.monthly_accounts_book_based_reports26,name='monthly_accounts_book_based_reports26'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months26/', accounts26.monthly_reports_choose_months26, name='monthly_reports_choose_months26'),
    path('monthly_detailed_daily_in_exp_items_report26/<mo>',accounts26.monthly_detailed_daily_in_exp_items_report26,name='monthly_detailed_daily_in_exp_items_report26'),

    path('single_monthly_reports_choose_months26/', accounts26.single_monthly_reports_choose_months26,name='single_monthly_reports_choose_months26'),
    path('single_monthly_daily_in_exp_items_report26/<mo>',accounts26.single_monthly_daily_in_exp_items_report26,name='single_monthly_daily_in_exp_items_report26'),

    path('accounts_dash_board_ob_ch26/',accounts26.accounts_dash_board_ob_ch26,name='accounts_dash_board_ob_ch26'),
    path('accounts_dash_board26/',accounts26.accounts_dash_board26,name='accounts_dash_board26'),

    path('profit_sharing_choose_months26', accounts26.profit_sharing_choose_months26,name='profit_sharing_choose_months26'),
    path('profit_sharing26/<mo>', accounts26.profit_sharing26, name='profit_sharing26'),
    path('view_share_holders26', accounts26.view_share_holders26, name='view_share_holders26'),
    path('create_share_holders26', accounts26.create_share_holders26, name='create_share_holders26'),
    path('regi_share_holders26', accounts26.regi_share_holders26, name='regi_share_holders26'),
    path('update_share_holders26/<id>', accounts26.update_share_holders26, name='update_share_holders26'),
    path('delete_share_holders26/<id>', accounts26.delete_share_holders26, name='delete_share_holders26'),
    path('view_deleted_share_holders26', accounts26.view_deleted_share_holders26, name='view_deleted_share_holders26'),

    path('regi_multiple_share_holders26', accounts26.regi_multiple_share_holders26, name='regi_multiple_share_holders26'),

    #############BRANCH SETTINGS START HERE ########################

    path('guest_rent_update_ob_ch26/', branch_settings26.guest_rent_update_ob_ch26, name='guest_rent_update_ob_ch26'),

    ############BRANCH SETTINGS END HERE ############################

]

