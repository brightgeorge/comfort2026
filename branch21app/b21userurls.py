from django.urls import path, include

from . import admin_branch21
from . import admin_branch21
from . import branch21
from . import reports21
from . import payment21
from . import admin_dashboard_calculations_br21
from . import accounts21
from . import branch_settings21

urlpatterns = [

    path('branch1_dashboard_ob_ch21/', branch21.branch1_dashboard_ob_ch21, name='branch1_dashboard_ob_ch21'),
    path('branch1_dashboard21/',branch21.branch1_dashboard21,name='branch1_dashboard21'),
    path('user_dashboard_calculations_ob_ch21/',branch21.user_dashboard_calculations_ob_ch21,name='user_dashboard_calculations_ob_ch21'),

    path('background_ob_ch21',branch21.background_ob_ch21,name='background_ob_ch21'),
    path('background_regi_ob_ch21',branch21.background_regi_ob_ch21,name='background_regi_ob_ch21'),
    path('custom_background_regi_ob_ch21',branch21.custom_background_regi_ob_ch21,name='custom_background_regi_ob_ch21'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch21/',admin_branch21.branch1_room_create_regi_ob_ch21,name='branch1_room_create_regi_ob_ch21'),
    path('view_all_room_ob_ch21/',admin_branch21.view_all_room_ob_ch21,name='view_all_room_ob_ch21'),
    path('delete_room_ob_ch21/<id>',admin_branch21.delete_room_ob_ch21,name='delete_room_ob_ch21'),

    path('branch1_room_create_ob_ch21/',admin_branch21.branch1_room_create_ob_ch21,name='branch1_room_create_ob_ch21'),

    path('multiple_branch1_room_create_regi21/',admin_branch21.multiple_branch1_room_create_regi21,name='multiple_branch1_room_create_regi21'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch21/', admin_branch21.pg1_bed_create_regi_ob_ch21, name='pg1_bed_create_regi_ob_ch21'),
    path('pg1_view_all_beds_ob_ch21/', admin_branch21.pg1_view_all_beds_ob_ch21, name='pg1_view_all_beds_ob_ch21'),
    path('delete_bed_ob_ch21/<id>', admin_branch21.delete_bed_ob_ch21, name='delete_bed_ob_ch21'),

    path('pg1_bed_create_ob_ch21/', admin_branch21.pg1_bed_create_ob_ch21, name='pg1_bed_create_ob_ch21'),

    path('single_pg1_bed_create_regi_ob_ch21/',admin_branch21.single_pg1_bed_create_regi_ob_ch21,name='single_pg1_bed_create_regi_ob_ch21'),
    path('update_bed_basic_details_ob_ch21/<id>',admin_branch21.update_bed_basic_details_ob_ch21, name='update_bed_basic_details_ob_ch21'),

    path('multiple_single_pg1_bed_create_regi21/',admin_branch21.multiple_single_pg1_bed_create_regi21,name='multiple_single_pg1_bed_create_regi21'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch21/<id>',branch21.br1_admit_guest_ob_ch21,name='br1_admit_guest_ob_ch21'),
    path('view_all_new_guest_ob_ch21/',branch21.view_all_new_guest_ob_ch21,name='view_all_new_guest_ob_ch21'),
    path('update_br1_admit_guest_ob_ch21/<id>',branch21.update_br1_admit_guest_ob_ch21,name='update_br1_admit_guest_ob_ch21'),
    path('vacate_br1_guest_ob_ch21/<id>',branch21.vacate_br1_guest_ob_ch21,name='vacate_br1_guest_ob_ch21'),

    path('active_guest_details_ob_ch21/<guest_code>',branch21.active_guest_details_ob_ch21,name='active_guest_details_ob_ch21'),
    path('view_all_guest_ob_ch21/',branch21.view_all_guest_ob_ch21,name='view_all_guest_ob_ch21'),
    path('shift_guest_ob_ch21/<id>',branch21.shift_guest_ob_ch21,name='shift_guest_ob_ch21'),
    path('shift_guest_regi_ob_ch21/',branch21.shift_guest_regi_ob_ch21,name='shift_guest_regi_ob_ch21'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch21/',branch21.update_all_rent_ob_ch21,name='update_all_rent_ob_ch21'),

    path('multiple_br1_admit_guest21/<id>',branch21.multiple_br1_admit_guest21,name='multiple_br1_admit_guest21'),

#guest end here


##################################
#_ADVANCE_ob_ch21 START HERE
################################


    path('choose_months_advance_ob_ch21/',branch21.choose_months_advance_ob_ch21,name='choose_months_advance_ob_ch21'),

    path('jan_advance_ob_ch21/', branch21.jan_advance_ob_ch21, name='jan_advance_ob_ch21'),
    path('jan_make_payments_advance_ob_ch21/<id>', branch21.jan_make_payments_advance_ob_ch21,name='jan_make_payments_advance_ob_ch21'),
    path('feb_advance_ob_ch21/', branch21.feb_advance_ob_ch21, name='feb_advance_ob_ch21'),
    path('feb_make_payments_advance_ob_ch21/<id>', branch21.feb_make_payments_advance_ob_ch21,name='feb_make_payments_advance_ob_ch21'),
    path('march_advance_ob_ch21/', branch21.march_advance_ob_ch21, name='march_advance_ob_ch21'),
    path('march_make_payments_advance_ob_ch21/<id>', branch21.march_make_payments_advance_ob_ch21,name='march_make_payments_advance_ob_ch21'),
    path('april_advance_ob_ch21/', branch21.april_advance_ob_ch21, name='april_advance_ob_ch21'),
    path('april_make_payments_advance_ob_ch21/<id>', branch21.april_make_payments_advance_ob_ch21, name='april_make_payments_advance_ob_ch21'),

    path('may_advance_ob_ch21/',branch21.may_advance_ob_ch21,name='may_advance_ob_ch21'),
    path('may_make_payments_advance_ob_ch21/<id>', branch21.may_make_payments_advance_ob_ch21, name='may_make_payments_advance_ob_ch21'),
    path('june_advance_ob_ch21/',branch21.june_advance_ob_ch21,name='june_advance_ob_ch21'),
    path('june_make_payments_advance_ob_ch21/<id>', branch21.june_make_payments_advance_ob_ch21, name='june_make_payments_advance_ob_ch21'),
    path('july_advance_ob_ch21/',branch21.july_advance_ob_ch21,name='july_advance_ob_ch21'),
    path('july_make_payments_advance_ob_ch21/<id>', branch21.july_make_payments_advance_ob_ch21, name='july_make_payments_advance_ob_ch21'),
    path('auguest_advance_ob_ch21/', branch21.auguest_advance_ob_ch21, name='auguest_advance_ob_ch21'),
    path('auguest_make_payments_advance_ob_ch21/<id>', branch21.auguest_make_payments_advance_ob_ch21, name='auguest_make_payments_advance_ob_ch21'),

    path('sept_advance_ob_ch21/', branch21.sept_advance_ob_ch21, name='sept_advance_ob_ch21'),
    path('sept_make_payments_advance_ob_ch21/<id>', branch21.sept_make_payments_advance_ob_ch21,name='sept_make_payments_advance_ob_ch21'),
    path('october_advance_ob_ch21/', branch21.october_advance_ob_ch21, name='october_advance_ob_ch21'),
    path('october_make_payments_advance_ob_ch21/<id>', branch21.october_make_payments_advance_ob_ch21, name='october_make_payments_advance_ob_ch21'),
    path('nov_advance_ob_ch21/', branch21.nov_advance_ob_ch21, name='nov_advance_ob_ch21'),
    path('nov_make_payments_advance_ob_ch21/<id>', branch21.nov_make_payments_advance_ob_ch21,name='nov_make_payments_advance_ob_ch21'),
    path('dec_advance_ob_ch21/', branch21.dec_advance_ob_ch21, name='dec_advance_ob_ch21'),
    path('dec_make_payments_advance_ob_ch21/<id>', branch21.dec_make_payments_advance_ob_ch21, name='dec_make_payments_advance_ob_ch21'),



##################################
#_ADVANCE_ob_ch21 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch21/',branch21.choose_months_ob_ch21,name='choose_months_ob_ch21'),

    path('jan_ob_ch21/',branch21.jan_ob_ch21,name='jan_ob_ch21'),
    path('jan_manke_payments_ob_ch21/<id>',branch21.jan_manke_payments_ob_ch21,name='jan_manke_payments_ob_ch21'),

    path('feb_ob_ch21/',branch21.feb_ob_ch21,name='feb_ob_ch21'),
    path('feb_manke_payments_ob_ch21/<id>',branch21.feb_manke_payments_ob_ch21,name='feb_manke_payments_ob_ch21'),

    path('march_ob_ch21/',branch21.march_ob_ch21,name='march_ob_ch21'),
    path('march_manke_payments_ob_ch21/<id>',branch21.march_manke_payments_ob_ch21,name='march_manke_payments_ob_ch21'),

    path('april_ob_ch21/',branch21.april_ob_ch21,name='april_ob_ch21'),
    path('april_make_payments_ob_ch21/<id>',branch21.april_make_payments_ob_ch21,name='april_make_payments_ob_ch21'),

    path('may_ob_ch21/',branch21.may_ob_ch21,name='may_ob_ch21'),
    path('may_make_payments_ob_ch21/<id>',branch21.may_make_payments_ob_ch21,name='may_make_payments_ob_ch21'),

    path('june_ob_ch21/',branch21.june_ob_ch21,name='june_ob_ch21'),
    path('june_make_payments_ob_ch21/<id>',branch21.june_make_payments_ob_ch21,name='june_make_payments_ob_ch21'),

    path('july_ob_ch21/',branch21.july_ob_ch21,name='july_ob_ch21'),
    path('july_make_payments_ob_ch21/<id>',branch21.july_make_payments_ob_ch21,name='july_make_payments_ob_ch21'),

    path('aug_ob_ch21/',branch21.aug_ob_ch21,name='aug_ob_ch21'),
    path('aug_make_payments_ob_ch21/<id>',branch21.aug_make_payments_ob_ch21,name='aug_make_payments_ob_ch21'),

    path('sept_ob_ch21/',branch21.sept_ob_ch21,name='sept_ob_ch21'),
    path('sept_make_payments_ob_ch21/<id>',branch21.sept_make_payments_ob_ch21,name='sept_make_payments_ob_ch21'),

    path('oct_ob_ch21/',branch21.oct_ob_ch21,name='oct_ob_ch21'),
    path('oct_make_payments_ob_ch21/<id>',branch21.oct_make_payments_ob_ch21,name='oct_make_payments_ob_ch21'),

    path('nov_ob_ch21/',branch21.nov_ob_ch21,name='nov_ob_ch21'),
    path('nov_make_payments_ob_ch21/<id>',branch21.nov_make_payments_ob_ch21,name='nov_make_payments_ob_ch21'),

    path('dec_ob_ch21/',branch21.dec_ob_ch21,name='dec_ob_ch21'),
    path('dec_make_payments_ob_ch21/<id>',branch21.dec_make_payments_ob_ch21,name='dec_make_payments_ob_ch21'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch21/', payment21.choose_user_ob_ch21, name='choose_user_ob_ch21'),
    path('payment_user_details_ob_ch21/<id>', payment21.payment_user_details_ob_ch21, name='payment_user_details_ob_ch21'),
    path('close_choose_user_ob_ch21/<id>',payment21.close_choose_user_ob_ch21,name='close_choose_user_ob_ch21'),

    path('monthly_jan_make_payments_ob_ch21/<id>', payment21.monthly_jan_make_payments_ob_ch21, name='monthly_jan_make_payments_ob_ch21'),
    path('monthly_feb_make_payments_ob_ch21/<id>', payment21.monthly_feb_make_payments_ob_ch21, name='monthly_feb_make_payments_ob_ch21'),
    path('monthly_march_make_payments_ob_ch21/<id>', payment21.monthly_march_make_payments_ob_ch21, name='monthly_march_make_payments_ob_ch21'),
    path('monthly_april_make_payments_ob_ch21/<id>', payment21.monthly_april_make_payments_ob_ch21, name='monthly_april_make_payments_ob_ch21'),
    path('monthly_may_make_payments_ob_ch21/<id>', payment21.monthly_may_make_payments_ob_ch21, name='monthly_may_make_payments_ob_ch21'),
    path('monthly_june_make_payments_ob_ch21/<id>', payment21.monthly_june_make_payments_ob_ch21, name='monthly_june_make_payments_ob_ch21'),

    path('monthly_july_make_payments_ob_ch21/<id>', payment21.monthly_july_make_payments_ob_ch21, name='monthly_july_make_payments_ob_ch21'),
    path('monthly_aug_make_payments_ob_ch21/<id>', payment21.monthly_aug_make_payments_ob_ch21, name='monthly_aug_make_payments_ob_ch21'),
    path('monthly_sept_make_payments_ob_ch21/<id>', payment21.monthly_sept_make_payments_ob_ch21, name='monthly_sept_make_payments_ob_ch21'),
    path('monthly_oct_make_payments_ob_ch21/<id>', payment21.monthly_oct_make_payments_ob_ch21, name='monthly_oct_make_payments_ob_ch21'),
    path('monthly_nov_make_payments_ob_ch21/<id>', payment21.monthly_nov_make_payments_ob_ch21, name='monthly_nov_make_payments_ob_ch21'),
    path('monthly_dec_make_payments_ob_ch21/<id>', payment21.monthly_dec_make_payments_ob_ch21, name='monthly_dec_make_payments_ob_ch21'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch21/',branch21.unpaid_rent_choose_months_ob_ch21,name='unpaid_rent_choose_months_ob_ch21'),

    path('jan_unpaid_rent_ob_ch21/', branch21.jan_unpaid_rent_ob_ch21, name='jan_unpaid_rent_ob_ch21'),
    path('table_jan_unpaid_rent_ob_ch21/', branch21.table_jan_unpaid_rent_ob_ch21, name='table_jan_unpaid_rent_ob_ch21'),
    path('feb_unpaid_rent_ob_ch21/', branch21.feb_unpaid_rent_ob_ch21, name='feb_unpaid_rent_ob_ch21'),
    path('table_feb_unpaid_rent_ob_ch21/', branch21.table_feb_unpaid_rent_ob_ch21, name='table_feb_unpaid_rent_ob_ch21'),
    path('mar_unpaid_rent_ob_ch21/', branch21.mar_unpaid_rent_ob_ch21, name='mar_unpaid_rent_ob_ch21'),
    path('table_mar_unpaid_rent_ob_ch21/', branch21.table_mar_unpaid_rent_ob_ch21, name='table_mar_unpaid_rent_ob_ch21'),
    path('april_unpaid_rent_ob_ch21/', branch21.april_unpaid_rent_ob_ch21, name='april_unpaid_rent_ob_ch21'),
    path('table_april_unpaid_rent_ob_ch21/', branch21.table_april_unpaid_rent_ob_ch21, name='table_april_unpaid_rent_ob_ch21'),

    path('may_unpaid_rent_ob_ch21/', branch21.may_unpaid_rent_ob_ch21, name='may_unpaid_rent_ob_ch21'),
    path('table_may_unpaid_rent_ob_ch21/', branch21.table_may_unpaid_rent_ob_ch21, name='table_may_unpaid_rent_ob_ch21'),
    path('june_unpaid_rent_ob_ch21/', branch21.june_unpaid_rent_ob_ch21, name='june_unpaid_rent_ob_ch21'),
    path('table_june_unpaid_rent_ob_ch21/', branch21.table_june_unpaid_rent_ob_ch21, name='table_june_unpaid_rent_ob_ch21'),
    path('july_unpaid_rent_ob_ch21/', branch21.july_unpaid_rent_ob_ch21, name='july_unpaid_rent_ob_ch21'),
    path('table_july_unpaid_rent_ob_ch21',branch21.table_july_unpaid_rent_ob_ch21,name='table_july_unpaid_rent_ob_ch21'),
    path('aug_unpaid_rent_ob_ch21/', branch21.aug_unpaid_rent_ob_ch21, name='aug_unpaid_rent_ob_ch21'),
    path('table_aug_unpaid_rent_ob_ch21/',branch21.table_aug_unpaid_rent_ob_ch21,name='table_aug_unpaid_rent_ob_ch21'),

    path('sept_unpaid_rent_ob_ch21/', branch21.sept_unpaid_rent_ob_ch21, name='sept_unpaid_rent_ob_ch21'),
    path('table_sept_unpaid_rent_ob_ch21/', branch21.table_sept_unpaid_rent_ob_ch21, name='table_sept_unpaid_rent_ob_ch21'),
    path('oct_unpaid_rent_ob_ch21/', branch21.oct_unpaid_rent_ob_ch21, name='oct_unpaid_rent_ob_ch21'),
    path('table_oct_unpaid_rent_ob_ch21/', branch21.table_oct_unpaid_rent_ob_ch21, name='table_oct_unpaid_rent_ob_ch21'),
    path('nov_unpaid_rent_ob_ch21/', branch21.nov_unpaid_rent_ob_ch21, name='nov_unpaid_rent_ob_ch21'),
    path('table_nov_unpaid_rent_ob_ch21/', branch21.table_nov_unpaid_rent_ob_ch21, name='table_nov_unpaid_rent_ob_ch21'),
    path('dec_unpaid_rent_ob_ch21/', branch21.dec_unpaid_rent_ob_ch21, name='dec_unpaid_rent_ob_ch21'),
    path('table_dec_unpaid_rent_ob_ch21/', branch21.table_dec_unpaid_rent_ob_ch21, name='table_dec_unpaid_rent_ob_ch21'),

    path('details_of_unpaid_guests_ob_ch21/<id>',branch21.details_of_unpaid_guests_ob_ch21,name='details_of_unpaid_guests_ob_ch21'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch21/',branch21.paid_rent_choose_months_ob_ch21,name='paid_rent_choose_months_ob_ch21'),
    path('partially_paid_guest_choose_months_ob_ch21/',reports21.partially_paid_guest_choose_months_ob_ch21,name='partially_paid_guest_choose_months_ob_ch21'),

    path('jan_paid_rent_ob_ch21/', branch21.jan_paid_rent_ob_ch21, name='jan_paid_rent_ob_ch21'),
    path('table_jan_paid_rent_ob_ch21/', branch21.table_jan_paid_rent_ob_ch21, name='table_jan_paid_rent_ob_ch21'),
    path('jan_full_paid_guest_ob_ch21/', reports21.jan_full_paid_guest_ob_ch21, name='jan_full_paid_guest_ob_ch21'),
    path('jan_partially_paid_guest_ob_ch21/', reports21.jan_partially_paid_guest_ob_ch21, name='jan_partially_paid_guest_ob_ch21'),
    path('table_jan_partially_paid_guest_ob_ch21/', reports21.table_jan_partially_paid_guest_ob_ch21,name='table_jan_partially_paid_guest_ob_ch21'),

    path('feb_paid_rent_ob_ch21/', branch21.feb_paid_rent_ob_ch21, name='feb_paid_rent_ob_ch21'),
    path('table_feb_paid_rent_ob_ch21/', branch21.table_feb_paid_rent_ob_ch21, name='table_feb_paid_rent_ob_ch21'),
    path('feb_full_paid_guest_ob_ch21/', reports21.feb_full_paid_guest_ob_ch21, name='feb_full_paid_guest_ob_ch21'),
    path('feb_partially_paid_guest_ob_ch21/', reports21.feb_partially_paid_guest_ob_ch21, name='feb_partially_paid_guest_ob_ch21'),
    path('table_feb_partially_paid_guest_ob_ch21/', reports21.table_feb_partially_paid_guest_ob_ch21,name='table_feb_partially_paid_guest_ob_ch21'),

    path('mar_paid_rent_ob_ch21/', branch21.mar_paid_rent_ob_ch21, name='mar_paid_rent_ob_ch21'),
    path('table_mar_paid_rent_ob_ch21/', branch21.table_mar_paid_rent_ob_ch21, name='table_mar_paid_rent_ob_ch21'),
    path('march_full_paid_guest_ob_ch21/', reports21.march_full_paid_guest_ob_ch21, name='march_full_paid_guest_ob_ch21'),
    path('march_partially_paid_guest_ob_ch21/', reports21.march_partially_paid_guest_ob_ch21, name='march_partially_paid_guest_ob_ch21'),
    path('table_march_partially_paid_guest_ob_ch21/', reports21.table_march_partially_paid_guest_ob_ch21,name='table_march_partially_paid_guest_ob_ch21'),

    path('april_paid_rent_ob_ch21/', branch21.april_paid_rent_ob_ch21, name='april_paid_rent_ob_ch21'),
    path('table_april_paid_rent_ob_ch21/', branch21.table_april_paid_rent_ob_ch21, name='table_april_paid_rent_ob_ch21'),
    path('april_full_paid_guest_ob_ch21/', reports21.april_full_paid_guest_ob_ch21, name='april_full_paid_guest_ob_ch21'),
    path('april_partially_paid_guest_ob_ch21/', reports21.april_partially_paid_guest_ob_ch21, name='april_partially_paid_guest_ob_ch21'),
    path('table_april_partially_paid_guest_ob_ch21/', reports21.table_april_partially_paid_guest_ob_ch21,name='table_april_partially_paid_guest_ob_ch21'),

    path('may_paid_rent_ob_ch21/', branch21.may_paid_rent_ob_ch21, name='may_paid_rent_ob_ch21'),
    path('table_may_paid_rent_ob_ch21/', branch21.table_may_paid_rent_ob_ch21, name='table_may_paid_rent_ob_ch21'),
    path('may_full_paid_guest_ob_ch21/', reports21.may_full_paid_guest_ob_ch21, name='may_full_paid_guest_ob_ch21'),
    path('may_partially_paid_guest_ob_ch21/', reports21.may_partially_paid_guest_ob_ch21, name='may_partially_paid_guest_ob_ch21'),
    path('table_may_partially_paid_guest_ob_ch21/', reports21.table_may_partially_paid_guest_ob_ch21, name='table_may_partially_paid_guest_ob_ch21'),

    path('june_paid_rent_ob_ch21/', branch21.june_paid_rent_ob_ch21, name='june_paid_rent_ob_ch21'),
    path('table_june_paid_rent_ob_ch21/', branch21.table_june_paid_rent_ob_ch21, name='table_june_paid_rent_ob_ch21'),
    path('june_full_paid_guest_ob_ch21/', reports21.june_full_paid_guest_ob_ch21, name='june_full_paid_guest_ob_ch21'),
    path('june_partially_paid_guest_ob_ch21/', reports21.june_partially_paid_guest_ob_ch21, name='june_partially_paid_guest_ob_ch21'),
    path('table_june_partially_paid_guest_ob_ch21/', reports21.table_june_partially_paid_guest_ob_ch21, name='table_june_partially_paid_guest_ob_ch21'),

    path('july_paid_rent_ob_ch21/', branch21.july_paid_rent_ob_ch21, name='july_paid_rent_ob_ch21'),
    path('table_july_paid_rent_ob_ch21/', branch21.table_july_paid_rent_ob_ch21, name='table_july_paid_rent_ob_ch21'),
    path('july_full_paid_guest_ob_ch21/', reports21.july_full_paid_guest_ob_ch21, name='july_full_paid_guest_ob_ch21'),
    path('july_partially_paid_guest_ob_ch21/', reports21.july_partially_paid_guest_ob_ch21, name='july_partially_paid_guest_ob_ch21'),
    path('table_july_partially_paid_guest_ob_ch21/', reports21.table_july_partially_paid_guest_ob_ch21, name='table_july_partially_paid_guest_ob_ch21'),

    path('aug_paid_rent_ob_ch21/', branch21.aug_paid_rent_ob_ch21, name='aug_paid_rent_ob_ch21'),
    path('table_aug_paid_rent_ob_ch21/', branch21.table_aug_paid_rent_ob_ch21, name='table_aug_paid_rent_ob_ch21'),
    path('auguest_full_paid_guest_ob_ch21/', reports21.auguest_full_paid_guest_ob_ch21, name='auguest_full_paid_guest_ob_ch21'),
    path('auguest_partially_paid_guest_ob_ch21/', reports21.auguest_partially_paid_guest_ob_ch21,name='auguest_partially_paid_guest_ob_ch21'),
    path('table_auguest_partially_paid_guest_ob_ch21/', reports21.table_auguest_partially_paid_guest_ob_ch21,name='table_auguest_partially_paid_guest_ob_ch21'),

    path('sept_paid_rent_ob_ch21/', branch21.sept_paid_rent_ob_ch21, name='sept_paid_rent_ob_ch21'),
    path('table_sept_paid_rent_ob_ch21/', branch21.table_sept_paid_rent_ob_ch21, name='table_sept_paid_rent_ob_ch21'),
    path('sept_full_paid_guest_ob_ch21/', reports21.sept_full_paid_guest_ob_ch21, name='sept_full_paid_guest_ob_ch21'),
    path('sept_partially_paid_guest_ob_ch21/', reports21.sept_partially_paid_guest_ob_ch21, name='sept_partially_paid_guest_ob_ch21'),
    path('table_sept_partially_paid_guest_ob_ch21/', reports21.table_sept_partially_paid_guest_ob_ch21,name='table_sept_partially_paid_guest_ob_ch21'),

    path('oct_paid_rent_ob_ch21/', branch21.oct_paid_rent_ob_ch21, name='oct_paid_rent_ob_ch21'),
    path('table_oct_paid_rent_ob_ch21/', branch21.table_oct_paid_rent_ob_ch21, name='table_oct_paid_rent_ob_ch21'),
    path('october_full_paid_guest_ob_ch21/', reports21.october_full_paid_guest_ob_ch21, name='october_full_paid_guest_ob_ch21'),
    path('october_partially_paid_guest_ob_ch21/', reports21.october_partially_paid_guest_ob_ch21,name='october_partially_paid_guest_ob_ch21'),
    path('table_october_partially_paid_guest_ob_ch21/', reports21.table_october_partially_paid_guest_ob_ch21,name='table_october_partially_paid_guest_ob_ch21'),

    path('nov_paid_rent_ob_ch21/', branch21.nov_paid_rent_ob_ch21, name='nov_paid_rent_ob_ch21'),
    path('table_nov_paid_rent_ob_ch21/', branch21.table_nov_paid_rent_ob_ch21, name='table_nov_paid_rent_ob_ch21'),
    path('nov_full_paid_guest_ob_ch21/', reports21.nov_full_paid_guest_ob_ch21, name='nov_full_paid_guest_ob_ch21'),
    path('nov_partially_paid_guest_ob_ch21/', reports21.nov_partially_paid_guest_ob_ch21, name='nov_partially_paid_guest_ob_ch21'),
    path('table_nov_partially_paid_guest_ob_ch21/', reports21.table_nov_partially_paid_guest_ob_ch21,name='table_nov_partially_paid_guest_ob_ch21'),

    path('dec_paid_rent_ob_ch21/', branch21.dec_paid_rent_ob_ch21, name='dec_paid_rent_ob_ch21'),
    path('table_dec_paid_rent_ob_ch21/', branch21.table_dec_paid_rent_ob_ch21, name='table_dec_paid_rent_ob_ch21'),
    path('dec_full_paid_guest_ob_ch21/', reports21.dec_full_paid_guest_ob_ch21, name='dec_full_paid_guest_ob_ch21'),
    path('dec_partially_paid_guest_ob_ch21/', reports21.dec_partially_paid_guest_ob_ch21, name='dec_partially_paid_guest_ob_ch21'),
    path('table_dec_partially_paid_guest_ob_ch21/', reports21.table_dec_partially_paid_guest_ob_ch21,name='table_dec_partially_paid_guest_ob_ch21'),

    path('details_of_paid_guests_ob_ch21/<id>',branch21.details_of_paid_guests_ob_ch21,name='details_of_paid_guests_ob_ch21'),
    path('full_paid_guest_ob_ch21/',reports21.full_paid_guest_ob_ch21,name='full_paid_guest_ob_ch21'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch21/',branch21.viewall_vacate_guest_ob_ch21,name='viewall_vacate_guest_ob_ch21'),
    path('details_of_vacate_guest_ob_ch21/<id>',branch21.details_of_vacate_guest_ob_ch21,name='details_of_vacate_guest_ob_ch21'),
    path('full_vacated_guest_details_ob_ch21',branch21.full_vacated_guest_details_ob_ch21,name='full_vacated_guest_details_ob_ch21'),
    path('full_vacated_guest_table_ob_ch21',branch21.full_vacated_guest_table_ob_ch21,name='full_vacated_guest_table_ob_ch21'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch21/<id>', branch21.jan_manke_payments_vacate_ob_ch21, name='jan_manke_payments_vacate_ob_ch21'),
    path('feb_manke_payments_vacate_ob_ch21/<id>', branch21.feb_manke_payments_vacate_ob_ch21, name='feb_manke_payments_vacate_ob_ch21'),
    path('march_manke_payments_vacate_ob_ch21/<id>', branch21.march_manke_payments_vacate_ob_ch21, name='march_manke_payments_vacate_ob_ch21'),
    path('april_make_payments_vacate_ob_ch21/<id>', branch21.april_make_payments_vacate_ob_ch21, name='april_make_payments_vacate_ob_ch21'),

    path('may_make_payments_vacate_ob_ch21/<id>', branch21.may_make_payments_vacate_ob_ch21, name='may_make_payments_vacate_ob_ch21'),
    path('june_make_payments_vacate_ob_ch21/<id>', branch21.june_make_payments_vacate_ob_ch21, name='june_make_payments_vacate_ob_ch21'),
    path('july_make_payments_vacate_ob_ch21/<id>', branch21.july_make_payments_vacate_ob_ch21, name='july_make_payments_vacate_ob_ch21'),
    path('aug_make_payments_vacate_ob_ch21/<id>', branch21.aug_make_payments_vacate_ob_ch21, name='aug_make_payments_vacate_ob_ch21'),

    path('sept_make_payments_vacate_ob_ch21/<id>', branch21.sept_make_payments_vacate_ob_ch21, name='sept_make_payments_vacate_ob_ch21'),
    path('oct_make_payments_vacate_ob_ch21/<id>', branch21.oct_make_payments_vacate_ob_ch21, name='oct_make_payments_vacate_ob_ch21'),
    path('nov_make_payments_vacate_ob_ch21/<id>', branch21.nov_make_payments_vacate_ob_ch21, name='nov_make_payments_vacate_ob_ch21'),
    path('dec_make_payments_vacate_ob_ch21/<id>', branch21.dec_make_payments_vacate_ob_ch21, name='dec_make_payments_vacate_ob_ch21'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch21/',branch21.detail_guest_general_ob_ch21,name='detail_guest_general_ob_ch21'),

    path('jan_print_ob_ch21/',branch21.jan_print_ob_ch21,name='jan_print_ob_ch21'),
    path('feb_print_ob_ch21/',branch21.feb_print_ob_ch21,name='feb_print_ob_ch21'),
    path('march_print_ob_ch21/',branch21.march_print_ob_ch21,name='march_print_ob_ch21'),
    path('april_print_ob_ch21/',branch21.april_print_ob_ch21,name='april_print_ob_ch21'),

    path('may_print_ob_ch21/',branch21.may_print_ob_ch21,name='may_print_ob_ch21'),
    path('june_print_ob_ch21/',branch21.june_print_ob_ch21,name='june_print_ob_ch21'),
    path('july_print_ob_ch21/', branch21.july_print_ob_ch21, name='july_print_ob_ch21'),
    path('aug_print_ob_ch21/', branch21.aug_print_ob_ch21, name='aug_print_ob_ch21'),

    path('sept_print_ob_ch21/', branch21.sept_print_ob_ch21, name='sept_print_ob_ch21'),
    path('oct_print_ob_ch21/', branch21.oct_print_ob_ch21, name='oct_print_ob_ch21'),
    path('nov_print_ob_ch21/', branch21.nov_print_ob_ch21, name='nov_print_ob_ch21'),
    path('dec_print_ob_ch21/', branch21.dec_print_ob_ch21, name='dec_print_ob_ch21'),

    path('new_year_jan_print_ob_ch21/', branch21.new_year_jan_print_ob_ch21, name='new_year_jan_print_ob_ch21'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch21/', branch21.jan_close_ob_ch21, name='jan_close_ob_ch21'),
    path('jan_close_decision_page_ob_ch21/', branch21.jan_close_decision_page_ob_ch21, name='jan_close_decision_page_ob_ch21'),
    path('feb_close/', branch21.feb_close_ob_ch21, name='feb_close_ob_ch21'),
    path('feb_close_decision_page_ob_ch21/', branch21.feb_close_decision_page_ob_ch21, name='feb_close_decision_page_ob_ch21'),
    path('mar_close_ob_ch21/', branch21.mar_close_ob_ch21, name='mar_close_ob_ch21'),
    path('mar_close_decision_page/', branch21.mar_close_decision_page_ob_ch21, name='mar_close_decision_page_ob_ch21'),
    path('apr_close_ob_ch21/', branch21.apr_close_ob_ch21, name='apr_close_ob_ch21'),
    path('apr_close_decision_page_ob_ch21/', branch21.apr_close_decision_page_ob_ch21, name='apr_close_decision_page_ob_ch21'),

    path('may_close_ob_ch21/', branch21.may_close_ob_ch21, name='may_close_ob_ch21'),
    path('may_close_decision_page_ob_ch21/', branch21.may_close_decision_page_ob_ch21, name='may_close_decision_page_ob_ch21'),
    path('jun_close_ob_ch21/', branch21.jun_close_ob_ch21, name='jun_close_ob_ch21'),
    path('jun_close_decision_page_ob_ch21/', branch21.jun_close_decision_page_ob_ch21, name='jun_close_decision_page_ob_ch21'),
    path('jul_close_ob_ch21/', branch21.jul_close_ob_ch21, name='jul_close_ob_ch21'),
    path('jul_close_decision_page_ob_ch21/', branch21.jul_close_decision_page_ob_ch21, name='jul_close_decision_page_ob_ch21'),
    path('aug_close_ob_ch21/', branch21.aug_close_ob_ch21, name='aug_close_ob_ch21'),
    path('aug_close_decision_page_ob_ch21/', branch21.aug_close_decision_page_ob_ch21, name='aug_close_decision_page_ob_ch21'),

    path('sep_close_ob_ch21/', branch21.sep_close_ob_ch21, name='sep_close_ob_ch21'),
    path('sep_close_decision_page_ob_ch21/', branch21.sep_close_decision_page_ob_ch21, name='sep_close_decision_page_ob_ch21'),
    path('oct_close_ob_ch21/', branch21.oct_close_ob_ch21, name='oct_close_ob_ch21'),
    path('oct_close_decision_page_ob_ch21/', branch21.oct_close_decision_page_ob_ch21, name='oct_close_decision_page_ob_ch21'),
    path('nov_close_ob_ch21/', branch21.nov_close_ob_ch21, name='nov_close_ob_ch21'),
    path('nov_close_decision_page_ob_ch21/', branch21.nov_close_decision_page_ob_ch21, name='nov_close_decision_page_ob_ch21'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch21/',reports21.detailed_report_choose_months_ob_ch21,name='detailed_report_choose_months_ob_ch21'),

    path('jan_details_live_ob_ch21/', reports21.jan_details_live_ob_ch21, name='jan_details_live_ob_ch21'),
    path('jan_print_live_ob_ch21/', reports21.jan_print_live_ob_ch21, name='jan_print_live_ob_ch21'),
    path('feb_details_live_ob_ch21/', reports21.feb_details_live_ob_ch21, name='feb_details_live_ob_ch21'),
    path('feb_print_live_ob_ch21/', reports21.feb_print_live_ob_ch21, name='feb_print_live_ob_ch21'),
    path('march_details_live_ob_ch21/', reports21.march_details_live_ob_ch21, name='march_details_live_ob_ch21'),
    path('march_print_live_ob_ch21/', reports21.march_print_live_ob_ch21, name='march_print_live_ob_ch21'),

    path('april_details_live_ob_ch21/', reports21.april_details_live_ob_ch21, name='april_details_live_ob_ch21'),
    path('april_print_live_ob_ch21/', reports21.april_print_live_ob_ch21, name='april_print_live_ob_ch21'),
    path('may_details_live_ob_ch21/', reports21.may_details_live_ob_ch21, name='may_details_live_ob_ch21'),
    path('may_print_live_ob_ch21/', reports21.may_print_live_ob_ch21, name='may_print_live_ob_ch21'),
    path('june_details_live_ob_ch21/',reports21.june_details_live_ob_ch21,name='june_details_live_ob_ch21'),
    path('june_print_live_ob_ch21/', reports21.june_print_live_ob_ch21, name='june_print_live_ob_ch21'),

    path('july_details_live_ob_ch21/', reports21.july_details_live_ob_ch21, name='july_details_live_ob_ch21'),
    path('july_print_live_ob_ch21/', reports21.july_print_live_ob_ch21, name='july_print_live_ob_ch21'),
    path('auguest_details_live_ob_ch21/', reports21.auguest_details_live_ob_ch21, name='auguest_details_live_ob_ch21'),
    path('auguest_print_live_ob_ch21/', reports21.auguest_print_live_ob_ch21, name='auguest_print_live_ob_ch21'),
    path('sept_details_live_ob_ch21/', reports21.sept_details_live_ob_ch21, name='sept_details_live_ob_ch21'),
    path('sept_print_live_ob_ch21/', reports21.sept_print_live_ob_ch21, name='sept_print_live_ob_ch21'),

    path('october_details_live_ob_ch21/', reports21.october_details_live_ob_ch21, name='october_details_live_ob_ch21'),
    path('october_print_live_ob_ch21/', reports21.october_print_live_ob_ch21, name='october_print_live_ob_ch21'),
    path('nov_details_live_ob_ch21/', reports21.nov_details_live_ob_ch21, name='nov_details_live_ob_ch21'),
    path('nov_print_live_ob_ch21/', reports21.nov_print_live_ob_ch21, name='nov_print_live_ob_ch21'),
    path('dec_details_live_ob_ch21/', reports21.dec_details_live_ob_ch21, name='dec_details_live_ob_ch21'),
    path('dec_print_live_ob_ch21/', reports21.dec_print_live_ob_ch21, name='dec_print_live_ob_ch21'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch21/', reports21.viewall_vaccant_room_ob_ch21, name='viewall_vaccant_room_ob_ch21'),

    path('d_ob_ch21/', branch21.dynamic, name='dynamic'),

    path('manage_bed_ob_ch21/', branch21.manage_bed_ob_ch21, name='manage_bed_ob_ch21'),
    path('manage_new_guest_ob_ch21/', branch21.manage_new_guest_ob_ch21, name='manage_new_guest_ob_ch21'),
    path('manage_update_new_guest_ob_ch21/<id>', branch21.manage_update_new_guest_ob_ch21, name='manage_update_new_guest_ob_ch21'),
    path('manage_update_beds_ob_ch21/<id>', branch21.manage_update_beds_ob_ch21, name='manage_update_beds_ob_ch21'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch21/', branch21.view_all_due_amt_ob_ch21, name='view_all_due_amt_ob_ch21'),
    path('due_amt_mgt_choose_months_ob_ch21/', branch21.due_amt_mgt_choose_months_ob_ch21, name='due_amt_mgt_choose_months_ob_ch21'),

    path('view_jan_account_details_ob_ch21/', branch21.view_jan_account_details_ob_ch21, name='view_jan_account_details_ob_ch21'),
    path('jan_account_mgt_ob_ch21/<id>',branch21.jan_account_mgt_ob_ch21,name='jan_account_mgt_ob_ch21'),
    path('view_feb_account_details_ob_ch21/', branch21.view_feb_account_details_ob_ch21, name='view_feb_account_details_ob_ch21'),
    path('feb_account_mgt_ob_ch21/<id>',branch21.feb_account_mgt_ob_ch21,name='feb_account_mgt_ob_ch21'),
    path('view_march_account_details_ob_ch21/', branch21.view_march_account_details_ob_ch21, name='view_march_account_details_ob_ch21'),
    path('march_account_mgt_ob_ch21/<id>',branch21.march_account_mgt_ob_ch21,name='march_account_mgt_ob_ch21'),
    path('view_april_account_details_ob_ch21/', branch21.view_april_account_details_ob_ch21, name='view_april_account_details_ob_ch21'),
    path('april_account_mgt_ob_ch21/<id>',branch21.april_account_mgt_ob_ch21,name='april_account_mgt_ob_ch21'),

    path('view_may_account_details_ob_ch21/',branch21.view_may_account_details_ob_ch21,name='view_may_account_details_ob_ch21'),
    path('may_account_mgt_ob_ch21/<id>', branch21.may_account_mgt_ob_ch21, name='may_account_mgt_ob_ch21'),
    path('view_june_account_details_ob_ch21/', branch21.view_june_account_details_ob_ch21, name='view_june_account_details_ob_ch21'),
    path('june_account_mgt_ob_ch21/<id>',branch21.june_account_mgt_ob_ch21,name='june_account_mgt_ob_ch21'),
    path('view_july_account_details_ob_ch21/', branch21.view_july_account_details_ob_ch21, name='view_july_account_details_ob_ch21'),
    path('july_account_mgt_ob_ch21/<id>',branch21.july_account_mgt_ob_ch21,name='july_account_mgt_ob_ch21'),
    path('view_auguest_account_details_ob_ch21/', branch21.view_auguest_account_details_ob_ch21, name='view_auguest_account_details_ob_ch21'),
    path('auguest_account_mgt_ob_ch21/<id>',branch21.auguest_account_mgt_ob_ch21,name='auguest_account_mgt_ob_ch21'),

    path('view_sept_account_details_ob_ch21/', branch21.view_sept_account_details_ob_ch21, name='view_sept_account_details_ob_ch21'),
    path('sept_account_mgt_ob_ch21/<id>',branch21.sept_account_mgt_ob_ch21,name='sept_account_mgt_ob_ch21'),
    path('view_october_account_details_ob_ch21/', branch21.view_october_account_details_ob_ch21, name='view_october_account_details_ob_ch21'),
    path('october_account_mgt_ob_ch21/<id>',branch21.october_account_mgt_ob_ch21,name='october_account_mgt_ob_ch21'),
    path('view_nov_account_details_ob_ch21/', branch21.view_nov_account_details_ob_ch21, name='view_nov_account_details_ob_ch21'),
    path('nov_account_mgt_ob_ch21/<id>',branch21.nov_account_mgt_ob_ch21,name='nov_account_mgt_ob_ch21'),
    path('view_dec_account_details_ob_ch21/', branch21.view_dec_account_details_ob_ch21, name='view_dec_account_details_ob_ch21'),
    path('dec_account_mgt_ob_ch21/<id>',branch21.dec_account_mgt_ob_ch21,name='dec_account_mgt_ob_ch21'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch21', admin_dashboard_calculations_br21.monthly_details_due_ob_ch21, name='monthly_details_due_ob_ch21'),
    path('monthly_collection_details_ob_ch21/', admin_dashboard_calculations_br21.monthly_collection_details_ob_ch21, name='monthly_collection_details_ob_ch21'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch21/',branch21.guest_all_ob_ch21,name='guest_all_ob_ch21'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category21/', accounts21.view_all_category21, name='view_all_category21'),
    path('create_new_category21/', accounts21.create_new_category21, name='create_new_category21'),
    path('regi_new_category21/', accounts21.regi_new_category21, name='regi_new_category21'),
    path('update_category21/<id>',accounts21.update_category21,name='update_category21'),

    path('delete_category21/<id>', accounts21.delete_category21, name='delete_category21'),
    path('view_all_category_delete21/', accounts21.view_all_category_delete21, name='view_all_category_delete21'),

    path('regi_multiple_new_category21/', accounts21.regi_multiple_new_category21, name='regi_multiple_new_category21'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items21/', accounts21.view_all_items21, name='view_all_items21'),
    path('create_new_item21/', accounts21.create_new_item21, name='create_new_item21'),
    path('regi_new_item21/', accounts21.regi_new_item21, name='regi_new_item21'),
    path('delete_item21/<id>',accounts21.delete_item21,name='delete_item21'),
    path('update_item21/<id>', accounts21.update_item21, name='update_item21'),
    path('view_all_items_delete21/',accounts21.view_all_items_delete21,name='view_all_items_delete21'),

    path('regi_multiple_new_item21/', accounts21.regi_multiple_new_item21, name='regi_multiple_new_item21'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger21/', accounts21.view_all_ledger21, name='view_all_ledger21'),
    path('create_new_ledger21/', accounts21.create_new_ledger21, name='create_new_ledger21'),
    path('regi_new_ledger21/', accounts21.regi_new_ledger21, name='regi_new_ledger21'),
    path('delete_ledger21/<id>',accounts21.delete_ledger21,name='delete_ledger21'),
    path('update_ledger21/<id>',accounts21.update_ledger21,name='update_ledger21'),
    path('view_all_ledger_delete21/',accounts21.view_all_ledger_delete21,name='view_all_ledger_delete21'),

    path('regi_multiple_new_ledger21/', accounts21.regi_multiple_new_ledger21, name='regi_multiple_new_ledger21'),

    ##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book21/', accounts21.view_all_accounts_book21, name='view_all_accounts_book21'),
    path('create_new_accounts_book21/', accounts21.create_new_accounts_book21, name='create_new_accounts_book21'),
    path('regi_new_accounts_book21/', accounts21.regi_new_accounts_book21, name='regi_new_accounts_book21'),
    path('update_accounts_book21/<id>',accounts21.update_accounts_book21,name='update_accounts_book21'),
    path('delete_accounts_book21/<id>',accounts21.delete_accounts_book21,name='delete_accounts_book21'),
    path('view_all_accounts_book_delete21/',accounts21.view_all_accounts_book_delete21,name='view_all_accounts_book_delete21'),

    path('regi_multiple_new_accounts_book21/', accounts21.regi_multiple_new_accounts_book21,name='regi_multiple_new_accounts_book21'),

    ##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries21/', accounts21.get_countries21, name='get_countries21'),

    path('in_exp_items_entry21/', accounts21.in_exp_items_entry21, name='in_exp_items_entry21'),
    path('reg_in_exp_items_entry21/', accounts21.reg_in_exp_items_entry21, name='reg_in_exp_items_entry21'),
    path('delete_journal21/<id>',accounts21.delete_journal21,name='delete_journal21'),
    path('update_in_exp_items_entry21/<id>',accounts21.update_in_exp_items_entry21,name='update_in_exp_items_entry21'),
    path('detailed_journal_report21/',accounts21.detailed_journal_report21,name='detailed_journal_report21'),
    path('journal_report_deleted21/',accounts21.journal_report_deleted21,name='journal_report_deleted21'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise21/', accounts21.daily_category_wise21, name='daily_category_wise21'),
    path('monthly_category_based_reports21/',accounts21.monthly_category_based_reports21,name='monthly_category_based_reports21'),
    path('yearly_category_based_reports21/', accounts21.yearly_category_based_reports21,name='yearly_category_based_reports21'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed21/', accounts21.daily_detailed21, name='daily_detailed21'),
    path('monthly_detailed21/',accounts21.monthly_detailed21,name='monthly_detailed21'),
    path('yearly_detailed21/',accounts21.yearly_detailed21,name='yearly_detailed21'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports21/', accounts21.item_based_reports21, name='item_based_reports21'),
    path('daily_item_based_reports21/',accounts21.daily_item_based_reports21,name='daily_item_based_reports21'),
    path('monthly_item_based_reports21/',accounts21.monthly_item_based_reports21,name='monthly_item_based_reports21'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports21/', accounts21.ledger_based_reports21, name='ledger_based_reports21'),
    path('monthly_ledger_based_reports21/', accounts21.monthly_ledger_based_reports21, name='monthly_ledger_based_reports21'),
    path('daily_ledger_based_reports21/',accounts21.daily_ledger_based_reports21,name='daily_ledger_based_reports21'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports21/', accounts21.accounts_book_based_reports21, name='accounts_book_based_reports21'),
    path('daily_accounts_book_based_reports21/',accounts21.daily_accounts_book_based_reports21,name='daily_accounts_book_based_reports21'),
    path('monthly_accounts_book_based_reports21/',accounts21.monthly_accounts_book_based_reports21,name='monthly_accounts_book_based_reports21'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months21/', accounts21.monthly_reports_choose_months21, name='monthly_reports_choose_months21'),
    path('monthly_detailed_daily_in_exp_items_report21/<mo>',accounts21.monthly_detailed_daily_in_exp_items_report21,name='monthly_detailed_daily_in_exp_items_report21'),

    path('single_monthly_reports_choose_months21/', accounts21.single_monthly_reports_choose_months21,name='single_monthly_reports_choose_months21'),
    path('single_monthly_daily_in_exp_items_report21/<mo>',accounts21.single_monthly_daily_in_exp_items_report21,name='single_monthly_daily_in_exp_items_report21'),

    path('accounts_dash_board_ob_ch21/',accounts21.accounts_dash_board_ob_ch21,name='accounts_dash_board_ob_ch21'),
    path('accounts_dash_board21/',accounts21.accounts_dash_board21,name='accounts_dash_board21'),

    path('profit_sharing_choose_months21', accounts21.profit_sharing_choose_months21,name='profit_sharing_choose_months21'),
    path('profit_sharing21/<mo>', accounts21.profit_sharing21, name='profit_sharing21'),
    path('view_share_holders21', accounts21.view_share_holders21, name='view_share_holders21'),
    path('create_share_holders21', accounts21.create_share_holders21, name='create_share_holders21'),
    path('regi_share_holders21', accounts21.regi_share_holders21, name='regi_share_holders21'),
    path('update_share_holders21/<id>', accounts21.update_share_holders21, name='update_share_holders21'),
    path('delete_share_holders21/<id>', accounts21.delete_share_holders21, name='delete_share_holders21'),
    path('view_deleted_share_holders21', accounts21.view_deleted_share_holders21, name='view_deleted_share_holders21'),

    path('regi_multiple_share_holders21', accounts21.regi_multiple_share_holders21, name='regi_multiple_share_holders21'),

    #############BRANCH SETTINGS START HERE ########################

    path('guest_rent_update_ob_ch21/', branch_settings21.guest_rent_update_ob_ch21, name='guest_rent_update_ob_ch21'),

    ############BRANCH SETTINGS END HERE ############################

]

