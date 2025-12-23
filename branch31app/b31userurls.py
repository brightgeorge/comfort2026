from django.urls import path, include

from . import admin_branch31
from . import admin_branch31
from . import branch31
from . import reports31
from . import payment31
from . import admin_dashboard_calculations_br31
from . import accounts31
from . import branch_settings31

urlpatterns = [

    path('branch1_dashboard_ob_ch31/', branch31.branch1_dashboard_ob_ch31, name='branch1_dashboard_ob_ch31'),
    path('branch1_dashboard31/',branch31.branch1_dashboard31,name='branch1_dashboard31'),
    path('user_dashboard_calculations_ob_ch31/',branch31.user_dashboard_calculations_ob_ch31,name='user_dashboard_calculations_ob_ch31'),

    path('background_ob_ch31',branch31.background_ob_ch31,name='background_ob_ch31'),
    path('background_regi_ob_ch31',branch31.background_regi_ob_ch31,name='background_regi_ob_ch31'),
    path('custom_background_regi_ob_ch31',branch31.custom_background_regi_ob_ch31,name='custom_background_regi_ob_ch31'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch31/',admin_branch31.branch1_room_create_regi_ob_ch31,name='branch1_room_create_regi_ob_ch31'),
    path('view_all_room_ob_ch31/',admin_branch31.view_all_room_ob_ch31,name='view_all_room_ob_ch31'),
    path('delete_room_ob_ch31/<id>',admin_branch31.delete_room_ob_ch31,name='delete_room_ob_ch31'),

    path('branch1_room_create_ob_ch31/',admin_branch31.branch1_room_create_ob_ch31,name='branch1_room_create_ob_ch31'),

    path('multiple_branch1_room_create_regi31/',admin_branch31.multiple_branch1_room_create_regi31,name='multiple_branch1_room_create_regi31'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch31/', admin_branch31.pg1_bed_create_regi_ob_ch31, name='pg1_bed_create_regi_ob_ch31'),
    path('pg1_view_all_beds_ob_ch31/', admin_branch31.pg1_view_all_beds_ob_ch31, name='pg1_view_all_beds_ob_ch31'),
    path('delete_bed_ob_ch31/<id>', admin_branch31.delete_bed_ob_ch31, name='delete_bed_ob_ch31'),

    path('pg1_bed_create_ob_ch31/', admin_branch31.pg1_bed_create_ob_ch31, name='pg1_bed_create_ob_ch31'),

    path('single_pg1_bed_create_regi_ob_ch31/',admin_branch31.single_pg1_bed_create_regi_ob_ch31,name='single_pg1_bed_create_regi_ob_ch31'),
    path('update_bed_basic_details_ob_ch31/<id>',admin_branch31.update_bed_basic_details_ob_ch31, name='update_bed_basic_details_ob_ch31'),

    path('multiple_single_pg1_bed_create_regi31/',admin_branch31.multiple_single_pg1_bed_create_regi31,name='multiple_single_pg1_bed_create_regi31'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch31/<id>',branch31.br1_admit_guest_ob_ch31,name='br1_admit_guest_ob_ch31'),
    path('view_all_new_guest_ob_ch31/',branch31.view_all_new_guest_ob_ch31,name='view_all_new_guest_ob_ch31'),
    path('update_br1_admit_guest_ob_ch31/<id>',branch31.update_br1_admit_guest_ob_ch31,name='update_br1_admit_guest_ob_ch31'),
    path('vacate_br1_guest_ob_ch31/<id>',branch31.vacate_br1_guest_ob_ch31,name='vacate_br1_guest_ob_ch31'),

    path('active_guest_details_ob_ch31/<guest_code>',branch31.active_guest_details_ob_ch31,name='active_guest_details_ob_ch31'),
    path('view_all_guest_ob_ch31/',branch31.view_all_guest_ob_ch31,name='view_all_guest_ob_ch31'),
    path('shift_guest_ob_ch31/<id>',branch31.shift_guest_ob_ch31,name='shift_guest_ob_ch31'),
    path('shift_guest_regi_ob_ch31/',branch31.shift_guest_regi_ob_ch31,name='shift_guest_regi_ob_ch31'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch31/',branch31.update_all_rent_ob_ch31,name='update_all_rent_ob_ch31'),

    path('multiple_br1_admit_guest31/<id>',branch31.multiple_br1_admit_guest31,name='multiple_br1_admit_guest31'),

#guest end here


##################################
#_ADVANCE_ob_ch31 START HERE
################################


    path('choose_months_advance_ob_ch31/',branch31.choose_months_advance_ob_ch31,name='choose_months_advance_ob_ch31'),

    path('jan_advance_ob_ch31/', branch31.jan_advance_ob_ch31, name='jan_advance_ob_ch31'),
    path('jan_make_payments_advance_ob_ch31/<id>', branch31.jan_make_payments_advance_ob_ch31,name='jan_make_payments_advance_ob_ch31'),
    path('feb_advance_ob_ch31/', branch31.feb_advance_ob_ch31, name='feb_advance_ob_ch31'),
    path('feb_make_payments_advance_ob_ch31/<id>', branch31.feb_make_payments_advance_ob_ch31,name='feb_make_payments_advance_ob_ch31'),
    path('march_advance_ob_ch31/', branch31.march_advance_ob_ch31, name='march_advance_ob_ch31'),
    path('march_make_payments_advance_ob_ch31/<id>', branch31.march_make_payments_advance_ob_ch31,name='march_make_payments_advance_ob_ch31'),
    path('april_advance_ob_ch31/', branch31.april_advance_ob_ch31, name='april_advance_ob_ch31'),
    path('april_make_payments_advance_ob_ch31/<id>', branch31.april_make_payments_advance_ob_ch31, name='april_make_payments_advance_ob_ch31'),

    path('may_advance_ob_ch31/',branch31.may_advance_ob_ch31,name='may_advance_ob_ch31'),
    path('may_make_payments_advance_ob_ch31/<id>', branch31.may_make_payments_advance_ob_ch31, name='may_make_payments_advance_ob_ch31'),
    path('june_advance_ob_ch31/',branch31.june_advance_ob_ch31,name='june_advance_ob_ch31'),
    path('june_make_payments_advance_ob_ch31/<id>', branch31.june_make_payments_advance_ob_ch31, name='june_make_payments_advance_ob_ch31'),
    path('july_advance_ob_ch31/',branch31.july_advance_ob_ch31,name='july_advance_ob_ch31'),
    path('july_make_payments_advance_ob_ch31/<id>', branch31.july_make_payments_advance_ob_ch31, name='july_make_payments_advance_ob_ch31'),
    path('auguest_advance_ob_ch31/', branch31.auguest_advance_ob_ch31, name='auguest_advance_ob_ch31'),
    path('auguest_make_payments_advance_ob_ch31/<id>', branch31.auguest_make_payments_advance_ob_ch31, name='auguest_make_payments_advance_ob_ch31'),

    path('sept_advance_ob_ch31/', branch31.sept_advance_ob_ch31, name='sept_advance_ob_ch31'),
    path('sept_make_payments_advance_ob_ch31/<id>', branch31.sept_make_payments_advance_ob_ch31,name='sept_make_payments_advance_ob_ch31'),
    path('october_advance_ob_ch31/', branch31.october_advance_ob_ch31, name='october_advance_ob_ch31'),
    path('october_make_payments_advance_ob_ch31/<id>', branch31.october_make_payments_advance_ob_ch31, name='october_make_payments_advance_ob_ch31'),
    path('nov_advance_ob_ch31/', branch31.nov_advance_ob_ch31, name='nov_advance_ob_ch31'),
    path('nov_make_payments_advance_ob_ch31/<id>', branch31.nov_make_payments_advance_ob_ch31,name='nov_make_payments_advance_ob_ch31'),
    path('dec_advance_ob_ch31/', branch31.dec_advance_ob_ch31, name='dec_advance_ob_ch31'),
    path('dec_make_payments_advance_ob_ch31/<id>', branch31.dec_make_payments_advance_ob_ch31, name='dec_make_payments_advance_ob_ch31'),



##################################
#_ADVANCE_ob_ch31 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch31/',branch31.choose_months_ob_ch31,name='choose_months_ob_ch31'),

    path('jan_ob_ch31/',branch31.jan_ob_ch31,name='jan_ob_ch31'),
    path('jan_manke_payments_ob_ch31/<id>',branch31.jan_manke_payments_ob_ch31,name='jan_manke_payments_ob_ch31'),

    path('feb_ob_ch31/',branch31.feb_ob_ch31,name='feb_ob_ch31'),
    path('feb_manke_payments_ob_ch31/<id>',branch31.feb_manke_payments_ob_ch31,name='feb_manke_payments_ob_ch31'),

    path('march_ob_ch31/',branch31.march_ob_ch31,name='march_ob_ch31'),
    path('march_manke_payments_ob_ch31/<id>',branch31.march_manke_payments_ob_ch31,name='march_manke_payments_ob_ch31'),

    path('april_ob_ch31/',branch31.april_ob_ch31,name='april_ob_ch31'),
    path('april_make_payments_ob_ch31/<id>',branch31.april_make_payments_ob_ch31,name='april_make_payments_ob_ch31'),

    path('may_ob_ch31/',branch31.may_ob_ch31,name='may_ob_ch31'),
    path('may_make_payments_ob_ch31/<id>',branch31.may_make_payments_ob_ch31,name='may_make_payments_ob_ch31'),

    path('june_ob_ch31/',branch31.june_ob_ch31,name='june_ob_ch31'),
    path('june_make_payments_ob_ch31/<id>',branch31.june_make_payments_ob_ch31,name='june_make_payments_ob_ch31'),

    path('july_ob_ch31/',branch31.july_ob_ch31,name='july_ob_ch31'),
    path('july_make_payments_ob_ch31/<id>',branch31.july_make_payments_ob_ch31,name='july_make_payments_ob_ch31'),

    path('aug_ob_ch31/',branch31.aug_ob_ch31,name='aug_ob_ch31'),
    path('aug_make_payments_ob_ch31/<id>',branch31.aug_make_payments_ob_ch31,name='aug_make_payments_ob_ch31'),

    path('sept_ob_ch31/',branch31.sept_ob_ch31,name='sept_ob_ch31'),
    path('sept_make_payments_ob_ch31/<id>',branch31.sept_make_payments_ob_ch31,name='sept_make_payments_ob_ch31'),

    path('oct_ob_ch31/',branch31.oct_ob_ch31,name='oct_ob_ch31'),
    path('oct_make_payments_ob_ch31/<id>',branch31.oct_make_payments_ob_ch31,name='oct_make_payments_ob_ch31'),

    path('nov_ob_ch31/',branch31.nov_ob_ch31,name='nov_ob_ch31'),
    path('nov_make_payments_ob_ch31/<id>',branch31.nov_make_payments_ob_ch31,name='nov_make_payments_ob_ch31'),

    path('dec_ob_ch31/',branch31.dec_ob_ch31,name='dec_ob_ch31'),
    path('dec_make_payments_ob_ch31/<id>',branch31.dec_make_payments_ob_ch31,name='dec_make_payments_ob_ch31'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch31/', payment31.choose_user_ob_ch31, name='choose_user_ob_ch31'),
    path('payment_user_details_ob_ch31/<id>', payment31.payment_user_details_ob_ch31, name='payment_user_details_ob_ch31'),
    path('close_choose_user_ob_ch31/<id>',payment31.close_choose_user_ob_ch31,name='close_choose_user_ob_ch31'),

    path('monthly_jan_make_payments_ob_ch31/<id>', payment31.monthly_jan_make_payments_ob_ch31, name='monthly_jan_make_payments_ob_ch31'),
    path('monthly_feb_make_payments_ob_ch31/<id>', payment31.monthly_feb_make_payments_ob_ch31, name='monthly_feb_make_payments_ob_ch31'),
    path('monthly_march_make_payments_ob_ch31/<id>', payment31.monthly_march_make_payments_ob_ch31, name='monthly_march_make_payments_ob_ch31'),
    path('monthly_april_make_payments_ob_ch31/<id>', payment31.monthly_april_make_payments_ob_ch31, name='monthly_april_make_payments_ob_ch31'),
    path('monthly_may_make_payments_ob_ch31/<id>', payment31.monthly_may_make_payments_ob_ch31, name='monthly_may_make_payments_ob_ch31'),
    path('monthly_june_make_payments_ob_ch31/<id>', payment31.monthly_june_make_payments_ob_ch31, name='monthly_june_make_payments_ob_ch31'),

    path('monthly_july_make_payments_ob_ch31/<id>', payment31.monthly_july_make_payments_ob_ch31, name='monthly_july_make_payments_ob_ch31'),
    path('monthly_aug_make_payments_ob_ch31/<id>', payment31.monthly_aug_make_payments_ob_ch31, name='monthly_aug_make_payments_ob_ch31'),
    path('monthly_sept_make_payments_ob_ch31/<id>', payment31.monthly_sept_make_payments_ob_ch31, name='monthly_sept_make_payments_ob_ch31'),
    path('monthly_oct_make_payments_ob_ch31/<id>', payment31.monthly_oct_make_payments_ob_ch31, name='monthly_oct_make_payments_ob_ch31'),
    path('monthly_nov_make_payments_ob_ch31/<id>', payment31.monthly_nov_make_payments_ob_ch31, name='monthly_nov_make_payments_ob_ch31'),
    path('monthly_dec_make_payments_ob_ch31/<id>', payment31.monthly_dec_make_payments_ob_ch31, name='monthly_dec_make_payments_ob_ch31'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch31/',branch31.unpaid_rent_choose_months_ob_ch31,name='unpaid_rent_choose_months_ob_ch31'),

    path('jan_unpaid_rent_ob_ch31/', branch31.jan_unpaid_rent_ob_ch31, name='jan_unpaid_rent_ob_ch31'),
    path('table_jan_unpaid_rent_ob_ch31/', branch31.table_jan_unpaid_rent_ob_ch31, name='table_jan_unpaid_rent_ob_ch31'),
    path('feb_unpaid_rent_ob_ch31/', branch31.feb_unpaid_rent_ob_ch31, name='feb_unpaid_rent_ob_ch31'),
    path('table_feb_unpaid_rent_ob_ch31/', branch31.table_feb_unpaid_rent_ob_ch31, name='table_feb_unpaid_rent_ob_ch31'),
    path('mar_unpaid_rent_ob_ch31/', branch31.mar_unpaid_rent_ob_ch31, name='mar_unpaid_rent_ob_ch31'),
    path('table_mar_unpaid_rent_ob_ch31/', branch31.table_mar_unpaid_rent_ob_ch31, name='table_mar_unpaid_rent_ob_ch31'),
    path('april_unpaid_rent_ob_ch31/', branch31.april_unpaid_rent_ob_ch31, name='april_unpaid_rent_ob_ch31'),
    path('table_april_unpaid_rent_ob_ch31/', branch31.table_april_unpaid_rent_ob_ch31, name='table_april_unpaid_rent_ob_ch31'),

    path('may_unpaid_rent_ob_ch31/', branch31.may_unpaid_rent_ob_ch31, name='may_unpaid_rent_ob_ch31'),
    path('table_may_unpaid_rent_ob_ch31/', branch31.table_may_unpaid_rent_ob_ch31, name='table_may_unpaid_rent_ob_ch31'),
    path('june_unpaid_rent_ob_ch31/', branch31.june_unpaid_rent_ob_ch31, name='june_unpaid_rent_ob_ch31'),
    path('table_june_unpaid_rent_ob_ch31/', branch31.table_june_unpaid_rent_ob_ch31, name='table_june_unpaid_rent_ob_ch31'),
    path('july_unpaid_rent_ob_ch31/', branch31.july_unpaid_rent_ob_ch31, name='july_unpaid_rent_ob_ch31'),
    path('table_july_unpaid_rent_ob_ch31',branch31.table_july_unpaid_rent_ob_ch31,name='table_july_unpaid_rent_ob_ch31'),
    path('aug_unpaid_rent_ob_ch31/', branch31.aug_unpaid_rent_ob_ch31, name='aug_unpaid_rent_ob_ch31'),
    path('table_aug_unpaid_rent_ob_ch31/',branch31.table_aug_unpaid_rent_ob_ch31,name='table_aug_unpaid_rent_ob_ch31'),

    path('sept_unpaid_rent_ob_ch31/', branch31.sept_unpaid_rent_ob_ch31, name='sept_unpaid_rent_ob_ch31'),
    path('table_sept_unpaid_rent_ob_ch31/', branch31.table_sept_unpaid_rent_ob_ch31, name='table_sept_unpaid_rent_ob_ch31'),
    path('oct_unpaid_rent_ob_ch31/', branch31.oct_unpaid_rent_ob_ch31, name='oct_unpaid_rent_ob_ch31'),
    path('table_oct_unpaid_rent_ob_ch31/', branch31.table_oct_unpaid_rent_ob_ch31, name='table_oct_unpaid_rent_ob_ch31'),
    path('nov_unpaid_rent_ob_ch31/', branch31.nov_unpaid_rent_ob_ch31, name='nov_unpaid_rent_ob_ch31'),
    path('table_nov_unpaid_rent_ob_ch31/', branch31.table_nov_unpaid_rent_ob_ch31, name='table_nov_unpaid_rent_ob_ch31'),
    path('dec_unpaid_rent_ob_ch31/', branch31.dec_unpaid_rent_ob_ch31, name='dec_unpaid_rent_ob_ch31'),
    path('table_dec_unpaid_rent_ob_ch31/', branch31.table_dec_unpaid_rent_ob_ch31, name='table_dec_unpaid_rent_ob_ch31'),

    path('details_of_unpaid_guests_ob_ch31/<id>',branch31.details_of_unpaid_guests_ob_ch31,name='details_of_unpaid_guests_ob_ch31'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch31/',branch31.paid_rent_choose_months_ob_ch31,name='paid_rent_choose_months_ob_ch31'),
    path('partially_paid_guest_choose_months_ob_ch31/',reports31.partially_paid_guest_choose_months_ob_ch31,name='partially_paid_guest_choose_months_ob_ch31'),

    path('jan_paid_rent_ob_ch31/', branch31.jan_paid_rent_ob_ch31, name='jan_paid_rent_ob_ch31'),
    path('table_jan_paid_rent_ob_ch31/', branch31.table_jan_paid_rent_ob_ch31, name='table_jan_paid_rent_ob_ch31'),
    path('jan_full_paid_guest_ob_ch31/', reports31.jan_full_paid_guest_ob_ch31, name='jan_full_paid_guest_ob_ch31'),
    path('jan_partially_paid_guest_ob_ch31/', reports31.jan_partially_paid_guest_ob_ch31, name='jan_partially_paid_guest_ob_ch31'),
    path('table_jan_partially_paid_guest_ob_ch31/', reports31.table_jan_partially_paid_guest_ob_ch31,name='table_jan_partially_paid_guest_ob_ch31'),

    path('feb_paid_rent_ob_ch31/', branch31.feb_paid_rent_ob_ch31, name='feb_paid_rent_ob_ch31'),
    path('table_feb_paid_rent_ob_ch31/', branch31.table_feb_paid_rent_ob_ch31, name='table_feb_paid_rent_ob_ch31'),
    path('feb_full_paid_guest_ob_ch31/', reports31.feb_full_paid_guest_ob_ch31, name='feb_full_paid_guest_ob_ch31'),
    path('feb_partially_paid_guest_ob_ch31/', reports31.feb_partially_paid_guest_ob_ch31, name='feb_partially_paid_guest_ob_ch31'),
    path('table_feb_partially_paid_guest_ob_ch31/', reports31.table_feb_partially_paid_guest_ob_ch31,name='table_feb_partially_paid_guest_ob_ch31'),

    path('mar_paid_rent_ob_ch31/', branch31.mar_paid_rent_ob_ch31, name='mar_paid_rent_ob_ch31'),
    path('table_mar_paid_rent_ob_ch31/', branch31.table_mar_paid_rent_ob_ch31, name='table_mar_paid_rent_ob_ch31'),
    path('march_full_paid_guest_ob_ch31/', reports31.march_full_paid_guest_ob_ch31, name='march_full_paid_guest_ob_ch31'),
    path('march_partially_paid_guest_ob_ch31/', reports31.march_partially_paid_guest_ob_ch31, name='march_partially_paid_guest_ob_ch31'),
    path('table_march_partially_paid_guest_ob_ch31/', reports31.table_march_partially_paid_guest_ob_ch31,name='table_march_partially_paid_guest_ob_ch31'),

    path('april_paid_rent_ob_ch31/', branch31.april_paid_rent_ob_ch31, name='april_paid_rent_ob_ch31'),
    path('table_april_paid_rent_ob_ch31/', branch31.table_april_paid_rent_ob_ch31, name='table_april_paid_rent_ob_ch31'),
    path('april_full_paid_guest_ob_ch31/', reports31.april_full_paid_guest_ob_ch31, name='april_full_paid_guest_ob_ch31'),
    path('april_partially_paid_guest_ob_ch31/', reports31.april_partially_paid_guest_ob_ch31, name='april_partially_paid_guest_ob_ch31'),
    path('table_april_partially_paid_guest_ob_ch31/', reports31.table_april_partially_paid_guest_ob_ch31,name='table_april_partially_paid_guest_ob_ch31'),

    path('may_paid_rent_ob_ch31/', branch31.may_paid_rent_ob_ch31, name='may_paid_rent_ob_ch31'),
    path('table_may_paid_rent_ob_ch31/', branch31.table_may_paid_rent_ob_ch31, name='table_may_paid_rent_ob_ch31'),
    path('may_full_paid_guest_ob_ch31/', reports31.may_full_paid_guest_ob_ch31, name='may_full_paid_guest_ob_ch31'),
    path('may_partially_paid_guest_ob_ch31/', reports31.may_partially_paid_guest_ob_ch31, name='may_partially_paid_guest_ob_ch31'),
    path('table_may_partially_paid_guest_ob_ch31/', reports31.table_may_partially_paid_guest_ob_ch31, name='table_may_partially_paid_guest_ob_ch31'),

    path('june_paid_rent_ob_ch31/', branch31.june_paid_rent_ob_ch31, name='june_paid_rent_ob_ch31'),
    path('table_june_paid_rent_ob_ch31/', branch31.table_june_paid_rent_ob_ch31, name='table_june_paid_rent_ob_ch31'),
    path('june_full_paid_guest_ob_ch31/', reports31.june_full_paid_guest_ob_ch31, name='june_full_paid_guest_ob_ch31'),
    path('june_partially_paid_guest_ob_ch31/', reports31.june_partially_paid_guest_ob_ch31, name='june_partially_paid_guest_ob_ch31'),
    path('table_june_partially_paid_guest_ob_ch31/', reports31.table_june_partially_paid_guest_ob_ch31, name='table_june_partially_paid_guest_ob_ch31'),

    path('july_paid_rent_ob_ch31/', branch31.july_paid_rent_ob_ch31, name='july_paid_rent_ob_ch31'),
    path('table_july_paid_rent_ob_ch31/', branch31.table_july_paid_rent_ob_ch31, name='table_july_paid_rent_ob_ch31'),
    path('july_full_paid_guest_ob_ch31/', reports31.july_full_paid_guest_ob_ch31, name='july_full_paid_guest_ob_ch31'),
    path('july_partially_paid_guest_ob_ch31/', reports31.july_partially_paid_guest_ob_ch31, name='july_partially_paid_guest_ob_ch31'),
    path('table_july_partially_paid_guest_ob_ch31/', reports31.table_july_partially_paid_guest_ob_ch31, name='table_july_partially_paid_guest_ob_ch31'),

    path('aug_paid_rent_ob_ch31/', branch31.aug_paid_rent_ob_ch31, name='aug_paid_rent_ob_ch31'),
    path('table_aug_paid_rent_ob_ch31/', branch31.table_aug_paid_rent_ob_ch31, name='table_aug_paid_rent_ob_ch31'),
    path('auguest_full_paid_guest_ob_ch31/', reports31.auguest_full_paid_guest_ob_ch31, name='auguest_full_paid_guest_ob_ch31'),
    path('auguest_partially_paid_guest_ob_ch31/', reports31.auguest_partially_paid_guest_ob_ch31,name='auguest_partially_paid_guest_ob_ch31'),
    path('table_auguest_partially_paid_guest_ob_ch31/', reports31.table_auguest_partially_paid_guest_ob_ch31,name='table_auguest_partially_paid_guest_ob_ch31'),

    path('sept_paid_rent_ob_ch31/', branch31.sept_paid_rent_ob_ch31, name='sept_paid_rent_ob_ch31'),
    path('table_sept_paid_rent_ob_ch31/', branch31.table_sept_paid_rent_ob_ch31, name='table_sept_paid_rent_ob_ch31'),
    path('sept_full_paid_guest_ob_ch31/', reports31.sept_full_paid_guest_ob_ch31, name='sept_full_paid_guest_ob_ch31'),
    path('sept_partially_paid_guest_ob_ch31/', reports31.sept_partially_paid_guest_ob_ch31, name='sept_partially_paid_guest_ob_ch31'),
    path('table_sept_partially_paid_guest_ob_ch31/', reports31.table_sept_partially_paid_guest_ob_ch31,name='table_sept_partially_paid_guest_ob_ch31'),

    path('oct_paid_rent_ob_ch31/', branch31.oct_paid_rent_ob_ch31, name='oct_paid_rent_ob_ch31'),
    path('table_oct_paid_rent_ob_ch31/', branch31.table_oct_paid_rent_ob_ch31, name='table_oct_paid_rent_ob_ch31'),
    path('october_full_paid_guest_ob_ch31/', reports31.october_full_paid_guest_ob_ch31, name='october_full_paid_guest_ob_ch31'),
    path('october_partially_paid_guest_ob_ch31/', reports31.october_partially_paid_guest_ob_ch31,name='october_partially_paid_guest_ob_ch31'),
    path('table_october_partially_paid_guest_ob_ch31/', reports31.table_october_partially_paid_guest_ob_ch31,name='table_october_partially_paid_guest_ob_ch31'),

    path('nov_paid_rent_ob_ch31/', branch31.nov_paid_rent_ob_ch31, name='nov_paid_rent_ob_ch31'),
    path('table_nov_paid_rent_ob_ch31/', branch31.table_nov_paid_rent_ob_ch31, name='table_nov_paid_rent_ob_ch31'),
    path('nov_full_paid_guest_ob_ch31/', reports31.nov_full_paid_guest_ob_ch31, name='nov_full_paid_guest_ob_ch31'),
    path('nov_partially_paid_guest_ob_ch31/', reports31.nov_partially_paid_guest_ob_ch31, name='nov_partially_paid_guest_ob_ch31'),
    path('table_nov_partially_paid_guest_ob_ch31/', reports31.table_nov_partially_paid_guest_ob_ch31,name='table_nov_partially_paid_guest_ob_ch31'),

    path('dec_paid_rent_ob_ch31/', branch31.dec_paid_rent_ob_ch31, name='dec_paid_rent_ob_ch31'),
    path('table_dec_paid_rent_ob_ch31/', branch31.table_dec_paid_rent_ob_ch31, name='table_dec_paid_rent_ob_ch31'),
    path('dec_full_paid_guest_ob_ch31/', reports31.dec_full_paid_guest_ob_ch31, name='dec_full_paid_guest_ob_ch31'),
    path('dec_partially_paid_guest_ob_ch31/', reports31.dec_partially_paid_guest_ob_ch31, name='dec_partially_paid_guest_ob_ch31'),
    path('table_dec_partially_paid_guest_ob_ch31/', reports31.table_dec_partially_paid_guest_ob_ch31,name='table_dec_partially_paid_guest_ob_ch31'),

    path('details_of_paid_guests_ob_ch31/<id>',branch31.details_of_paid_guests_ob_ch31,name='details_of_paid_guests_ob_ch31'),
    path('full_paid_guest_ob_ch31/',reports31.full_paid_guest_ob_ch31,name='full_paid_guest_ob_ch31'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch31/',branch31.viewall_vacate_guest_ob_ch31,name='viewall_vacate_guest_ob_ch31'),
    path('details_of_vacate_guest_ob_ch31/<id>',branch31.details_of_vacate_guest_ob_ch31,name='details_of_vacate_guest_ob_ch31'),
    path('full_vacated_guest_details_ob_ch31',branch31.full_vacated_guest_details_ob_ch31,name='full_vacated_guest_details_ob_ch31'),
    path('full_vacated_guest_table_ob_ch31',branch31.full_vacated_guest_table_ob_ch31,name='full_vacated_guest_table_ob_ch31'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch31/<id>', branch31.jan_manke_payments_vacate_ob_ch31, name='jan_manke_payments_vacate_ob_ch31'),
    path('feb_manke_payments_vacate_ob_ch31/<id>', branch31.feb_manke_payments_vacate_ob_ch31, name='feb_manke_payments_vacate_ob_ch31'),
    path('march_manke_payments_vacate_ob_ch31/<id>', branch31.march_manke_payments_vacate_ob_ch31, name='march_manke_payments_vacate_ob_ch31'),
    path('april_make_payments_vacate_ob_ch31/<id>', branch31.april_make_payments_vacate_ob_ch31, name='april_make_payments_vacate_ob_ch31'),

    path('may_make_payments_vacate_ob_ch31/<id>', branch31.may_make_payments_vacate_ob_ch31, name='may_make_payments_vacate_ob_ch31'),
    path('june_make_payments_vacate_ob_ch31/<id>', branch31.june_make_payments_vacate_ob_ch31, name='june_make_payments_vacate_ob_ch31'),
    path('july_make_payments_vacate_ob_ch31/<id>', branch31.july_make_payments_vacate_ob_ch31, name='july_make_payments_vacate_ob_ch31'),
    path('aug_make_payments_vacate_ob_ch31/<id>', branch31.aug_make_payments_vacate_ob_ch31, name='aug_make_payments_vacate_ob_ch31'),

    path('sept_make_payments_vacate_ob_ch31/<id>', branch31.sept_make_payments_vacate_ob_ch31, name='sept_make_payments_vacate_ob_ch31'),
    path('oct_make_payments_vacate_ob_ch31/<id>', branch31.oct_make_payments_vacate_ob_ch31, name='oct_make_payments_vacate_ob_ch31'),
    path('nov_make_payments_vacate_ob_ch31/<id>', branch31.nov_make_payments_vacate_ob_ch31, name='nov_make_payments_vacate_ob_ch31'),
    path('dec_make_payments_vacate_ob_ch31/<id>', branch31.dec_make_payments_vacate_ob_ch31, name='dec_make_payments_vacate_ob_ch31'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch31/',branch31.detail_guest_general_ob_ch31,name='detail_guest_general_ob_ch31'),

    path('jan_print_ob_ch31/',branch31.jan_print_ob_ch31,name='jan_print_ob_ch31'),
    path('feb_print_ob_ch31/',branch31.feb_print_ob_ch31,name='feb_print_ob_ch31'),
    path('march_print_ob_ch31/',branch31.march_print_ob_ch31,name='march_print_ob_ch31'),
    path('april_print_ob_ch31/',branch31.april_print_ob_ch31,name='april_print_ob_ch31'),

    path('may_print_ob_ch31/',branch31.may_print_ob_ch31,name='may_print_ob_ch31'),
    path('june_print_ob_ch31/',branch31.june_print_ob_ch31,name='june_print_ob_ch31'),
    path('july_print_ob_ch31/', branch31.july_print_ob_ch31, name='july_print_ob_ch31'),
    path('aug_print_ob_ch31/', branch31.aug_print_ob_ch31, name='aug_print_ob_ch31'),

    path('sept_print_ob_ch31/', branch31.sept_print_ob_ch31, name='sept_print_ob_ch31'),
    path('oct_print_ob_ch31/', branch31.oct_print_ob_ch31, name='oct_print_ob_ch31'),
    path('nov_print_ob_ch31/', branch31.nov_print_ob_ch31, name='nov_print_ob_ch31'),
    path('dec_print_ob_ch31/', branch31.dec_print_ob_ch31, name='dec_print_ob_ch31'),

    path('new_year_jan_print_ob_ch31/', branch31.new_year_jan_print_ob_ch31, name='new_year_jan_print_ob_ch31'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch31/', branch31.jan_close_ob_ch31, name='jan_close_ob_ch31'),
    path('jan_close_decision_page_ob_ch31/', branch31.jan_close_decision_page_ob_ch31, name='jan_close_decision_page_ob_ch31'),
    path('feb_close/', branch31.feb_close_ob_ch31, name='feb_close_ob_ch31'),
    path('feb_close_decision_page_ob_ch31/', branch31.feb_close_decision_page_ob_ch31, name='feb_close_decision_page_ob_ch31'),
    path('mar_close_ob_ch31/', branch31.mar_close_ob_ch31, name='mar_close_ob_ch31'),
    path('mar_close_decision_page/', branch31.mar_close_decision_page_ob_ch31, name='mar_close_decision_page_ob_ch31'),
    path('apr_close_ob_ch31/', branch31.apr_close_ob_ch31, name='apr_close_ob_ch31'),
    path('apr_close_decision_page_ob_ch31/', branch31.apr_close_decision_page_ob_ch31, name='apr_close_decision_page_ob_ch31'),

    path('may_close_ob_ch31/', branch31.may_close_ob_ch31, name='may_close_ob_ch31'),
    path('may_close_decision_page_ob_ch31/', branch31.may_close_decision_page_ob_ch31, name='may_close_decision_page_ob_ch31'),
    path('jun_close_ob_ch31/', branch31.jun_close_ob_ch31, name='jun_close_ob_ch31'),
    path('jun_close_decision_page_ob_ch31/', branch31.jun_close_decision_page_ob_ch31, name='jun_close_decision_page_ob_ch31'),
    path('jul_close_ob_ch31/', branch31.jul_close_ob_ch31, name='jul_close_ob_ch31'),
    path('jul_close_decision_page_ob_ch31/', branch31.jul_close_decision_page_ob_ch31, name='jul_close_decision_page_ob_ch31'),
    path('aug_close_ob_ch31/', branch31.aug_close_ob_ch31, name='aug_close_ob_ch31'),
    path('aug_close_decision_page_ob_ch31/', branch31.aug_close_decision_page_ob_ch31, name='aug_close_decision_page_ob_ch31'),

    path('sep_close_ob_ch31/', branch31.sep_close_ob_ch31, name='sep_close_ob_ch31'),
    path('sep_close_decision_page_ob_ch31/', branch31.sep_close_decision_page_ob_ch31, name='sep_close_decision_page_ob_ch31'),
    path('oct_close_ob_ch31/', branch31.oct_close_ob_ch31, name='oct_close_ob_ch31'),
    path('oct_close_decision_page_ob_ch31/', branch31.oct_close_decision_page_ob_ch31, name='oct_close_decision_page_ob_ch31'),
    path('nov_close_ob_ch31/', branch31.nov_close_ob_ch31, name='nov_close_ob_ch31'),
    path('nov_close_decision_page_ob_ch31/', branch31.nov_close_decision_page_ob_ch31, name='nov_close_decision_page_ob_ch31'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch31/',reports31.detailed_report_choose_months_ob_ch31,name='detailed_report_choose_months_ob_ch31'),

    path('jan_details_live_ob_ch31/', reports31.jan_details_live_ob_ch31, name='jan_details_live_ob_ch31'),
    path('jan_print_live_ob_ch31/', reports31.jan_print_live_ob_ch31, name='jan_print_live_ob_ch31'),
    path('feb_details_live_ob_ch31/', reports31.feb_details_live_ob_ch31, name='feb_details_live_ob_ch31'),
    path('feb_print_live_ob_ch31/', reports31.feb_print_live_ob_ch31, name='feb_print_live_ob_ch31'),
    path('march_details_live_ob_ch31/', reports31.march_details_live_ob_ch31, name='march_details_live_ob_ch31'),
    path('march_print_live_ob_ch31/', reports31.march_print_live_ob_ch31, name='march_print_live_ob_ch31'),

    path('april_details_live_ob_ch31/', reports31.april_details_live_ob_ch31, name='april_details_live_ob_ch31'),
    path('april_print_live_ob_ch31/', reports31.april_print_live_ob_ch31, name='april_print_live_ob_ch31'),
    path('may_details_live_ob_ch31/', reports31.may_details_live_ob_ch31, name='may_details_live_ob_ch31'),
    path('may_print_live_ob_ch31/', reports31.may_print_live_ob_ch31, name='may_print_live_ob_ch31'),
    path('june_details_live_ob_ch31/',reports31.june_details_live_ob_ch31,name='june_details_live_ob_ch31'),
    path('june_print_live_ob_ch31/', reports31.june_print_live_ob_ch31, name='june_print_live_ob_ch31'),

    path('july_details_live_ob_ch31/', reports31.july_details_live_ob_ch31, name='july_details_live_ob_ch31'),
    path('july_print_live_ob_ch31/', reports31.july_print_live_ob_ch31, name='july_print_live_ob_ch31'),
    path('auguest_details_live_ob_ch31/', reports31.auguest_details_live_ob_ch31, name='auguest_details_live_ob_ch31'),
    path('auguest_print_live_ob_ch31/', reports31.auguest_print_live_ob_ch31, name='auguest_print_live_ob_ch31'),
    path('sept_details_live_ob_ch31/', reports31.sept_details_live_ob_ch31, name='sept_details_live_ob_ch31'),
    path('sept_print_live_ob_ch31/', reports31.sept_print_live_ob_ch31, name='sept_print_live_ob_ch31'),

    path('october_details_live_ob_ch31/', reports31.october_details_live_ob_ch31, name='october_details_live_ob_ch31'),
    path('october_print_live_ob_ch31/', reports31.october_print_live_ob_ch31, name='october_print_live_ob_ch31'),
    path('nov_details_live_ob_ch31/', reports31.nov_details_live_ob_ch31, name='nov_details_live_ob_ch31'),
    path('nov_print_live_ob_ch31/', reports31.nov_print_live_ob_ch31, name='nov_print_live_ob_ch31'),
    path('dec_details_live_ob_ch31/', reports31.dec_details_live_ob_ch31, name='dec_details_live_ob_ch31'),
    path('dec_print_live_ob_ch31/', reports31.dec_print_live_ob_ch31, name='dec_print_live_ob_ch31'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch31/', reports31.viewall_vaccant_room_ob_ch31, name='viewall_vaccant_room_ob_ch31'),

    path('d_ob_ch31/', branch31.dynamic, name='dynamic'),

    path('manage_bed_ob_ch31/', branch31.manage_bed_ob_ch31, name='manage_bed_ob_ch31'),
    path('manage_new_guest_ob_ch31/', branch31.manage_new_guest_ob_ch31, name='manage_new_guest_ob_ch31'),
    path('manage_update_new_guest_ob_ch31/<id>', branch31.manage_update_new_guest_ob_ch31, name='manage_update_new_guest_ob_ch31'),
    path('manage_update_beds_ob_ch31/<id>', branch31.manage_update_beds_ob_ch31, name='manage_update_beds_ob_ch31'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch31/', branch31.view_all_due_amt_ob_ch31, name='view_all_due_amt_ob_ch31'),
    path('due_amt_mgt_choose_months_ob_ch31/', branch31.due_amt_mgt_choose_months_ob_ch31, name='due_amt_mgt_choose_months_ob_ch31'),

    path('view_jan_account_details_ob_ch31/', branch31.view_jan_account_details_ob_ch31, name='view_jan_account_details_ob_ch31'),
    path('jan_account_mgt_ob_ch31/<id>',branch31.jan_account_mgt_ob_ch31,name='jan_account_mgt_ob_ch31'),
    path('view_feb_account_details_ob_ch31/', branch31.view_feb_account_details_ob_ch31, name='view_feb_account_details_ob_ch31'),
    path('feb_account_mgt_ob_ch31/<id>',branch31.feb_account_mgt_ob_ch31,name='feb_account_mgt_ob_ch31'),
    path('view_march_account_details_ob_ch31/', branch31.view_march_account_details_ob_ch31, name='view_march_account_details_ob_ch31'),
    path('march_account_mgt_ob_ch31/<id>',branch31.march_account_mgt_ob_ch31,name='march_account_mgt_ob_ch31'),
    path('view_april_account_details_ob_ch31/', branch31.view_april_account_details_ob_ch31, name='view_april_account_details_ob_ch31'),
    path('april_account_mgt_ob_ch31/<id>',branch31.april_account_mgt_ob_ch31,name='april_account_mgt_ob_ch31'),

    path('view_may_account_details_ob_ch31/',branch31.view_may_account_details_ob_ch31,name='view_may_account_details_ob_ch31'),
    path('may_account_mgt_ob_ch31/<id>', branch31.may_account_mgt_ob_ch31, name='may_account_mgt_ob_ch31'),
    path('view_june_account_details_ob_ch31/', branch31.view_june_account_details_ob_ch31, name='view_june_account_details_ob_ch31'),
    path('june_account_mgt_ob_ch31/<id>',branch31.june_account_mgt_ob_ch31,name='june_account_mgt_ob_ch31'),
    path('view_july_account_details_ob_ch31/', branch31.view_july_account_details_ob_ch31, name='view_july_account_details_ob_ch31'),
    path('july_account_mgt_ob_ch31/<id>',branch31.july_account_mgt_ob_ch31,name='july_account_mgt_ob_ch31'),
    path('view_auguest_account_details_ob_ch31/', branch31.view_auguest_account_details_ob_ch31, name='view_auguest_account_details_ob_ch31'),
    path('auguest_account_mgt_ob_ch31/<id>',branch31.auguest_account_mgt_ob_ch31,name='auguest_account_mgt_ob_ch31'),

    path('view_sept_account_details_ob_ch31/', branch31.view_sept_account_details_ob_ch31, name='view_sept_account_details_ob_ch31'),
    path('sept_account_mgt_ob_ch31/<id>',branch31.sept_account_mgt_ob_ch31,name='sept_account_mgt_ob_ch31'),
    path('view_october_account_details_ob_ch31/', branch31.view_october_account_details_ob_ch31, name='view_october_account_details_ob_ch31'),
    path('october_account_mgt_ob_ch31/<id>',branch31.october_account_mgt_ob_ch31,name='october_account_mgt_ob_ch31'),
    path('view_nov_account_details_ob_ch31/', branch31.view_nov_account_details_ob_ch31, name='view_nov_account_details_ob_ch31'),
    path('nov_account_mgt_ob_ch31/<id>',branch31.nov_account_mgt_ob_ch31,name='nov_account_mgt_ob_ch31'),
    path('view_dec_account_details_ob_ch31/', branch31.view_dec_account_details_ob_ch31, name='view_dec_account_details_ob_ch31'),
    path('dec_account_mgt_ob_ch31/<id>',branch31.dec_account_mgt_ob_ch31,name='dec_account_mgt_ob_ch31'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch31', admin_dashboard_calculations_br31.monthly_details_due_ob_ch31, name='monthly_details_due_ob_ch31'),
    path('monthly_collection_details_ob_ch31/', admin_dashboard_calculations_br31.monthly_collection_details_ob_ch31, name='monthly_collection_details_ob_ch31'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch31/',branch31.guest_all_ob_ch31,name='guest_all_ob_ch31'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category31/', accounts31.view_all_category31, name='view_all_category31'),
    path('create_new_category31/', accounts31.create_new_category31, name='create_new_category31'),
    path('regi_new_category31/', accounts31.regi_new_category31, name='regi_new_category31'),
    path('update_category31/<id>',accounts31.update_category31,name='update_category31'),

    path('delete_category31/<id>', accounts31.delete_category31, name='delete_category31'),
    path('view_all_category_delete31/', accounts31.view_all_category_delete31, name='view_all_category_delete31'),

    path('regi_multiple_new_category31/', accounts31.regi_multiple_new_category31, name='regi_multiple_new_category31'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items31/', accounts31.view_all_items31, name='view_all_items31'),
    path('create_new_item31/', accounts31.create_new_item31, name='create_new_item31'),
    path('regi_new_item31/', accounts31.regi_new_item31, name='regi_new_item31'),
    path('delete_item31/<id>',accounts31.delete_item31,name='delete_item31'),
    path('update_item31/<id>', accounts31.update_item31, name='update_item31'),
    path('view_all_items_delete31/',accounts31.view_all_items_delete31,name='view_all_items_delete31'),

    path('regi_multiple_new_item31/', accounts31.regi_multiple_new_item31, name='regi_multiple_new_item31'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger31/', accounts31.view_all_ledger31, name='view_all_ledger31'),
    path('create_new_ledger31/', accounts31.create_new_ledger31, name='create_new_ledger31'),
    path('regi_new_ledger31/', accounts31.regi_new_ledger31, name='regi_new_ledger31'),
    path('delete_ledger31/<id>',accounts31.delete_ledger31,name='delete_ledger31'),
    path('update_ledger31/<id>',accounts31.update_ledger31,name='update_ledger31'),
    path('view_all_ledger_delete31/',accounts31.view_all_ledger_delete31,name='view_all_ledger_delete31'),

    path('regi_multiple_new_ledger31/', accounts31.regi_multiple_new_ledger31, name='regi_multiple_new_ledger31'),

    ##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book31/', accounts31.view_all_accounts_book31, name='view_all_accounts_book31'),
    path('create_new_accounts_book31/', accounts31.create_new_accounts_book31, name='create_new_accounts_book31'),
    path('regi_new_accounts_book31/', accounts31.regi_new_accounts_book31, name='regi_new_accounts_book31'),
    path('update_accounts_book31/<id>',accounts31.update_accounts_book31,name='update_accounts_book31'),
    path('delete_accounts_book31/<id>',accounts31.delete_accounts_book31,name='delete_accounts_book31'),
    path('view_all_accounts_book_delete31/',accounts31.view_all_accounts_book_delete31,name='view_all_accounts_book_delete31'),

    path('regi_multiple_new_accounts_book31/', accounts31.regi_multiple_new_accounts_book31,name='regi_multiple_new_accounts_book31'),

    ##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries31/', accounts31.get_countries31, name='get_countries31'),

    path('in_exp_items_entry31/', accounts31.in_exp_items_entry31, name='in_exp_items_entry31'),
    path('reg_in_exp_items_entry31/', accounts31.reg_in_exp_items_entry31, name='reg_in_exp_items_entry31'),
    path('delete_journal31/<id>',accounts31.delete_journal31,name='delete_journal31'),
    path('update_in_exp_items_entry31/<id>',accounts31.update_in_exp_items_entry31,name='update_in_exp_items_entry31'),
    path('detailed_journal_report31/',accounts31.detailed_journal_report31,name='detailed_journal_report31'),
    path('journal_report_deleted31/',accounts31.journal_report_deleted31,name='journal_report_deleted31'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise31/', accounts31.daily_category_wise31, name='daily_category_wise31'),
    path('monthly_category_based_reports31/',accounts31.monthly_category_based_reports31,name='monthly_category_based_reports31'),
    path('yearly_category_based_reports31/', accounts31.yearly_category_based_reports31,name='yearly_category_based_reports31'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed31/', accounts31.daily_detailed31, name='daily_detailed31'),
    path('monthly_detailed31/',accounts31.monthly_detailed31,name='monthly_detailed31'),
    path('yearly_detailed31/',accounts31.yearly_detailed31,name='yearly_detailed31'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports31/', accounts31.item_based_reports31, name='item_based_reports31'),
    path('daily_item_based_reports31/',accounts31.daily_item_based_reports31,name='daily_item_based_reports31'),
    path('monthly_item_based_reports31/',accounts31.monthly_item_based_reports31,name='monthly_item_based_reports31'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports31/', accounts31.ledger_based_reports31, name='ledger_based_reports31'),
    path('monthly_ledger_based_reports31/', accounts31.monthly_ledger_based_reports31, name='monthly_ledger_based_reports31'),
    path('daily_ledger_based_reports31/',accounts31.daily_ledger_based_reports31,name='daily_ledger_based_reports31'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports31/', accounts31.accounts_book_based_reports31, name='accounts_book_based_reports31'),
    path('daily_accounts_book_based_reports31/',accounts31.daily_accounts_book_based_reports31,name='daily_accounts_book_based_reports31'),
    path('monthly_accounts_book_based_reports31/',accounts31.monthly_accounts_book_based_reports31,name='monthly_accounts_book_based_reports31'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months31/', accounts31.monthly_reports_choose_months31, name='monthly_reports_choose_months31'),
    path('monthly_detailed_daily_in_exp_items_report31/<mo>',accounts31.monthly_detailed_daily_in_exp_items_report31,name='monthly_detailed_daily_in_exp_items_report31'),

    path('single_monthly_reports_choose_months31/', accounts31.single_monthly_reports_choose_months31,name='single_monthly_reports_choose_months31'),
    path('single_monthly_daily_in_exp_items_report31/<mo>',accounts31.single_monthly_daily_in_exp_items_report31,name='single_monthly_daily_in_exp_items_report31'),

    path('accounts_dash_board_ob_ch31/',accounts31.accounts_dash_board_ob_ch31,name='accounts_dash_board_ob_ch31'),
    path('accounts_dash_board31/',accounts31.accounts_dash_board31,name='accounts_dash_board31'),

    path('profit_sharing_choose_months31', accounts31.profit_sharing_choose_months31,name='profit_sharing_choose_months31'),
    path('profit_sharing31/<mo>', accounts31.profit_sharing31, name='profit_sharing31'),
    path('view_share_holders31', accounts31.view_share_holders31, name='view_share_holders31'),
    path('create_share_holders31', accounts31.create_share_holders31, name='create_share_holders31'),
    path('regi_share_holders31', accounts31.regi_share_holders31, name='regi_share_holders31'),
    path('update_share_holders31/<id>', accounts31.update_share_holders31, name='update_share_holders31'),
    path('delete_share_holders31/<id>', accounts31.delete_share_holders31, name='delete_share_holders31'),
    path('view_deleted_share_holders31', accounts31.view_deleted_share_holders31, name='view_deleted_share_holders31'),

    path('regi_multiple_share_holders31', accounts31.regi_multiple_share_holders31, name='regi_multiple_share_holders31'),

    #############BRANCH SETTINGS START HERE ########################

    path('guest_rent_update_ob_ch31/', branch_settings31.guest_rent_update_ob_ch31, name='guest_rent_update_ob_ch31'),

    ############BRANCH SETTINGS END HERE ############################

]

