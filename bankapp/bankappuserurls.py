from django.urls import path
from . import views
from . import banking_app

urlpatterns = [

    path('view_all_members/', banking_app.view_all_members, name='view_all_members'),
    path('member_creation/', banking_app.member_creation, name='member_creation'),
    path('member_regi/', banking_app.member_regi, name='member_regi'),
    path('update_member/<id>', banking_app.update_member, name='update_member'),
    path('delete_member/<id>', banking_app.delete_member, name='delete_member'),
    path('view_all_deleted_members/', banking_app.view_all_deleted_members, name='view_all_deleted_members'),

    path('choose_months/<id>', banking_app.choose_months, name='choose_months'),
    path('enter_amount/<id>', banking_app.enter_amount, name='enter_amount'),
    path('amount_regi/', banking_app.amount_regi, name='amount_regi'),
    path('view_all_transaction/', banking_app.view_all_transaction, name='view_all_transaction'),
    path('view_all_transaction_byid/<id>/<mth>', banking_app.view_all_transaction_byid, name='view_all_transaction_byid'),
    path('memberwise_transaction_details/', banking_app.memberwise_transaction_details, name='memberwise_transaction_details'),
    path('update_amount_transaction/<id>', banking_app.update_amount_transaction, name='update_amount_transaction'),
    path('delete_amount_transaction/<id>', banking_app.delete_amount_transaction, name='delete_amount_transaction'),
    path('view_all_deleted_transaction/<id>', banking_app.view_all_deleted_transaction, name='view_all_deleted_transaction'),

]