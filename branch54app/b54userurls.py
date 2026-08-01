from django.urls import path, include

from . import admin_branch54
from . import admin_branch54
from . import branch54
from . import reports54
from . import payment54
from . import admin_dashboard_calculations_br54
from . import accounts54

urlpatterns = [

    path('branch1_dashboard_ob_ch54/', branch54.branch1_dashboard_ob_ch54, name='branch1_dashboard_ob_ch54'),
    path('branch1_dashboard54/',branch54.branch1_dashboard54,name='branch1_dashboard54'),
    path('user_dashboard_calculations_ob_ch54/',branch54.user_dashboard_calculations_ob_ch54,name='user_dashboard_calculations_ob_ch54'),

    path('background_ob_ch54',branch54.background_ob_ch54,name='background_ob_ch54'),
    path('background_regi_ob_ch54',branch54.background_regi_ob_ch54,name='background_regi_ob_ch54'),
    path('custom_background_regi_ob_ch54',branch54.custom_background_regi_ob_ch54,name='custom_background_regi_ob_ch54'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch54/',admin_branch54.branch1_room_create_regi_ob_ch54,name='branch1_room_create_regi_ob_ch54'),
    path('view_all_room_ob_ch54/',admin_branch54.view_all_room_ob_ch54,name='view_all_room_ob_ch54'),
    path('delete_room_ob_ch54/<id>',admin_branch54.delete_room_ob_ch54,name='delete_room_ob_ch54'),

    path('branch1_room_create_ob_ch54/',admin_branch54.branch1_room_create_ob_ch54,name='branch1_room_create_ob_ch54'),

    path('multiple_branch1_room_create_regi54/',admin_branch54.multiple_branch1_room_create_regi54,name='multiple_branch1_room_create_regi54'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch54/', admin_branch54.pg1_bed_create_regi_ob_ch54, name='pg1_bed_create_regi_ob_ch54'),
    path('pg1_view_all_beds_ob_ch54/', admin_branch54.pg1_view_all_beds_ob_ch54, name='pg1_view_all_beds_ob_ch54'),
    path('delete_bed_ob_ch54/<id>', admin_branch54.delete_bed_ob_ch54, name='delete_bed_ob_ch54'),

    path('pg1_bed_create_ob_ch54/', admin_branch54.pg1_bed_create_ob_ch54, name='pg1_bed_create_ob_ch54'),

    path('single_pg1_bed_create_regi_ob_ch54/',admin_branch54.single_pg1_bed_create_regi_ob_ch54,name='single_pg1_bed_create_regi_ob_ch54'),
    path('update_bed_basic_details_ob_ch54/<id>',admin_branch54.update_bed_basic_details_ob_ch54, name='update_bed_basic_details_ob_ch54'),

    path('multiple_single_pg1_bed_create_regi54/',admin_branch54.multiple_single_pg1_bed_create_regi54,name='multiple_single_pg1_bed_create_regi54'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch54/<id>',branch54.br1_admit_guest_ob_ch54,name='br1_admit_guest_ob_ch54'),
    path('view_all_new_guest_ob_ch54/',branch54.view_all_new_guest_ob_ch54,name='view_all_new_guest_ob_ch54'),
    path('update_br1_admit_guest_ob_ch54/<id>',branch54.update_br1_admit_guest_ob_ch54,name='update_br1_admit_guest_ob_ch54'),
    path('vacate_br1_guest_ob_ch54/<id>',branch54.vacate_br1_guest_ob_ch54,name='vacate_br1_guest_ob_ch54'),

    path('active_guest_details_ob_ch54/<guest_code>',branch54.active_guest_details_ob_ch54,name='active_guest_details_ob_ch54'),
    path('view_all_guest_ob_ch54/',branch54.view_all_guest_ob_ch54,name='view_all_guest_ob_ch54'),
    path('shift_guest_ob_ch54/<id>',branch54.shift_guest_ob_ch54,name='shift_guest_ob_ch54'),
    path('shift_guest_regi_ob_ch54/',branch54.shift_guest_regi_ob_ch54,name='shift_guest_regi_ob_ch54'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch54/',branch54.update_all_rent_ob_ch54,name='update_all_rent_ob_ch54'),

    path('multiple_br1_admit_guest54/<id>',branch54.multiple_br1_admit_guest54,name='multiple_br1_admit_guest54'),

#guest end here


##################################
#_ADVANCE_ob_ch54 START HERE
################################


    path('choose_months_advance_ob_ch54/',branch54.choose_months_advance_ob_ch54,name='choose_months_advance_ob_ch54'),

    path('jan_advance_ob_ch54/', branch54.jan_advance_ob_ch54, name='jan_advance_ob_ch54'),
    path('jan_make_payments_advance_ob_ch54/<id>', branch54.jan_make_payments_advance_ob_ch54,name='jan_make_payments_advance_ob_ch54'),
    path('feb_advance_ob_ch54/', branch54.feb_advance_ob_ch54, name='feb_advance_ob_ch54'),
    path('feb_make_payments_advance_ob_ch54/<id>', branch54.feb_make_payments_advance_ob_ch54,name='feb_make_payments_advance_ob_ch54'),
    path('march_advance_ob_ch54/', branch54.march_advance_ob_ch54, name='march_advance_ob_ch54'),
    path('march_make_payments_advance_ob_ch54/<id>', branch54.march_make_payments_advance_ob_ch54,name='march_make_payments_advance_ob_ch54'),
    path('april_advance_ob_ch54/', branch54.april_advance_ob_ch54, name='april_advance_ob_ch54'),
    path('april_make_payments_advance_ob_ch54/<id>', branch54.april_make_payments_advance_ob_ch54, name='april_make_payments_advance_ob_ch54'),

    path('may_advance_ob_ch54/',branch54.may_advance_ob_ch54,name='may_advance_ob_ch54'),
    path('may_make_payments_advance_ob_ch54/<id>', branch54.may_make_payments_advance_ob_ch54, name='may_make_payments_advance_ob_ch54'),
    path('june_advance_ob_ch54/',branch54.june_advance_ob_ch54,name='june_advance_ob_ch54'),
    path('june_make_payments_advance_ob_ch54/<id>', branch54.june_make_payments_advance_ob_ch54, name='june_make_payments_advance_ob_ch54'),
    path('july_advance_ob_ch54/',branch54.july_advance_ob_ch54,name='july_advance_ob_ch54'),
    path('july_make_payments_advance_ob_ch54/<id>', branch54.july_make_payments_advance_ob_ch54, name='july_make_payments_advance_ob_ch54'),
    path('auguest_advance_ob_ch54/', branch54.auguest_advance_ob_ch54, name='auguest_advance_ob_ch54'),
    path('auguest_make_payments_advance_ob_ch54/<id>', branch54.auguest_make_payments_advance_ob_ch54, name='auguest_make_payments_advance_ob_ch54'),

    path('sept_advance_ob_ch54/', branch54.sept_advance_ob_ch54, name='sept_advance_ob_ch54'),
    path('sept_make_payments_advance_ob_ch54/<id>', branch54.sept_make_payments_advance_ob_ch54,name='sept_make_payments_advance_ob_ch54'),
    path('october_advance_ob_ch54/', branch54.october_advance_ob_ch54, name='october_advance_ob_ch54'),
    path('october_make_payments_advance_ob_ch54/<id>', branch54.october_make_payments_advance_ob_ch54, name='october_make_payments_advance_ob_ch54'),
    path('nov_advance_ob_ch54/', branch54.nov_advance_ob_ch54, name='nov_advance_ob_ch54'),
    path('nov_make_payments_advance_ob_ch54/<id>', branch54.nov_make_payments_advance_ob_ch54,name='nov_make_payments_advance_ob_ch54'),
    path('dec_advance_ob_ch54/', branch54.dec_advance_ob_ch54, name='dec_advance_ob_ch54'),
    path('dec_make_payments_advance_ob_ch54/<id>', branch54.dec_make_payments_advance_ob_ch54, name='dec_make_payments_advance_ob_ch54'),



##################################
#_ADVANCE_ob_ch54 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch54/',branch54.choose_months_ob_ch54,name='choose_months_ob_ch54'),

    path('jan_ob_ch54/',branch54.jan_ob_ch54,name='jan_ob_ch54'),
    path('jan_manke_payments_ob_ch54/<id>',branch54.jan_manke_payments_ob_ch54,name='jan_manke_payments_ob_ch54'),

    path('feb_ob_ch54/',branch54.feb_ob_ch54,name='feb_ob_ch54'),
    path('feb_manke_payments_ob_ch54/<id>',branch54.feb_manke_payments_ob_ch54,name='feb_manke_payments_ob_ch54'),

    path('march_ob_ch54/',branch54.march_ob_ch54,name='march_ob_ch54'),
    path('march_manke_payments_ob_ch54/<id>',branch54.march_manke_payments_ob_ch54,name='march_manke_payments_ob_ch54'),

    path('april_ob_ch54/',branch54.april_ob_ch54,name='april_ob_ch54'),
    path('april_make_payments_ob_ch54/<id>',branch54.april_make_payments_ob_ch54,name='april_make_payments_ob_ch54'),

    path('may_ob_ch54/',branch54.may_ob_ch54,name='may_ob_ch54'),
    path('may_make_payments_ob_ch54/<id>',branch54.may_make_payments_ob_ch54,name='may_make_payments_ob_ch54'),

    path('june_ob_ch54/',branch54.june_ob_ch54,name='june_ob_ch54'),
    path('june_make_payments_ob_ch54/<id>',branch54.june_make_payments_ob_ch54,name='june_make_payments_ob_ch54'),

    path('july_ob_ch54/',branch54.july_ob_ch54,name='july_ob_ch54'),
    path('july_make_payments_ob_ch54/<id>',branch54.july_make_payments_ob_ch54,name='july_make_payments_ob_ch54'),

    path('aug_ob_ch54/',branch54.aug_ob_ch54,name='aug_ob_ch54'),
    path('aug_make_payments_ob_ch54/<id>',branch54.aug_make_payments_ob_ch54,name='aug_make_payments_ob_ch54'),

    path('sept_ob_ch54/',branch54.sept_ob_ch54,name='sept_ob_ch54'),
    path('sept_make_payments_ob_ch54/<id>',branch54.sept_make_payments_ob_ch54,name='sept_make_payments_ob_ch54'),

    path('oct_ob_ch54/',branch54.oct_ob_ch54,name='oct_ob_ch54'),
    path('oct_make_payments_ob_ch54/<id>',branch54.oct_make_payments_ob_ch54,name='oct_make_payments_ob_ch54'),

    path('nov_ob_ch54/',branch54.nov_ob_ch54,name='nov_ob_ch54'),
    path('nov_make_payments_ob_ch54/<id>',branch54.nov_make_payments_ob_ch54,name='nov_make_payments_ob_ch54'),

    path('dec_ob_ch54/',branch54.dec_ob_ch54,name='dec_ob_ch54'),
    path('dec_make_payments_ob_ch54/<id>',branch54.dec_make_payments_ob_ch54,name='dec_make_payments_ob_ch54'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch54/', payment54.choose_user_ob_ch54, name='choose_user_ob_ch54'),
    path('payment_user_details_ob_ch54/<id>', payment54.payment_user_details_ob_ch54, name='payment_user_details_ob_ch54'),
    path('close_choose_user_ob_ch54/<id>',payment54.close_choose_user_ob_ch54,name='close_choose_user_ob_ch54'),

    path('monthly_jan_make_payments_ob_ch54/<id>', payment54.monthly_jan_make_payments_ob_ch54, name='monthly_jan_make_payments_ob_ch54'),
    path('monthly_feb_make_payments_ob_ch54/<id>', payment54.monthly_feb_make_payments_ob_ch54, name='monthly_feb_make_payments_ob_ch54'),
    path('monthly_march_make_payments_ob_ch54/<id>', payment54.monthly_march_make_payments_ob_ch54, name='monthly_march_make_payments_ob_ch54'),
    path('monthly_april_make_payments_ob_ch54/<id>', payment54.monthly_april_make_payments_ob_ch54, name='monthly_april_make_payments_ob_ch54'),
    path('monthly_may_make_payments_ob_ch54/<id>', payment54.monthly_may_make_payments_ob_ch54, name='monthly_may_make_payments_ob_ch54'),
    path('monthly_june_make_payments_ob_ch54/<id>', payment54.monthly_june_make_payments_ob_ch54, name='monthly_june_make_payments_ob_ch54'),

    path('monthly_july_make_payments_ob_ch54/<id>', payment54.monthly_july_make_payments_ob_ch54, name='monthly_july_make_payments_ob_ch54'),
    path('monthly_aug_make_payments_ob_ch54/<id>', payment54.monthly_aug_make_payments_ob_ch54, name='monthly_aug_make_payments_ob_ch54'),
    path('monthly_sept_make_payments_ob_ch54/<id>', payment54.monthly_sept_make_payments_ob_ch54, name='monthly_sept_make_payments_ob_ch54'),
    path('monthly_oct_make_payments_ob_ch54/<id>', payment54.monthly_oct_make_payments_ob_ch54, name='monthly_oct_make_payments_ob_ch54'),
    path('monthly_nov_make_payments_ob_ch54/<id>', payment54.monthly_nov_make_payments_ob_ch54, name='monthly_nov_make_payments_ob_ch54'),
    path('monthly_dec_make_payments_ob_ch54/<id>', payment54.monthly_dec_make_payments_ob_ch54, name='monthly_dec_make_payments_ob_ch54'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch54/',branch54.unpaid_rent_choose_months_ob_ch54,name='unpaid_rent_choose_months_ob_ch54'),

    path('jan_unpaid_rent_ob_ch54/', branch54.jan_unpaid_rent_ob_ch54, name='jan_unpaid_rent_ob_ch54'),
    path('table_jan_unpaid_rent_ob_ch54/', branch54.table_jan_unpaid_rent_ob_ch54, name='table_jan_unpaid_rent_ob_ch54'),
    path('feb_unpaid_rent_ob_ch54/', branch54.feb_unpaid_rent_ob_ch54, name='feb_unpaid_rent_ob_ch54'),
    path('table_feb_unpaid_rent_ob_ch54/', branch54.table_feb_unpaid_rent_ob_ch54, name='table_feb_unpaid_rent_ob_ch54'),
    path('mar_unpaid_rent_ob_ch54/', branch54.mar_unpaid_rent_ob_ch54, name='mar_unpaid_rent_ob_ch54'),
    path('table_mar_unpaid_rent_ob_ch54/', branch54.table_mar_unpaid_rent_ob_ch54, name='table_mar_unpaid_rent_ob_ch54'),
    path('april_unpaid_rent_ob_ch54/', branch54.april_unpaid_rent_ob_ch54, name='april_unpaid_rent_ob_ch54'),
    path('table_april_unpaid_rent_ob_ch54/', branch54.table_april_unpaid_rent_ob_ch54, name='table_april_unpaid_rent_ob_ch54'),

    path('may_unpaid_rent_ob_ch54/', branch54.may_unpaid_rent_ob_ch54, name='may_unpaid_rent_ob_ch54'),
    path('table_may_unpaid_rent_ob_ch54/', branch54.table_may_unpaid_rent_ob_ch54, name='table_may_unpaid_rent_ob_ch54'),
    path('june_unpaid_rent_ob_ch54/', branch54.june_unpaid_rent_ob_ch54, name='june_unpaid_rent_ob_ch54'),
    path('table_june_unpaid_rent_ob_ch54/', branch54.table_june_unpaid_rent_ob_ch54, name='table_june_unpaid_rent_ob_ch54'),
    path('july_unpaid_rent_ob_ch54/', branch54.july_unpaid_rent_ob_ch54, name='july_unpaid_rent_ob_ch54'),
    path('table_july_unpaid_rent_ob_ch54',branch54.table_july_unpaid_rent_ob_ch54,name='table_july_unpaid_rent_ob_ch54'),
    path('aug_unpaid_rent_ob_ch54/', branch54.aug_unpaid_rent_ob_ch54, name='aug_unpaid_rent_ob_ch54'),
    path('table_aug_unpaid_rent_ob_ch54/',branch54.table_aug_unpaid_rent_ob_ch54,name='table_aug_unpaid_rent_ob_ch54'),

    path('sept_unpaid_rent_ob_ch54/', branch54.sept_unpaid_rent_ob_ch54, name='sept_unpaid_rent_ob_ch54'),
    path('table_sept_unpaid_rent_ob_ch54/', branch54.table_sept_unpaid_rent_ob_ch54, name='table_sept_unpaid_rent_ob_ch54'),
    path('oct_unpaid_rent_ob_ch54/', branch54.oct_unpaid_rent_ob_ch54, name='oct_unpaid_rent_ob_ch54'),
    path('table_oct_unpaid_rent_ob_ch54/', branch54.table_oct_unpaid_rent_ob_ch54, name='table_oct_unpaid_rent_ob_ch54'),
    path('nov_unpaid_rent_ob_ch54/', branch54.nov_unpaid_rent_ob_ch54, name='nov_unpaid_rent_ob_ch54'),
    path('table_nov_unpaid_rent_ob_ch54/', branch54.table_nov_unpaid_rent_ob_ch54, name='table_nov_unpaid_rent_ob_ch54'),
    path('dec_unpaid_rent_ob_ch54/', branch54.dec_unpaid_rent_ob_ch54, name='dec_unpaid_rent_ob_ch54'),
    path('table_dec_unpaid_rent_ob_ch54/', branch54.table_dec_unpaid_rent_ob_ch54, name='table_dec_unpaid_rent_ob_ch54'),

    path('details_of_unpaid_guests_ob_ch54/<id>',branch54.details_of_unpaid_guests_ob_ch54,name='details_of_unpaid_guests_ob_ch54'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch54/',branch54.paid_rent_choose_months_ob_ch54,name='paid_rent_choose_months_ob_ch54'),
    path('partially_paid_guest_choose_months_ob_ch54/',reports54.partially_paid_guest_choose_months_ob_ch54,name='partially_paid_guest_choose_months_ob_ch54'),

    path('jan_paid_rent_ob_ch54/', branch54.jan_paid_rent_ob_ch54, name='jan_paid_rent_ob_ch54'),
    path('table_jan_paid_rent_ob_ch54/', branch54.table_jan_paid_rent_ob_ch54, name='table_jan_paid_rent_ob_ch54'),
    path('jan_full_paid_guest_ob_ch54/', reports54.jan_full_paid_guest_ob_ch54, name='jan_full_paid_guest_ob_ch54'),
    path('jan_partially_paid_guest_ob_ch54/', reports54.jan_partially_paid_guest_ob_ch54, name='jan_partially_paid_guest_ob_ch54'),
    path('table_jan_partially_paid_guest_ob_ch54/', reports54.table_jan_partially_paid_guest_ob_ch54,name='table_jan_partially_paid_guest_ob_ch54'),

    path('feb_paid_rent_ob_ch54/', branch54.feb_paid_rent_ob_ch54, name='feb_paid_rent_ob_ch54'),
    path('table_feb_paid_rent_ob_ch54/', branch54.table_feb_paid_rent_ob_ch54, name='table_feb_paid_rent_ob_ch54'),
    path('feb_full_paid_guest_ob_ch54/', reports54.feb_full_paid_guest_ob_ch54, name='feb_full_paid_guest_ob_ch54'),
    path('feb_partially_paid_guest_ob_ch54/', reports54.feb_partially_paid_guest_ob_ch54, name='feb_partially_paid_guest_ob_ch54'),
    path('table_feb_partially_paid_guest_ob_ch54/', reports54.table_feb_partially_paid_guest_ob_ch54,name='table_feb_partially_paid_guest_ob_ch54'),

    path('mar_paid_rent_ob_ch54/', branch54.mar_paid_rent_ob_ch54, name='mar_paid_rent_ob_ch54'),
    path('table_mar_paid_rent_ob_ch54/', branch54.table_mar_paid_rent_ob_ch54, name='table_mar_paid_rent_ob_ch54'),
    path('march_full_paid_guest_ob_ch54/', reports54.march_full_paid_guest_ob_ch54, name='march_full_paid_guest_ob_ch54'),
    path('march_partially_paid_guest_ob_ch54/', reports54.march_partially_paid_guest_ob_ch54, name='march_partially_paid_guest_ob_ch54'),
    path('table_march_partially_paid_guest_ob_ch54/', reports54.table_march_partially_paid_guest_ob_ch54,name='table_march_partially_paid_guest_ob_ch54'),

    path('april_paid_rent_ob_ch54/', branch54.april_paid_rent_ob_ch54, name='april_paid_rent_ob_ch54'),
    path('table_april_paid_rent_ob_ch54/', branch54.table_april_paid_rent_ob_ch54, name='table_april_paid_rent_ob_ch54'),
    path('april_full_paid_guest_ob_ch54/', reports54.april_full_paid_guest_ob_ch54, name='april_full_paid_guest_ob_ch54'),
    path('april_partially_paid_guest_ob_ch54/', reports54.april_partially_paid_guest_ob_ch54, name='april_partially_paid_guest_ob_ch54'),
    path('table_april_partially_paid_guest_ob_ch54/', reports54.table_april_partially_paid_guest_ob_ch54,name='table_april_partially_paid_guest_ob_ch54'),

    path('may_paid_rent_ob_ch54/', branch54.may_paid_rent_ob_ch54, name='may_paid_rent_ob_ch54'),
    path('table_may_paid_rent_ob_ch54/', branch54.table_may_paid_rent_ob_ch54, name='table_may_paid_rent_ob_ch54'),
    path('may_full_paid_guest_ob_ch54/', reports54.may_full_paid_guest_ob_ch54, name='may_full_paid_guest_ob_ch54'),
    path('may_partially_paid_guest_ob_ch54/', reports54.may_partially_paid_guest_ob_ch54, name='may_partially_paid_guest_ob_ch54'),
    path('table_may_partially_paid_guest_ob_ch54/', reports54.table_may_partially_paid_guest_ob_ch54, name='table_may_partially_paid_guest_ob_ch54'),

    path('june_paid_rent_ob_ch54/', branch54.june_paid_rent_ob_ch54, name='june_paid_rent_ob_ch54'),
    path('table_june_paid_rent_ob_ch54/', branch54.table_june_paid_rent_ob_ch54, name='table_june_paid_rent_ob_ch54'),
    path('june_full_paid_guest_ob_ch54/', reports54.june_full_paid_guest_ob_ch54, name='june_full_paid_guest_ob_ch54'),
    path('june_partially_paid_guest_ob_ch54/', reports54.june_partially_paid_guest_ob_ch54, name='june_partially_paid_guest_ob_ch54'),
    path('table_june_partially_paid_guest_ob_ch54/', reports54.table_june_partially_paid_guest_ob_ch54, name='table_june_partially_paid_guest_ob_ch54'),

    path('july_paid_rent_ob_ch54/', branch54.july_paid_rent_ob_ch54, name='july_paid_rent_ob_ch54'),
    path('table_july_paid_rent_ob_ch54/', branch54.table_july_paid_rent_ob_ch54, name='table_july_paid_rent_ob_ch54'),
    path('july_full_paid_guest_ob_ch54/', reports54.july_full_paid_guest_ob_ch54, name='july_full_paid_guest_ob_ch54'),
    path('july_partially_paid_guest_ob_ch54/', reports54.july_partially_paid_guest_ob_ch54, name='july_partially_paid_guest_ob_ch54'),
    path('table_july_partially_paid_guest_ob_ch54/', reports54.table_july_partially_paid_guest_ob_ch54, name='table_july_partially_paid_guest_ob_ch54'),

    path('aug_paid_rent_ob_ch54/', branch54.aug_paid_rent_ob_ch54, name='aug_paid_rent_ob_ch54'),
    path('table_aug_paid_rent_ob_ch54/', branch54.table_aug_paid_rent_ob_ch54, name='table_aug_paid_rent_ob_ch54'),
    path('auguest_full_paid_guest_ob_ch54/', reports54.auguest_full_paid_guest_ob_ch54, name='auguest_full_paid_guest_ob_ch54'),
    path('auguest_partially_paid_guest_ob_ch54/', reports54.auguest_partially_paid_guest_ob_ch54,name='auguest_partially_paid_guest_ob_ch54'),
    path('table_auguest_partially_paid_guest_ob_ch54/', reports54.table_auguest_partially_paid_guest_ob_ch54,name='table_auguest_partially_paid_guest_ob_ch54'),

    path('sept_paid_rent_ob_ch54/', branch54.sept_paid_rent_ob_ch54, name='sept_paid_rent_ob_ch54'),
    path('table_sept_paid_rent_ob_ch54/', branch54.table_sept_paid_rent_ob_ch54, name='table_sept_paid_rent_ob_ch54'),
    path('sept_full_paid_guest_ob_ch54/', reports54.sept_full_paid_guest_ob_ch54, name='sept_full_paid_guest_ob_ch54'),
    path('sept_partially_paid_guest_ob_ch54/', reports54.sept_partially_paid_guest_ob_ch54, name='sept_partially_paid_guest_ob_ch54'),
    path('table_sept_partially_paid_guest_ob_ch54/', reports54.table_sept_partially_paid_guest_ob_ch54,name='table_sept_partially_paid_guest_ob_ch54'),

    path('oct_paid_rent_ob_ch54/', branch54.oct_paid_rent_ob_ch54, name='oct_paid_rent_ob_ch54'),
    path('table_oct_paid_rent_ob_ch54/', branch54.table_oct_paid_rent_ob_ch54, name='table_oct_paid_rent_ob_ch54'),
    path('october_full_paid_guest_ob_ch54/', reports54.october_full_paid_guest_ob_ch54, name='october_full_paid_guest_ob_ch54'),
    path('october_partially_paid_guest_ob_ch54/', reports54.october_partially_paid_guest_ob_ch54,name='october_partially_paid_guest_ob_ch54'),
    path('table_october_partially_paid_guest_ob_ch54/', reports54.table_october_partially_paid_guest_ob_ch54,name='table_october_partially_paid_guest_ob_ch54'),

    path('nov_paid_rent_ob_ch54/', branch54.nov_paid_rent_ob_ch54, name='nov_paid_rent_ob_ch54'),
    path('table_nov_paid_rent_ob_ch54/', branch54.table_nov_paid_rent_ob_ch54, name='table_nov_paid_rent_ob_ch54'),
    path('nov_full_paid_guest_ob_ch54/', reports54.nov_full_paid_guest_ob_ch54, name='nov_full_paid_guest_ob_ch54'),
    path('nov_partially_paid_guest_ob_ch54/', reports54.nov_partially_paid_guest_ob_ch54, name='nov_partially_paid_guest_ob_ch54'),
    path('table_nov_partially_paid_guest_ob_ch54/', reports54.table_nov_partially_paid_guest_ob_ch54,name='table_nov_partially_paid_guest_ob_ch54'),

    path('dec_paid_rent_ob_ch54/', branch54.dec_paid_rent_ob_ch54, name='dec_paid_rent_ob_ch54'),
    path('table_dec_paid_rent_ob_ch54/', branch54.table_dec_paid_rent_ob_ch54, name='table_dec_paid_rent_ob_ch54'),
    path('dec_full_paid_guest_ob_ch54/', reports54.dec_full_paid_guest_ob_ch54, name='dec_full_paid_guest_ob_ch54'),
    path('dec_partially_paid_guest_ob_ch54/', reports54.dec_partially_paid_guest_ob_ch54, name='dec_partially_paid_guest_ob_ch54'),
    path('table_dec_partially_paid_guest_ob_ch54/', reports54.table_dec_partially_paid_guest_ob_ch54,name='table_dec_partially_paid_guest_ob_ch54'),

    path('details_of_paid_guests_ob_ch54/<id>',branch54.details_of_paid_guests_ob_ch54,name='details_of_paid_guests_ob_ch54'),
    path('full_paid_guest_ob_ch54/',reports54.full_paid_guest_ob_ch54,name='full_paid_guest_ob_ch54'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch54/',branch54.viewall_vacate_guest_ob_ch54,name='viewall_vacate_guest_ob_ch54'),
    path('details_of_vacate_guest_ob_ch54/<id>',branch54.details_of_vacate_guest_ob_ch54,name='details_of_vacate_guest_ob_ch54'),
    path('full_vacated_guest_details_ob_ch54',branch54.full_vacated_guest_details_ob_ch54,name='full_vacated_guest_details_ob_ch54'),
    path('full_vacated_guest_table_ob_ch54',branch54.full_vacated_guest_table_ob_ch54,name='full_vacated_guest_table_ob_ch54'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch54/<id>', branch54.jan_manke_payments_vacate_ob_ch54, name='jan_manke_payments_vacate_ob_ch54'),
    path('feb_manke_payments_vacate_ob_ch54/<id>', branch54.feb_manke_payments_vacate_ob_ch54, name='feb_manke_payments_vacate_ob_ch54'),
    path('march_manke_payments_vacate_ob_ch54/<id>', branch54.march_manke_payments_vacate_ob_ch54, name='march_manke_payments_vacate_ob_ch54'),
    path('april_make_payments_vacate_ob_ch54/<id>', branch54.april_make_payments_vacate_ob_ch54, name='april_make_payments_vacate_ob_ch54'),

    path('may_make_payments_vacate_ob_ch54/<id>', branch54.may_make_payments_vacate_ob_ch54, name='may_make_payments_vacate_ob_ch54'),
    path('june_make_payments_vacate_ob_ch54/<id>', branch54.june_make_payments_vacate_ob_ch54, name='june_make_payments_vacate_ob_ch54'),
    path('july_make_payments_vacate_ob_ch54/<id>', branch54.july_make_payments_vacate_ob_ch54, name='july_make_payments_vacate_ob_ch54'),
    path('aug_make_payments_vacate_ob_ch54/<id>', branch54.aug_make_payments_vacate_ob_ch54, name='aug_make_payments_vacate_ob_ch54'),

    path('sept_make_payments_vacate_ob_ch54/<id>', branch54.sept_make_payments_vacate_ob_ch54, name='sept_make_payments_vacate_ob_ch54'),
    path('oct_make_payments_vacate_ob_ch54/<id>', branch54.oct_make_payments_vacate_ob_ch54, name='oct_make_payments_vacate_ob_ch54'),
    path('nov_make_payments_vacate_ob_ch54/<id>', branch54.nov_make_payments_vacate_ob_ch54, name='nov_make_payments_vacate_ob_ch54'),
    path('dec_make_payments_vacate_ob_ch54/<id>', branch54.dec_make_payments_vacate_ob_ch54, name='dec_make_payments_vacate_ob_ch54'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch54/',branch54.detail_guest_general_ob_ch54,name='detail_guest_general_ob_ch54'),

    path('jan_print_ob_ch54/',branch54.jan_print_ob_ch54,name='jan_print_ob_ch54'),
    path('feb_print_ob_ch54/',branch54.feb_print_ob_ch54,name='feb_print_ob_ch54'),
    path('march_print_ob_ch54/',branch54.march_print_ob_ch54,name='march_print_ob_ch54'),
    path('april_print_ob_ch54/',branch54.april_print_ob_ch54,name='april_print_ob_ch54'),

    path('may_print_ob_ch54/',branch54.may_print_ob_ch54,name='may_print_ob_ch54'),
    path('june_print_ob_ch54/',branch54.june_print_ob_ch54,name='june_print_ob_ch54'),
    path('july_print_ob_ch54/', branch54.july_print_ob_ch54, name='july_print_ob_ch54'),
    path('aug_print_ob_ch54/', branch54.aug_print_ob_ch54, name='aug_print_ob_ch54'),

    path('sept_print_ob_ch54/', branch54.sept_print_ob_ch54, name='sept_print_ob_ch54'),
    path('oct_print_ob_ch54/', branch54.oct_print_ob_ch54, name='oct_print_ob_ch54'),
    path('nov_print_ob_ch54/', branch54.nov_print_ob_ch54, name='nov_print_ob_ch54'),
    path('dec_print_ob_ch54/', branch54.dec_print_ob_ch54, name='dec_print_ob_ch54'),

    path('new_year_jan_print_ob_ch54/', branch54.new_year_jan_print_ob_ch54, name='new_year_jan_print_ob_ch54'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch54/', branch54.jan_close_ob_ch54, name='jan_close_ob_ch54'),
    path('jan_close_decision_page_ob_ch54/', branch54.jan_close_decision_page_ob_ch54, name='jan_close_decision_page_ob_ch54'),
    path('feb_close/', branch54.feb_close_ob_ch54, name='feb_close_ob_ch54'),
    path('feb_close_decision_page_ob_ch54/', branch54.feb_close_decision_page_ob_ch54, name='feb_close_decision_page_ob_ch54'),
    path('mar_close_ob_ch54/', branch54.mar_close_ob_ch54, name='mar_close_ob_ch54'),
    path('mar_close_decision_page/', branch54.mar_close_decision_page_ob_ch54, name='mar_close_decision_page_ob_ch54'),
    path('apr_close_ob_ch54/', branch54.apr_close_ob_ch54, name='apr_close_ob_ch54'),
    path('apr_close_decision_page_ob_ch54/', branch54.apr_close_decision_page_ob_ch54, name='apr_close_decision_page_ob_ch54'),

    path('may_close_ob_ch54/', branch54.may_close_ob_ch54, name='may_close_ob_ch54'),
    path('may_close_decision_page_ob_ch54/', branch54.may_close_decision_page_ob_ch54, name='may_close_decision_page_ob_ch54'),
    path('jun_close_ob_ch54/', branch54.jun_close_ob_ch54, name='jun_close_ob_ch54'),
    path('jun_close_decision_page_ob_ch54/', branch54.jun_close_decision_page_ob_ch54, name='jun_close_decision_page_ob_ch54'),
    path('jul_close_ob_ch54/', branch54.jul_close_ob_ch54, name='jul_close_ob_ch54'),
    path('jul_close_decision_page_ob_ch54/', branch54.jul_close_decision_page_ob_ch54, name='jul_close_decision_page_ob_ch54'),
    path('aug_close_ob_ch54/', branch54.aug_close_ob_ch54, name='aug_close_ob_ch54'),
    path('aug_close_decision_page_ob_ch54/', branch54.aug_close_decision_page_ob_ch54, name='aug_close_decision_page_ob_ch54'),

    path('sep_close_ob_ch54/', branch54.sep_close_ob_ch54, name='sep_close_ob_ch54'),
    path('sep_close_decision_page_ob_ch54/', branch54.sep_close_decision_page_ob_ch54, name='sep_close_decision_page_ob_ch54'),
    path('oct_close_ob_ch54/', branch54.oct_close_ob_ch54, name='oct_close_ob_ch54'),
    path('oct_close_decision_page_ob_ch54/', branch54.oct_close_decision_page_ob_ch54, name='oct_close_decision_page_ob_ch54'),
    path('nov_close_ob_ch54/', branch54.nov_close_ob_ch54, name='nov_close_ob_ch54'),
    path('nov_close_decision_page_ob_ch54/', branch54.nov_close_decision_page_ob_ch54, name='nov_close_decision_page_ob_ch54'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch54/',reports54.detailed_report_choose_months_ob_ch54,name='detailed_report_choose_months_ob_ch54'),

    path('jan_details_live_ob_ch54/', reports54.jan_details_live_ob_ch54, name='jan_details_live_ob_ch54'),
    path('jan_print_live_ob_ch54/', reports54.jan_print_live_ob_ch54, name='jan_print_live_ob_ch54'),
    path('feb_details_live_ob_ch54/', reports54.feb_details_live_ob_ch54, name='feb_details_live_ob_ch54'),
    path('feb_print_live_ob_ch54/', reports54.feb_print_live_ob_ch54, name='feb_print_live_ob_ch54'),
    path('march_details_live_ob_ch54/', reports54.march_details_live_ob_ch54, name='march_details_live_ob_ch54'),
    path('march_print_live_ob_ch54/', reports54.march_print_live_ob_ch54, name='march_print_live_ob_ch54'),

    path('april_details_live_ob_ch54/', reports54.april_details_live_ob_ch54, name='april_details_live_ob_ch54'),
    path('april_print_live_ob_ch54/', reports54.april_print_live_ob_ch54, name='april_print_live_ob_ch54'),
    path('may_details_live_ob_ch54/', reports54.may_details_live_ob_ch54, name='may_details_live_ob_ch54'),
    path('may_print_live_ob_ch54/', reports54.may_print_live_ob_ch54, name='may_print_live_ob_ch54'),
    path('june_details_live_ob_ch54/',reports54.june_details_live_ob_ch54,name='june_details_live_ob_ch54'),
    path('june_print_live_ob_ch54/', reports54.june_print_live_ob_ch54, name='june_print_live_ob_ch54'),

    path('july_details_live_ob_ch54/', reports54.july_details_live_ob_ch54, name='july_details_live_ob_ch54'),
    path('july_print_live_ob_ch54/', reports54.july_print_live_ob_ch54, name='july_print_live_ob_ch54'),
    path('auguest_details_live_ob_ch54/', reports54.auguest_details_live_ob_ch54, name='auguest_details_live_ob_ch54'),
    path('auguest_print_live_ob_ch54/', reports54.auguest_print_live_ob_ch54, name='auguest_print_live_ob_ch54'),
    path('sept_details_live_ob_ch54/', reports54.sept_details_live_ob_ch54, name='sept_details_live_ob_ch54'),
    path('sept_print_live_ob_ch54/', reports54.sept_print_live_ob_ch54, name='sept_print_live_ob_ch54'),

    path('october_details_live_ob_ch54/', reports54.october_details_live_ob_ch54, name='october_details_live_ob_ch54'),
    path('october_print_live_ob_ch54/', reports54.october_print_live_ob_ch54, name='october_print_live_ob_ch54'),
    path('nov_details_live_ob_ch54/', reports54.nov_details_live_ob_ch54, name='nov_details_live_ob_ch54'),
    path('nov_print_live_ob_ch54/', reports54.nov_print_live_ob_ch54, name='nov_print_live_ob_ch54'),
    path('dec_details_live_ob_ch54/', reports54.dec_details_live_ob_ch54, name='dec_details_live_ob_ch54'),
    path('dec_print_live_ob_ch54/', reports54.dec_print_live_ob_ch54, name='dec_print_live_ob_ch54'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch54/', reports54.viewall_vaccant_room_ob_ch54, name='viewall_vaccant_room_ob_ch54'),

    path('d_ob_ch54/', branch54.dynamic, name='dynamic'),

    path('manage_bed_ob_ch54/', branch54.manage_bed_ob_ch54, name='manage_bed_ob_ch54'),
    path('manage_new_guest_ob_ch54/', branch54.manage_new_guest_ob_ch54, name='manage_new_guest_ob_ch54'),
    path('manage_update_new_guest_ob_ch54/<id>', branch54.manage_update_new_guest_ob_ch54, name='manage_update_new_guest_ob_ch54'),
    path('manage_update_beds_ob_ch54/<id>', branch54.manage_update_beds_ob_ch54, name='manage_update_beds_ob_ch54'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch54/', branch54.view_all_due_amt_ob_ch54, name='view_all_due_amt_ob_ch54'),
    path('due_amt_mgt_choose_months_ob_ch54/', branch54.due_amt_mgt_choose_months_ob_ch54, name='due_amt_mgt_choose_months_ob_ch54'),

    path('view_jan_account_details_ob_ch54/', branch54.view_jan_account_details_ob_ch54, name='view_jan_account_details_ob_ch54'),
    path('jan_account_mgt_ob_ch54/<id>',branch54.jan_account_mgt_ob_ch54,name='jan_account_mgt_ob_ch54'),
    path('view_feb_account_details_ob_ch54/', branch54.view_feb_account_details_ob_ch54, name='view_feb_account_details_ob_ch54'),
    path('feb_account_mgt_ob_ch54/<id>',branch54.feb_account_mgt_ob_ch54,name='feb_account_mgt_ob_ch54'),
    path('view_march_account_details_ob_ch54/', branch54.view_march_account_details_ob_ch54, name='view_march_account_details_ob_ch54'),
    path('march_account_mgt_ob_ch54/<id>',branch54.march_account_mgt_ob_ch54,name='march_account_mgt_ob_ch54'),
    path('view_april_account_details_ob_ch54/', branch54.view_april_account_details_ob_ch54, name='view_april_account_details_ob_ch54'),
    path('april_account_mgt_ob_ch54/<id>',branch54.april_account_mgt_ob_ch54,name='april_account_mgt_ob_ch54'),

    path('view_may_account_details_ob_ch54/',branch54.view_may_account_details_ob_ch54,name='view_may_account_details_ob_ch54'),
    path('may_account_mgt_ob_ch54/<id>', branch54.may_account_mgt_ob_ch54, name='may_account_mgt_ob_ch54'),
    path('view_june_account_details_ob_ch54/', branch54.view_june_account_details_ob_ch54, name='view_june_account_details_ob_ch54'),
    path('june_account_mgt_ob_ch54/<id>',branch54.june_account_mgt_ob_ch54,name='june_account_mgt_ob_ch54'),
    path('view_july_account_details_ob_ch54/', branch54.view_july_account_details_ob_ch54, name='view_july_account_details_ob_ch54'),
    path('july_account_mgt_ob_ch54/<id>',branch54.july_account_mgt_ob_ch54,name='july_account_mgt_ob_ch54'),
    path('view_auguest_account_details_ob_ch54/', branch54.view_auguest_account_details_ob_ch54, name='view_auguest_account_details_ob_ch54'),
    path('auguest_account_mgt_ob_ch54/<id>',branch54.auguest_account_mgt_ob_ch54,name='auguest_account_mgt_ob_ch54'),

    path('view_sept_account_details_ob_ch54/', branch54.view_sept_account_details_ob_ch54, name='view_sept_account_details_ob_ch54'),
    path('sept_account_mgt_ob_ch54/<id>',branch54.sept_account_mgt_ob_ch54,name='sept_account_mgt_ob_ch54'),
    path('view_october_account_details_ob_ch54/', branch54.view_october_account_details_ob_ch54, name='view_october_account_details_ob_ch54'),
    path('october_account_mgt_ob_ch54/<id>',branch54.october_account_mgt_ob_ch54,name='october_account_mgt_ob_ch54'),
    path('view_nov_account_details_ob_ch54/', branch54.view_nov_account_details_ob_ch54, name='view_nov_account_details_ob_ch54'),
    path('nov_account_mgt_ob_ch54/<id>',branch54.nov_account_mgt_ob_ch54,name='nov_account_mgt_ob_ch54'),
    path('view_dec_account_details_ob_ch54/', branch54.view_dec_account_details_ob_ch54, name='view_dec_account_details_ob_ch54'),
    path('dec_account_mgt_ob_ch54/<id>',branch54.dec_account_mgt_ob_ch54,name='dec_account_mgt_ob_ch54'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch54', admin_dashboard_calculations_br54.monthly_details_due_ob_ch54, name='monthly_details_due_ob_ch54'),
    path('monthly_collection_details_ob_ch54/', admin_dashboard_calculations_br54.monthly_collection_details_ob_ch54, name='monthly_collection_details_ob_ch54'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch54/',branch54.guest_all_ob_ch54,name='guest_all_ob_ch54'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category54/', accounts54.view_all_category54, name='view_all_category54'),
    path('create_new_category54/', accounts54.create_new_category54, name='create_new_category54'),
    path('regi_new_category54/', accounts54.regi_new_category54, name='regi_new_category54'),
    path('update_category54/<id>',accounts54.update_category54,name='update_category54'),

    path('delete_category54/<id>', accounts54.delete_category54, name='delete_category54'),
    path('view_all_category_delete54/', accounts54.view_all_category_delete54, name='view_all_category_delete54'),

    path('regi_multiple_new_category54/', accounts54.regi_multiple_new_category54, name='regi_multiple_new_category54'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items54/', accounts54.view_all_items54, name='view_all_items54'),
    path('create_new_item54/', accounts54.create_new_item54, name='create_new_item54'),
    path('regi_new_item54/', accounts54.regi_new_item54, name='regi_new_item54'),
    path('delete_item54/<id>',accounts54.delete_item54,name='delete_item54'),
    path('update_item54/<id>', accounts54.update_item54, name='update_item54'),
    path('view_all_items_delete54/',accounts54.view_all_items_delete54,name='view_all_items_delete54'),

    path('regi_multiple_new_item54/', accounts54.regi_multiple_new_item54, name='regi_multiple_new_item54'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger54/', accounts54.view_all_ledger54, name='view_all_ledger54'),
    path('create_new_ledger54/', accounts54.create_new_ledger54, name='create_new_ledger54'),
    path('regi_new_ledger54/', accounts54.regi_new_ledger54, name='regi_new_ledger54'),
    path('delete_ledger54/<id>',accounts54.delete_ledger54,name='delete_ledger54'),
    path('update_ledger54/<id>',accounts54.update_ledger54,name='update_ledger54'),
    path('view_all_ledger_delete54/',accounts54.view_all_ledger_delete54,name='view_all_ledger_delete54'),

    path('regi_multiple_new_ledger54/', accounts54.regi_multiple_new_ledger54, name='regi_multiple_new_ledger54'),

    ##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book54/', accounts54.view_all_accounts_book54, name='view_all_accounts_book54'),
    path('create_new_accounts_book54/', accounts54.create_new_accounts_book54, name='create_new_accounts_book54'),
    path('regi_new_accounts_book54/', accounts54.regi_new_accounts_book54, name='regi_new_accounts_book54'),
    path('update_accounts_book54/<id>',accounts54.update_accounts_book54,name='update_accounts_book54'),
    path('delete_accounts_book54/<id>',accounts54.delete_accounts_book54,name='delete_accounts_book54'),
    path('view_all_accounts_book_delete54/',accounts54.view_all_accounts_book_delete54,name='view_all_accounts_book_delete54'),

    path('regi_multiple_new_accounts_book54/', accounts54.regi_multiple_new_accounts_book54,name='regi_multiple_new_accounts_book54'),

    ##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries54/', accounts54.get_countries54, name='get_countries54'),

    path('in_exp_items_entry54/', accounts54.in_exp_items_entry54, name='in_exp_items_entry54'),
    path('reg_in_exp_items_entry54/', accounts54.reg_in_exp_items_entry54, name='reg_in_exp_items_entry54'),
    path('delete_journal54/<id>',accounts54.delete_journal54,name='delete_journal54'),
    path('update_in_exp_items_entry54/<id>',accounts54.update_in_exp_items_entry54,name='update_in_exp_items_entry54'),
    path('detailed_journal_report54/',accounts54.detailed_journal_report54,name='detailed_journal_report54'),
    path('journal_report_deleted54/',accounts54.journal_report_deleted54,name='journal_report_deleted54'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise54/', accounts54.daily_category_wise54, name='daily_category_wise54'),
    path('monthly_category_based_reports54/',accounts54.monthly_category_based_reports54,name='monthly_category_based_reports54'),
    path('yearly_category_based_reports54/', accounts54.yearly_category_based_reports54,name='yearly_category_based_reports54'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed54/', accounts54.daily_detailed54, name='daily_detailed54'),
    path('monthly_detailed54/',accounts54.monthly_detailed54,name='monthly_detailed54'),
    path('yearly_detailed54/',accounts54.yearly_detailed54,name='yearly_detailed54'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports54/', accounts54.item_based_reports54, name='item_based_reports54'),
    path('daily_item_based_reports54/',accounts54.daily_item_based_reports54,name='daily_item_based_reports54'),
    path('monthly_item_based_reports54/',accounts54.monthly_item_based_reports54,name='monthly_item_based_reports54'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports54/', accounts54.ledger_based_reports54, name='ledger_based_reports54'),
    path('monthly_ledger_based_reports54/', accounts54.monthly_ledger_based_reports54, name='monthly_ledger_based_reports54'),
    path('daily_ledger_based_reports54/',accounts54.daily_ledger_based_reports54,name='daily_ledger_based_reports54'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports54/', accounts54.accounts_book_based_reports54, name='accounts_book_based_reports54'),
    path('daily_accounts_book_based_reports54/',accounts54.daily_accounts_book_based_reports54,name='daily_accounts_book_based_reports54'),
    path('monthly_accounts_book_based_reports54/',accounts54.monthly_accounts_book_based_reports54,name='monthly_accounts_book_based_reports54'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months54/', accounts54.monthly_reports_choose_months54, name='monthly_reports_choose_months54'),
    path('monthly_detailed_daily_in_exp_items_report54/<mo>',accounts54.monthly_detailed_daily_in_exp_items_report54,name='monthly_detailed_daily_in_exp_items_report54'),

    path('single_monthly_reports_choose_months54/', accounts54.single_monthly_reports_choose_months54,name='single_monthly_reports_choose_months54'),
    path('single_monthly_daily_in_exp_items_report54/<mo>',accounts54.single_monthly_daily_in_exp_items_report54,name='single_monthly_daily_in_exp_items_report54'),

    path('accounts_dash_board_ob_ch54/',accounts54.accounts_dash_board_ob_ch54,name='accounts_dash_board_ob_ch54'),
    path('accounts_dash_board54/',accounts54.accounts_dash_board54,name='accounts_dash_board54'),

    path('profit_sharing_choose_months54', accounts54.profit_sharing_choose_months54,name='profit_sharing_choose_months54'),
    path('profit_sharing54/<mo>', accounts54.profit_sharing54, name='profit_sharing54'),
    path('view_share_holders54', accounts54.view_share_holders54, name='view_share_holders54'),
    path('create_share_holders54', accounts54.create_share_holders54, name='create_share_holders54'),
    path('regi_share_holders54', accounts54.regi_share_holders54, name='regi_share_holders54'),
    path('update_share_holders54/<id>', accounts54.update_share_holders54, name='update_share_holders54'),
    path('delete_share_holders54/<id>', accounts54.delete_share_holders54, name='delete_share_holders54'),
    path('view_deleted_share_holders54', accounts54.view_deleted_share_holders54, name='view_deleted_share_holders54'),

    path('regi_multiple_share_holders54', accounts54.regi_multiple_share_holders54, name='regi_multiple_share_holders54'),

]

