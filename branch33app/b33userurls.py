from django.urls import path, include

from . import admin_branch33
from . import admin_branch33
from . import branch33
from . import reports33
from . import payment33
from . import admin_dashboard_calculations_br33
from . import accounts33
from . import branch_settings33

urlpatterns = [

    path('branch1_dashboard_ob_ch33/', branch33.branch1_dashboard_ob_ch33, name='branch1_dashboard_ob_ch33'),
    path('branch1_dashboard33/',branch33.branch1_dashboard33,name='branch1_dashboard33'),
    path('user_dashboard_calculations_ob_ch33/',branch33.user_dashboard_calculations_ob_ch33,name='user_dashboard_calculations_ob_ch33'),

    path('background_ob_ch33',branch33.background_ob_ch33,name='background_ob_ch33'),
    path('background_regi_ob_ch33',branch33.background_regi_ob_ch33,name='background_regi_ob_ch33'),
    path('custom_background_regi_ob_ch33',branch33.custom_background_regi_ob_ch33,name='custom_background_regi_ob_ch33'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch33/',admin_branch33.branch1_room_create_regi_ob_ch33,name='branch1_room_create_regi_ob_ch33'),
    path('view_all_room_ob_ch33/',admin_branch33.view_all_room_ob_ch33,name='view_all_room_ob_ch33'),
    path('delete_room_ob_ch33/<id>',admin_branch33.delete_room_ob_ch33,name='delete_room_ob_ch33'),

    path('branch1_room_create_ob_ch33/',admin_branch33.branch1_room_create_ob_ch33,name='branch1_room_create_ob_ch33'),

    path('multiple_branch1_room_create_regi33/',admin_branch33.multiple_branch1_room_create_regi33,name='multiple_branch1_room_create_regi33'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch33/', admin_branch33.pg1_bed_create_regi_ob_ch33, name='pg1_bed_create_regi_ob_ch33'),
    path('pg1_view_all_beds_ob_ch33/', admin_branch33.pg1_view_all_beds_ob_ch33, name='pg1_view_all_beds_ob_ch33'),
    path('delete_bed_ob_ch33/<id>', admin_branch33.delete_bed_ob_ch33, name='delete_bed_ob_ch33'),

    path('pg1_bed_create_ob_ch33/', admin_branch33.pg1_bed_create_ob_ch33, name='pg1_bed_create_ob_ch33'),

    path('single_pg1_bed_create_regi_ob_ch33/',admin_branch33.single_pg1_bed_create_regi_ob_ch33,name='single_pg1_bed_create_regi_ob_ch33'),
    path('update_bed_basic_details_ob_ch33/<id>',admin_branch33.update_bed_basic_details_ob_ch33, name='update_bed_basic_details_ob_ch33'),

    path('multiple_single_pg1_bed_create_regi33/',admin_branch33.multiple_single_pg1_bed_create_regi33,name='multiple_single_pg1_bed_create_regi33'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch33/<id>',branch33.br1_admit_guest_ob_ch33,name='br1_admit_guest_ob_ch33'),
    path('view_all_new_guest_ob_ch33/',branch33.view_all_new_guest_ob_ch33,name='view_all_new_guest_ob_ch33'),
    path('update_br1_admit_guest_ob_ch33/<id>',branch33.update_br1_admit_guest_ob_ch33,name='update_br1_admit_guest_ob_ch33'),
    path('vacate_br1_guest_ob_ch33/<id>',branch33.vacate_br1_guest_ob_ch33,name='vacate_br1_guest_ob_ch33'),

    path('active_guest_details_ob_ch33/<guest_code>',branch33.active_guest_details_ob_ch33,name='active_guest_details_ob_ch33'),
    path('view_all_guest_ob_ch33/',branch33.view_all_guest_ob_ch33,name='view_all_guest_ob_ch33'),
    path('shift_guest_ob_ch33/<id>',branch33.shift_guest_ob_ch33,name='shift_guest_ob_ch33'),
    path('shift_guest_regi_ob_ch33/',branch33.shift_guest_regi_ob_ch33,name='shift_guest_regi_ob_ch33'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch33/',branch33.update_all_rent_ob_ch33,name='update_all_rent_ob_ch33'),

    path('multiple_br1_admit_guest33/<id>',branch33.multiple_br1_admit_guest33,name='multiple_br1_admit_guest33'),

#guest end here


##################################
#_ADVANCE_ob_ch33 START HERE
################################


    path('choose_months_advance_ob_ch33/',branch33.choose_months_advance_ob_ch33,name='choose_months_advance_ob_ch33'),

    path('jan_advance_ob_ch33/', branch33.jan_advance_ob_ch33, name='jan_advance_ob_ch33'),
    path('jan_make_payments_advance_ob_ch33/<id>', branch33.jan_make_payments_advance_ob_ch33,name='jan_make_payments_advance_ob_ch33'),
    path('feb_advance_ob_ch33/', branch33.feb_advance_ob_ch33, name='feb_advance_ob_ch33'),
    path('feb_make_payments_advance_ob_ch33/<id>', branch33.feb_make_payments_advance_ob_ch33,name='feb_make_payments_advance_ob_ch33'),
    path('march_advance_ob_ch33/', branch33.march_advance_ob_ch33, name='march_advance_ob_ch33'),
    path('march_make_payments_advance_ob_ch33/<id>', branch33.march_make_payments_advance_ob_ch33,name='march_make_payments_advance_ob_ch33'),
    path('april_advance_ob_ch33/', branch33.april_advance_ob_ch33, name='april_advance_ob_ch33'),
    path('april_make_payments_advance_ob_ch33/<id>', branch33.april_make_payments_advance_ob_ch33, name='april_make_payments_advance_ob_ch33'),

    path('may_advance_ob_ch33/',branch33.may_advance_ob_ch33,name='may_advance_ob_ch33'),
    path('may_make_payments_advance_ob_ch33/<id>', branch33.may_make_payments_advance_ob_ch33, name='may_make_payments_advance_ob_ch33'),
    path('june_advance_ob_ch33/',branch33.june_advance_ob_ch33,name='june_advance_ob_ch33'),
    path('june_make_payments_advance_ob_ch33/<id>', branch33.june_make_payments_advance_ob_ch33, name='june_make_payments_advance_ob_ch33'),
    path('july_advance_ob_ch33/',branch33.july_advance_ob_ch33,name='july_advance_ob_ch33'),
    path('july_make_payments_advance_ob_ch33/<id>', branch33.july_make_payments_advance_ob_ch33, name='july_make_payments_advance_ob_ch33'),
    path('auguest_advance_ob_ch33/', branch33.auguest_advance_ob_ch33, name='auguest_advance_ob_ch33'),
    path('auguest_make_payments_advance_ob_ch33/<id>', branch33.auguest_make_payments_advance_ob_ch33, name='auguest_make_payments_advance_ob_ch33'),

    path('sept_advance_ob_ch33/', branch33.sept_advance_ob_ch33, name='sept_advance_ob_ch33'),
    path('sept_make_payments_advance_ob_ch33/<id>', branch33.sept_make_payments_advance_ob_ch33,name='sept_make_payments_advance_ob_ch33'),
    path('october_advance_ob_ch33/', branch33.october_advance_ob_ch33, name='october_advance_ob_ch33'),
    path('october_make_payments_advance_ob_ch33/<id>', branch33.october_make_payments_advance_ob_ch33, name='october_make_payments_advance_ob_ch33'),
    path('nov_advance_ob_ch33/', branch33.nov_advance_ob_ch33, name='nov_advance_ob_ch33'),
    path('nov_make_payments_advance_ob_ch33/<id>', branch33.nov_make_payments_advance_ob_ch33,name='nov_make_payments_advance_ob_ch33'),
    path('dec_advance_ob_ch33/', branch33.dec_advance_ob_ch33, name='dec_advance_ob_ch33'),
    path('dec_make_payments_advance_ob_ch33/<id>', branch33.dec_make_payments_advance_ob_ch33, name='dec_make_payments_advance_ob_ch33'),



##################################
#_ADVANCE_ob_ch33 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch33/',branch33.choose_months_ob_ch33,name='choose_months_ob_ch33'),

    path('jan_ob_ch33/',branch33.jan_ob_ch33,name='jan_ob_ch33'),
    path('jan_manke_payments_ob_ch33/<id>',branch33.jan_manke_payments_ob_ch33,name='jan_manke_payments_ob_ch33'),

    path('feb_ob_ch33/',branch33.feb_ob_ch33,name='feb_ob_ch33'),
    path('feb_manke_payments_ob_ch33/<id>',branch33.feb_manke_payments_ob_ch33,name='feb_manke_payments_ob_ch33'),

    path('march_ob_ch33/',branch33.march_ob_ch33,name='march_ob_ch33'),
    path('march_manke_payments_ob_ch33/<id>',branch33.march_manke_payments_ob_ch33,name='march_manke_payments_ob_ch33'),

    path('april_ob_ch33/',branch33.april_ob_ch33,name='april_ob_ch33'),
    path('april_make_payments_ob_ch33/<id>',branch33.april_make_payments_ob_ch33,name='april_make_payments_ob_ch33'),

    path('may_ob_ch33/',branch33.may_ob_ch33,name='may_ob_ch33'),
    path('may_make_payments_ob_ch33/<id>',branch33.may_make_payments_ob_ch33,name='may_make_payments_ob_ch33'),

    path('june_ob_ch33/',branch33.june_ob_ch33,name='june_ob_ch33'),
    path('june_make_payments_ob_ch33/<id>',branch33.june_make_payments_ob_ch33,name='june_make_payments_ob_ch33'),

    path('july_ob_ch33/',branch33.july_ob_ch33,name='july_ob_ch33'),
    path('july_make_payments_ob_ch33/<id>',branch33.july_make_payments_ob_ch33,name='july_make_payments_ob_ch33'),

    path('aug_ob_ch33/',branch33.aug_ob_ch33,name='aug_ob_ch33'),
    path('aug_make_payments_ob_ch33/<id>',branch33.aug_make_payments_ob_ch33,name='aug_make_payments_ob_ch33'),

    path('sept_ob_ch33/',branch33.sept_ob_ch33,name='sept_ob_ch33'),
    path('sept_make_payments_ob_ch33/<id>',branch33.sept_make_payments_ob_ch33,name='sept_make_payments_ob_ch33'),

    path('oct_ob_ch33/',branch33.oct_ob_ch33,name='oct_ob_ch33'),
    path('oct_make_payments_ob_ch33/<id>',branch33.oct_make_payments_ob_ch33,name='oct_make_payments_ob_ch33'),

    path('nov_ob_ch33/',branch33.nov_ob_ch33,name='nov_ob_ch33'),
    path('nov_make_payments_ob_ch33/<id>',branch33.nov_make_payments_ob_ch33,name='nov_make_payments_ob_ch33'),

    path('dec_ob_ch33/',branch33.dec_ob_ch33,name='dec_ob_ch33'),
    path('dec_make_payments_ob_ch33/<id>',branch33.dec_make_payments_ob_ch33,name='dec_make_payments_ob_ch33'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch33/', payment33.choose_user_ob_ch33, name='choose_user_ob_ch33'),
    path('payment_user_details_ob_ch33/<id>', payment33.payment_user_details_ob_ch33, name='payment_user_details_ob_ch33'),
    path('close_choose_user_ob_ch33/<id>',payment33.close_choose_user_ob_ch33,name='close_choose_user_ob_ch33'),

    path('monthly_jan_make_payments_ob_ch33/<id>', payment33.monthly_jan_make_payments_ob_ch33, name='monthly_jan_make_payments_ob_ch33'),
    path('monthly_feb_make_payments_ob_ch33/<id>', payment33.monthly_feb_make_payments_ob_ch33, name='monthly_feb_make_payments_ob_ch33'),
    path('monthly_march_make_payments_ob_ch33/<id>', payment33.monthly_march_make_payments_ob_ch33, name='monthly_march_make_payments_ob_ch33'),
    path('monthly_april_make_payments_ob_ch33/<id>', payment33.monthly_april_make_payments_ob_ch33, name='monthly_april_make_payments_ob_ch33'),
    path('monthly_may_make_payments_ob_ch33/<id>', payment33.monthly_may_make_payments_ob_ch33, name='monthly_may_make_payments_ob_ch33'),
    path('monthly_june_make_payments_ob_ch33/<id>', payment33.monthly_june_make_payments_ob_ch33, name='monthly_june_make_payments_ob_ch33'),

    path('monthly_july_make_payments_ob_ch33/<id>', payment33.monthly_july_make_payments_ob_ch33, name='monthly_july_make_payments_ob_ch33'),
    path('monthly_aug_make_payments_ob_ch33/<id>', payment33.monthly_aug_make_payments_ob_ch33, name='monthly_aug_make_payments_ob_ch33'),
    path('monthly_sept_make_payments_ob_ch33/<id>', payment33.monthly_sept_make_payments_ob_ch33, name='monthly_sept_make_payments_ob_ch33'),
    path('monthly_oct_make_payments_ob_ch33/<id>', payment33.monthly_oct_make_payments_ob_ch33, name='monthly_oct_make_payments_ob_ch33'),
    path('monthly_nov_make_payments_ob_ch33/<id>', payment33.monthly_nov_make_payments_ob_ch33, name='monthly_nov_make_payments_ob_ch33'),
    path('monthly_dec_make_payments_ob_ch33/<id>', payment33.monthly_dec_make_payments_ob_ch33, name='monthly_dec_make_payments_ob_ch33'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch33/',branch33.unpaid_rent_choose_months_ob_ch33,name='unpaid_rent_choose_months_ob_ch33'),

    path('jan_unpaid_rent_ob_ch33/', branch33.jan_unpaid_rent_ob_ch33, name='jan_unpaid_rent_ob_ch33'),
    path('table_jan_unpaid_rent_ob_ch33/', branch33.table_jan_unpaid_rent_ob_ch33, name='table_jan_unpaid_rent_ob_ch33'),
    path('feb_unpaid_rent_ob_ch33/', branch33.feb_unpaid_rent_ob_ch33, name='feb_unpaid_rent_ob_ch33'),
    path('table_feb_unpaid_rent_ob_ch33/', branch33.table_feb_unpaid_rent_ob_ch33, name='table_feb_unpaid_rent_ob_ch33'),
    path('mar_unpaid_rent_ob_ch33/', branch33.mar_unpaid_rent_ob_ch33, name='mar_unpaid_rent_ob_ch33'),
    path('table_mar_unpaid_rent_ob_ch33/', branch33.table_mar_unpaid_rent_ob_ch33, name='table_mar_unpaid_rent_ob_ch33'),
    path('april_unpaid_rent_ob_ch33/', branch33.april_unpaid_rent_ob_ch33, name='april_unpaid_rent_ob_ch33'),
    path('table_april_unpaid_rent_ob_ch33/', branch33.table_april_unpaid_rent_ob_ch33, name='table_april_unpaid_rent_ob_ch33'),

    path('may_unpaid_rent_ob_ch33/', branch33.may_unpaid_rent_ob_ch33, name='may_unpaid_rent_ob_ch33'),
    path('table_may_unpaid_rent_ob_ch33/', branch33.table_may_unpaid_rent_ob_ch33, name='table_may_unpaid_rent_ob_ch33'),
    path('june_unpaid_rent_ob_ch33/', branch33.june_unpaid_rent_ob_ch33, name='june_unpaid_rent_ob_ch33'),
    path('table_june_unpaid_rent_ob_ch33/', branch33.table_june_unpaid_rent_ob_ch33, name='table_june_unpaid_rent_ob_ch33'),
    path('july_unpaid_rent_ob_ch33/', branch33.july_unpaid_rent_ob_ch33, name='july_unpaid_rent_ob_ch33'),
    path('table_july_unpaid_rent_ob_ch33',branch33.table_july_unpaid_rent_ob_ch33,name='table_july_unpaid_rent_ob_ch33'),
    path('aug_unpaid_rent_ob_ch33/', branch33.aug_unpaid_rent_ob_ch33, name='aug_unpaid_rent_ob_ch33'),
    path('table_aug_unpaid_rent_ob_ch33/',branch33.table_aug_unpaid_rent_ob_ch33,name='table_aug_unpaid_rent_ob_ch33'),

    path('sept_unpaid_rent_ob_ch33/', branch33.sept_unpaid_rent_ob_ch33, name='sept_unpaid_rent_ob_ch33'),
    path('table_sept_unpaid_rent_ob_ch33/', branch33.table_sept_unpaid_rent_ob_ch33, name='table_sept_unpaid_rent_ob_ch33'),
    path('oct_unpaid_rent_ob_ch33/', branch33.oct_unpaid_rent_ob_ch33, name='oct_unpaid_rent_ob_ch33'),
    path('table_oct_unpaid_rent_ob_ch33/', branch33.table_oct_unpaid_rent_ob_ch33, name='table_oct_unpaid_rent_ob_ch33'),
    path('nov_unpaid_rent_ob_ch33/', branch33.nov_unpaid_rent_ob_ch33, name='nov_unpaid_rent_ob_ch33'),
    path('table_nov_unpaid_rent_ob_ch33/', branch33.table_nov_unpaid_rent_ob_ch33, name='table_nov_unpaid_rent_ob_ch33'),
    path('dec_unpaid_rent_ob_ch33/', branch33.dec_unpaid_rent_ob_ch33, name='dec_unpaid_rent_ob_ch33'),
    path('table_dec_unpaid_rent_ob_ch33/', branch33.table_dec_unpaid_rent_ob_ch33, name='table_dec_unpaid_rent_ob_ch33'),

    path('details_of_unpaid_guests_ob_ch33/<id>',branch33.details_of_unpaid_guests_ob_ch33,name='details_of_unpaid_guests_ob_ch33'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch33/',branch33.paid_rent_choose_months_ob_ch33,name='paid_rent_choose_months_ob_ch33'),
    path('partially_paid_guest_choose_months_ob_ch33/',reports33.partially_paid_guest_choose_months_ob_ch33,name='partially_paid_guest_choose_months_ob_ch33'),

    path('jan_paid_rent_ob_ch33/', branch33.jan_paid_rent_ob_ch33, name='jan_paid_rent_ob_ch33'),
    path('table_jan_paid_rent_ob_ch33/', branch33.table_jan_paid_rent_ob_ch33, name='table_jan_paid_rent_ob_ch33'),
    path('jan_full_paid_guest_ob_ch33/', reports33.jan_full_paid_guest_ob_ch33, name='jan_full_paid_guest_ob_ch33'),
    path('jan_partially_paid_guest_ob_ch33/', reports33.jan_partially_paid_guest_ob_ch33, name='jan_partially_paid_guest_ob_ch33'),
    path('table_jan_partially_paid_guest_ob_ch33/', reports33.table_jan_partially_paid_guest_ob_ch33,name='table_jan_partially_paid_guest_ob_ch33'),

    path('feb_paid_rent_ob_ch33/', branch33.feb_paid_rent_ob_ch33, name='feb_paid_rent_ob_ch33'),
    path('table_feb_paid_rent_ob_ch33/', branch33.table_feb_paid_rent_ob_ch33, name='table_feb_paid_rent_ob_ch33'),
    path('feb_full_paid_guest_ob_ch33/', reports33.feb_full_paid_guest_ob_ch33, name='feb_full_paid_guest_ob_ch33'),
    path('feb_partially_paid_guest_ob_ch33/', reports33.feb_partially_paid_guest_ob_ch33, name='feb_partially_paid_guest_ob_ch33'),
    path('table_feb_partially_paid_guest_ob_ch33/', reports33.table_feb_partially_paid_guest_ob_ch33,name='table_feb_partially_paid_guest_ob_ch33'),

    path('mar_paid_rent_ob_ch33/', branch33.mar_paid_rent_ob_ch33, name='mar_paid_rent_ob_ch33'),
    path('table_mar_paid_rent_ob_ch33/', branch33.table_mar_paid_rent_ob_ch33, name='table_mar_paid_rent_ob_ch33'),
    path('march_full_paid_guest_ob_ch33/', reports33.march_full_paid_guest_ob_ch33, name='march_full_paid_guest_ob_ch33'),
    path('march_partially_paid_guest_ob_ch33/', reports33.march_partially_paid_guest_ob_ch33, name='march_partially_paid_guest_ob_ch33'),
    path('table_march_partially_paid_guest_ob_ch33/', reports33.table_march_partially_paid_guest_ob_ch33,name='table_march_partially_paid_guest_ob_ch33'),

    path('april_paid_rent_ob_ch33/', branch33.april_paid_rent_ob_ch33, name='april_paid_rent_ob_ch33'),
    path('table_april_paid_rent_ob_ch33/', branch33.table_april_paid_rent_ob_ch33, name='table_april_paid_rent_ob_ch33'),
    path('april_full_paid_guest_ob_ch33/', reports33.april_full_paid_guest_ob_ch33, name='april_full_paid_guest_ob_ch33'),
    path('april_partially_paid_guest_ob_ch33/', reports33.april_partially_paid_guest_ob_ch33, name='april_partially_paid_guest_ob_ch33'),
    path('table_april_partially_paid_guest_ob_ch33/', reports33.table_april_partially_paid_guest_ob_ch33,name='table_april_partially_paid_guest_ob_ch33'),

    path('may_paid_rent_ob_ch33/', branch33.may_paid_rent_ob_ch33, name='may_paid_rent_ob_ch33'),
    path('table_may_paid_rent_ob_ch33/', branch33.table_may_paid_rent_ob_ch33, name='table_may_paid_rent_ob_ch33'),
    path('may_full_paid_guest_ob_ch33/', reports33.may_full_paid_guest_ob_ch33, name='may_full_paid_guest_ob_ch33'),
    path('may_partially_paid_guest_ob_ch33/', reports33.may_partially_paid_guest_ob_ch33, name='may_partially_paid_guest_ob_ch33'),
    path('table_may_partially_paid_guest_ob_ch33/', reports33.table_may_partially_paid_guest_ob_ch33, name='table_may_partially_paid_guest_ob_ch33'),

    path('june_paid_rent_ob_ch33/', branch33.june_paid_rent_ob_ch33, name='june_paid_rent_ob_ch33'),
    path('table_june_paid_rent_ob_ch33/', branch33.table_june_paid_rent_ob_ch33, name='table_june_paid_rent_ob_ch33'),
    path('june_full_paid_guest_ob_ch33/', reports33.june_full_paid_guest_ob_ch33, name='june_full_paid_guest_ob_ch33'),
    path('june_partially_paid_guest_ob_ch33/', reports33.june_partially_paid_guest_ob_ch33, name='june_partially_paid_guest_ob_ch33'),
    path('table_june_partially_paid_guest_ob_ch33/', reports33.table_june_partially_paid_guest_ob_ch33, name='table_june_partially_paid_guest_ob_ch33'),

    path('july_paid_rent_ob_ch33/', branch33.july_paid_rent_ob_ch33, name='july_paid_rent_ob_ch33'),
    path('table_july_paid_rent_ob_ch33/', branch33.table_july_paid_rent_ob_ch33, name='table_july_paid_rent_ob_ch33'),
    path('july_full_paid_guest_ob_ch33/', reports33.july_full_paid_guest_ob_ch33, name='july_full_paid_guest_ob_ch33'),
    path('july_partially_paid_guest_ob_ch33/', reports33.july_partially_paid_guest_ob_ch33, name='july_partially_paid_guest_ob_ch33'),
    path('table_july_partially_paid_guest_ob_ch33/', reports33.table_july_partially_paid_guest_ob_ch33, name='table_july_partially_paid_guest_ob_ch33'),

    path('aug_paid_rent_ob_ch33/', branch33.aug_paid_rent_ob_ch33, name='aug_paid_rent_ob_ch33'),
    path('table_aug_paid_rent_ob_ch33/', branch33.table_aug_paid_rent_ob_ch33, name='table_aug_paid_rent_ob_ch33'),
    path('auguest_full_paid_guest_ob_ch33/', reports33.auguest_full_paid_guest_ob_ch33, name='auguest_full_paid_guest_ob_ch33'),
    path('auguest_partially_paid_guest_ob_ch33/', reports33.auguest_partially_paid_guest_ob_ch33,name='auguest_partially_paid_guest_ob_ch33'),
    path('table_auguest_partially_paid_guest_ob_ch33/', reports33.table_auguest_partially_paid_guest_ob_ch33,name='table_auguest_partially_paid_guest_ob_ch33'),

    path('sept_paid_rent_ob_ch33/', branch33.sept_paid_rent_ob_ch33, name='sept_paid_rent_ob_ch33'),
    path('table_sept_paid_rent_ob_ch33/', branch33.table_sept_paid_rent_ob_ch33, name='table_sept_paid_rent_ob_ch33'),
    path('sept_full_paid_guest_ob_ch33/', reports33.sept_full_paid_guest_ob_ch33, name='sept_full_paid_guest_ob_ch33'),
    path('sept_partially_paid_guest_ob_ch33/', reports33.sept_partially_paid_guest_ob_ch33, name='sept_partially_paid_guest_ob_ch33'),
    path('table_sept_partially_paid_guest_ob_ch33/', reports33.table_sept_partially_paid_guest_ob_ch33,name='table_sept_partially_paid_guest_ob_ch33'),

    path('oct_paid_rent_ob_ch33/', branch33.oct_paid_rent_ob_ch33, name='oct_paid_rent_ob_ch33'),
    path('table_oct_paid_rent_ob_ch33/', branch33.table_oct_paid_rent_ob_ch33, name='table_oct_paid_rent_ob_ch33'),
    path('october_full_paid_guest_ob_ch33/', reports33.october_full_paid_guest_ob_ch33, name='october_full_paid_guest_ob_ch33'),
    path('october_partially_paid_guest_ob_ch33/', reports33.october_partially_paid_guest_ob_ch33,name='october_partially_paid_guest_ob_ch33'),
    path('table_october_partially_paid_guest_ob_ch33/', reports33.table_october_partially_paid_guest_ob_ch33,name='table_october_partially_paid_guest_ob_ch33'),

    path('nov_paid_rent_ob_ch33/', branch33.nov_paid_rent_ob_ch33, name='nov_paid_rent_ob_ch33'),
    path('table_nov_paid_rent_ob_ch33/', branch33.table_nov_paid_rent_ob_ch33, name='table_nov_paid_rent_ob_ch33'),
    path('nov_full_paid_guest_ob_ch33/', reports33.nov_full_paid_guest_ob_ch33, name='nov_full_paid_guest_ob_ch33'),
    path('nov_partially_paid_guest_ob_ch33/', reports33.nov_partially_paid_guest_ob_ch33, name='nov_partially_paid_guest_ob_ch33'),
    path('table_nov_partially_paid_guest_ob_ch33/', reports33.table_nov_partially_paid_guest_ob_ch33,name='table_nov_partially_paid_guest_ob_ch33'),

    path('dec_paid_rent_ob_ch33/', branch33.dec_paid_rent_ob_ch33, name='dec_paid_rent_ob_ch33'),
    path('table_dec_paid_rent_ob_ch33/', branch33.table_dec_paid_rent_ob_ch33, name='table_dec_paid_rent_ob_ch33'),
    path('dec_full_paid_guest_ob_ch33/', reports33.dec_full_paid_guest_ob_ch33, name='dec_full_paid_guest_ob_ch33'),
    path('dec_partially_paid_guest_ob_ch33/', reports33.dec_partially_paid_guest_ob_ch33, name='dec_partially_paid_guest_ob_ch33'),
    path('table_dec_partially_paid_guest_ob_ch33/', reports33.table_dec_partially_paid_guest_ob_ch33,name='table_dec_partially_paid_guest_ob_ch33'),

    path('details_of_paid_guests_ob_ch33/<id>',branch33.details_of_paid_guests_ob_ch33,name='details_of_paid_guests_ob_ch33'),
    path('full_paid_guest_ob_ch33/',reports33.full_paid_guest_ob_ch33,name='full_paid_guest_ob_ch33'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch33/',branch33.viewall_vacate_guest_ob_ch33,name='viewall_vacate_guest_ob_ch33'),
    path('details_of_vacate_guest_ob_ch33/<id>',branch33.details_of_vacate_guest_ob_ch33,name='details_of_vacate_guest_ob_ch33'),
    path('full_vacated_guest_details_ob_ch33',branch33.full_vacated_guest_details_ob_ch33,name='full_vacated_guest_details_ob_ch33'),
    path('full_vacated_guest_table_ob_ch33',branch33.full_vacated_guest_table_ob_ch33,name='full_vacated_guest_table_ob_ch33'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch33/<id>', branch33.jan_manke_payments_vacate_ob_ch33, name='jan_manke_payments_vacate_ob_ch33'),
    path('feb_manke_payments_vacate_ob_ch33/<id>', branch33.feb_manke_payments_vacate_ob_ch33, name='feb_manke_payments_vacate_ob_ch33'),
    path('march_manke_payments_vacate_ob_ch33/<id>', branch33.march_manke_payments_vacate_ob_ch33, name='march_manke_payments_vacate_ob_ch33'),
    path('april_make_payments_vacate_ob_ch33/<id>', branch33.april_make_payments_vacate_ob_ch33, name='april_make_payments_vacate_ob_ch33'),

    path('may_make_payments_vacate_ob_ch33/<id>', branch33.may_make_payments_vacate_ob_ch33, name='may_make_payments_vacate_ob_ch33'),
    path('june_make_payments_vacate_ob_ch33/<id>', branch33.june_make_payments_vacate_ob_ch33, name='june_make_payments_vacate_ob_ch33'),
    path('july_make_payments_vacate_ob_ch33/<id>', branch33.july_make_payments_vacate_ob_ch33, name='july_make_payments_vacate_ob_ch33'),
    path('aug_make_payments_vacate_ob_ch33/<id>', branch33.aug_make_payments_vacate_ob_ch33, name='aug_make_payments_vacate_ob_ch33'),

    path('sept_make_payments_vacate_ob_ch33/<id>', branch33.sept_make_payments_vacate_ob_ch33, name='sept_make_payments_vacate_ob_ch33'),
    path('oct_make_payments_vacate_ob_ch33/<id>', branch33.oct_make_payments_vacate_ob_ch33, name='oct_make_payments_vacate_ob_ch33'),
    path('nov_make_payments_vacate_ob_ch33/<id>', branch33.nov_make_payments_vacate_ob_ch33, name='nov_make_payments_vacate_ob_ch33'),
    path('dec_make_payments_vacate_ob_ch33/<id>', branch33.dec_make_payments_vacate_ob_ch33, name='dec_make_payments_vacate_ob_ch33'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch33/',branch33.detail_guest_general_ob_ch33,name='detail_guest_general_ob_ch33'),

    path('jan_print_ob_ch33/',branch33.jan_print_ob_ch33,name='jan_print_ob_ch33'),
    path('feb_print_ob_ch33/',branch33.feb_print_ob_ch33,name='feb_print_ob_ch33'),
    path('march_print_ob_ch33/',branch33.march_print_ob_ch33,name='march_print_ob_ch33'),
    path('april_print_ob_ch33/',branch33.april_print_ob_ch33,name='april_print_ob_ch33'),

    path('may_print_ob_ch33/',branch33.may_print_ob_ch33,name='may_print_ob_ch33'),
    path('june_print_ob_ch33/',branch33.june_print_ob_ch33,name='june_print_ob_ch33'),
    path('july_print_ob_ch33/', branch33.july_print_ob_ch33, name='july_print_ob_ch33'),
    path('aug_print_ob_ch33/', branch33.aug_print_ob_ch33, name='aug_print_ob_ch33'),

    path('sept_print_ob_ch33/', branch33.sept_print_ob_ch33, name='sept_print_ob_ch33'),
    path('oct_print_ob_ch33/', branch33.oct_print_ob_ch33, name='oct_print_ob_ch33'),
    path('nov_print_ob_ch33/', branch33.nov_print_ob_ch33, name='nov_print_ob_ch33'),
    path('dec_print_ob_ch33/', branch33.dec_print_ob_ch33, name='dec_print_ob_ch33'),

    path('new_year_jan_print_ob_ch33/', branch33.new_year_jan_print_ob_ch33, name='new_year_jan_print_ob_ch33'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch33/', branch33.jan_close_ob_ch33, name='jan_close_ob_ch33'),
    path('jan_close_decision_page_ob_ch33/', branch33.jan_close_decision_page_ob_ch33, name='jan_close_decision_page_ob_ch33'),
    path('feb_close/', branch33.feb_close_ob_ch33, name='feb_close_ob_ch33'),
    path('feb_close_decision_page_ob_ch33/', branch33.feb_close_decision_page_ob_ch33, name='feb_close_decision_page_ob_ch33'),
    path('mar_close_ob_ch33/', branch33.mar_close_ob_ch33, name='mar_close_ob_ch33'),
    path('mar_close_decision_page/', branch33.mar_close_decision_page_ob_ch33, name='mar_close_decision_page_ob_ch33'),
    path('apr_close_ob_ch33/', branch33.apr_close_ob_ch33, name='apr_close_ob_ch33'),
    path('apr_close_decision_page_ob_ch33/', branch33.apr_close_decision_page_ob_ch33, name='apr_close_decision_page_ob_ch33'),

    path('may_close_ob_ch33/', branch33.may_close_ob_ch33, name='may_close_ob_ch33'),
    path('may_close_decision_page_ob_ch33/', branch33.may_close_decision_page_ob_ch33, name='may_close_decision_page_ob_ch33'),
    path('jun_close_ob_ch33/', branch33.jun_close_ob_ch33, name='jun_close_ob_ch33'),
    path('jun_close_decision_page_ob_ch33/', branch33.jun_close_decision_page_ob_ch33, name='jun_close_decision_page_ob_ch33'),
    path('jul_close_ob_ch33/', branch33.jul_close_ob_ch33, name='jul_close_ob_ch33'),
    path('jul_close_decision_page_ob_ch33/', branch33.jul_close_decision_page_ob_ch33, name='jul_close_decision_page_ob_ch33'),
    path('aug_close_ob_ch33/', branch33.aug_close_ob_ch33, name='aug_close_ob_ch33'),
    path('aug_close_decision_page_ob_ch33/', branch33.aug_close_decision_page_ob_ch33, name='aug_close_decision_page_ob_ch33'),

    path('sep_close_ob_ch33/', branch33.sep_close_ob_ch33, name='sep_close_ob_ch33'),
    path('sep_close_decision_page_ob_ch33/', branch33.sep_close_decision_page_ob_ch33, name='sep_close_decision_page_ob_ch33'),
    path('oct_close_ob_ch33/', branch33.oct_close_ob_ch33, name='oct_close_ob_ch33'),
    path('oct_close_decision_page_ob_ch33/', branch33.oct_close_decision_page_ob_ch33, name='oct_close_decision_page_ob_ch33'),
    path('nov_close_ob_ch33/', branch33.nov_close_ob_ch33, name='nov_close_ob_ch33'),
    path('nov_close_decision_page_ob_ch33/', branch33.nov_close_decision_page_ob_ch33, name='nov_close_decision_page_ob_ch33'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch33/',reports33.detailed_report_choose_months_ob_ch33,name='detailed_report_choose_months_ob_ch33'),

    path('jan_details_live_ob_ch33/', reports33.jan_details_live_ob_ch33, name='jan_details_live_ob_ch33'),
    path('jan_print_live_ob_ch33/', reports33.jan_print_live_ob_ch33, name='jan_print_live_ob_ch33'),
    path('feb_details_live_ob_ch33/', reports33.feb_details_live_ob_ch33, name='feb_details_live_ob_ch33'),
    path('feb_print_live_ob_ch33/', reports33.feb_print_live_ob_ch33, name='feb_print_live_ob_ch33'),
    path('march_details_live_ob_ch33/', reports33.march_details_live_ob_ch33, name='march_details_live_ob_ch33'),
    path('march_print_live_ob_ch33/', reports33.march_print_live_ob_ch33, name='march_print_live_ob_ch33'),

    path('april_details_live_ob_ch33/', reports33.april_details_live_ob_ch33, name='april_details_live_ob_ch33'),
    path('april_print_live_ob_ch33/', reports33.april_print_live_ob_ch33, name='april_print_live_ob_ch33'),
    path('may_details_live_ob_ch33/', reports33.may_details_live_ob_ch33, name='may_details_live_ob_ch33'),
    path('may_print_live_ob_ch33/', reports33.may_print_live_ob_ch33, name='may_print_live_ob_ch33'),
    path('june_details_live_ob_ch33/',reports33.june_details_live_ob_ch33,name='june_details_live_ob_ch33'),
    path('june_print_live_ob_ch33/', reports33.june_print_live_ob_ch33, name='june_print_live_ob_ch33'),

    path('july_details_live_ob_ch33/', reports33.july_details_live_ob_ch33, name='july_details_live_ob_ch33'),
    path('july_print_live_ob_ch33/', reports33.july_print_live_ob_ch33, name='july_print_live_ob_ch33'),
    path('auguest_details_live_ob_ch33/', reports33.auguest_details_live_ob_ch33, name='auguest_details_live_ob_ch33'),
    path('auguest_print_live_ob_ch33/', reports33.auguest_print_live_ob_ch33, name='auguest_print_live_ob_ch33'),
    path('sept_details_live_ob_ch33/', reports33.sept_details_live_ob_ch33, name='sept_details_live_ob_ch33'),
    path('sept_print_live_ob_ch33/', reports33.sept_print_live_ob_ch33, name='sept_print_live_ob_ch33'),

    path('october_details_live_ob_ch33/', reports33.october_details_live_ob_ch33, name='october_details_live_ob_ch33'),
    path('october_print_live_ob_ch33/', reports33.october_print_live_ob_ch33, name='october_print_live_ob_ch33'),
    path('nov_details_live_ob_ch33/', reports33.nov_details_live_ob_ch33, name='nov_details_live_ob_ch33'),
    path('nov_print_live_ob_ch33/', reports33.nov_print_live_ob_ch33, name='nov_print_live_ob_ch33'),
    path('dec_details_live_ob_ch33/', reports33.dec_details_live_ob_ch33, name='dec_details_live_ob_ch33'),
    path('dec_print_live_ob_ch33/', reports33.dec_print_live_ob_ch33, name='dec_print_live_ob_ch33'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch33/', reports33.viewall_vaccant_room_ob_ch33, name='viewall_vaccant_room_ob_ch33'),

    path('d_ob_ch33/', branch33.dynamic, name='dynamic'),

    path('manage_bed_ob_ch33/', branch33.manage_bed_ob_ch33, name='manage_bed_ob_ch33'),
    path('manage_new_guest_ob_ch33/', branch33.manage_new_guest_ob_ch33, name='manage_new_guest_ob_ch33'),
    path('manage_update_new_guest_ob_ch33/<id>', branch33.manage_update_new_guest_ob_ch33, name='manage_update_new_guest_ob_ch33'),
    path('manage_update_beds_ob_ch33/<id>', branch33.manage_update_beds_ob_ch33, name='manage_update_beds_ob_ch33'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch33/', branch33.view_all_due_amt_ob_ch33, name='view_all_due_amt_ob_ch33'),
    path('due_amt_mgt_choose_months_ob_ch33/', branch33.due_amt_mgt_choose_months_ob_ch33, name='due_amt_mgt_choose_months_ob_ch33'),

    path('view_jan_account_details_ob_ch33/', branch33.view_jan_account_details_ob_ch33, name='view_jan_account_details_ob_ch33'),
    path('jan_account_mgt_ob_ch33/<id>',branch33.jan_account_mgt_ob_ch33,name='jan_account_mgt_ob_ch33'),
    path('view_feb_account_details_ob_ch33/', branch33.view_feb_account_details_ob_ch33, name='view_feb_account_details_ob_ch33'),
    path('feb_account_mgt_ob_ch33/<id>',branch33.feb_account_mgt_ob_ch33,name='feb_account_mgt_ob_ch33'),
    path('view_march_account_details_ob_ch33/', branch33.view_march_account_details_ob_ch33, name='view_march_account_details_ob_ch33'),
    path('march_account_mgt_ob_ch33/<id>',branch33.march_account_mgt_ob_ch33,name='march_account_mgt_ob_ch33'),
    path('view_april_account_details_ob_ch33/', branch33.view_april_account_details_ob_ch33, name='view_april_account_details_ob_ch33'),
    path('april_account_mgt_ob_ch33/<id>',branch33.april_account_mgt_ob_ch33,name='april_account_mgt_ob_ch33'),

    path('view_may_account_details_ob_ch33/',branch33.view_may_account_details_ob_ch33,name='view_may_account_details_ob_ch33'),
    path('may_account_mgt_ob_ch33/<id>', branch33.may_account_mgt_ob_ch33, name='may_account_mgt_ob_ch33'),
    path('view_june_account_details_ob_ch33/', branch33.view_june_account_details_ob_ch33, name='view_june_account_details_ob_ch33'),
    path('june_account_mgt_ob_ch33/<id>',branch33.june_account_mgt_ob_ch33,name='june_account_mgt_ob_ch33'),
    path('view_july_account_details_ob_ch33/', branch33.view_july_account_details_ob_ch33, name='view_july_account_details_ob_ch33'),
    path('july_account_mgt_ob_ch33/<id>',branch33.july_account_mgt_ob_ch33,name='july_account_mgt_ob_ch33'),
    path('view_auguest_account_details_ob_ch33/', branch33.view_auguest_account_details_ob_ch33, name='view_auguest_account_details_ob_ch33'),
    path('auguest_account_mgt_ob_ch33/<id>',branch33.auguest_account_mgt_ob_ch33,name='auguest_account_mgt_ob_ch33'),

    path('view_sept_account_details_ob_ch33/', branch33.view_sept_account_details_ob_ch33, name='view_sept_account_details_ob_ch33'),
    path('sept_account_mgt_ob_ch33/<id>',branch33.sept_account_mgt_ob_ch33,name='sept_account_mgt_ob_ch33'),
    path('view_october_account_details_ob_ch33/', branch33.view_october_account_details_ob_ch33, name='view_october_account_details_ob_ch33'),
    path('october_account_mgt_ob_ch33/<id>',branch33.october_account_mgt_ob_ch33,name='october_account_mgt_ob_ch33'),
    path('view_nov_account_details_ob_ch33/', branch33.view_nov_account_details_ob_ch33, name='view_nov_account_details_ob_ch33'),
    path('nov_account_mgt_ob_ch33/<id>',branch33.nov_account_mgt_ob_ch33,name='nov_account_mgt_ob_ch33'),
    path('view_dec_account_details_ob_ch33/', branch33.view_dec_account_details_ob_ch33, name='view_dec_account_details_ob_ch33'),
    path('dec_account_mgt_ob_ch33/<id>',branch33.dec_account_mgt_ob_ch33,name='dec_account_mgt_ob_ch33'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch33', admin_dashboard_calculations_br33.monthly_details_due_ob_ch33, name='monthly_details_due_ob_ch33'),
    path('monthly_collection_details_ob_ch33/', admin_dashboard_calculations_br33.monthly_collection_details_ob_ch33, name='monthly_collection_details_ob_ch33'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch33/',branch33.guest_all_ob_ch33,name='guest_all_ob_ch33'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category33/', accounts33.view_all_category33, name='view_all_category33'),
    path('create_new_category33/', accounts33.create_new_category33, name='create_new_category33'),
    path('regi_new_category33/', accounts33.regi_new_category33, name='regi_new_category33'),
    path('update_category33/<id>',accounts33.update_category33,name='update_category33'),

    path('delete_category33/<id>', accounts33.delete_category33, name='delete_category33'),
    path('view_all_category_delete33/', accounts33.view_all_category_delete33, name='view_all_category_delete33'),

    path('regi_multiple_new_category33/', accounts33.regi_multiple_new_category33, name='regi_multiple_new_category33'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items33/', accounts33.view_all_items33, name='view_all_items33'),
    path('create_new_item33/', accounts33.create_new_item33, name='create_new_item33'),
    path('regi_new_item33/', accounts33.regi_new_item33, name='regi_new_item33'),
    path('delete_item33/<id>',accounts33.delete_item33,name='delete_item33'),
    path('update_item33/<id>', accounts33.update_item33, name='update_item33'),
    path('view_all_items_delete33/',accounts33.view_all_items_delete33,name='view_all_items_delete33'),

    path('regi_multiple_new_item33/', accounts33.regi_multiple_new_item33, name='regi_multiple_new_item33'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger33/', accounts33.view_all_ledger33, name='view_all_ledger33'),
    path('create_new_ledger33/', accounts33.create_new_ledger33, name='create_new_ledger33'),
    path('regi_new_ledger33/', accounts33.regi_new_ledger33, name='regi_new_ledger33'),
    path('delete_ledger33/<id>',accounts33.delete_ledger33,name='delete_ledger33'),
    path('update_ledger33/<id>',accounts33.update_ledger33,name='update_ledger33'),
    path('view_all_ledger_delete33/',accounts33.view_all_ledger_delete33,name='view_all_ledger_delete33'),

    path('regi_multiple_new_ledger33/', accounts33.regi_multiple_new_ledger33, name='regi_multiple_new_ledger33'),

    ##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book33/', accounts33.view_all_accounts_book33, name='view_all_accounts_book33'),
    path('create_new_accounts_book33/', accounts33.create_new_accounts_book33, name='create_new_accounts_book33'),
    path('regi_new_accounts_book33/', accounts33.regi_new_accounts_book33, name='regi_new_accounts_book33'),
    path('update_accounts_book33/<id>',accounts33.update_accounts_book33,name='update_accounts_book33'),
    path('delete_accounts_book33/<id>',accounts33.delete_accounts_book33,name='delete_accounts_book33'),
    path('view_all_accounts_book_delete33/',accounts33.view_all_accounts_book_delete33,name='view_all_accounts_book_delete33'),

    path('regi_multiple_new_accounts_book33/', accounts33.regi_multiple_new_accounts_book33,name='regi_multiple_new_accounts_book33'),

    ##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries33/', accounts33.get_countries33, name='get_countries33'),

    path('in_exp_items_entry33/', accounts33.in_exp_items_entry33, name='in_exp_items_entry33'),
    path('reg_in_exp_items_entry33/', accounts33.reg_in_exp_items_entry33, name='reg_in_exp_items_entry33'),
    path('delete_journal33/<id>',accounts33.delete_journal33,name='delete_journal33'),
    path('update_in_exp_items_entry33/<id>',accounts33.update_in_exp_items_entry33,name='update_in_exp_items_entry33'),
    path('detailed_journal_report33/',accounts33.detailed_journal_report33,name='detailed_journal_report33'),
    path('journal_report_deleted33/',accounts33.journal_report_deleted33,name='journal_report_deleted33'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise33/', accounts33.daily_category_wise33, name='daily_category_wise33'),
    path('monthly_category_based_reports33/',accounts33.monthly_category_based_reports33,name='monthly_category_based_reports33'),
    path('yearly_category_based_reports33/', accounts33.yearly_category_based_reports33,name='yearly_category_based_reports33'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed33/', accounts33.daily_detailed33, name='daily_detailed33'),
    path('monthly_detailed33/',accounts33.monthly_detailed33,name='monthly_detailed33'),
    path('yearly_detailed33/',accounts33.yearly_detailed33,name='yearly_detailed33'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports33/', accounts33.item_based_reports33, name='item_based_reports33'),
    path('daily_item_based_reports33/',accounts33.daily_item_based_reports33,name='daily_item_based_reports33'),
    path('monthly_item_based_reports33/',accounts33.monthly_item_based_reports33,name='monthly_item_based_reports33'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports33/', accounts33.ledger_based_reports33, name='ledger_based_reports33'),
    path('monthly_ledger_based_reports33/', accounts33.monthly_ledger_based_reports33, name='monthly_ledger_based_reports33'),
    path('daily_ledger_based_reports33/',accounts33.daily_ledger_based_reports33,name='daily_ledger_based_reports33'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports33/', accounts33.accounts_book_based_reports33, name='accounts_book_based_reports33'),
    path('daily_accounts_book_based_reports33/',accounts33.daily_accounts_book_based_reports33,name='daily_accounts_book_based_reports33'),
    path('monthly_accounts_book_based_reports33/',accounts33.monthly_accounts_book_based_reports33,name='monthly_accounts_book_based_reports33'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months33/', accounts33.monthly_reports_choose_months33, name='monthly_reports_choose_months33'),
    path('monthly_detailed_daily_in_exp_items_report33/<mo>',accounts33.monthly_detailed_daily_in_exp_items_report33,name='monthly_detailed_daily_in_exp_items_report33'),

    path('single_monthly_reports_choose_months33/', accounts33.single_monthly_reports_choose_months33,name='single_monthly_reports_choose_months33'),
    path('single_monthly_daily_in_exp_items_report33/<mo>',accounts33.single_monthly_daily_in_exp_items_report33,name='single_monthly_daily_in_exp_items_report33'),

    path('accounts_dash_board_ob_ch33/',accounts33.accounts_dash_board_ob_ch33,name='accounts_dash_board_ob_ch33'),
    path('accounts_dash_board33/',accounts33.accounts_dash_board33,name='accounts_dash_board33'),

    path('profit_sharing_choose_months33', accounts33.profit_sharing_choose_months33,name='profit_sharing_choose_months33'),
    path('profit_sharing33/<mo>', accounts33.profit_sharing33, name='profit_sharing33'),
    path('view_share_holders33', accounts33.view_share_holders33, name='view_share_holders33'),
    path('create_share_holders33', accounts33.create_share_holders33, name='create_share_holders33'),
    path('regi_share_holders33', accounts33.regi_share_holders33, name='regi_share_holders33'),
    path('update_share_holders33/<id>', accounts33.update_share_holders33, name='update_share_holders33'),
    path('delete_share_holders33/<id>', accounts33.delete_share_holders33, name='delete_share_holders33'),
    path('view_deleted_share_holders33', accounts33.view_deleted_share_holders33, name='view_deleted_share_holders33'),

    path('regi_multiple_share_holders33', accounts33.regi_multiple_share_holders33, name='regi_multiple_share_holders33'),

    #############BRANCH SETTINGS START HERE ########################

    path('guest_rent_update_ob_ch33/', branch_settings33.guest_rent_update_ob_ch33, name='guest_rent_update_ob_ch33'),

    ############BRANCH SETTINGS END HERE ############################

]

