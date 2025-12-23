from django.urls import path, include

from . import admin_branch34
from . import admin_branch34
from . import branch34
from . import reports34
from . import payment34
from . import admin_dashboard_calculations_br34
from . import accounts34
from . import branch_settings34

urlpatterns = [

    path('branch1_dashboard_ob_ch34/', branch34.branch1_dashboard_ob_ch34, name='branch1_dashboard_ob_ch34'),
    path('branch1_dashboard34/',branch34.branch1_dashboard34,name='branch1_dashboard34'),
    path('user_dashboard_calculations_ob_ch34/',branch34.user_dashboard_calculations_ob_ch34,name='user_dashboard_calculations_ob_ch34'),

    path('background_ob_ch34',branch34.background_ob_ch34,name='background_ob_ch34'),
    path('background_regi_ob_ch34',branch34.background_regi_ob_ch34,name='background_regi_ob_ch34'),
    path('custom_background_regi_ob_ch34',branch34.custom_background_regi_ob_ch34,name='custom_background_regi_ob_ch34'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch34/',admin_branch34.branch1_room_create_regi_ob_ch34,name='branch1_room_create_regi_ob_ch34'),
    path('view_all_room_ob_ch34/',admin_branch34.view_all_room_ob_ch34,name='view_all_room_ob_ch34'),
    path('delete_room_ob_ch34/<id>',admin_branch34.delete_room_ob_ch34,name='delete_room_ob_ch34'),

    path('branch1_room_create_ob_ch34/',admin_branch34.branch1_room_create_ob_ch34,name='branch1_room_create_ob_ch34'),

    path('multiple_branch1_room_create_regi34/',admin_branch34.multiple_branch1_room_create_regi34,name='multiple_branch1_room_create_regi34'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch34/', admin_branch34.pg1_bed_create_regi_ob_ch34, name='pg1_bed_create_regi_ob_ch34'),
    path('pg1_view_all_beds_ob_ch34/', admin_branch34.pg1_view_all_beds_ob_ch34, name='pg1_view_all_beds_ob_ch34'),
    path('delete_bed_ob_ch34/<id>', admin_branch34.delete_bed_ob_ch34, name='delete_bed_ob_ch34'),

    path('pg1_bed_create_ob_ch34/', admin_branch34.pg1_bed_create_ob_ch34, name='pg1_bed_create_ob_ch34'),

    path('single_pg1_bed_create_regi_ob_ch34/',admin_branch34.single_pg1_bed_create_regi_ob_ch34,name='single_pg1_bed_create_regi_ob_ch34'),
    path('update_bed_basic_details_ob_ch34/<id>',admin_branch34.update_bed_basic_details_ob_ch34, name='update_bed_basic_details_ob_ch34'),

    path('multiple_single_pg1_bed_create_regi34/',admin_branch34.multiple_single_pg1_bed_create_regi34,name='multiple_single_pg1_bed_create_regi34'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch34/<id>',branch34.br1_admit_guest_ob_ch34,name='br1_admit_guest_ob_ch34'),
    path('view_all_new_guest_ob_ch34/',branch34.view_all_new_guest_ob_ch34,name='view_all_new_guest_ob_ch34'),
    path('update_br1_admit_guest_ob_ch34/<id>',branch34.update_br1_admit_guest_ob_ch34,name='update_br1_admit_guest_ob_ch34'),
    path('vacate_br1_guest_ob_ch34/<id>',branch34.vacate_br1_guest_ob_ch34,name='vacate_br1_guest_ob_ch34'),

    path('active_guest_details_ob_ch34/<guest_code>',branch34.active_guest_details_ob_ch34,name='active_guest_details_ob_ch34'),
    path('view_all_guest_ob_ch34/',branch34.view_all_guest_ob_ch34,name='view_all_guest_ob_ch34'),
    path('shift_guest_ob_ch34/<id>',branch34.shift_guest_ob_ch34,name='shift_guest_ob_ch34'),
    path('shift_guest_regi_ob_ch34/',branch34.shift_guest_regi_ob_ch34,name='shift_guest_regi_ob_ch34'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch34/',branch34.update_all_rent_ob_ch34,name='update_all_rent_ob_ch34'),

    path('multiple_br1_admit_guest34/<id>',branch34.multiple_br1_admit_guest34,name='multiple_br1_admit_guest34'),

#guest end here


##################################
#_ADVANCE_ob_ch34 START HERE
################################


    path('choose_months_advance_ob_ch34/',branch34.choose_months_advance_ob_ch34,name='choose_months_advance_ob_ch34'),

    path('jan_advance_ob_ch34/', branch34.jan_advance_ob_ch34, name='jan_advance_ob_ch34'),
    path('jan_make_payments_advance_ob_ch34/<id>', branch34.jan_make_payments_advance_ob_ch34,name='jan_make_payments_advance_ob_ch34'),
    path('feb_advance_ob_ch34/', branch34.feb_advance_ob_ch34, name='feb_advance_ob_ch34'),
    path('feb_make_payments_advance_ob_ch34/<id>', branch34.feb_make_payments_advance_ob_ch34,name='feb_make_payments_advance_ob_ch34'),
    path('march_advance_ob_ch34/', branch34.march_advance_ob_ch34, name='march_advance_ob_ch34'),
    path('march_make_payments_advance_ob_ch34/<id>', branch34.march_make_payments_advance_ob_ch34,name='march_make_payments_advance_ob_ch34'),
    path('april_advance_ob_ch34/', branch34.april_advance_ob_ch34, name='april_advance_ob_ch34'),
    path('april_make_payments_advance_ob_ch34/<id>', branch34.april_make_payments_advance_ob_ch34, name='april_make_payments_advance_ob_ch34'),

    path('may_advance_ob_ch34/',branch34.may_advance_ob_ch34,name='may_advance_ob_ch34'),
    path('may_make_payments_advance_ob_ch34/<id>', branch34.may_make_payments_advance_ob_ch34, name='may_make_payments_advance_ob_ch34'),
    path('june_advance_ob_ch34/',branch34.june_advance_ob_ch34,name='june_advance_ob_ch34'),
    path('june_make_payments_advance_ob_ch34/<id>', branch34.june_make_payments_advance_ob_ch34, name='june_make_payments_advance_ob_ch34'),
    path('july_advance_ob_ch34/',branch34.july_advance_ob_ch34,name='july_advance_ob_ch34'),
    path('july_make_payments_advance_ob_ch34/<id>', branch34.july_make_payments_advance_ob_ch34, name='july_make_payments_advance_ob_ch34'),
    path('auguest_advance_ob_ch34/', branch34.auguest_advance_ob_ch34, name='auguest_advance_ob_ch34'),
    path('auguest_make_payments_advance_ob_ch34/<id>', branch34.auguest_make_payments_advance_ob_ch34, name='auguest_make_payments_advance_ob_ch34'),

    path('sept_advance_ob_ch34/', branch34.sept_advance_ob_ch34, name='sept_advance_ob_ch34'),
    path('sept_make_payments_advance_ob_ch34/<id>', branch34.sept_make_payments_advance_ob_ch34,name='sept_make_payments_advance_ob_ch34'),
    path('october_advance_ob_ch34/', branch34.october_advance_ob_ch34, name='october_advance_ob_ch34'),
    path('october_make_payments_advance_ob_ch34/<id>', branch34.october_make_payments_advance_ob_ch34, name='october_make_payments_advance_ob_ch34'),
    path('nov_advance_ob_ch34/', branch34.nov_advance_ob_ch34, name='nov_advance_ob_ch34'),
    path('nov_make_payments_advance_ob_ch34/<id>', branch34.nov_make_payments_advance_ob_ch34,name='nov_make_payments_advance_ob_ch34'),
    path('dec_advance_ob_ch34/', branch34.dec_advance_ob_ch34, name='dec_advance_ob_ch34'),
    path('dec_make_payments_advance_ob_ch34/<id>', branch34.dec_make_payments_advance_ob_ch34, name='dec_make_payments_advance_ob_ch34'),



##################################
#_ADVANCE_ob_ch34 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch34/',branch34.choose_months_ob_ch34,name='choose_months_ob_ch34'),

    path('jan_ob_ch34/',branch34.jan_ob_ch34,name='jan_ob_ch34'),
    path('jan_manke_payments_ob_ch34/<id>',branch34.jan_manke_payments_ob_ch34,name='jan_manke_payments_ob_ch34'),

    path('feb_ob_ch34/',branch34.feb_ob_ch34,name='feb_ob_ch34'),
    path('feb_manke_payments_ob_ch34/<id>',branch34.feb_manke_payments_ob_ch34,name='feb_manke_payments_ob_ch34'),

    path('march_ob_ch34/',branch34.march_ob_ch34,name='march_ob_ch34'),
    path('march_manke_payments_ob_ch34/<id>',branch34.march_manke_payments_ob_ch34,name='march_manke_payments_ob_ch34'),

    path('april_ob_ch34/',branch34.april_ob_ch34,name='april_ob_ch34'),
    path('april_make_payments_ob_ch34/<id>',branch34.april_make_payments_ob_ch34,name='april_make_payments_ob_ch34'),

    path('may_ob_ch34/',branch34.may_ob_ch34,name='may_ob_ch34'),
    path('may_make_payments_ob_ch34/<id>',branch34.may_make_payments_ob_ch34,name='may_make_payments_ob_ch34'),

    path('june_ob_ch34/',branch34.june_ob_ch34,name='june_ob_ch34'),
    path('june_make_payments_ob_ch34/<id>',branch34.june_make_payments_ob_ch34,name='june_make_payments_ob_ch34'),

    path('july_ob_ch34/',branch34.july_ob_ch34,name='july_ob_ch34'),
    path('july_make_payments_ob_ch34/<id>',branch34.july_make_payments_ob_ch34,name='july_make_payments_ob_ch34'),

    path('aug_ob_ch34/',branch34.aug_ob_ch34,name='aug_ob_ch34'),
    path('aug_make_payments_ob_ch34/<id>',branch34.aug_make_payments_ob_ch34,name='aug_make_payments_ob_ch34'),

    path('sept_ob_ch34/',branch34.sept_ob_ch34,name='sept_ob_ch34'),
    path('sept_make_payments_ob_ch34/<id>',branch34.sept_make_payments_ob_ch34,name='sept_make_payments_ob_ch34'),

    path('oct_ob_ch34/',branch34.oct_ob_ch34,name='oct_ob_ch34'),
    path('oct_make_payments_ob_ch34/<id>',branch34.oct_make_payments_ob_ch34,name='oct_make_payments_ob_ch34'),

    path('nov_ob_ch34/',branch34.nov_ob_ch34,name='nov_ob_ch34'),
    path('nov_make_payments_ob_ch34/<id>',branch34.nov_make_payments_ob_ch34,name='nov_make_payments_ob_ch34'),

    path('dec_ob_ch34/',branch34.dec_ob_ch34,name='dec_ob_ch34'),
    path('dec_make_payments_ob_ch34/<id>',branch34.dec_make_payments_ob_ch34,name='dec_make_payments_ob_ch34'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch34/', payment34.choose_user_ob_ch34, name='choose_user_ob_ch34'),
    path('payment_user_details_ob_ch34/<id>', payment34.payment_user_details_ob_ch34, name='payment_user_details_ob_ch34'),
    path('close_choose_user_ob_ch34/<id>',payment34.close_choose_user_ob_ch34,name='close_choose_user_ob_ch34'),

    path('monthly_jan_make_payments_ob_ch34/<id>', payment34.monthly_jan_make_payments_ob_ch34, name='monthly_jan_make_payments_ob_ch34'),
    path('monthly_feb_make_payments_ob_ch34/<id>', payment34.monthly_feb_make_payments_ob_ch34, name='monthly_feb_make_payments_ob_ch34'),
    path('monthly_march_make_payments_ob_ch34/<id>', payment34.monthly_march_make_payments_ob_ch34, name='monthly_march_make_payments_ob_ch34'),
    path('monthly_april_make_payments_ob_ch34/<id>', payment34.monthly_april_make_payments_ob_ch34, name='monthly_april_make_payments_ob_ch34'),
    path('monthly_may_make_payments_ob_ch34/<id>', payment34.monthly_may_make_payments_ob_ch34, name='monthly_may_make_payments_ob_ch34'),
    path('monthly_june_make_payments_ob_ch34/<id>', payment34.monthly_june_make_payments_ob_ch34, name='monthly_june_make_payments_ob_ch34'),

    path('monthly_july_make_payments_ob_ch34/<id>', payment34.monthly_july_make_payments_ob_ch34, name='monthly_july_make_payments_ob_ch34'),
    path('monthly_aug_make_payments_ob_ch34/<id>', payment34.monthly_aug_make_payments_ob_ch34, name='monthly_aug_make_payments_ob_ch34'),
    path('monthly_sept_make_payments_ob_ch34/<id>', payment34.monthly_sept_make_payments_ob_ch34, name='monthly_sept_make_payments_ob_ch34'),
    path('monthly_oct_make_payments_ob_ch34/<id>', payment34.monthly_oct_make_payments_ob_ch34, name='monthly_oct_make_payments_ob_ch34'),
    path('monthly_nov_make_payments_ob_ch34/<id>', payment34.monthly_nov_make_payments_ob_ch34, name='monthly_nov_make_payments_ob_ch34'),
    path('monthly_dec_make_payments_ob_ch34/<id>', payment34.monthly_dec_make_payments_ob_ch34, name='monthly_dec_make_payments_ob_ch34'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch34/',branch34.unpaid_rent_choose_months_ob_ch34,name='unpaid_rent_choose_months_ob_ch34'),

    path('jan_unpaid_rent_ob_ch34/', branch34.jan_unpaid_rent_ob_ch34, name='jan_unpaid_rent_ob_ch34'),
    path('table_jan_unpaid_rent_ob_ch34/', branch34.table_jan_unpaid_rent_ob_ch34, name='table_jan_unpaid_rent_ob_ch34'),
    path('feb_unpaid_rent_ob_ch34/', branch34.feb_unpaid_rent_ob_ch34, name='feb_unpaid_rent_ob_ch34'),
    path('table_feb_unpaid_rent_ob_ch34/', branch34.table_feb_unpaid_rent_ob_ch34, name='table_feb_unpaid_rent_ob_ch34'),
    path('mar_unpaid_rent_ob_ch34/', branch34.mar_unpaid_rent_ob_ch34, name='mar_unpaid_rent_ob_ch34'),
    path('table_mar_unpaid_rent_ob_ch34/', branch34.table_mar_unpaid_rent_ob_ch34, name='table_mar_unpaid_rent_ob_ch34'),
    path('april_unpaid_rent_ob_ch34/', branch34.april_unpaid_rent_ob_ch34, name='april_unpaid_rent_ob_ch34'),
    path('table_april_unpaid_rent_ob_ch34/', branch34.table_april_unpaid_rent_ob_ch34, name='table_april_unpaid_rent_ob_ch34'),

    path('may_unpaid_rent_ob_ch34/', branch34.may_unpaid_rent_ob_ch34, name='may_unpaid_rent_ob_ch34'),
    path('table_may_unpaid_rent_ob_ch34/', branch34.table_may_unpaid_rent_ob_ch34, name='table_may_unpaid_rent_ob_ch34'),
    path('june_unpaid_rent_ob_ch34/', branch34.june_unpaid_rent_ob_ch34, name='june_unpaid_rent_ob_ch34'),
    path('table_june_unpaid_rent_ob_ch34/', branch34.table_june_unpaid_rent_ob_ch34, name='table_june_unpaid_rent_ob_ch34'),
    path('july_unpaid_rent_ob_ch34/', branch34.july_unpaid_rent_ob_ch34, name='july_unpaid_rent_ob_ch34'),
    path('table_july_unpaid_rent_ob_ch34',branch34.table_july_unpaid_rent_ob_ch34,name='table_july_unpaid_rent_ob_ch34'),
    path('aug_unpaid_rent_ob_ch34/', branch34.aug_unpaid_rent_ob_ch34, name='aug_unpaid_rent_ob_ch34'),
    path('table_aug_unpaid_rent_ob_ch34/',branch34.table_aug_unpaid_rent_ob_ch34,name='table_aug_unpaid_rent_ob_ch34'),

    path('sept_unpaid_rent_ob_ch34/', branch34.sept_unpaid_rent_ob_ch34, name='sept_unpaid_rent_ob_ch34'),
    path('table_sept_unpaid_rent_ob_ch34/', branch34.table_sept_unpaid_rent_ob_ch34, name='table_sept_unpaid_rent_ob_ch34'),
    path('oct_unpaid_rent_ob_ch34/', branch34.oct_unpaid_rent_ob_ch34, name='oct_unpaid_rent_ob_ch34'),
    path('table_oct_unpaid_rent_ob_ch34/', branch34.table_oct_unpaid_rent_ob_ch34, name='table_oct_unpaid_rent_ob_ch34'),
    path('nov_unpaid_rent_ob_ch34/', branch34.nov_unpaid_rent_ob_ch34, name='nov_unpaid_rent_ob_ch34'),
    path('table_nov_unpaid_rent_ob_ch34/', branch34.table_nov_unpaid_rent_ob_ch34, name='table_nov_unpaid_rent_ob_ch34'),
    path('dec_unpaid_rent_ob_ch34/', branch34.dec_unpaid_rent_ob_ch34, name='dec_unpaid_rent_ob_ch34'),
    path('table_dec_unpaid_rent_ob_ch34/', branch34.table_dec_unpaid_rent_ob_ch34, name='table_dec_unpaid_rent_ob_ch34'),

    path('details_of_unpaid_guests_ob_ch34/<id>',branch34.details_of_unpaid_guests_ob_ch34,name='details_of_unpaid_guests_ob_ch34'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch34/',branch34.paid_rent_choose_months_ob_ch34,name='paid_rent_choose_months_ob_ch34'),
    path('partially_paid_guest_choose_months_ob_ch34/',reports34.partially_paid_guest_choose_months_ob_ch34,name='partially_paid_guest_choose_months_ob_ch34'),

    path('jan_paid_rent_ob_ch34/', branch34.jan_paid_rent_ob_ch34, name='jan_paid_rent_ob_ch34'),
    path('table_jan_paid_rent_ob_ch34/', branch34.table_jan_paid_rent_ob_ch34, name='table_jan_paid_rent_ob_ch34'),
    path('jan_full_paid_guest_ob_ch34/', reports34.jan_full_paid_guest_ob_ch34, name='jan_full_paid_guest_ob_ch34'),
    path('jan_partially_paid_guest_ob_ch34/', reports34.jan_partially_paid_guest_ob_ch34, name='jan_partially_paid_guest_ob_ch34'),
    path('table_jan_partially_paid_guest_ob_ch34/', reports34.table_jan_partially_paid_guest_ob_ch34,name='table_jan_partially_paid_guest_ob_ch34'),

    path('feb_paid_rent_ob_ch34/', branch34.feb_paid_rent_ob_ch34, name='feb_paid_rent_ob_ch34'),
    path('table_feb_paid_rent_ob_ch34/', branch34.table_feb_paid_rent_ob_ch34, name='table_feb_paid_rent_ob_ch34'),
    path('feb_full_paid_guest_ob_ch34/', reports34.feb_full_paid_guest_ob_ch34, name='feb_full_paid_guest_ob_ch34'),
    path('feb_partially_paid_guest_ob_ch34/', reports34.feb_partially_paid_guest_ob_ch34, name='feb_partially_paid_guest_ob_ch34'),
    path('table_feb_partially_paid_guest_ob_ch34/', reports34.table_feb_partially_paid_guest_ob_ch34,name='table_feb_partially_paid_guest_ob_ch34'),

    path('mar_paid_rent_ob_ch34/', branch34.mar_paid_rent_ob_ch34, name='mar_paid_rent_ob_ch34'),
    path('table_mar_paid_rent_ob_ch34/', branch34.table_mar_paid_rent_ob_ch34, name='table_mar_paid_rent_ob_ch34'),
    path('march_full_paid_guest_ob_ch34/', reports34.march_full_paid_guest_ob_ch34, name='march_full_paid_guest_ob_ch34'),
    path('march_partially_paid_guest_ob_ch34/', reports34.march_partially_paid_guest_ob_ch34, name='march_partially_paid_guest_ob_ch34'),
    path('table_march_partially_paid_guest_ob_ch34/', reports34.table_march_partially_paid_guest_ob_ch34,name='table_march_partially_paid_guest_ob_ch34'),

    path('april_paid_rent_ob_ch34/', branch34.april_paid_rent_ob_ch34, name='april_paid_rent_ob_ch34'),
    path('table_april_paid_rent_ob_ch34/', branch34.table_april_paid_rent_ob_ch34, name='table_april_paid_rent_ob_ch34'),
    path('april_full_paid_guest_ob_ch34/', reports34.april_full_paid_guest_ob_ch34, name='april_full_paid_guest_ob_ch34'),
    path('april_partially_paid_guest_ob_ch34/', reports34.april_partially_paid_guest_ob_ch34, name='april_partially_paid_guest_ob_ch34'),
    path('table_april_partially_paid_guest_ob_ch34/', reports34.table_april_partially_paid_guest_ob_ch34,name='table_april_partially_paid_guest_ob_ch34'),

    path('may_paid_rent_ob_ch34/', branch34.may_paid_rent_ob_ch34, name='may_paid_rent_ob_ch34'),
    path('table_may_paid_rent_ob_ch34/', branch34.table_may_paid_rent_ob_ch34, name='table_may_paid_rent_ob_ch34'),
    path('may_full_paid_guest_ob_ch34/', reports34.may_full_paid_guest_ob_ch34, name='may_full_paid_guest_ob_ch34'),
    path('may_partially_paid_guest_ob_ch34/', reports34.may_partially_paid_guest_ob_ch34, name='may_partially_paid_guest_ob_ch34'),
    path('table_may_partially_paid_guest_ob_ch34/', reports34.table_may_partially_paid_guest_ob_ch34, name='table_may_partially_paid_guest_ob_ch34'),

    path('june_paid_rent_ob_ch34/', branch34.june_paid_rent_ob_ch34, name='june_paid_rent_ob_ch34'),
    path('table_june_paid_rent_ob_ch34/', branch34.table_june_paid_rent_ob_ch34, name='table_june_paid_rent_ob_ch34'),
    path('june_full_paid_guest_ob_ch34/', reports34.june_full_paid_guest_ob_ch34, name='june_full_paid_guest_ob_ch34'),
    path('june_partially_paid_guest_ob_ch34/', reports34.june_partially_paid_guest_ob_ch34, name='june_partially_paid_guest_ob_ch34'),
    path('table_june_partially_paid_guest_ob_ch34/', reports34.table_june_partially_paid_guest_ob_ch34, name='table_june_partially_paid_guest_ob_ch34'),

    path('july_paid_rent_ob_ch34/', branch34.july_paid_rent_ob_ch34, name='july_paid_rent_ob_ch34'),
    path('table_july_paid_rent_ob_ch34/', branch34.table_july_paid_rent_ob_ch34, name='table_july_paid_rent_ob_ch34'),
    path('july_full_paid_guest_ob_ch34/', reports34.july_full_paid_guest_ob_ch34, name='july_full_paid_guest_ob_ch34'),
    path('july_partially_paid_guest_ob_ch34/', reports34.july_partially_paid_guest_ob_ch34, name='july_partially_paid_guest_ob_ch34'),
    path('table_july_partially_paid_guest_ob_ch34/', reports34.table_july_partially_paid_guest_ob_ch34, name='table_july_partially_paid_guest_ob_ch34'),

    path('aug_paid_rent_ob_ch34/', branch34.aug_paid_rent_ob_ch34, name='aug_paid_rent_ob_ch34'),
    path('table_aug_paid_rent_ob_ch34/', branch34.table_aug_paid_rent_ob_ch34, name='table_aug_paid_rent_ob_ch34'),
    path('auguest_full_paid_guest_ob_ch34/', reports34.auguest_full_paid_guest_ob_ch34, name='auguest_full_paid_guest_ob_ch34'),
    path('auguest_partially_paid_guest_ob_ch34/', reports34.auguest_partially_paid_guest_ob_ch34,name='auguest_partially_paid_guest_ob_ch34'),
    path('table_auguest_partially_paid_guest_ob_ch34/', reports34.table_auguest_partially_paid_guest_ob_ch34,name='table_auguest_partially_paid_guest_ob_ch34'),

    path('sept_paid_rent_ob_ch34/', branch34.sept_paid_rent_ob_ch34, name='sept_paid_rent_ob_ch34'),
    path('table_sept_paid_rent_ob_ch34/', branch34.table_sept_paid_rent_ob_ch34, name='table_sept_paid_rent_ob_ch34'),
    path('sept_full_paid_guest_ob_ch34/', reports34.sept_full_paid_guest_ob_ch34, name='sept_full_paid_guest_ob_ch34'),
    path('sept_partially_paid_guest_ob_ch34/', reports34.sept_partially_paid_guest_ob_ch34, name='sept_partially_paid_guest_ob_ch34'),
    path('table_sept_partially_paid_guest_ob_ch34/', reports34.table_sept_partially_paid_guest_ob_ch34,name='table_sept_partially_paid_guest_ob_ch34'),

    path('oct_paid_rent_ob_ch34/', branch34.oct_paid_rent_ob_ch34, name='oct_paid_rent_ob_ch34'),
    path('table_oct_paid_rent_ob_ch34/', branch34.table_oct_paid_rent_ob_ch34, name='table_oct_paid_rent_ob_ch34'),
    path('october_full_paid_guest_ob_ch34/', reports34.october_full_paid_guest_ob_ch34, name='october_full_paid_guest_ob_ch34'),
    path('october_partially_paid_guest_ob_ch34/', reports34.october_partially_paid_guest_ob_ch34,name='october_partially_paid_guest_ob_ch34'),
    path('table_october_partially_paid_guest_ob_ch34/', reports34.table_october_partially_paid_guest_ob_ch34,name='table_october_partially_paid_guest_ob_ch34'),

    path('nov_paid_rent_ob_ch34/', branch34.nov_paid_rent_ob_ch34, name='nov_paid_rent_ob_ch34'),
    path('table_nov_paid_rent_ob_ch34/', branch34.table_nov_paid_rent_ob_ch34, name='table_nov_paid_rent_ob_ch34'),
    path('nov_full_paid_guest_ob_ch34/', reports34.nov_full_paid_guest_ob_ch34, name='nov_full_paid_guest_ob_ch34'),
    path('nov_partially_paid_guest_ob_ch34/', reports34.nov_partially_paid_guest_ob_ch34, name='nov_partially_paid_guest_ob_ch34'),
    path('table_nov_partially_paid_guest_ob_ch34/', reports34.table_nov_partially_paid_guest_ob_ch34,name='table_nov_partially_paid_guest_ob_ch34'),

    path('dec_paid_rent_ob_ch34/', branch34.dec_paid_rent_ob_ch34, name='dec_paid_rent_ob_ch34'),
    path('table_dec_paid_rent_ob_ch34/', branch34.table_dec_paid_rent_ob_ch34, name='table_dec_paid_rent_ob_ch34'),
    path('dec_full_paid_guest_ob_ch34/', reports34.dec_full_paid_guest_ob_ch34, name='dec_full_paid_guest_ob_ch34'),
    path('dec_partially_paid_guest_ob_ch34/', reports34.dec_partially_paid_guest_ob_ch34, name='dec_partially_paid_guest_ob_ch34'),
    path('table_dec_partially_paid_guest_ob_ch34/', reports34.table_dec_partially_paid_guest_ob_ch34,name='table_dec_partially_paid_guest_ob_ch34'),

    path('details_of_paid_guests_ob_ch34/<id>',branch34.details_of_paid_guests_ob_ch34,name='details_of_paid_guests_ob_ch34'),
    path('full_paid_guest_ob_ch34/',reports34.full_paid_guest_ob_ch34,name='full_paid_guest_ob_ch34'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch34/',branch34.viewall_vacate_guest_ob_ch34,name='viewall_vacate_guest_ob_ch34'),
    path('details_of_vacate_guest_ob_ch34/<id>',branch34.details_of_vacate_guest_ob_ch34,name='details_of_vacate_guest_ob_ch34'),
    path('full_vacated_guest_details_ob_ch34',branch34.full_vacated_guest_details_ob_ch34,name='full_vacated_guest_details_ob_ch34'),
    path('full_vacated_guest_table_ob_ch34',branch34.full_vacated_guest_table_ob_ch34,name='full_vacated_guest_table_ob_ch34'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch34/<id>', branch34.jan_manke_payments_vacate_ob_ch34, name='jan_manke_payments_vacate_ob_ch34'),
    path('feb_manke_payments_vacate_ob_ch34/<id>', branch34.feb_manke_payments_vacate_ob_ch34, name='feb_manke_payments_vacate_ob_ch34'),
    path('march_manke_payments_vacate_ob_ch34/<id>', branch34.march_manke_payments_vacate_ob_ch34, name='march_manke_payments_vacate_ob_ch34'),
    path('april_make_payments_vacate_ob_ch34/<id>', branch34.april_make_payments_vacate_ob_ch34, name='april_make_payments_vacate_ob_ch34'),

    path('may_make_payments_vacate_ob_ch34/<id>', branch34.may_make_payments_vacate_ob_ch34, name='may_make_payments_vacate_ob_ch34'),
    path('june_make_payments_vacate_ob_ch34/<id>', branch34.june_make_payments_vacate_ob_ch34, name='june_make_payments_vacate_ob_ch34'),
    path('july_make_payments_vacate_ob_ch34/<id>', branch34.july_make_payments_vacate_ob_ch34, name='july_make_payments_vacate_ob_ch34'),
    path('aug_make_payments_vacate_ob_ch34/<id>', branch34.aug_make_payments_vacate_ob_ch34, name='aug_make_payments_vacate_ob_ch34'),

    path('sept_make_payments_vacate_ob_ch34/<id>', branch34.sept_make_payments_vacate_ob_ch34, name='sept_make_payments_vacate_ob_ch34'),
    path('oct_make_payments_vacate_ob_ch34/<id>', branch34.oct_make_payments_vacate_ob_ch34, name='oct_make_payments_vacate_ob_ch34'),
    path('nov_make_payments_vacate_ob_ch34/<id>', branch34.nov_make_payments_vacate_ob_ch34, name='nov_make_payments_vacate_ob_ch34'),
    path('dec_make_payments_vacate_ob_ch34/<id>', branch34.dec_make_payments_vacate_ob_ch34, name='dec_make_payments_vacate_ob_ch34'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch34/',branch34.detail_guest_general_ob_ch34,name='detail_guest_general_ob_ch34'),

    path('jan_print_ob_ch34/',branch34.jan_print_ob_ch34,name='jan_print_ob_ch34'),
    path('feb_print_ob_ch34/',branch34.feb_print_ob_ch34,name='feb_print_ob_ch34'),
    path('march_print_ob_ch34/',branch34.march_print_ob_ch34,name='march_print_ob_ch34'),
    path('april_print_ob_ch34/',branch34.april_print_ob_ch34,name='april_print_ob_ch34'),

    path('may_print_ob_ch34/',branch34.may_print_ob_ch34,name='may_print_ob_ch34'),
    path('june_print_ob_ch34/',branch34.june_print_ob_ch34,name='june_print_ob_ch34'),
    path('july_print_ob_ch34/', branch34.july_print_ob_ch34, name='july_print_ob_ch34'),
    path('aug_print_ob_ch34/', branch34.aug_print_ob_ch34, name='aug_print_ob_ch34'),

    path('sept_print_ob_ch34/', branch34.sept_print_ob_ch34, name='sept_print_ob_ch34'),
    path('oct_print_ob_ch34/', branch34.oct_print_ob_ch34, name='oct_print_ob_ch34'),
    path('nov_print_ob_ch34/', branch34.nov_print_ob_ch34, name='nov_print_ob_ch34'),
    path('dec_print_ob_ch34/', branch34.dec_print_ob_ch34, name='dec_print_ob_ch34'),

    path('new_year_jan_print_ob_ch34/', branch34.new_year_jan_print_ob_ch34, name='new_year_jan_print_ob_ch34'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch34/', branch34.jan_close_ob_ch34, name='jan_close_ob_ch34'),
    path('jan_close_decision_page_ob_ch34/', branch34.jan_close_decision_page_ob_ch34, name='jan_close_decision_page_ob_ch34'),
    path('feb_close/', branch34.feb_close_ob_ch34, name='feb_close_ob_ch34'),
    path('feb_close_decision_page_ob_ch34/', branch34.feb_close_decision_page_ob_ch34, name='feb_close_decision_page_ob_ch34'),
    path('mar_close_ob_ch34/', branch34.mar_close_ob_ch34, name='mar_close_ob_ch34'),
    path('mar_close_decision_page/', branch34.mar_close_decision_page_ob_ch34, name='mar_close_decision_page_ob_ch34'),
    path('apr_close_ob_ch34/', branch34.apr_close_ob_ch34, name='apr_close_ob_ch34'),
    path('apr_close_decision_page_ob_ch34/', branch34.apr_close_decision_page_ob_ch34, name='apr_close_decision_page_ob_ch34'),

    path('may_close_ob_ch34/', branch34.may_close_ob_ch34, name='may_close_ob_ch34'),
    path('may_close_decision_page_ob_ch34/', branch34.may_close_decision_page_ob_ch34, name='may_close_decision_page_ob_ch34'),
    path('jun_close_ob_ch34/', branch34.jun_close_ob_ch34, name='jun_close_ob_ch34'),
    path('jun_close_decision_page_ob_ch34/', branch34.jun_close_decision_page_ob_ch34, name='jun_close_decision_page_ob_ch34'),
    path('jul_close_ob_ch34/', branch34.jul_close_ob_ch34, name='jul_close_ob_ch34'),
    path('jul_close_decision_page_ob_ch34/', branch34.jul_close_decision_page_ob_ch34, name='jul_close_decision_page_ob_ch34'),
    path('aug_close_ob_ch34/', branch34.aug_close_ob_ch34, name='aug_close_ob_ch34'),
    path('aug_close_decision_page_ob_ch34/', branch34.aug_close_decision_page_ob_ch34, name='aug_close_decision_page_ob_ch34'),

    path('sep_close_ob_ch34/', branch34.sep_close_ob_ch34, name='sep_close_ob_ch34'),
    path('sep_close_decision_page_ob_ch34/', branch34.sep_close_decision_page_ob_ch34, name='sep_close_decision_page_ob_ch34'),
    path('oct_close_ob_ch34/', branch34.oct_close_ob_ch34, name='oct_close_ob_ch34'),
    path('oct_close_decision_page_ob_ch34/', branch34.oct_close_decision_page_ob_ch34, name='oct_close_decision_page_ob_ch34'),
    path('nov_close_ob_ch34/', branch34.nov_close_ob_ch34, name='nov_close_ob_ch34'),
    path('nov_close_decision_page_ob_ch34/', branch34.nov_close_decision_page_ob_ch34, name='nov_close_decision_page_ob_ch34'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch34/',reports34.detailed_report_choose_months_ob_ch34,name='detailed_report_choose_months_ob_ch34'),

    path('jan_details_live_ob_ch34/', reports34.jan_details_live_ob_ch34, name='jan_details_live_ob_ch34'),
    path('jan_print_live_ob_ch34/', reports34.jan_print_live_ob_ch34, name='jan_print_live_ob_ch34'),
    path('feb_details_live_ob_ch34/', reports34.feb_details_live_ob_ch34, name='feb_details_live_ob_ch34'),
    path('feb_print_live_ob_ch34/', reports34.feb_print_live_ob_ch34, name='feb_print_live_ob_ch34'),
    path('march_details_live_ob_ch34/', reports34.march_details_live_ob_ch34, name='march_details_live_ob_ch34'),
    path('march_print_live_ob_ch34/', reports34.march_print_live_ob_ch34, name='march_print_live_ob_ch34'),

    path('april_details_live_ob_ch34/', reports34.april_details_live_ob_ch34, name='april_details_live_ob_ch34'),
    path('april_print_live_ob_ch34/', reports34.april_print_live_ob_ch34, name='april_print_live_ob_ch34'),
    path('may_details_live_ob_ch34/', reports34.may_details_live_ob_ch34, name='may_details_live_ob_ch34'),
    path('may_print_live_ob_ch34/', reports34.may_print_live_ob_ch34, name='may_print_live_ob_ch34'),
    path('june_details_live_ob_ch34/',reports34.june_details_live_ob_ch34,name='june_details_live_ob_ch34'),
    path('june_print_live_ob_ch34/', reports34.june_print_live_ob_ch34, name='june_print_live_ob_ch34'),

    path('july_details_live_ob_ch34/', reports34.july_details_live_ob_ch34, name='july_details_live_ob_ch34'),
    path('july_print_live_ob_ch34/', reports34.july_print_live_ob_ch34, name='july_print_live_ob_ch34'),
    path('auguest_details_live_ob_ch34/', reports34.auguest_details_live_ob_ch34, name='auguest_details_live_ob_ch34'),
    path('auguest_print_live_ob_ch34/', reports34.auguest_print_live_ob_ch34, name='auguest_print_live_ob_ch34'),
    path('sept_details_live_ob_ch34/', reports34.sept_details_live_ob_ch34, name='sept_details_live_ob_ch34'),
    path('sept_print_live_ob_ch34/', reports34.sept_print_live_ob_ch34, name='sept_print_live_ob_ch34'),

    path('october_details_live_ob_ch34/', reports34.october_details_live_ob_ch34, name='october_details_live_ob_ch34'),
    path('october_print_live_ob_ch34/', reports34.october_print_live_ob_ch34, name='october_print_live_ob_ch34'),
    path('nov_details_live_ob_ch34/', reports34.nov_details_live_ob_ch34, name='nov_details_live_ob_ch34'),
    path('nov_print_live_ob_ch34/', reports34.nov_print_live_ob_ch34, name='nov_print_live_ob_ch34'),
    path('dec_details_live_ob_ch34/', reports34.dec_details_live_ob_ch34, name='dec_details_live_ob_ch34'),
    path('dec_print_live_ob_ch34/', reports34.dec_print_live_ob_ch34, name='dec_print_live_ob_ch34'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch34/', reports34.viewall_vaccant_room_ob_ch34, name='viewall_vaccant_room_ob_ch34'),

    path('d_ob_ch34/', branch34.dynamic, name='dynamic'),

    path('manage_bed_ob_ch34/', branch34.manage_bed_ob_ch34, name='manage_bed_ob_ch34'),
    path('manage_new_guest_ob_ch34/', branch34.manage_new_guest_ob_ch34, name='manage_new_guest_ob_ch34'),
    path('manage_update_new_guest_ob_ch34/<id>', branch34.manage_update_new_guest_ob_ch34, name='manage_update_new_guest_ob_ch34'),
    path('manage_update_beds_ob_ch34/<id>', branch34.manage_update_beds_ob_ch34, name='manage_update_beds_ob_ch34'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch34/', branch34.view_all_due_amt_ob_ch34, name='view_all_due_amt_ob_ch34'),
    path('due_amt_mgt_choose_months_ob_ch34/', branch34.due_amt_mgt_choose_months_ob_ch34, name='due_amt_mgt_choose_months_ob_ch34'),

    path('view_jan_account_details_ob_ch34/', branch34.view_jan_account_details_ob_ch34, name='view_jan_account_details_ob_ch34'),
    path('jan_account_mgt_ob_ch34/<id>',branch34.jan_account_mgt_ob_ch34,name='jan_account_mgt_ob_ch34'),
    path('view_feb_account_details_ob_ch34/', branch34.view_feb_account_details_ob_ch34, name='view_feb_account_details_ob_ch34'),
    path('feb_account_mgt_ob_ch34/<id>',branch34.feb_account_mgt_ob_ch34,name='feb_account_mgt_ob_ch34'),
    path('view_march_account_details_ob_ch34/', branch34.view_march_account_details_ob_ch34, name='view_march_account_details_ob_ch34'),
    path('march_account_mgt_ob_ch34/<id>',branch34.march_account_mgt_ob_ch34,name='march_account_mgt_ob_ch34'),
    path('view_april_account_details_ob_ch34/', branch34.view_april_account_details_ob_ch34, name='view_april_account_details_ob_ch34'),
    path('april_account_mgt_ob_ch34/<id>',branch34.april_account_mgt_ob_ch34,name='april_account_mgt_ob_ch34'),

    path('view_may_account_details_ob_ch34/',branch34.view_may_account_details_ob_ch34,name='view_may_account_details_ob_ch34'),
    path('may_account_mgt_ob_ch34/<id>', branch34.may_account_mgt_ob_ch34, name='may_account_mgt_ob_ch34'),
    path('view_june_account_details_ob_ch34/', branch34.view_june_account_details_ob_ch34, name='view_june_account_details_ob_ch34'),
    path('june_account_mgt_ob_ch34/<id>',branch34.june_account_mgt_ob_ch34,name='june_account_mgt_ob_ch34'),
    path('view_july_account_details_ob_ch34/', branch34.view_july_account_details_ob_ch34, name='view_july_account_details_ob_ch34'),
    path('july_account_mgt_ob_ch34/<id>',branch34.july_account_mgt_ob_ch34,name='july_account_mgt_ob_ch34'),
    path('view_auguest_account_details_ob_ch34/', branch34.view_auguest_account_details_ob_ch34, name='view_auguest_account_details_ob_ch34'),
    path('auguest_account_mgt_ob_ch34/<id>',branch34.auguest_account_mgt_ob_ch34,name='auguest_account_mgt_ob_ch34'),

    path('view_sept_account_details_ob_ch34/', branch34.view_sept_account_details_ob_ch34, name='view_sept_account_details_ob_ch34'),
    path('sept_account_mgt_ob_ch34/<id>',branch34.sept_account_mgt_ob_ch34,name='sept_account_mgt_ob_ch34'),
    path('view_october_account_details_ob_ch34/', branch34.view_october_account_details_ob_ch34, name='view_october_account_details_ob_ch34'),
    path('october_account_mgt_ob_ch34/<id>',branch34.october_account_mgt_ob_ch34,name='october_account_mgt_ob_ch34'),
    path('view_nov_account_details_ob_ch34/', branch34.view_nov_account_details_ob_ch34, name='view_nov_account_details_ob_ch34'),
    path('nov_account_mgt_ob_ch34/<id>',branch34.nov_account_mgt_ob_ch34,name='nov_account_mgt_ob_ch34'),
    path('view_dec_account_details_ob_ch34/', branch34.view_dec_account_details_ob_ch34, name='view_dec_account_details_ob_ch34'),
    path('dec_account_mgt_ob_ch34/<id>',branch34.dec_account_mgt_ob_ch34,name='dec_account_mgt_ob_ch34'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch34', admin_dashboard_calculations_br34.monthly_details_due_ob_ch34, name='monthly_details_due_ob_ch34'),
    path('monthly_collection_details_ob_ch34/', admin_dashboard_calculations_br34.monthly_collection_details_ob_ch34, name='monthly_collection_details_ob_ch34'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch34/',branch34.guest_all_ob_ch34,name='guest_all_ob_ch34'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category34/', accounts34.view_all_category34, name='view_all_category34'),
    path('create_new_category34/', accounts34.create_new_category34, name='create_new_category34'),
    path('regi_new_category34/', accounts34.regi_new_category34, name='regi_new_category34'),
    path('update_category34/<id>',accounts34.update_category34,name='update_category34'),

    path('delete_category34/<id>', accounts34.delete_category34, name='delete_category34'),
    path('view_all_category_delete34/', accounts34.view_all_category_delete34, name='view_all_category_delete34'),

    path('regi_multiple_new_category34/', accounts34.regi_multiple_new_category34, name='regi_multiple_new_category34'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items34/', accounts34.view_all_items34, name='view_all_items34'),
    path('create_new_item34/', accounts34.create_new_item34, name='create_new_item34'),
    path('regi_new_item34/', accounts34.regi_new_item34, name='regi_new_item34'),
    path('delete_item34/<id>',accounts34.delete_item34,name='delete_item34'),
    path('update_item34/<id>', accounts34.update_item34, name='update_item34'),
    path('view_all_items_delete34/',accounts34.view_all_items_delete34,name='view_all_items_delete34'),

    path('regi_multiple_new_item34/', accounts34.regi_multiple_new_item34, name='regi_multiple_new_item34'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger34/', accounts34.view_all_ledger34, name='view_all_ledger34'),
    path('create_new_ledger34/', accounts34.create_new_ledger34, name='create_new_ledger34'),
    path('regi_new_ledger34/', accounts34.regi_new_ledger34, name='regi_new_ledger34'),
    path('delete_ledger34/<id>',accounts34.delete_ledger34,name='delete_ledger34'),
    path('update_ledger34/<id>',accounts34.update_ledger34,name='update_ledger34'),
    path('view_all_ledger_delete34/',accounts34.view_all_ledger_delete34,name='view_all_ledger_delete34'),

    path('regi_multiple_new_ledger34/', accounts34.regi_multiple_new_ledger34, name='regi_multiple_new_ledger34'),

    ##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book34/', accounts34.view_all_accounts_book34, name='view_all_accounts_book34'),
    path('create_new_accounts_book34/', accounts34.create_new_accounts_book34, name='create_new_accounts_book34'),
    path('regi_new_accounts_book34/', accounts34.regi_new_accounts_book34, name='regi_new_accounts_book34'),
    path('update_accounts_book34/<id>',accounts34.update_accounts_book34,name='update_accounts_book34'),
    path('delete_accounts_book34/<id>',accounts34.delete_accounts_book34,name='delete_accounts_book34'),
    path('view_all_accounts_book_delete34/',accounts34.view_all_accounts_book_delete34,name='view_all_accounts_book_delete34'),

    path('regi_multiple_new_accounts_book34/', accounts34.regi_multiple_new_accounts_book34,name='regi_multiple_new_accounts_book34'),

    ##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries34/', accounts34.get_countries34, name='get_countries34'),

    path('in_exp_items_entry34/', accounts34.in_exp_items_entry34, name='in_exp_items_entry34'),
    path('reg_in_exp_items_entry34/', accounts34.reg_in_exp_items_entry34, name='reg_in_exp_items_entry34'),
    path('delete_journal34/<id>',accounts34.delete_journal34,name='delete_journal34'),
    path('update_in_exp_items_entry34/<id>',accounts34.update_in_exp_items_entry34,name='update_in_exp_items_entry34'),
    path('detailed_journal_report34/',accounts34.detailed_journal_report34,name='detailed_journal_report34'),
    path('journal_report_deleted34/',accounts34.journal_report_deleted34,name='journal_report_deleted34'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise34/', accounts34.daily_category_wise34, name='daily_category_wise34'),
    path('monthly_category_based_reports34/',accounts34.monthly_category_based_reports34,name='monthly_category_based_reports34'),
    path('yearly_category_based_reports34/', accounts34.yearly_category_based_reports34,name='yearly_category_based_reports34'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed34/', accounts34.daily_detailed34, name='daily_detailed34'),
    path('monthly_detailed34/',accounts34.monthly_detailed34,name='monthly_detailed34'),
    path('yearly_detailed34/',accounts34.yearly_detailed34,name='yearly_detailed34'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports34/', accounts34.item_based_reports34, name='item_based_reports34'),
    path('daily_item_based_reports34/',accounts34.daily_item_based_reports34,name='daily_item_based_reports34'),
    path('monthly_item_based_reports34/',accounts34.monthly_item_based_reports34,name='monthly_item_based_reports34'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports34/', accounts34.ledger_based_reports34, name='ledger_based_reports34'),
    path('monthly_ledger_based_reports34/', accounts34.monthly_ledger_based_reports34, name='monthly_ledger_based_reports34'),
    path('daily_ledger_based_reports34/',accounts34.daily_ledger_based_reports34,name='daily_ledger_based_reports34'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports34/', accounts34.accounts_book_based_reports34, name='accounts_book_based_reports34'),
    path('daily_accounts_book_based_reports34/',accounts34.daily_accounts_book_based_reports34,name='daily_accounts_book_based_reports34'),
    path('monthly_accounts_book_based_reports34/',accounts34.monthly_accounts_book_based_reports34,name='monthly_accounts_book_based_reports34'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months34/', accounts34.monthly_reports_choose_months34, name='monthly_reports_choose_months34'),
    path('monthly_detailed_daily_in_exp_items_report34/<mo>',accounts34.monthly_detailed_daily_in_exp_items_report34,name='monthly_detailed_daily_in_exp_items_report34'),

    path('single_monthly_reports_choose_months34/', accounts34.single_monthly_reports_choose_months34,name='single_monthly_reports_choose_months34'),
    path('single_monthly_daily_in_exp_items_report34/<mo>',accounts34.single_monthly_daily_in_exp_items_report34,name='single_monthly_daily_in_exp_items_report34'),

    path('accounts_dash_board_ob_ch34/',accounts34.accounts_dash_board_ob_ch34,name='accounts_dash_board_ob_ch34'),
    path('accounts_dash_board34/',accounts34.accounts_dash_board34,name='accounts_dash_board34'),

    path('profit_sharing_choose_months34', accounts34.profit_sharing_choose_months34,name='profit_sharing_choose_months34'),
    path('profit_sharing34/<mo>', accounts34.profit_sharing34, name='profit_sharing34'),
    path('view_share_holders34', accounts34.view_share_holders34, name='view_share_holders34'),
    path('create_share_holders34', accounts34.create_share_holders34, name='create_share_holders34'),
    path('regi_share_holders34', accounts34.regi_share_holders34, name='regi_share_holders34'),
    path('update_share_holders34/<id>', accounts34.update_share_holders34, name='update_share_holders34'),
    path('delete_share_holders34/<id>', accounts34.delete_share_holders34, name='delete_share_holders34'),
    path('view_deleted_share_holders34', accounts34.view_deleted_share_holders34, name='view_deleted_share_holders34'),

    path('regi_multiple_share_holders34', accounts34.regi_multiple_share_holders34, name='regi_multiple_share_holders34'),

    #############BRANCH SETTINGS START HERE ########################

    path('guest_rent_update_ob_ch34/', branch_settings34.guest_rent_update_ob_ch34, name='guest_rent_update_ob_ch34'),

    ############BRANCH SETTINGS END HERE ############################

]

