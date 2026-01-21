from django.urls import path, include

from . import admin_branch81
from . import admin_branch81
from . import branch81
from . import reports81
from . import payment81
from . import admin_dashboard_calculations_br81
from . import accounts81

urlpatterns = [

    path('branch1_dashboard_ob_ch81/', branch81.branch1_dashboard_ob_ch81, name='branch1_dashboard_ob_ch81'),
    path('user_dashboard_calculations_ob_ch81/',branch81.user_dashboard_calculations_ob_ch81,name='user_dashboard_calculations_ob_ch81'),

    path('background_ob_ch81',branch81.background_ob_ch81,name='background_ob_ch81'),
    path('background_regi_ob_ch81',branch81.background_regi_ob_ch81,name='background_regi_ob_ch81'),
    path('custom_background_regi_ob_ch81',branch81.custom_background_regi_ob_ch81,name='custom_background_regi_ob_ch81'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch81/',admin_branch81.branch1_room_create_regi_ob_ch81,name='branch1_room_create_regi_ob_ch81'),
    path('view_all_room_ob_ch81/',admin_branch81.view_all_room_ob_ch81,name='view_all_room_ob_ch81'),
    path('delete_room_ob_ch81/<id>',admin_branch81.delete_room_ob_ch81,name='delete_room_ob_ch81'),

    path('branch1_room_create_ob_ch81/',admin_branch81.branch1_room_create_ob_ch81,name='branch1_room_create_ob_ch81'),

    path('multiple_branch1_room_create_regi81/',admin_branch81.multiple_branch1_room_create_regi81,name='multiple_branch1_room_create_regi81'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch81/', admin_branch81.pg1_bed_create_regi_ob_ch81, name='pg1_bed_create_regi_ob_ch81'),
    path('pg1_view_all_beds_ob_ch81/', admin_branch81.pg1_view_all_beds_ob_ch81, name='pg1_view_all_beds_ob_ch81'),
    path('delete_bed_ob_ch81/<id>', admin_branch81.delete_bed_ob_ch81, name='delete_bed_ob_ch81'),

    path('pg1_bed_create_ob_ch81/', admin_branch81.pg1_bed_create_ob_ch81, name='pg1_bed_create_ob_ch81'),

    path('single_pg1_bed_create_regi_ob_ch81/',admin_branch81.single_pg1_bed_create_regi_ob_ch81,name='single_pg1_bed_create_regi_ob_ch81'),
    path('update_bed_basic_details_ob_ch81/<id>',admin_branch81.update_bed_basic_details_ob_ch81, name='update_bed_basic_details_ob_ch81'),

    path('multiple_single_pg1_bed_create_regi81/',admin_branch81.multiple_single_pg1_bed_create_regi81,name='multiple_single_pg1_bed_create_regi81'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch81/<id>',branch81.br1_admit_guest_ob_ch81,name='br1_admit_guest_ob_ch81'),
    path('view_all_new_guest_ob_ch81/',branch81.view_all_new_guest_ob_ch81,name='view_all_new_guest_ob_ch81'),
    path('update_br1_admit_guest_ob_ch81/<id>',branch81.update_br1_admit_guest_ob_ch81,name='update_br1_admit_guest_ob_ch81'),
    path('vacate_br1_guest_ob_ch81/<id>',branch81.vacate_br1_guest_ob_ch81,name='vacate_br1_guest_ob_ch81'),

    path('active_guest_details_ob_ch81/<guest_code>',branch81.active_guest_details_ob_ch81,name='active_guest_details_ob_ch81'),
    path('view_all_guest_ob_ch81/',branch81.view_all_guest_ob_ch81,name='view_all_guest_ob_ch81'),
    path('shift_guest_ob_ch81/<id>',branch81.shift_guest_ob_ch81,name='shift_guest_ob_ch81'),
    path('shift_guest_regi_ob_ch81/',branch81.shift_guest_regi_ob_ch81,name='shift_guest_regi_ob_ch81'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch81/',branch81.update_all_rent_ob_ch81,name='update_all_rent_ob_ch81'),

    path('multiple_br1_admit_guest81/<id>',branch81.multiple_br1_admit_guest81,name='multiple_br1_admit_guest81'),

#guest end here


##################################
#_ADVANCE_ob_ch81 START HERE
################################


    path('choose_months_advance_ob_ch81/',branch81.choose_months_advance_ob_ch81,name='choose_months_advance_ob_ch81'),

    path('jan_advance_ob_ch81/', branch81.jan_advance_ob_ch81, name='jan_advance_ob_ch81'),
    path('jan_make_payments_advance_ob_ch81/<id>', branch81.jan_make_payments_advance_ob_ch81,name='jan_make_payments_advance_ob_ch81'),
    path('feb_advance_ob_ch81/', branch81.feb_advance_ob_ch81, name='feb_advance_ob_ch81'),
    path('feb_make_payments_advance_ob_ch81/<id>', branch81.feb_make_payments_advance_ob_ch81,name='feb_make_payments_advance_ob_ch81'),
    path('march_advance_ob_ch81/', branch81.march_advance_ob_ch81, name='march_advance_ob_ch81'),
    path('march_make_payments_advance_ob_ch81/<id>', branch81.march_make_payments_advance_ob_ch81,name='march_make_payments_advance_ob_ch81'),
    path('april_advance_ob_ch81/', branch81.april_advance_ob_ch81, name='april_advance_ob_ch81'),
    path('april_make_payments_advance_ob_ch81/<id>', branch81.april_make_payments_advance_ob_ch81, name='april_make_payments_advance_ob_ch81'),

    path('may_advance_ob_ch81/',branch81.may_advance_ob_ch81,name='may_advance_ob_ch81'),
    path('may_make_payments_advance_ob_ch81/<id>', branch81.may_make_payments_advance_ob_ch81, name='may_make_payments_advance_ob_ch81'),
    path('june_advance_ob_ch81/',branch81.june_advance_ob_ch81,name='june_advance_ob_ch81'),
    path('june_make_payments_advance_ob_ch81/<id>', branch81.june_make_payments_advance_ob_ch81, name='june_make_payments_advance_ob_ch81'),
    path('july_advance_ob_ch81/',branch81.july_advance_ob_ch81,name='july_advance_ob_ch81'),
    path('july_make_payments_advance_ob_ch81/<id>', branch81.july_make_payments_advance_ob_ch81, name='july_make_payments_advance_ob_ch81'),
    path('auguest_advance_ob_ch81/', branch81.auguest_advance_ob_ch81, name='auguest_advance_ob_ch81'),
    path('auguest_make_payments_advance_ob_ch81/<id>', branch81.auguest_make_payments_advance_ob_ch81, name='auguest_make_payments_advance_ob_ch81'),

    path('sept_advance_ob_ch81/', branch81.sept_advance_ob_ch81, name='sept_advance_ob_ch81'),
    path('sept_make_payments_advance_ob_ch81/<id>', branch81.sept_make_payments_advance_ob_ch81,name='sept_make_payments_advance_ob_ch81'),
    path('october_advance_ob_ch81/', branch81.october_advance_ob_ch81, name='october_advance_ob_ch81'),
    path('october_make_payments_advance_ob_ch81/<id>', branch81.october_make_payments_advance_ob_ch81, name='october_make_payments_advance_ob_ch81'),
    path('nov_advance_ob_ch81/', branch81.nov_advance_ob_ch81, name='nov_advance_ob_ch81'),
    path('nov_make_payments_advance_ob_ch81/<id>', branch81.nov_make_payments_advance_ob_ch81,name='nov_make_payments_advance_ob_ch81'),
    path('dec_advance_ob_ch81/', branch81.dec_advance_ob_ch81, name='dec_advance_ob_ch81'),
    path('dec_make_payments_advance_ob_ch81/<id>', branch81.dec_make_payments_advance_ob_ch81, name='dec_make_payments_advance_ob_ch81'),



##################################
#_ADVANCE_ob_ch81 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch81/',branch81.choose_months_ob_ch81,name='choose_months_ob_ch81'),

    path('jan_ob_ch81/',branch81.jan_ob_ch81,name='jan_ob_ch81'),
    path('jan_manke_payments_ob_ch81/<id>',branch81.jan_manke_payments_ob_ch81,name='jan_manke_payments_ob_ch81'),

    path('feb_ob_ch81/',branch81.feb_ob_ch81,name='feb_ob_ch81'),
    path('feb_manke_payments_ob_ch81/<id>',branch81.feb_manke_payments_ob_ch81,name='feb_manke_payments_ob_ch81'),

    path('march_ob_ch81/',branch81.march_ob_ch81,name='march_ob_ch81'),
    path('march_manke_payments_ob_ch81/<id>',branch81.march_manke_payments_ob_ch81,name='march_manke_payments_ob_ch81'),

    path('april_ob_ch81/',branch81.april_ob_ch81,name='april_ob_ch81'),
    path('april_make_payments_ob_ch81/<id>',branch81.april_make_payments_ob_ch81,name='april_make_payments_ob_ch81'),

    path('may_ob_ch81/',branch81.may_ob_ch81,name='may_ob_ch81'),
    path('may_make_payments_ob_ch81/<id>',branch81.may_make_payments_ob_ch81,name='may_make_payments_ob_ch81'),

    path('june_ob_ch81/',branch81.june_ob_ch81,name='june_ob_ch81'),
    path('june_make_payments_ob_ch81/<id>',branch81.june_make_payments_ob_ch81,name='june_make_payments_ob_ch81'),

    path('july_ob_ch81/',branch81.july_ob_ch81,name='july_ob_ch81'),
    path('july_make_payments_ob_ch81/<id>',branch81.july_make_payments_ob_ch81,name='july_make_payments_ob_ch81'),

    path('aug_ob_ch81/',branch81.aug_ob_ch81,name='aug_ob_ch81'),
    path('aug_make_payments_ob_ch81/<id>',branch81.aug_make_payments_ob_ch81,name='aug_make_payments_ob_ch81'),

    path('sept_ob_ch81/',branch81.sept_ob_ch81,name='sept_ob_ch81'),
    path('sept_make_payments_ob_ch81/<id>',branch81.sept_make_payments_ob_ch81,name='sept_make_payments_ob_ch81'),

    path('oct_ob_ch81/',branch81.oct_ob_ch81,name='oct_ob_ch81'),
    path('oct_make_payments_ob_ch81/<id>',branch81.oct_make_payments_ob_ch81,name='oct_make_payments_ob_ch81'),

    path('nov_ob_ch81/',branch81.nov_ob_ch81,name='nov_ob_ch81'),
    path('nov_make_payments_ob_ch81/<id>',branch81.nov_make_payments_ob_ch81,name='nov_make_payments_ob_ch81'),

    path('dec_ob_ch81/',branch81.dec_ob_ch81,name='dec_ob_ch81'),
    path('dec_make_payments_ob_ch81/<id>',branch81.dec_make_payments_ob_ch81,name='dec_make_payments_ob_ch81'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch81/', payment81.choose_user_ob_ch81, name='choose_user_ob_ch81'),
    path('payment_user_details_ob_ch81/<id>', payment81.payment_user_details_ob_ch81, name='payment_user_details_ob_ch81'),
    path('close_choose_user_ob_ch81/<id>',payment81.close_choose_user_ob_ch81,name='close_choose_user_ob_ch81'),

    path('monthly_jan_make_payments_ob_ch81/<id>', payment81.monthly_jan_make_payments_ob_ch81, name='monthly_jan_make_payments_ob_ch81'),
    path('monthly_feb_make_payments_ob_ch81/<id>', payment81.monthly_feb_make_payments_ob_ch81, name='monthly_feb_make_payments_ob_ch81'),
    path('monthly_march_make_payments_ob_ch81/<id>', payment81.monthly_march_make_payments_ob_ch81, name='monthly_march_make_payments_ob_ch81'),
    path('monthly_april_make_payments_ob_ch81/<id>', payment81.monthly_april_make_payments_ob_ch81, name='monthly_april_make_payments_ob_ch81'),
    path('monthly_may_make_payments_ob_ch81/<id>', payment81.monthly_may_make_payments_ob_ch81, name='monthly_may_make_payments_ob_ch81'),
    path('monthly_june_make_payments_ob_ch81/<id>', payment81.monthly_june_make_payments_ob_ch81, name='monthly_june_make_payments_ob_ch81'),

    path('monthly_july_make_payments_ob_ch81/<id>', payment81.monthly_july_make_payments_ob_ch81, name='monthly_july_make_payments_ob_ch81'),
    path('monthly_aug_make_payments_ob_ch81/<id>', payment81.monthly_aug_make_payments_ob_ch81, name='monthly_aug_make_payments_ob_ch81'),
    path('monthly_sept_make_payments_ob_ch81/<id>', payment81.monthly_sept_make_payments_ob_ch81, name='monthly_sept_make_payments_ob_ch81'),
    path('monthly_oct_make_payments_ob_ch81/<id>', payment81.monthly_oct_make_payments_ob_ch81, name='monthly_oct_make_payments_ob_ch81'),
    path('monthly_nov_make_payments_ob_ch81/<id>', payment81.monthly_nov_make_payments_ob_ch81, name='monthly_nov_make_payments_ob_ch81'),
    path('monthly_dec_make_payments_ob_ch81/<id>', payment81.monthly_dec_make_payments_ob_ch81, name='monthly_dec_make_payments_ob_ch81'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch81/',branch81.unpaid_rent_choose_months_ob_ch81,name='unpaid_rent_choose_months_ob_ch81'),

    path('jan_unpaid_rent_ob_ch81/', branch81.jan_unpaid_rent_ob_ch81, name='jan_unpaid_rent_ob_ch81'),
    path('table_jan_unpaid_rent_ob_ch81/', branch81.table_jan_unpaid_rent_ob_ch81, name='table_jan_unpaid_rent_ob_ch81'),
    path('feb_unpaid_rent_ob_ch81/', branch81.feb_unpaid_rent_ob_ch81, name='feb_unpaid_rent_ob_ch81'),
    path('table_feb_unpaid_rent_ob_ch81/', branch81.table_feb_unpaid_rent_ob_ch81, name='table_feb_unpaid_rent_ob_ch81'),
    path('mar_unpaid_rent_ob_ch81/', branch81.mar_unpaid_rent_ob_ch81, name='mar_unpaid_rent_ob_ch81'),
    path('table_mar_unpaid_rent_ob_ch81/', branch81.table_mar_unpaid_rent_ob_ch81, name='table_mar_unpaid_rent_ob_ch81'),
    path('april_unpaid_rent_ob_ch81/', branch81.april_unpaid_rent_ob_ch81, name='april_unpaid_rent_ob_ch81'),
    path('table_april_unpaid_rent_ob_ch81/', branch81.table_april_unpaid_rent_ob_ch81, name='table_april_unpaid_rent_ob_ch81'),

    path('may_unpaid_rent_ob_ch81/', branch81.may_unpaid_rent_ob_ch81, name='may_unpaid_rent_ob_ch81'),
    path('table_may_unpaid_rent_ob_ch81/', branch81.table_may_unpaid_rent_ob_ch81, name='table_may_unpaid_rent_ob_ch81'),
    path('june_unpaid_rent_ob_ch81/', branch81.june_unpaid_rent_ob_ch81, name='june_unpaid_rent_ob_ch81'),
    path('table_june_unpaid_rent_ob_ch81/', branch81.table_june_unpaid_rent_ob_ch81, name='table_june_unpaid_rent_ob_ch81'),
    path('july_unpaid_rent_ob_ch81/', branch81.july_unpaid_rent_ob_ch81, name='july_unpaid_rent_ob_ch81'),
    path('table_july_unpaid_rent_ob_ch81',branch81.table_july_unpaid_rent_ob_ch81,name='table_july_unpaid_rent_ob_ch81'),
    path('aug_unpaid_rent_ob_ch81/', branch81.aug_unpaid_rent_ob_ch81, name='aug_unpaid_rent_ob_ch81'),
    path('table_aug_unpaid_rent_ob_ch81/',branch81.table_aug_unpaid_rent_ob_ch81,name='table_aug_unpaid_rent_ob_ch81'),

    path('sept_unpaid_rent_ob_ch81/', branch81.sept_unpaid_rent_ob_ch81, name='sept_unpaid_rent_ob_ch81'),
    path('table_sept_unpaid_rent_ob_ch81/', branch81.table_sept_unpaid_rent_ob_ch81, name='table_sept_unpaid_rent_ob_ch81'),
    path('oct_unpaid_rent_ob_ch81/', branch81.oct_unpaid_rent_ob_ch81, name='oct_unpaid_rent_ob_ch81'),
    path('table_oct_unpaid_rent_ob_ch81/', branch81.table_oct_unpaid_rent_ob_ch81, name='table_oct_unpaid_rent_ob_ch81'),
    path('nov_unpaid_rent_ob_ch81/', branch81.nov_unpaid_rent_ob_ch81, name='nov_unpaid_rent_ob_ch81'),
    path('table_nov_unpaid_rent_ob_ch81/', branch81.table_nov_unpaid_rent_ob_ch81, name='table_nov_unpaid_rent_ob_ch81'),
    path('dec_unpaid_rent_ob_ch81/', branch81.dec_unpaid_rent_ob_ch81, name='dec_unpaid_rent_ob_ch81'),
    path('table_dec_unpaid_rent_ob_ch81/', branch81.table_dec_unpaid_rent_ob_ch81, name='table_dec_unpaid_rent_ob_ch81'),

    path('details_of_unpaid_guests_ob_ch81/<id>',branch81.details_of_unpaid_guests_ob_ch81,name='details_of_unpaid_guests_ob_ch81'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch81/',branch81.paid_rent_choose_months_ob_ch81,name='paid_rent_choose_months_ob_ch81'),
    path('partially_paid_guest_choose_months_ob_ch81/',reports81.partially_paid_guest_choose_months_ob_ch81,name='partially_paid_guest_choose_months_ob_ch81'),

    path('jan_paid_rent_ob_ch81/', branch81.jan_paid_rent_ob_ch81, name='jan_paid_rent_ob_ch81'),
    path('table_jan_paid_rent_ob_ch81/', branch81.table_jan_paid_rent_ob_ch81, name='table_jan_paid_rent_ob_ch81'),
    path('jan_full_paid_guest_ob_ch81/', reports81.jan_full_paid_guest_ob_ch81, name='jan_full_paid_guest_ob_ch81'),
    path('jan_partially_paid_guest_ob_ch81/', reports81.jan_partially_paid_guest_ob_ch81, name='jan_partially_paid_guest_ob_ch81'),
    path('table_jan_partially_paid_guest_ob_ch81/', reports81.table_jan_partially_paid_guest_ob_ch81,name='table_jan_partially_paid_guest_ob_ch81'),

    path('feb_paid_rent_ob_ch81/', branch81.feb_paid_rent_ob_ch81, name='feb_paid_rent_ob_ch81'),
    path('table_feb_paid_rent_ob_ch81/', branch81.table_feb_paid_rent_ob_ch81, name='table_feb_paid_rent_ob_ch81'),
    path('feb_full_paid_guest_ob_ch81/', reports81.feb_full_paid_guest_ob_ch81, name='feb_full_paid_guest_ob_ch81'),
    path('feb_partially_paid_guest_ob_ch81/', reports81.feb_partially_paid_guest_ob_ch81, name='feb_partially_paid_guest_ob_ch81'),
    path('table_feb_partially_paid_guest_ob_ch81/', reports81.table_feb_partially_paid_guest_ob_ch81,name='table_feb_partially_paid_guest_ob_ch81'),

    path('mar_paid_rent_ob_ch81/', branch81.mar_paid_rent_ob_ch81, name='mar_paid_rent_ob_ch81'),
    path('table_mar_paid_rent_ob_ch81/', branch81.table_mar_paid_rent_ob_ch81, name='table_mar_paid_rent_ob_ch81'),
    path('march_full_paid_guest_ob_ch81/', reports81.march_full_paid_guest_ob_ch81, name='march_full_paid_guest_ob_ch81'),
    path('march_partially_paid_guest_ob_ch81/', reports81.march_partially_paid_guest_ob_ch81, name='march_partially_paid_guest_ob_ch81'),
    path('table_march_partially_paid_guest_ob_ch81/', reports81.table_march_partially_paid_guest_ob_ch81,name='table_march_partially_paid_guest_ob_ch81'),

    path('april_paid_rent_ob_ch81/', branch81.april_paid_rent_ob_ch81, name='april_paid_rent_ob_ch81'),
    path('table_april_paid_rent_ob_ch81/', branch81.table_april_paid_rent_ob_ch81, name='table_april_paid_rent_ob_ch81'),
    path('april_full_paid_guest_ob_ch81/', reports81.april_full_paid_guest_ob_ch81, name='april_full_paid_guest_ob_ch81'),
    path('april_partially_paid_guest_ob_ch81/', reports81.april_partially_paid_guest_ob_ch81, name='april_partially_paid_guest_ob_ch81'),
    path('table_april_partially_paid_guest_ob_ch81/', reports81.table_april_partially_paid_guest_ob_ch81,name='table_april_partially_paid_guest_ob_ch81'),

    path('may_paid_rent_ob_ch81/', branch81.may_paid_rent_ob_ch81, name='may_paid_rent_ob_ch81'),
    path('table_may_paid_rent_ob_ch81/', branch81.table_may_paid_rent_ob_ch81, name='table_may_paid_rent_ob_ch81'),
    path('may_full_paid_guest_ob_ch81/', reports81.may_full_paid_guest_ob_ch81, name='may_full_paid_guest_ob_ch81'),
    path('may_partially_paid_guest_ob_ch81/', reports81.may_partially_paid_guest_ob_ch81, name='may_partially_paid_guest_ob_ch81'),
    path('table_may_partially_paid_guest_ob_ch81/', reports81.table_may_partially_paid_guest_ob_ch81, name='table_may_partially_paid_guest_ob_ch81'),

    path('june_paid_rent_ob_ch81/', branch81.june_paid_rent_ob_ch81, name='june_paid_rent_ob_ch81'),
    path('table_june_paid_rent_ob_ch81/', branch81.table_june_paid_rent_ob_ch81, name='table_june_paid_rent_ob_ch81'),
    path('june_full_paid_guest_ob_ch81/', reports81.june_full_paid_guest_ob_ch81, name='june_full_paid_guest_ob_ch81'),
    path('june_partially_paid_guest_ob_ch81/', reports81.june_partially_paid_guest_ob_ch81, name='june_partially_paid_guest_ob_ch81'),
    path('table_june_partially_paid_guest_ob_ch81/', reports81.table_june_partially_paid_guest_ob_ch81, name='table_june_partially_paid_guest_ob_ch81'),

    path('july_paid_rent_ob_ch81/', branch81.july_paid_rent_ob_ch81, name='july_paid_rent_ob_ch81'),
    path('table_july_paid_rent_ob_ch81/', branch81.table_july_paid_rent_ob_ch81, name='table_july_paid_rent_ob_ch81'),
    path('july_full_paid_guest_ob_ch81/', reports81.july_full_paid_guest_ob_ch81, name='july_full_paid_guest_ob_ch81'),
    path('july_partially_paid_guest_ob_ch81/', reports81.july_partially_paid_guest_ob_ch81, name='july_partially_paid_guest_ob_ch81'),
    path('table_july_partially_paid_guest_ob_ch81/', reports81.table_july_partially_paid_guest_ob_ch81, name='table_july_partially_paid_guest_ob_ch81'),

    path('aug_paid_rent_ob_ch81/', branch81.aug_paid_rent_ob_ch81, name='aug_paid_rent_ob_ch81'),
    path('table_aug_paid_rent_ob_ch81/', branch81.table_aug_paid_rent_ob_ch81, name='table_aug_paid_rent_ob_ch81'),
    path('auguest_full_paid_guest_ob_ch81/', reports81.auguest_full_paid_guest_ob_ch81, name='auguest_full_paid_guest_ob_ch81'),
    path('auguest_partially_paid_guest_ob_ch81/', reports81.auguest_partially_paid_guest_ob_ch81,name='auguest_partially_paid_guest_ob_ch81'),
    path('table_auguest_partially_paid_guest_ob_ch81/', reports81.table_auguest_partially_paid_guest_ob_ch81,name='table_auguest_partially_paid_guest_ob_ch81'),

    path('sept_paid_rent_ob_ch81/', branch81.sept_paid_rent_ob_ch81, name='sept_paid_rent_ob_ch81'),
    path('table_sept_paid_rent_ob_ch81/', branch81.table_sept_paid_rent_ob_ch81, name='table_sept_paid_rent_ob_ch81'),
    path('sept_full_paid_guest_ob_ch81/', reports81.sept_full_paid_guest_ob_ch81, name='sept_full_paid_guest_ob_ch81'),
    path('sept_partially_paid_guest_ob_ch81/', reports81.sept_partially_paid_guest_ob_ch81, name='sept_partially_paid_guest_ob_ch81'),
    path('table_sept_partially_paid_guest_ob_ch81/', reports81.table_sept_partially_paid_guest_ob_ch81,name='table_sept_partially_paid_guest_ob_ch81'),

    path('oct_paid_rent_ob_ch81/', branch81.oct_paid_rent_ob_ch81, name='oct_paid_rent_ob_ch81'),
    path('table_oct_paid_rent_ob_ch81/', branch81.table_oct_paid_rent_ob_ch81, name='table_oct_paid_rent_ob_ch81'),
    path('october_full_paid_guest_ob_ch81/', reports81.october_full_paid_guest_ob_ch81, name='october_full_paid_guest_ob_ch81'),
    path('october_partially_paid_guest_ob_ch81/', reports81.october_partially_paid_guest_ob_ch81,name='october_partially_paid_guest_ob_ch81'),
    path('table_october_partially_paid_guest_ob_ch81/', reports81.table_october_partially_paid_guest_ob_ch81,name='table_october_partially_paid_guest_ob_ch81'),

    path('nov_paid_rent_ob_ch81/', branch81.nov_paid_rent_ob_ch81, name='nov_paid_rent_ob_ch81'),
    path('table_nov_paid_rent_ob_ch81/', branch81.table_nov_paid_rent_ob_ch81, name='table_nov_paid_rent_ob_ch81'),
    path('nov_full_paid_guest_ob_ch81/', reports81.nov_full_paid_guest_ob_ch81, name='nov_full_paid_guest_ob_ch81'),
    path('nov_partially_paid_guest_ob_ch81/', reports81.nov_partially_paid_guest_ob_ch81, name='nov_partially_paid_guest_ob_ch81'),
    path('table_nov_partially_paid_guest_ob_ch81/', reports81.table_nov_partially_paid_guest_ob_ch81,name='table_nov_partially_paid_guest_ob_ch81'),

    path('dec_paid_rent_ob_ch81/', branch81.dec_paid_rent_ob_ch81, name='dec_paid_rent_ob_ch81'),
    path('table_dec_paid_rent_ob_ch81/', branch81.table_dec_paid_rent_ob_ch81, name='table_dec_paid_rent_ob_ch81'),
    path('dec_full_paid_guest_ob_ch81/', reports81.dec_full_paid_guest_ob_ch81, name='dec_full_paid_guest_ob_ch81'),
    path('dec_partially_paid_guest_ob_ch81/', reports81.dec_partially_paid_guest_ob_ch81, name='dec_partially_paid_guest_ob_ch81'),
    path('table_dec_partially_paid_guest_ob_ch81/', reports81.table_dec_partially_paid_guest_ob_ch81,name='table_dec_partially_paid_guest_ob_ch81'),

    path('details_of_paid_guests_ob_ch81/<id>',branch81.details_of_paid_guests_ob_ch81,name='details_of_paid_guests_ob_ch81'),
    path('full_paid_guest_ob_ch81/',reports81.full_paid_guest_ob_ch81,name='full_paid_guest_ob_ch81'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch81/',branch81.viewall_vacate_guest_ob_ch81,name='viewall_vacate_guest_ob_ch81'),
    path('details_of_vacate_guest_ob_ch81/<id>',branch81.details_of_vacate_guest_ob_ch81,name='details_of_vacate_guest_ob_ch81'),
    path('full_vacated_guest_details_ob_ch81',branch81.full_vacated_guest_details_ob_ch81,name='full_vacated_guest_details_ob_ch81'),
    path('full_vacated_guest_table_ob_ch81',branch81.full_vacated_guest_table_ob_ch81,name='full_vacated_guest_table_ob_ch81'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch81/<id>', branch81.jan_manke_payments_vacate_ob_ch81, name='jan_manke_payments_vacate_ob_ch81'),
    path('feb_manke_payments_vacate_ob_ch81/<id>', branch81.feb_manke_payments_vacate_ob_ch81, name='feb_manke_payments_vacate_ob_ch81'),
    path('march_manke_payments_vacate_ob_ch81/<id>', branch81.march_manke_payments_vacate_ob_ch81, name='march_manke_payments_vacate_ob_ch81'),
    path('april_make_payments_vacate_ob_ch81/<id>', branch81.april_make_payments_vacate_ob_ch81, name='april_make_payments_vacate_ob_ch81'),

    path('may_make_payments_vacate_ob_ch81/<id>', branch81.may_make_payments_vacate_ob_ch81, name='may_make_payments_vacate_ob_ch81'),
    path('june_make_payments_vacate_ob_ch81/<id>', branch81.june_make_payments_vacate_ob_ch81, name='june_make_payments_vacate_ob_ch81'),
    path('july_make_payments_vacate_ob_ch81/<id>', branch81.july_make_payments_vacate_ob_ch81, name='july_make_payments_vacate_ob_ch81'),
    path('aug_make_payments_vacate_ob_ch81/<id>', branch81.aug_make_payments_vacate_ob_ch81, name='aug_make_payments_vacate_ob_ch81'),

    path('sept_make_payments_vacate_ob_ch81/<id>', branch81.sept_make_payments_vacate_ob_ch81, name='sept_make_payments_vacate_ob_ch81'),
    path('oct_make_payments_vacate_ob_ch81/<id>', branch81.oct_make_payments_vacate_ob_ch81, name='oct_make_payments_vacate_ob_ch81'),
    path('nov_make_payments_vacate_ob_ch81/<id>', branch81.nov_make_payments_vacate_ob_ch81, name='nov_make_payments_vacate_ob_ch81'),
    path('dec_make_payments_vacate_ob_ch81/<id>', branch81.dec_make_payments_vacate_ob_ch81, name='dec_make_payments_vacate_ob_ch81'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch81/',branch81.detail_guest_general_ob_ch81,name='detail_guest_general_ob_ch81'),

    path('jan_print_ob_ch81/',branch81.jan_print_ob_ch81,name='jan_print_ob_ch81'),
    path('feb_print_ob_ch81/',branch81.feb_print_ob_ch81,name='feb_print_ob_ch81'),
    path('march_print_ob_ch81/',branch81.march_print_ob_ch81,name='march_print_ob_ch81'),
    path('april_print_ob_ch81/',branch81.april_print_ob_ch81,name='april_print_ob_ch81'),

    path('may_print_ob_ch81/',branch81.may_print_ob_ch81,name='may_print_ob_ch81'),
    path('june_print_ob_ch81/',branch81.june_print_ob_ch81,name='june_print_ob_ch81'),
    path('july_print_ob_ch81/', branch81.july_print_ob_ch81, name='july_print_ob_ch81'),
    path('aug_print_ob_ch81/', branch81.aug_print_ob_ch81, name='aug_print_ob_ch81'),

    path('sept_print_ob_ch81/', branch81.sept_print_ob_ch81, name='sept_print_ob_ch81'),
    path('oct_print_ob_ch81/', branch81.oct_print_ob_ch81, name='oct_print_ob_ch81'),
    path('nov_print_ob_ch81/', branch81.nov_print_ob_ch81, name='nov_print_ob_ch81'),
    path('dec_print_ob_ch81/', branch81.dec_print_ob_ch81, name='dec_print_ob_ch81'),

    path('new_year_jan_print_ob_ch81/', branch81.new_year_jan_print_ob_ch81, name='new_year_jan_print_ob_ch81'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch81/', branch81.jan_close_ob_ch81, name='jan_close_ob_ch81'),
    path('jan_close_decision_page_ob_ch81/', branch81.jan_close_decision_page_ob_ch81, name='jan_close_decision_page_ob_ch81'),
    path('feb_close/', branch81.feb_close_ob_ch81, name='feb_close_ob_ch81'),
    path('feb_close_decision_page_ob_ch81/', branch81.feb_close_decision_page_ob_ch81, name='feb_close_decision_page_ob_ch81'),
    path('mar_close_ob_ch81/', branch81.mar_close_ob_ch81, name='mar_close_ob_ch81'),
    path('mar_close_decision_page/', branch81.mar_close_decision_page_ob_ch81, name='mar_close_decision_page_ob_ch81'),
    path('apr_close_ob_ch81/', branch81.apr_close_ob_ch81, name='apr_close_ob_ch81'),
    path('apr_close_decision_page_ob_ch81/', branch81.apr_close_decision_page_ob_ch81, name='apr_close_decision_page_ob_ch81'),

    path('may_close_ob_ch81/', branch81.may_close_ob_ch81, name='may_close_ob_ch81'),
    path('may_close_decision_page_ob_ch81/', branch81.may_close_decision_page_ob_ch81, name='may_close_decision_page_ob_ch81'),
    path('jun_close_ob_ch81/', branch81.jun_close_ob_ch81, name='jun_close_ob_ch81'),
    path('jun_close_decision_page_ob_ch81/', branch81.jun_close_decision_page_ob_ch81, name='jun_close_decision_page_ob_ch81'),
    path('jul_close_ob_ch81/', branch81.jul_close_ob_ch81, name='jul_close_ob_ch81'),
    path('jul_close_decision_page_ob_ch81/', branch81.jul_close_decision_page_ob_ch81, name='jul_close_decision_page_ob_ch81'),
    path('aug_close_ob_ch81/', branch81.aug_close_ob_ch81, name='aug_close_ob_ch81'),
    path('aug_close_decision_page_ob_ch81/', branch81.aug_close_decision_page_ob_ch81, name='aug_close_decision_page_ob_ch81'),

    path('sep_close_ob_ch81/', branch81.sep_close_ob_ch81, name='sep_close_ob_ch81'),
    path('sep_close_decision_page_ob_ch81/', branch81.sep_close_decision_page_ob_ch81, name='sep_close_decision_page_ob_ch81'),
    path('oct_close_ob_ch81/', branch81.oct_close_ob_ch81, name='oct_close_ob_ch81'),
    path('oct_close_decision_page_ob_ch81/', branch81.oct_close_decision_page_ob_ch81, name='oct_close_decision_page_ob_ch81'),
    path('nov_close_ob_ch81/', branch81.nov_close_ob_ch81, name='nov_close_ob_ch81'),
    path('nov_close_decision_page_ob_ch81/', branch81.nov_close_decision_page_ob_ch81, name='nov_close_decision_page_ob_ch81'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch81/',reports81.detailed_report_choose_months_ob_ch81,name='detailed_report_choose_months_ob_ch81'),

    path('jan_details_live_ob_ch81/', reports81.jan_details_live_ob_ch81, name='jan_details_live_ob_ch81'),
    path('jan_print_live_ob_ch81/', reports81.jan_print_live_ob_ch81, name='jan_print_live_ob_ch81'),
    path('feb_details_live_ob_ch81/', reports81.feb_details_live_ob_ch81, name='feb_details_live_ob_ch81'),
    path('feb_print_live_ob_ch81/', reports81.feb_print_live_ob_ch81, name='feb_print_live_ob_ch81'),
    path('march_details_live_ob_ch81/', reports81.march_details_live_ob_ch81, name='march_details_live_ob_ch81'),
    path('march_print_live_ob_ch81/', reports81.march_print_live_ob_ch81, name='march_print_live_ob_ch81'),

    path('april_details_live_ob_ch81/', reports81.april_details_live_ob_ch81, name='april_details_live_ob_ch81'),
    path('april_print_live_ob_ch81/', reports81.april_print_live_ob_ch81, name='april_print_live_ob_ch81'),
    path('may_details_live_ob_ch81/', reports81.may_details_live_ob_ch81, name='may_details_live_ob_ch81'),
    path('may_print_live_ob_ch81/', reports81.may_print_live_ob_ch81, name='may_print_live_ob_ch81'),
    path('june_details_live_ob_ch81/',reports81.june_details_live_ob_ch81,name='june_details_live_ob_ch81'),
    path('june_print_live_ob_ch81/', reports81.june_print_live_ob_ch81, name='june_print_live_ob_ch81'),

    path('july_details_live_ob_ch81/', reports81.july_details_live_ob_ch81, name='july_details_live_ob_ch81'),
    path('july_print_live_ob_ch81/', reports81.july_print_live_ob_ch81, name='july_print_live_ob_ch81'),
    path('auguest_details_live_ob_ch81/', reports81.auguest_details_live_ob_ch81, name='auguest_details_live_ob_ch81'),
    path('auguest_print_live_ob_ch81/', reports81.auguest_print_live_ob_ch81, name='auguest_print_live_ob_ch81'),
    path('sept_details_live_ob_ch81/', reports81.sept_details_live_ob_ch81, name='sept_details_live_ob_ch81'),
    path('sept_print_live_ob_ch81/', reports81.sept_print_live_ob_ch81, name='sept_print_live_ob_ch81'),

    path('october_details_live_ob_ch81/', reports81.october_details_live_ob_ch81, name='october_details_live_ob_ch81'),
    path('october_print_live_ob_ch81/', reports81.october_print_live_ob_ch81, name='october_print_live_ob_ch81'),
    path('nov_details_live_ob_ch81/', reports81.nov_details_live_ob_ch81, name='nov_details_live_ob_ch81'),
    path('nov_print_live_ob_ch81/', reports81.nov_print_live_ob_ch81, name='nov_print_live_ob_ch81'),
    path('dec_details_live_ob_ch81/', reports81.dec_details_live_ob_ch81, name='dec_details_live_ob_ch81'),
    path('dec_print_live_ob_ch81/', reports81.dec_print_live_ob_ch81, name='dec_print_live_ob_ch81'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch81/', reports81.viewall_vaccant_room_ob_ch81, name='viewall_vaccant_room_ob_ch81'),

    path('d_ob_ch81/', branch81.dynamic, name='dynamic'),

    path('manage_bed_ob_ch81/', branch81.manage_bed_ob_ch81, name='manage_bed_ob_ch81'),
    path('manage_new_guest_ob_ch81/', branch81.manage_new_guest_ob_ch81, name='manage_new_guest_ob_ch81'),
    path('manage_update_new_guest_ob_ch81/<id>', branch81.manage_update_new_guest_ob_ch81, name='manage_update_new_guest_ob_ch81'),
    path('manage_update_beds_ob_ch81/<id>', branch81.manage_update_beds_ob_ch81, name='manage_update_beds_ob_ch81'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch81/', branch81.view_all_due_amt_ob_ch81, name='view_all_due_amt_ob_ch81'),
    path('due_amt_mgt_choose_months_ob_ch81/', branch81.due_amt_mgt_choose_months_ob_ch81, name='due_amt_mgt_choose_months_ob_ch81'),

    path('view_jan_account_details_ob_ch81/', branch81.view_jan_account_details_ob_ch81, name='view_jan_account_details_ob_ch81'),
    path('jan_account_mgt_ob_ch81/<id>',branch81.jan_account_mgt_ob_ch81,name='jan_account_mgt_ob_ch81'),
    path('view_feb_account_details_ob_ch81/', branch81.view_feb_account_details_ob_ch81, name='view_feb_account_details_ob_ch81'),
    path('feb_account_mgt_ob_ch81/<id>',branch81.feb_account_mgt_ob_ch81,name='feb_account_mgt_ob_ch81'),
    path('view_march_account_details_ob_ch81/', branch81.view_march_account_details_ob_ch81, name='view_march_account_details_ob_ch81'),
    path('march_account_mgt_ob_ch81/<id>',branch81.march_account_mgt_ob_ch81,name='march_account_mgt_ob_ch81'),
    path('view_april_account_details_ob_ch81/', branch81.view_april_account_details_ob_ch81, name='view_april_account_details_ob_ch81'),
    path('april_account_mgt_ob_ch81/<id>',branch81.april_account_mgt_ob_ch81,name='april_account_mgt_ob_ch81'),

    path('view_may_account_details_ob_ch81/',branch81.view_may_account_details_ob_ch81,name='view_may_account_details_ob_ch81'),
    path('may_account_mgt_ob_ch81/<id>', branch81.may_account_mgt_ob_ch81, name='may_account_mgt_ob_ch81'),
    path('view_june_account_details_ob_ch81/', branch81.view_june_account_details_ob_ch81, name='view_june_account_details_ob_ch81'),
    path('june_account_mgt_ob_ch81/<id>',branch81.june_account_mgt_ob_ch81,name='june_account_mgt_ob_ch81'),
    path('view_july_account_details_ob_ch81/', branch81.view_july_account_details_ob_ch81, name='view_july_account_details_ob_ch81'),
    path('july_account_mgt_ob_ch81/<id>',branch81.july_account_mgt_ob_ch81,name='july_account_mgt_ob_ch81'),
    path('view_auguest_account_details_ob_ch81/', branch81.view_auguest_account_details_ob_ch81, name='view_auguest_account_details_ob_ch81'),
    path('auguest_account_mgt_ob_ch81/<id>',branch81.auguest_account_mgt_ob_ch81,name='auguest_account_mgt_ob_ch81'),

    path('view_sept_account_details_ob_ch81/', branch81.view_sept_account_details_ob_ch81, name='view_sept_account_details_ob_ch81'),
    path('sept_account_mgt_ob_ch81/<id>',branch81.sept_account_mgt_ob_ch81,name='sept_account_mgt_ob_ch81'),
    path('view_october_account_details_ob_ch81/', branch81.view_october_account_details_ob_ch81, name='view_october_account_details_ob_ch81'),
    path('october_account_mgt_ob_ch81/<id>',branch81.october_account_mgt_ob_ch81,name='october_account_mgt_ob_ch81'),
    path('view_nov_account_details_ob_ch81/', branch81.view_nov_account_details_ob_ch81, name='view_nov_account_details_ob_ch81'),
    path('nov_account_mgt_ob_ch81/<id>',branch81.nov_account_mgt_ob_ch81,name='nov_account_mgt_ob_ch81'),
    path('view_dec_account_details_ob_ch81/', branch81.view_dec_account_details_ob_ch81, name='view_dec_account_details_ob_ch81'),
    path('dec_account_mgt_ob_ch81/<id>',branch81.dec_account_mgt_ob_ch81,name='dec_account_mgt_ob_ch81'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch81', admin_dashboard_calculations_br81.monthly_details_due_ob_ch81, name='monthly_details_due_ob_ch81'),
    path('monthly_collection_details_ob_ch81/', admin_dashboard_calculations_br81.monthly_collection_details_ob_ch81, name='monthly_collection_details_ob_ch81'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch81/',branch81.guest_all_ob_ch81,name='guest_all_ob_ch81'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************

    path('accounts_dash_board_ob_ch81/',accounts81.accounts_dash_board_ob_ch81,name='accounts_dash_board_ob_ch81'),



]

