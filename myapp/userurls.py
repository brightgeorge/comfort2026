from django.urls import path
from . import views
from . import guest_calculations
from . import room_vacant_calculations
from . import collection_calculations

urlpatterns = [

    path('', views.index, name='index'),
    path('login_request/', views.login_request, name='login_request'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('Comfortadmin_dashboard', views.Comfortadmin_dashboard, name='Comfortadmin_dashboard'),

    # ****user start here *****
    path('view_all_users/', views.view_all_users, name='view_all_users'),
    path('create_user/', views.create_user, name='create_user'),
    path('user_regi/', views.user_regi, name='user_regi'),
    path('delete_user/<id>', views.delete_user, name='delete_user'),
    path('user_update/<id>', views.user_update, name='user_update'),
    # ****user end here ******

    path('select_branch/',views.select_branch,name='select_branch'),
    path('admin_home/',views.admin_home,name='admin_home'),

    path('branchwise_guest_details/',guest_calculations.branchwise_guest_details,name='branchwise_guest_details'),

    path('vaccant_room_details/',room_vacant_calculations.vaccant_room_details,name='vaccant_room_details'),

    path('total_collection_details/',collection_calculations.total_collection_details,name='total_collection_details'),

    # logout
    path('logout/', views.logout, name='logout'),


]