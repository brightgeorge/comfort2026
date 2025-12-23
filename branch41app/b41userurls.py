from django.urls import path, include

from . import admin_branch41
from . import admin_branch41
from . import branch41
from . import reports41
from . import payment41
from . import admin_dashboard_calculations_br41
from . import accounts41
from . import branch_settings41

urlpatterns = [

    path('branch1_dashboard_ob_ch41/', branch41.branch1_dashboard_ob_ch41, name='branch1_dashboard_ob_ch41'),
    path('branch1_dashboard41/',branch41.branch1_dashboard41,name='branch1_dashboard41'),
    path('user_dashboard_calculations_ob_ch41/',branch41.user_dashboard_calculations_ob_ch41,name='user_dashboard_calculations_ob_ch41'),

    path('background_ob_ch41',branch41.background_ob_ch41,name='background_ob_ch41'),
    path('background_regi_ob_ch41',branch41.background_regi_ob_ch41,name='background_regi_ob_ch41'),
    path('custom_background_regi_ob_ch41',branch41.custom_background_regi_ob_ch41,name='custom_background_regi_ob_ch41'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch41/',admin_branch41.branch1_room_create_regi_ob_ch41,name='branch1_room_create_regi_ob_ch41'),
    path('view_all_room_ob_ch41/',admin_branch41.view_all_room_ob_ch41,name='view_all_room_ob_ch41'),
    path('delete_room_ob_ch41/<id>',admin_branch41.delete_room_ob_ch41,name='delete_room_ob_ch41'),

    path('branch1_room_create_ob_ch41/',admin_branch41.branch1_room_create_ob_ch41,name='branch1_room_create_ob_ch41'),

    path('multiple_branch1_room_create_regi41/',admin_branch41.multiple_branch1_room_create_regi41,name='multiple_branch1_room_create_regi41'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch41/', admin_branch41.pg1_bed_create_regi_ob_ch41, name='pg1_bed_create_regi_ob_ch41'),
    path('pg1_view_all_beds_ob_ch41/', admin_branch41.pg1_view_all_beds_ob_ch41, name='pg1_view_all_beds_ob_ch41'),
    path('delete_bed_ob_ch41/<id>', admin_branch41.delete_bed_ob_ch41, name='delete_bed_ob_ch41'),

    path('pg1_bed_create_ob_ch41/', admin_branch41.pg1_bed_create_ob_ch41, name='pg1_bed_create_ob_ch41'),

    path('single_pg1_bed_create_regi_ob_ch41/',admin_branch41.single_pg1_bed_create_regi_ob_ch41,name='single_pg1_bed_create_regi_ob_ch41'),
    path('update_bed_basic_details_ob_ch41/<id>',admin_branch41.update_bed_basic_details_ob_ch41, name='update_bed_basic_details_ob_ch41'),

    path('multiple_single_pg1_bed_create_regi41/',admin_branch41.multiple_single_pg1_bed_create_regi41,name='multiple_single_pg1_bed_create_regi41'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch41/<id>',branch41.br1_admit_guest_ob_ch41,name='br1_admit_guest_ob_ch41'),
    path('view_all_new_guest_ob_ch41/',branch41.view_all_new_guest_ob_ch41,name='view_all_new_guest_ob_ch41'),
    path('update_br1_admit_guest_ob_ch41/<id>',branch41.update_br1_admit_guest_ob_ch41,name='update_br1_admit_guest_ob_ch41'),
    path('vacate_br1_guest_ob_ch41/<id>',branch41.vacate_br1_guest_ob_ch41,name='vacate_br1_guest_ob_ch41'),

    path('active_guest_details_ob_ch41/<guest_code>',branch41.active_guest_details_ob_ch41,name='active_guest_details_ob_ch41'),
    path('view_all_guest_ob_ch41/',branch41.view_all_guest_ob_ch41,name='view_all_guest_ob_ch41'),
    path('shift_guest_ob_ch41/<id>',branch41.shift_guest_ob_ch41,name='shift_guest_ob_ch41'),
    path('shift_guest_regi_ob_ch41/',branch41.shift_guest_regi_ob_ch41,name='shift_guest_regi_ob_ch41'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch41/',branch41.update_all_rent_ob_ch41,name='update_all_rent_ob_ch41'),

    path('multiple_br1_admit_guest41/<id>',branch41.multiple_br1_admit_guest41,name='multiple_br1_admit_guest41'),

#guest end here


##################################
#_ADVANCE_ob_ch41 START HERE
################################


    path('choose_months_advance_ob_ch41/',branch41.choose_months_advance_ob_ch41,name='choose_months_advance_ob_ch41'),

    path('jan_advance_ob_ch41/', branch41.jan_advance_ob_ch41, name='jan_advance_ob_ch41'),
    path('jan_make_payments_advance_ob_ch41/<id>', branch41.jan_make_payments_advance_ob_ch41,name='jan_make_payments_advance_ob_ch41'),
    path('feb_advance_ob_ch41/', branch41.feb_advance_ob_ch41, name='feb_advance_ob_ch41'),
    path('feb_make_payments_advance_ob_ch41/<id>', branch41.feb_make_payments_advance_ob_ch41,name='feb_make_payments_advance_ob_ch41'),
    path('march_advance_ob_ch41/', branch41.march_advance_ob_ch41, name='march_advance_ob_ch41'),
    path('march_make_payments_advance_ob_ch41/<id>', branch41.march_make_payments_advance_ob_ch41,name='march_make_payments_advance_ob_ch41'),
    path('april_advance_ob_ch41/', branch41.april_advance_ob_ch41, name='april_advance_ob_ch41'),
    path('april_make_payments_advance_ob_ch41/<id>', branch41.april_make_payments_advance_ob_ch41, name='april_make_payments_advance_ob_ch41'),

    path('may_advance_ob_ch41/',branch41.may_advance_ob_ch41,name='may_advance_ob_ch41'),
    path('may_make_payments_advance_ob_ch41/<id>', branch41.may_make_payments_advance_ob_ch41, name='may_make_payments_advance_ob_ch41'),
    path('june_advance_ob_ch41/',branch41.june_advance_ob_ch41,name='june_advance_ob_ch41'),
    path('june_make_payments_advance_ob_ch41/<id>', branch41.june_make_payments_advance_ob_ch41, name='june_make_payments_advance_ob_ch41'),
    path('july_advance_ob_ch41/',branch41.july_advance_ob_ch41,name='july_advance_ob_ch41'),
    path('july_make_payments_advance_ob_ch41/<id>', branch41.july_make_payments_advance_ob_ch41, name='july_make_payments_advance_ob_ch41'),
    path('auguest_advance_ob_ch41/', branch41.auguest_advance_ob_ch41, name='auguest_advance_ob_ch41'),
    path('auguest_make_payments_advance_ob_ch41/<id>', branch41.auguest_make_payments_advance_ob_ch41, name='auguest_make_payments_advance_ob_ch41'),

    path('sept_advance_ob_ch41/', branch41.sept_advance_ob_ch41, name='sept_advance_ob_ch41'),
    path('sept_make_payments_advance_ob_ch41/<id>', branch41.sept_make_payments_advance_ob_ch41,name='sept_make_payments_advance_ob_ch41'),
    path('october_advance_ob_ch41/', branch41.october_advance_ob_ch41, name='october_advance_ob_ch41'),
    path('october_make_payments_advance_ob_ch41/<id>', branch41.october_make_payments_advance_ob_ch41, name='october_make_payments_advance_ob_ch41'),
    path('nov_advance_ob_ch41/', branch41.nov_advance_ob_ch41, name='nov_advance_ob_ch41'),
    path('nov_make_payments_advance_ob_ch41/<id>', branch41.nov_make_payments_advance_ob_ch41,name='nov_make_payments_advance_ob_ch41'),
    path('dec_advance_ob_ch41/', branch41.dec_advance_ob_ch41, name='dec_advance_ob_ch41'),
    path('dec_make_payments_advance_ob_ch41/<id>', branch41.dec_make_payments_advance_ob_ch41, name='dec_make_payments_advance_ob_ch41'),



##################################
#_ADVANCE_ob_ch41 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch41/',branch41.choose_months_ob_ch41,name='choose_months_ob_ch41'),

    path('jan_ob_ch41/',branch41.jan_ob_ch41,name='jan_ob_ch41'),
    path('jan_manke_payments_ob_ch41/<id>',branch41.jan_manke_payments_ob_ch41,name='jan_manke_payments_ob_ch41'),

    path('feb_ob_ch41/',branch41.feb_ob_ch41,name='feb_ob_ch41'),
    path('feb_manke_payments_ob_ch41/<id>',branch41.feb_manke_payments_ob_ch41,name='feb_manke_payments_ob_ch41'),

    path('march_ob_ch41/',branch41.march_ob_ch41,name='march_ob_ch41'),
    path('march_manke_payments_ob_ch41/<id>',branch41.march_manke_payments_ob_ch41,name='march_manke_payments_ob_ch41'),

    path('april_ob_ch41/',branch41.april_ob_ch41,name='april_ob_ch41'),
    path('april_make_payments_ob_ch41/<id>',branch41.april_make_payments_ob_ch41,name='april_make_payments_ob_ch41'),

    path('may_ob_ch41/',branch41.may_ob_ch41,name='may_ob_ch41'),
    path('may_make_payments_ob_ch41/<id>',branch41.may_make_payments_ob_ch41,name='may_make_payments_ob_ch41'),

    path('june_ob_ch41/',branch41.june_ob_ch41,name='june_ob_ch41'),
    path('june_make_payments_ob_ch41/<id>',branch41.june_make_payments_ob_ch41,name='june_make_payments_ob_ch41'),

    path('july_ob_ch41/',branch41.july_ob_ch41,name='july_ob_ch41'),
    path('july_make_payments_ob_ch41/<id>',branch41.july_make_payments_ob_ch41,name='july_make_payments_ob_ch41'),

    path('aug_ob_ch41/',branch41.aug_ob_ch41,name='aug_ob_ch41'),
    path('aug_make_payments_ob_ch41/<id>',branch41.aug_make_payments_ob_ch41,name='aug_make_payments_ob_ch41'),

    path('sept_ob_ch41/',branch41.sept_ob_ch41,name='sept_ob_ch41'),
    path('sept_make_payments_ob_ch41/<id>',branch41.sept_make_payments_ob_ch41,name='sept_make_payments_ob_ch41'),

    path('oct_ob_ch41/',branch41.oct_ob_ch41,name='oct_ob_ch41'),
    path('oct_make_payments_ob_ch41/<id>',branch41.oct_make_payments_ob_ch41,name='oct_make_payments_ob_ch41'),

    path('nov_ob_ch41/',branch41.nov_ob_ch41,name='nov_ob_ch41'),
    path('nov_make_payments_ob_ch41/<id>',branch41.nov_make_payments_ob_ch41,name='nov_make_payments_ob_ch41'),

    path('dec_ob_ch41/',branch41.dec_ob_ch41,name='dec_ob_ch41'),
    path('dec_make_payments_ob_ch41/<id>',branch41.dec_make_payments_ob_ch41,name='dec_make_payments_ob_ch41'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch41/', payment41.choose_user_ob_ch41, name='choose_user_ob_ch41'),
    path('payment_user_details_ob_ch41/<id>', payment41.payment_user_details_ob_ch41, name='payment_user_details_ob_ch41'),
    path('close_choose_user_ob_ch41/<id>',payment41.close_choose_user_ob_ch41,name='close_choose_user_ob_ch41'),

    path('monthly_jan_make_payments_ob_ch41/<id>', payment41.monthly_jan_make_payments_ob_ch41, name='monthly_jan_make_payments_ob_ch41'),
    path('monthly_feb_make_payments_ob_ch41/<id>', payment41.monthly_feb_make_payments_ob_ch41, name='monthly_feb_make_payments_ob_ch41'),
    path('monthly_march_make_payments_ob_ch41/<id>', payment41.monthly_march_make_payments_ob_ch41, name='monthly_march_make_payments_ob_ch41'),
    path('monthly_april_make_payments_ob_ch41/<id>', payment41.monthly_april_make_payments_ob_ch41, name='monthly_april_make_payments_ob_ch41'),
    path('monthly_may_make_payments_ob_ch41/<id>', payment41.monthly_may_make_payments_ob_ch41, name='monthly_may_make_payments_ob_ch41'),
    path('monthly_june_make_payments_ob_ch41/<id>', payment41.monthly_june_make_payments_ob_ch41, name='monthly_june_make_payments_ob_ch41'),

    path('monthly_july_make_payments_ob_ch41/<id>', payment41.monthly_july_make_payments_ob_ch41, name='monthly_july_make_payments_ob_ch41'),
    path('monthly_aug_make_payments_ob_ch41/<id>', payment41.monthly_aug_make_payments_ob_ch41, name='monthly_aug_make_payments_ob_ch41'),
    path('monthly_sept_make_payments_ob_ch41/<id>', payment41.monthly_sept_make_payments_ob_ch41, name='monthly_sept_make_payments_ob_ch41'),
    path('monthly_oct_make_payments_ob_ch41/<id>', payment41.monthly_oct_make_payments_ob_ch41, name='monthly_oct_make_payments_ob_ch41'),
    path('monthly_nov_make_payments_ob_ch41/<id>', payment41.monthly_nov_make_payments_ob_ch41, name='monthly_nov_make_payments_ob_ch41'),
    path('monthly_dec_make_payments_ob_ch41/<id>', payment41.monthly_dec_make_payments_ob_ch41, name='monthly_dec_make_payments_ob_ch41'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch41/',branch41.unpaid_rent_choose_months_ob_ch41,name='unpaid_rent_choose_months_ob_ch41'),

    path('jan_unpaid_rent_ob_ch41/', branch41.jan_unpaid_rent_ob_ch41, name='jan_unpaid_rent_ob_ch41'),
    path('table_jan_unpaid_rent_ob_ch41/', branch41.table_jan_unpaid_rent_ob_ch41, name='table_jan_unpaid_rent_ob_ch41'),
    path('feb_unpaid_rent_ob_ch41/', branch41.feb_unpaid_rent_ob_ch41, name='feb_unpaid_rent_ob_ch41'),
    path('table_feb_unpaid_rent_ob_ch41/', branch41.table_feb_unpaid_rent_ob_ch41, name='table_feb_unpaid_rent_ob_ch41'),
    path('mar_unpaid_rent_ob_ch41/', branch41.mar_unpaid_rent_ob_ch41, name='mar_unpaid_rent_ob_ch41'),
    path('table_mar_unpaid_rent_ob_ch41/', branch41.table_mar_unpaid_rent_ob_ch41, name='table_mar_unpaid_rent_ob_ch41'),
    path('april_unpaid_rent_ob_ch41/', branch41.april_unpaid_rent_ob_ch41, name='april_unpaid_rent_ob_ch41'),
    path('table_april_unpaid_rent_ob_ch41/', branch41.table_april_unpaid_rent_ob_ch41, name='table_april_unpaid_rent_ob_ch41'),

    path('may_unpaid_rent_ob_ch41/', branch41.may_unpaid_rent_ob_ch41, name='may_unpaid_rent_ob_ch41'),
    path('table_may_unpaid_rent_ob_ch41/', branch41.table_may_unpaid_rent_ob_ch41, name='table_may_unpaid_rent_ob_ch41'),
    path('june_unpaid_rent_ob_ch41/', branch41.june_unpaid_rent_ob_ch41, name='june_unpaid_rent_ob_ch41'),
    path('table_june_unpaid_rent_ob_ch41/', branch41.table_june_unpaid_rent_ob_ch41, name='table_june_unpaid_rent_ob_ch41'),
    path('july_unpaid_rent_ob_ch41/', branch41.july_unpaid_rent_ob_ch41, name='july_unpaid_rent_ob_ch41'),
    path('table_july_unpaid_rent_ob_ch41',branch41.table_july_unpaid_rent_ob_ch41,name='table_july_unpaid_rent_ob_ch41'),
    path('aug_unpaid_rent_ob_ch41/', branch41.aug_unpaid_rent_ob_ch41, name='aug_unpaid_rent_ob_ch41'),
    path('table_aug_unpaid_rent_ob_ch41/',branch41.table_aug_unpaid_rent_ob_ch41,name='table_aug_unpaid_rent_ob_ch41'),

    path('sept_unpaid_rent_ob_ch41/', branch41.sept_unpaid_rent_ob_ch41, name='sept_unpaid_rent_ob_ch41'),
    path('table_sept_unpaid_rent_ob_ch41/', branch41.table_sept_unpaid_rent_ob_ch41, name='table_sept_unpaid_rent_ob_ch41'),
    path('oct_unpaid_rent_ob_ch41/', branch41.oct_unpaid_rent_ob_ch41, name='oct_unpaid_rent_ob_ch41'),
    path('table_oct_unpaid_rent_ob_ch41/', branch41.table_oct_unpaid_rent_ob_ch41, name='table_oct_unpaid_rent_ob_ch41'),
    path('nov_unpaid_rent_ob_ch41/', branch41.nov_unpaid_rent_ob_ch41, name='nov_unpaid_rent_ob_ch41'),
    path('table_nov_unpaid_rent_ob_ch41/', branch41.table_nov_unpaid_rent_ob_ch41, name='table_nov_unpaid_rent_ob_ch41'),
    path('dec_unpaid_rent_ob_ch41/', branch41.dec_unpaid_rent_ob_ch41, name='dec_unpaid_rent_ob_ch41'),
    path('table_dec_unpaid_rent_ob_ch41/', branch41.table_dec_unpaid_rent_ob_ch41, name='table_dec_unpaid_rent_ob_ch41'),

    path('details_of_unpaid_guests_ob_ch41/<id>',branch41.details_of_unpaid_guests_ob_ch41,name='details_of_unpaid_guests_ob_ch41'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch41/',branch41.paid_rent_choose_months_ob_ch41,name='paid_rent_choose_months_ob_ch41'),
    path('partially_paid_guest_choose_months_ob_ch41/',reports41.partially_paid_guest_choose_months_ob_ch41,name='partially_paid_guest_choose_months_ob_ch41'),

    path('jan_paid_rent_ob_ch41/', branch41.jan_paid_rent_ob_ch41, name='jan_paid_rent_ob_ch41'),
    path('table_jan_paid_rent_ob_ch41/', branch41.table_jan_paid_rent_ob_ch41, name='table_jan_paid_rent_ob_ch41'),
    path('jan_full_paid_guest_ob_ch41/', reports41.jan_full_paid_guest_ob_ch41, name='jan_full_paid_guest_ob_ch41'),
    path('jan_partially_paid_guest_ob_ch41/', reports41.jan_partially_paid_guest_ob_ch41, name='jan_partially_paid_guest_ob_ch41'),
    path('table_jan_partially_paid_guest_ob_ch41/', reports41.table_jan_partially_paid_guest_ob_ch41,name='table_jan_partially_paid_guest_ob_ch41'),

    path('feb_paid_rent_ob_ch41/', branch41.feb_paid_rent_ob_ch41, name='feb_paid_rent_ob_ch41'),
    path('table_feb_paid_rent_ob_ch41/', branch41.table_feb_paid_rent_ob_ch41, name='table_feb_paid_rent_ob_ch41'),
    path('feb_full_paid_guest_ob_ch41/', reports41.feb_full_paid_guest_ob_ch41, name='feb_full_paid_guest_ob_ch41'),
    path('feb_partially_paid_guest_ob_ch41/', reports41.feb_partially_paid_guest_ob_ch41, name='feb_partially_paid_guest_ob_ch41'),
    path('table_feb_partially_paid_guest_ob_ch41/', reports41.table_feb_partially_paid_guest_ob_ch41,name='table_feb_partially_paid_guest_ob_ch41'),

    path('mar_paid_rent_ob_ch41/', branch41.mar_paid_rent_ob_ch41, name='mar_paid_rent_ob_ch41'),
    path('table_mar_paid_rent_ob_ch41/', branch41.table_mar_paid_rent_ob_ch41, name='table_mar_paid_rent_ob_ch41'),
    path('march_full_paid_guest_ob_ch41/', reports41.march_full_paid_guest_ob_ch41, name='march_full_paid_guest_ob_ch41'),
    path('march_partially_paid_guest_ob_ch41/', reports41.march_partially_paid_guest_ob_ch41, name='march_partially_paid_guest_ob_ch41'),
    path('table_march_partially_paid_guest_ob_ch41/', reports41.table_march_partially_paid_guest_ob_ch41,name='table_march_partially_paid_guest_ob_ch41'),

    path('april_paid_rent_ob_ch41/', branch41.april_paid_rent_ob_ch41, name='april_paid_rent_ob_ch41'),
    path('table_april_paid_rent_ob_ch41/', branch41.table_april_paid_rent_ob_ch41, name='table_april_paid_rent_ob_ch41'),
    path('april_full_paid_guest_ob_ch41/', reports41.april_full_paid_guest_ob_ch41, name='april_full_paid_guest_ob_ch41'),
    path('april_partially_paid_guest_ob_ch41/', reports41.april_partially_paid_guest_ob_ch41, name='april_partially_paid_guest_ob_ch41'),
    path('table_april_partially_paid_guest_ob_ch41/', reports41.table_april_partially_paid_guest_ob_ch41,name='table_april_partially_paid_guest_ob_ch41'),

    path('may_paid_rent_ob_ch41/', branch41.may_paid_rent_ob_ch41, name='may_paid_rent_ob_ch41'),
    path('table_may_paid_rent_ob_ch41/', branch41.table_may_paid_rent_ob_ch41, name='table_may_paid_rent_ob_ch41'),
    path('may_full_paid_guest_ob_ch41/', reports41.may_full_paid_guest_ob_ch41, name='may_full_paid_guest_ob_ch41'),
    path('may_partially_paid_guest_ob_ch41/', reports41.may_partially_paid_guest_ob_ch41, name='may_partially_paid_guest_ob_ch41'),
    path('table_may_partially_paid_guest_ob_ch41/', reports41.table_may_partially_paid_guest_ob_ch41, name='table_may_partially_paid_guest_ob_ch41'),

    path('june_paid_rent_ob_ch41/', branch41.june_paid_rent_ob_ch41, name='june_paid_rent_ob_ch41'),
    path('table_june_paid_rent_ob_ch41/', branch41.table_june_paid_rent_ob_ch41, name='table_june_paid_rent_ob_ch41'),
    path('june_full_paid_guest_ob_ch41/', reports41.june_full_paid_guest_ob_ch41, name='june_full_paid_guest_ob_ch41'),
    path('june_partially_paid_guest_ob_ch41/', reports41.june_partially_paid_guest_ob_ch41, name='june_partially_paid_guest_ob_ch41'),
    path('table_june_partially_paid_guest_ob_ch41/', reports41.table_june_partially_paid_guest_ob_ch41, name='table_june_partially_paid_guest_ob_ch41'),

    path('july_paid_rent_ob_ch41/', branch41.july_paid_rent_ob_ch41, name='july_paid_rent_ob_ch41'),
    path('table_july_paid_rent_ob_ch41/', branch41.table_july_paid_rent_ob_ch41, name='table_july_paid_rent_ob_ch41'),
    path('july_full_paid_guest_ob_ch41/', reports41.july_full_paid_guest_ob_ch41, name='july_full_paid_guest_ob_ch41'),
    path('july_partially_paid_guest_ob_ch41/', reports41.july_partially_paid_guest_ob_ch41, name='july_partially_paid_guest_ob_ch41'),
    path('table_july_partially_paid_guest_ob_ch41/', reports41.table_july_partially_paid_guest_ob_ch41, name='table_july_partially_paid_guest_ob_ch41'),

    path('aug_paid_rent_ob_ch41/', branch41.aug_paid_rent_ob_ch41, name='aug_paid_rent_ob_ch41'),
    path('table_aug_paid_rent_ob_ch41/', branch41.table_aug_paid_rent_ob_ch41, name='table_aug_paid_rent_ob_ch41'),
    path('auguest_full_paid_guest_ob_ch41/', reports41.auguest_full_paid_guest_ob_ch41, name='auguest_full_paid_guest_ob_ch41'),
    path('auguest_partially_paid_guest_ob_ch41/', reports41.auguest_partially_paid_guest_ob_ch41,name='auguest_partially_paid_guest_ob_ch41'),
    path('table_auguest_partially_paid_guest_ob_ch41/', reports41.table_auguest_partially_paid_guest_ob_ch41,name='table_auguest_partially_paid_guest_ob_ch41'),

    path('sept_paid_rent_ob_ch41/', branch41.sept_paid_rent_ob_ch41, name='sept_paid_rent_ob_ch41'),
    path('table_sept_paid_rent_ob_ch41/', branch41.table_sept_paid_rent_ob_ch41, name='table_sept_paid_rent_ob_ch41'),
    path('sept_full_paid_guest_ob_ch41/', reports41.sept_full_paid_guest_ob_ch41, name='sept_full_paid_guest_ob_ch41'),
    path('sept_partially_paid_guest_ob_ch41/', reports41.sept_partially_paid_guest_ob_ch41, name='sept_partially_paid_guest_ob_ch41'),
    path('table_sept_partially_paid_guest_ob_ch41/', reports41.table_sept_partially_paid_guest_ob_ch41,name='table_sept_partially_paid_guest_ob_ch41'),

    path('oct_paid_rent_ob_ch41/', branch41.oct_paid_rent_ob_ch41, name='oct_paid_rent_ob_ch41'),
    path('table_oct_paid_rent_ob_ch41/', branch41.table_oct_paid_rent_ob_ch41, name='table_oct_paid_rent_ob_ch41'),
    path('october_full_paid_guest_ob_ch41/', reports41.october_full_paid_guest_ob_ch41, name='october_full_paid_guest_ob_ch41'),
    path('october_partially_paid_guest_ob_ch41/', reports41.october_partially_paid_guest_ob_ch41,name='october_partially_paid_guest_ob_ch41'),
    path('table_october_partially_paid_guest_ob_ch41/', reports41.table_october_partially_paid_guest_ob_ch41,name='table_october_partially_paid_guest_ob_ch41'),

    path('nov_paid_rent_ob_ch41/', branch41.nov_paid_rent_ob_ch41, name='nov_paid_rent_ob_ch41'),
    path('table_nov_paid_rent_ob_ch41/', branch41.table_nov_paid_rent_ob_ch41, name='table_nov_paid_rent_ob_ch41'),
    path('nov_full_paid_guest_ob_ch41/', reports41.nov_full_paid_guest_ob_ch41, name='nov_full_paid_guest_ob_ch41'),
    path('nov_partially_paid_guest_ob_ch41/', reports41.nov_partially_paid_guest_ob_ch41, name='nov_partially_paid_guest_ob_ch41'),
    path('table_nov_partially_paid_guest_ob_ch41/', reports41.table_nov_partially_paid_guest_ob_ch41,name='table_nov_partially_paid_guest_ob_ch41'),

    path('dec_paid_rent_ob_ch41/', branch41.dec_paid_rent_ob_ch41, name='dec_paid_rent_ob_ch41'),
    path('table_dec_paid_rent_ob_ch41/', branch41.table_dec_paid_rent_ob_ch41, name='table_dec_paid_rent_ob_ch41'),
    path('dec_full_paid_guest_ob_ch41/', reports41.dec_full_paid_guest_ob_ch41, name='dec_full_paid_guest_ob_ch41'),
    path('dec_partially_paid_guest_ob_ch41/', reports41.dec_partially_paid_guest_ob_ch41, name='dec_partially_paid_guest_ob_ch41'),
    path('table_dec_partially_paid_guest_ob_ch41/', reports41.table_dec_partially_paid_guest_ob_ch41,name='table_dec_partially_paid_guest_ob_ch41'),

    path('details_of_paid_guests_ob_ch41/<id>',branch41.details_of_paid_guests_ob_ch41,name='details_of_paid_guests_ob_ch41'),
    path('full_paid_guest_ob_ch41/',reports41.full_paid_guest_ob_ch41,name='full_paid_guest_ob_ch41'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch41/',branch41.viewall_vacate_guest_ob_ch41,name='viewall_vacate_guest_ob_ch41'),
    path('details_of_vacate_guest_ob_ch41/<id>',branch41.details_of_vacate_guest_ob_ch41,name='details_of_vacate_guest_ob_ch41'),
    path('full_vacated_guest_details_ob_ch41',branch41.full_vacated_guest_details_ob_ch41,name='full_vacated_guest_details_ob_ch41'),
    path('full_vacated_guest_table_ob_ch41',branch41.full_vacated_guest_table_ob_ch41,name='full_vacated_guest_table_ob_ch41'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch41/<id>', branch41.jan_manke_payments_vacate_ob_ch41, name='jan_manke_payments_vacate_ob_ch41'),
    path('feb_manke_payments_vacate_ob_ch41/<id>', branch41.feb_manke_payments_vacate_ob_ch41, name='feb_manke_payments_vacate_ob_ch41'),
    path('march_manke_payments_vacate_ob_ch41/<id>', branch41.march_manke_payments_vacate_ob_ch41, name='march_manke_payments_vacate_ob_ch41'),
    path('april_make_payments_vacate_ob_ch41/<id>', branch41.april_make_payments_vacate_ob_ch41, name='april_make_payments_vacate_ob_ch41'),

    path('may_make_payments_vacate_ob_ch41/<id>', branch41.may_make_payments_vacate_ob_ch41, name='may_make_payments_vacate_ob_ch41'),
    path('june_make_payments_vacate_ob_ch41/<id>', branch41.june_make_payments_vacate_ob_ch41, name='june_make_payments_vacate_ob_ch41'),
    path('july_make_payments_vacate_ob_ch41/<id>', branch41.july_make_payments_vacate_ob_ch41, name='july_make_payments_vacate_ob_ch41'),
    path('aug_make_payments_vacate_ob_ch41/<id>', branch41.aug_make_payments_vacate_ob_ch41, name='aug_make_payments_vacate_ob_ch41'),

    path('sept_make_payments_vacate_ob_ch41/<id>', branch41.sept_make_payments_vacate_ob_ch41, name='sept_make_payments_vacate_ob_ch41'),
    path('oct_make_payments_vacate_ob_ch41/<id>', branch41.oct_make_payments_vacate_ob_ch41, name='oct_make_payments_vacate_ob_ch41'),
    path('nov_make_payments_vacate_ob_ch41/<id>', branch41.nov_make_payments_vacate_ob_ch41, name='nov_make_payments_vacate_ob_ch41'),
    path('dec_make_payments_vacate_ob_ch41/<id>', branch41.dec_make_payments_vacate_ob_ch41, name='dec_make_payments_vacate_ob_ch41'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch41/',branch41.detail_guest_general_ob_ch41,name='detail_guest_general_ob_ch41'),

    path('jan_print_ob_ch41/',branch41.jan_print_ob_ch41,name='jan_print_ob_ch41'),
    path('feb_print_ob_ch41/',branch41.feb_print_ob_ch41,name='feb_print_ob_ch41'),
    path('march_print_ob_ch41/',branch41.march_print_ob_ch41,name='march_print_ob_ch41'),
    path('april_print_ob_ch41/',branch41.april_print_ob_ch41,name='april_print_ob_ch41'),

    path('may_print_ob_ch41/',branch41.may_print_ob_ch41,name='may_print_ob_ch41'),
    path('june_print_ob_ch41/',branch41.june_print_ob_ch41,name='june_print_ob_ch41'),
    path('july_print_ob_ch41/', branch41.july_print_ob_ch41, name='july_print_ob_ch41'),
    path('aug_print_ob_ch41/', branch41.aug_print_ob_ch41, name='aug_print_ob_ch41'),

    path('sept_print_ob_ch41/', branch41.sept_print_ob_ch41, name='sept_print_ob_ch41'),
    path('oct_print_ob_ch41/', branch41.oct_print_ob_ch41, name='oct_print_ob_ch41'),
    path('nov_print_ob_ch41/', branch41.nov_print_ob_ch41, name='nov_print_ob_ch41'),
    path('dec_print_ob_ch41/', branch41.dec_print_ob_ch41, name='dec_print_ob_ch41'),

    path('new_year_jan_print_ob_ch41/', branch41.new_year_jan_print_ob_ch41, name='new_year_jan_print_ob_ch41'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch41/', branch41.jan_close_ob_ch41, name='jan_close_ob_ch41'),
    path('jan_close_decision_page_ob_ch41/', branch41.jan_close_decision_page_ob_ch41, name='jan_close_decision_page_ob_ch41'),
    path('feb_close/', branch41.feb_close_ob_ch41, name='feb_close_ob_ch41'),
    path('feb_close_decision_page_ob_ch41/', branch41.feb_close_decision_page_ob_ch41, name='feb_close_decision_page_ob_ch41'),
    path('mar_close_ob_ch41/', branch41.mar_close_ob_ch41, name='mar_close_ob_ch41'),
    path('mar_close_decision_page/', branch41.mar_close_decision_page_ob_ch41, name='mar_close_decision_page_ob_ch41'),
    path('apr_close_ob_ch41/', branch41.apr_close_ob_ch41, name='apr_close_ob_ch41'),
    path('apr_close_decision_page_ob_ch41/', branch41.apr_close_decision_page_ob_ch41, name='apr_close_decision_page_ob_ch41'),

    path('may_close_ob_ch41/', branch41.may_close_ob_ch41, name='may_close_ob_ch41'),
    path('may_close_decision_page_ob_ch41/', branch41.may_close_decision_page_ob_ch41, name='may_close_decision_page_ob_ch41'),
    path('jun_close_ob_ch41/', branch41.jun_close_ob_ch41, name='jun_close_ob_ch41'),
    path('jun_close_decision_page_ob_ch41/', branch41.jun_close_decision_page_ob_ch41, name='jun_close_decision_page_ob_ch41'),
    path('jul_close_ob_ch41/', branch41.jul_close_ob_ch41, name='jul_close_ob_ch41'),
    path('jul_close_decision_page_ob_ch41/', branch41.jul_close_decision_page_ob_ch41, name='jul_close_decision_page_ob_ch41'),
    path('aug_close_ob_ch41/', branch41.aug_close_ob_ch41, name='aug_close_ob_ch41'),
    path('aug_close_decision_page_ob_ch41/', branch41.aug_close_decision_page_ob_ch41, name='aug_close_decision_page_ob_ch41'),

    path('sep_close_ob_ch41/', branch41.sep_close_ob_ch41, name='sep_close_ob_ch41'),
    path('sep_close_decision_page_ob_ch41/', branch41.sep_close_decision_page_ob_ch41, name='sep_close_decision_page_ob_ch41'),
    path('oct_close_ob_ch41/', branch41.oct_close_ob_ch41, name='oct_close_ob_ch41'),
    path('oct_close_decision_page_ob_ch41/', branch41.oct_close_decision_page_ob_ch41, name='oct_close_decision_page_ob_ch41'),
    path('nov_close_ob_ch41/', branch41.nov_close_ob_ch41, name='nov_close_ob_ch41'),
    path('nov_close_decision_page_ob_ch41/', branch41.nov_close_decision_page_ob_ch41, name='nov_close_decision_page_ob_ch41'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch41/',reports41.detailed_report_choose_months_ob_ch41,name='detailed_report_choose_months_ob_ch41'),

    path('jan_details_live_ob_ch41/', reports41.jan_details_live_ob_ch41, name='jan_details_live_ob_ch41'),
    path('jan_print_live_ob_ch41/', reports41.jan_print_live_ob_ch41, name='jan_print_live_ob_ch41'),
    path('feb_details_live_ob_ch41/', reports41.feb_details_live_ob_ch41, name='feb_details_live_ob_ch41'),
    path('feb_print_live_ob_ch41/', reports41.feb_print_live_ob_ch41, name='feb_print_live_ob_ch41'),
    path('march_details_live_ob_ch41/', reports41.march_details_live_ob_ch41, name='march_details_live_ob_ch41'),
    path('march_print_live_ob_ch41/', reports41.march_print_live_ob_ch41, name='march_print_live_ob_ch41'),

    path('april_details_live_ob_ch41/', reports41.april_details_live_ob_ch41, name='april_details_live_ob_ch41'),
    path('april_print_live_ob_ch41/', reports41.april_print_live_ob_ch41, name='april_print_live_ob_ch41'),
    path('may_details_live_ob_ch41/', reports41.may_details_live_ob_ch41, name='may_details_live_ob_ch41'),
    path('may_print_live_ob_ch41/', reports41.may_print_live_ob_ch41, name='may_print_live_ob_ch41'),
    path('june_details_live_ob_ch41/',reports41.june_details_live_ob_ch41,name='june_details_live_ob_ch41'),
    path('june_print_live_ob_ch41/', reports41.june_print_live_ob_ch41, name='june_print_live_ob_ch41'),

    path('july_details_live_ob_ch41/', reports41.july_details_live_ob_ch41, name='july_details_live_ob_ch41'),
    path('july_print_live_ob_ch41/', reports41.july_print_live_ob_ch41, name='july_print_live_ob_ch41'),
    path('auguest_details_live_ob_ch41/', reports41.auguest_details_live_ob_ch41, name='auguest_details_live_ob_ch41'),
    path('auguest_print_live_ob_ch41/', reports41.auguest_print_live_ob_ch41, name='auguest_print_live_ob_ch41'),
    path('sept_details_live_ob_ch41/', reports41.sept_details_live_ob_ch41, name='sept_details_live_ob_ch41'),
    path('sept_print_live_ob_ch41/', reports41.sept_print_live_ob_ch41, name='sept_print_live_ob_ch41'),

    path('october_details_live_ob_ch41/', reports41.october_details_live_ob_ch41, name='october_details_live_ob_ch41'),
    path('october_print_live_ob_ch41/', reports41.october_print_live_ob_ch41, name='october_print_live_ob_ch41'),
    path('nov_details_live_ob_ch41/', reports41.nov_details_live_ob_ch41, name='nov_details_live_ob_ch41'),
    path('nov_print_live_ob_ch41/', reports41.nov_print_live_ob_ch41, name='nov_print_live_ob_ch41'),
    path('dec_details_live_ob_ch41/', reports41.dec_details_live_ob_ch41, name='dec_details_live_ob_ch41'),
    path('dec_print_live_ob_ch41/', reports41.dec_print_live_ob_ch41, name='dec_print_live_ob_ch41'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch41/', reports41.viewall_vaccant_room_ob_ch41, name='viewall_vaccant_room_ob_ch41'),

    path('d_ob_ch41/', branch41.dynamic, name='dynamic'),

    path('manage_bed_ob_ch41/', branch41.manage_bed_ob_ch41, name='manage_bed_ob_ch41'),
    path('manage_new_guest_ob_ch41/', branch41.manage_new_guest_ob_ch41, name='manage_new_guest_ob_ch41'),
    path('manage_update_new_guest_ob_ch41/<id>', branch41.manage_update_new_guest_ob_ch41, name='manage_update_new_guest_ob_ch41'),
    path('manage_update_beds_ob_ch41/<id>', branch41.manage_update_beds_ob_ch41, name='manage_update_beds_ob_ch41'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch41/', branch41.view_all_due_amt_ob_ch41, name='view_all_due_amt_ob_ch41'),
    path('due_amt_mgt_choose_months_ob_ch41/', branch41.due_amt_mgt_choose_months_ob_ch41, name='due_amt_mgt_choose_months_ob_ch41'),

    path('view_jan_account_details_ob_ch41/', branch41.view_jan_account_details_ob_ch41, name='view_jan_account_details_ob_ch41'),
    path('jan_account_mgt_ob_ch41/<id>',branch41.jan_account_mgt_ob_ch41,name='jan_account_mgt_ob_ch41'),
    path('view_feb_account_details_ob_ch41/', branch41.view_feb_account_details_ob_ch41, name='view_feb_account_details_ob_ch41'),
    path('feb_account_mgt_ob_ch41/<id>',branch41.feb_account_mgt_ob_ch41,name='feb_account_mgt_ob_ch41'),
    path('view_march_account_details_ob_ch41/', branch41.view_march_account_details_ob_ch41, name='view_march_account_details_ob_ch41'),
    path('march_account_mgt_ob_ch41/<id>',branch41.march_account_mgt_ob_ch41,name='march_account_mgt_ob_ch41'),
    path('view_april_account_details_ob_ch41/', branch41.view_april_account_details_ob_ch41, name='view_april_account_details_ob_ch41'),
    path('april_account_mgt_ob_ch41/<id>',branch41.april_account_mgt_ob_ch41,name='april_account_mgt_ob_ch41'),

    path('view_may_account_details_ob_ch41/',branch41.view_may_account_details_ob_ch41,name='view_may_account_details_ob_ch41'),
    path('may_account_mgt_ob_ch41/<id>', branch41.may_account_mgt_ob_ch41, name='may_account_mgt_ob_ch41'),
    path('view_june_account_details_ob_ch41/', branch41.view_june_account_details_ob_ch41, name='view_june_account_details_ob_ch41'),
    path('june_account_mgt_ob_ch41/<id>',branch41.june_account_mgt_ob_ch41,name='june_account_mgt_ob_ch41'),
    path('view_july_account_details_ob_ch41/', branch41.view_july_account_details_ob_ch41, name='view_july_account_details_ob_ch41'),
    path('july_account_mgt_ob_ch41/<id>',branch41.july_account_mgt_ob_ch41,name='july_account_mgt_ob_ch41'),
    path('view_auguest_account_details_ob_ch41/', branch41.view_auguest_account_details_ob_ch41, name='view_auguest_account_details_ob_ch41'),
    path('auguest_account_mgt_ob_ch41/<id>',branch41.auguest_account_mgt_ob_ch41,name='auguest_account_mgt_ob_ch41'),

    path('view_sept_account_details_ob_ch41/', branch41.view_sept_account_details_ob_ch41, name='view_sept_account_details_ob_ch41'),
    path('sept_account_mgt_ob_ch41/<id>',branch41.sept_account_mgt_ob_ch41,name='sept_account_mgt_ob_ch41'),
    path('view_october_account_details_ob_ch41/', branch41.view_october_account_details_ob_ch41, name='view_october_account_details_ob_ch41'),
    path('october_account_mgt_ob_ch41/<id>',branch41.october_account_mgt_ob_ch41,name='october_account_mgt_ob_ch41'),
    path('view_nov_account_details_ob_ch41/', branch41.view_nov_account_details_ob_ch41, name='view_nov_account_details_ob_ch41'),
    path('nov_account_mgt_ob_ch41/<id>',branch41.nov_account_mgt_ob_ch41,name='nov_account_mgt_ob_ch41'),
    path('view_dec_account_details_ob_ch41/', branch41.view_dec_account_details_ob_ch41, name='view_dec_account_details_ob_ch41'),
    path('dec_account_mgt_ob_ch41/<id>',branch41.dec_account_mgt_ob_ch41,name='dec_account_mgt_ob_ch41'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch41', admin_dashboard_calculations_br41.monthly_details_due_ob_ch41, name='monthly_details_due_ob_ch41'),
    path('monthly_collection_details_ob_ch41/', admin_dashboard_calculations_br41.monthly_collection_details_ob_ch41, name='monthly_collection_details_ob_ch41'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch41/',branch41.guest_all_ob_ch41,name='guest_all_ob_ch41'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category41/', accounts41.view_all_category41, name='view_all_category41'),
    path('create_new_category41/', accounts41.create_new_category41, name='create_new_category41'),
    path('regi_new_category41/', accounts41.regi_new_category41, name='regi_new_category41'),
    path('update_category41/<id>',accounts41.update_category41,name='update_category41'),

    path('delete_category41/<id>', accounts41.delete_category41, name='delete_category41'),
    path('view_all_category_delete41/', accounts41.view_all_category_delete41, name='view_all_category_delete41'),

    path('regi_multiple_new_category41/', accounts41.regi_multiple_new_category41, name='regi_multiple_new_category41'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items41/', accounts41.view_all_items41, name='view_all_items41'),
    path('create_new_item41/', accounts41.create_new_item41, name='create_new_item41'),
    path('regi_new_item41/', accounts41.regi_new_item41, name='regi_new_item41'),
    path('delete_item41/<id>',accounts41.delete_item41,name='delete_item41'),
    path('update_item41/<id>', accounts41.update_item41, name='update_item41'),
    path('view_all_items_delete41/',accounts41.view_all_items_delete41,name='view_all_items_delete41'),

    path('regi_multiple_new_item41/', accounts41.regi_multiple_new_item41, name='regi_multiple_new_item41'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger41/', accounts41.view_all_ledger41, name='view_all_ledger41'),
    path('create_new_ledger41/', accounts41.create_new_ledger41, name='create_new_ledger41'),
    path('regi_new_ledger41/', accounts41.regi_new_ledger41, name='regi_new_ledger41'),
    path('delete_ledger41/<id>',accounts41.delete_ledger41,name='delete_ledger41'),
    path('update_ledger41/<id>',accounts41.update_ledger41,name='update_ledger41'),
    path('view_all_ledger_delete41/',accounts41.view_all_ledger_delete41,name='view_all_ledger_delete41'),

    path('regi_multiple_new_ledger41/', accounts41.regi_multiple_new_ledger41, name='regi_multiple_new_ledger41'),

    ##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book41/', accounts41.view_all_accounts_book41, name='view_all_accounts_book41'),
    path('create_new_accounts_book41/', accounts41.create_new_accounts_book41, name='create_new_accounts_book41'),
    path('regi_new_accounts_book41/', accounts41.regi_new_accounts_book41, name='regi_new_accounts_book41'),
    path('update_accounts_book41/<id>',accounts41.update_accounts_book41,name='update_accounts_book41'),
    path('delete_accounts_book41/<id>',accounts41.delete_accounts_book41,name='delete_accounts_book41'),
    path('view_all_accounts_book_delete41/',accounts41.view_all_accounts_book_delete41,name='view_all_accounts_book_delete41'),

    path('regi_multiple_new_accounts_book41/', accounts41.regi_multiple_new_accounts_book41,name='regi_multiple_new_accounts_book41'),

    ##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries41/', accounts41.get_countries41, name='get_countries41'),

    path('in_exp_items_entry41/', accounts41.in_exp_items_entry41, name='in_exp_items_entry41'),
    path('reg_in_exp_items_entry41/', accounts41.reg_in_exp_items_entry41, name='reg_in_exp_items_entry41'),
    path('delete_journal41/<id>',accounts41.delete_journal41,name='delete_journal41'),
    path('update_in_exp_items_entry41/<id>',accounts41.update_in_exp_items_entry41,name='update_in_exp_items_entry41'),
    path('detailed_journal_report41/',accounts41.detailed_journal_report41,name='detailed_journal_report41'),
    path('journal_report_deleted41/',accounts41.journal_report_deleted41,name='journal_report_deleted41'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise41/', accounts41.daily_category_wise41, name='daily_category_wise41'),
    path('monthly_category_based_reports41/',accounts41.monthly_category_based_reports41,name='monthly_category_based_reports41'),
    path('yearly_category_based_reports41/', accounts41.yearly_category_based_reports41,name='yearly_category_based_reports41'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed41/', accounts41.daily_detailed41, name='daily_detailed41'),
    path('monthly_detailed41/',accounts41.monthly_detailed41,name='monthly_detailed41'),
    path('yearly_detailed41/',accounts41.yearly_detailed41,name='yearly_detailed41'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports41/', accounts41.item_based_reports41, name='item_based_reports41'),
    path('daily_item_based_reports41/',accounts41.daily_item_based_reports41,name='daily_item_based_reports41'),
    path('monthly_item_based_reports41/',accounts41.monthly_item_based_reports41,name='monthly_item_based_reports41'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports41/', accounts41.ledger_based_reports41, name='ledger_based_reports41'),
    path('monthly_ledger_based_reports41/', accounts41.monthly_ledger_based_reports41, name='monthly_ledger_based_reports41'),
    path('daily_ledger_based_reports41/',accounts41.daily_ledger_based_reports41,name='daily_ledger_based_reports41'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports41/', accounts41.accounts_book_based_reports41, name='accounts_book_based_reports41'),
    path('daily_accounts_book_based_reports41/',accounts41.daily_accounts_book_based_reports41,name='daily_accounts_book_based_reports41'),
    path('monthly_accounts_book_based_reports41/',accounts41.monthly_accounts_book_based_reports41,name='monthly_accounts_book_based_reports41'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months41/', accounts41.monthly_reports_choose_months41, name='monthly_reports_choose_months41'),
    path('monthly_detailed_daily_in_exp_items_report41/<mo>',accounts41.monthly_detailed_daily_in_exp_items_report41,name='monthly_detailed_daily_in_exp_items_report41'),

    path('single_monthly_reports_choose_months41/', accounts41.single_monthly_reports_choose_months41,name='single_monthly_reports_choose_months41'),
    path('single_monthly_daily_in_exp_items_report41/<mo>',accounts41.single_monthly_daily_in_exp_items_report41,name='single_monthly_daily_in_exp_items_report41'),

    path('accounts_dash_board_ob_ch41/',accounts41.accounts_dash_board_ob_ch41,name='accounts_dash_board_ob_ch41'),
    path('accounts_dash_board41/',accounts41.accounts_dash_board41,name='accounts_dash_board41'),

    path('profit_sharing_choose_months41', accounts41.profit_sharing_choose_months41,name='profit_sharing_choose_months41'),
    path('profit_sharing41/<mo>', accounts41.profit_sharing41, name='profit_sharing41'),
    path('view_share_holders41', accounts41.view_share_holders41, name='view_share_holders41'),
    path('create_share_holders41', accounts41.create_share_holders41, name='create_share_holders41'),
    path('regi_share_holders41', accounts41.regi_share_holders41, name='regi_share_holders41'),
    path('update_share_holders41/<id>', accounts41.update_share_holders41, name='update_share_holders41'),
    path('delete_share_holders41/<id>', accounts41.delete_share_holders41, name='delete_share_holders41'),
    path('view_deleted_share_holders41', accounts41.view_deleted_share_holders41, name='view_deleted_share_holders41'),

    path('regi_multiple_share_holders41', accounts41.regi_multiple_share_holders41, name='regi_multiple_share_holders41'),

    #############BRANCH SETTINGS START HERE ########################

    path('guest_rent_update_ob_ch41/', branch_settings41.guest_rent_update_ob_ch41, name='guest_rent_update_ob_ch41'),

    ############BRANCH SETTINGS END HERE ############################

]

