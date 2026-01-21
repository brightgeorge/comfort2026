from django.urls import path
from . import tally

urlpatterns = [
    path('ledger_list/', tally.dashboard, name='ledger_list'),
    path('add-credit/', tally.add_credit, name='add_credit'),
    path('add-debit/', tally.add_debit, name='add_debit'),
    path('edit-credit/<int:id>/', tally.edit_credit, name='edit_credit'),
    path('edit-debit/<int:id>/', tally.edit_debit, name='edit_debit'),
    path('delete-credit/<int:id>/', tally.delete_credit, name='delete_credit'),
    path('delete-debit/<int:id>/', tally.delete_debit, name='delete_debit'),
    path('export/', tally.export_ledger_to_excel, name='export_ledger_to_excel'),

    path('credit_all_entry_history/',tally.credit_all_entry_history,name='credit_all_entry_history'),
    path('debit_all_entry_history/',tally.debit_all_entry_history,name='debit_all_entry_history'),

    path('view_all_LedgerEntry_entries/',tally.view_all_LedgerEntry_entries,name='view_all_LedgerEntry_entries'),

    path('upload-ledger/', tally.upload_ledger_excel, name='upload_ledger'),
    path('save-ledger/', tally.save_ledger_entries, name='save_ledger'),

]