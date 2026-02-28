from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from datetime import datetime, date, time
from django.utils import timezone
from django.contrib import messages
from .models import LedgerEntry, LedgerEntryBackups
import openpyxl

from decimal import Decimal
from django.db.models import Max

def _fmt_currency(value):
    try:
        return '₹ ' + f"{value:,.2f}"
    except Exception:
        return value

def dashboard_OLD(request):
    entries = LedgerEntry.objects.filter(flag=1).order_by('timestamp', 'id')

    start = request.GET.get('start')
    end = request.GET.get('end')
    show_all = request.GET.get('show_all')

    if show_all:
        filtered = entries
        heading = "All Entries"
    elif start and end:
        try:
            s = datetime.fromisoformat(start)
            e = datetime.fromisoformat(end)
            filtered = entries.filter(timestamp__range=[s,e])
            heading = f"{s.date()} to {e.date()}"
        except Exception:
            filtered = entries.none()
            heading = "Invalid range"
    else:
        today = timezone.now().date()
        today_start = datetime.combine(today, time.min)
        today_end = datetime.combine(today, time.max)
        filtered = entries.filter(timestamp__range=[today_start, today_end])
        heading = str(today)

    credits = filtered.filter(credit_amount__isnull=False).order_by('timestamp','id')
    debits = filtered.filter(debit_amount__isnull=False).order_by('timestamp','id')

    total_credit = sum(float(e.credit_amount or 0) for e in credits)
    total_debit = sum(float(e.debit_amount or 0) for e in debits)
    balance = total_credit - total_debit

    context = {
        'credits': credits,
        'debits': debits,
        'total_credit': total_credit,
        'total_debit': total_debit,
        'balance': balance,
        'total_credit_display': _fmt_currency(total_credit),
        'total_debit_display': _fmt_currency(total_debit),
        'balance_display': _fmt_currency(balance),
        'start': start,
        'end': end,
        'show_all': show_all,
        'heading': heading,
    }
    return render(request, 'ledger_app/dashboard_side_by_side_with_msgs.html', context)

def dashboard(request):
    entries = LedgerEntry.objects.filter(flag=1).order_by('timestamp', 'id')

    start = request.GET.get('start')
    end = request.GET.get('end')
    show_all = request.GET.get('show_all')

    # If a date range is selected
    if start and end:
        try:
            s = datetime.fromisoformat(start)
            e = datetime.fromisoformat(end)
            filtered = entries.filter(timestamp__range=[s, e])
            heading = f"{s.date()} to {e.date()}"
        except Exception:
            filtered = entries.none()
            heading = "Invalid range"

    # If "Show All" clicked or no filters (default)
    else:
        filtered = entries
        heading = "All Entries"

    credits = filtered.filter(credit_amount__isnull=False).order_by('timestamp', 'id')
    debits = filtered.filter(debit_amount__isnull=False).order_by('timestamp', 'id')

    total_credit = sum(float(e.credit_amount or 0) for e in credits)
    total_debit = sum(float(e.debit_amount or 0) for e in debits)
    balance = total_credit - total_debit

    context = {
        'credits': credits,
        'debits': debits,
        'total_credit': total_credit,
        'total_debit': total_debit,
        'balance': balance,
        'total_credit_display': _fmt_currency(total_credit),
        'total_debit_display': _fmt_currency(total_debit),
        'balance_display': _fmt_currency(balance),
        'start': start,
        'end': end,
        'show_all': show_all,
        'heading': heading,
    }
    return render(request, 'ledger_app/dashboard_side_by_side_with_msgs.html', context)

def add_credit(request):
    if request.method == 'POST':
        from django.utils import timezone

        today = timezone.now()
        date_part = today.strftime("%d%m%Y")
        print('date_part date_part',date_part)

        count = LedgerEntry.objects.count() + 1
        print('count count', count)
        result_entry_id = int(f"{date_part}{count}")
        print('result_entry_id result_entry_id',result_entry_id)

        particular = request.POST.get('particular') or None
        amount = request.POST.get('amount') or None
        amount = float(amount) if amount not in [None,''] else None

        from datetime import datetime
        now = datetime.now()

        LedgerEntry.objects.create(particular_credit=particular, credit_amount=amount,
                                   timestamp=now,created_at=now,updated_at=now,entry_id=result_entry_id, flag=1)
        LedgerEntryBackups.objects.create(particular_credit=particular, credit_amount=amount,
                                          timestamp=now,created_at=now,updated_at=now,entry_id=result_entry_id, flag=1)
        messages.success(request, 'Credit entry added successfully!')
        return redirect('ledger_list')
    return render(request, 'ledger_app/add_credit.html')

def add_debit(request):
    if request.method == 'POST':
        from django.utils import timezone

        today = timezone.now()
        date_part = today.strftime("%d%m%Y")
        print('date_part date_part', date_part)

        count = LedgerEntry.objects.count() + 1
        print('count count', count)
        result_entry_id = int(f"{date_part}{count}")
        print('result_entry_id result_entry_id', result_entry_id)

        particular = request.POST.get('particular') or None
        amount = request.POST.get('amount') or None
        amount = float(amount) if amount not in [None,''] else None

        from datetime import datetime
        now = datetime.now()

        LedgerEntry.objects.create(particular_debit=particular, debit_amount=amount,
                                   timestamp=now,created_at=now,updated_at=now,entry_id=result_entry_id, flag=1)
        LedgerEntryBackups.objects.create(particular_debit=particular, debit_amount=amount,
                                          timestamp=now,created_at=now,updated_at=now,entry_id=result_entry_id, flag=1)
        messages.success(request, 'Debit entry added successfully!')
        return redirect('ledger_list')
    return render(request, 'ledger_app/add_debit.html')

def edit_credit(request, id):
    entry = get_object_or_404(LedgerEntry, id=id)
    if request.method == 'POST':
        entry.particular_credit = request.POST.get('particular') or None
        amt = request.POST.get('amount') or None
        entry.credit_amount = float(amt) if amt not in [None,''] else None
        entry.particular_debit = None
        entry.debit_amount = None
        entry.save()
        print('id id id', id)

        entry = LedgerEntry.objects.filter(id=id).first()

        from datetime import datetime
        now = datetime.now()
        LedgerEntryBackups.objects.create(particular_credit=request.POST.get('particular') or None,
                                          credit_amount=float(amt) if amt not in [None,''] else None,
                                          timestamp=now,created_at=now,updated_at=now,entry_id=entry.entry_id,flag=1)
        messages.success(request, 'Credit entry updated successfully!')
        return redirect('ledger_list')
    return render(request, 'ledger_app/edit_credit.html', {'entry': entry})

def edit_debit(request, id):
    entry = get_object_or_404(LedgerEntry, id=id)
    if request.method == 'POST':
        entry.particular_debit = request.POST.get('particular') or None
        amt = request.POST.get('amount') or None
        entry.debit_amount = float(amt) if amt not in [None,''] else None
        entry.particular_credit = None
        entry.credit_amount = None
        entry.save()

        entry = LedgerEntry.objects.filter(id=id).first()

        from datetime import datetime
        now = datetime.now()
        LedgerEntryBackups.objects.create(particular_debit=request.POST.get('particular') or None,
                                          debit_amount=float(amt) if amt not in [None,''] else None,
                                          timestamp=now,created_at=now,updated_at=now,entry_id=entry.entry_id,flag=1)
        messages.success(request, 'Debit entry updated successfully!')
        return redirect('ledger_list')
    return render(request, 'ledger_app/edit_debit.html', {'entry': entry})

def delete_credit(request, id):
    entry = get_object_or_404(LedgerEntry, id=id)
    entry.flag = 2
    entry.save()
    messages.success(request, 'Credit entry deleted successfully!')
    return redirect('ledger_list')

def delete_debit(request, id):
    entry = get_object_or_404(LedgerEntry, id=id)
    entry.flag = 2
    entry.save()
    messages.success(request, 'Debit entry deleted successfully!')
    return redirect('ledger_list')

def export_ledger_to_excel(request):
    entries = LedgerEntry.objects.filter(flag=1).order_by('timestamp', 'id')

    start = request.GET.get('start')
    end = request.GET.get('end')
    show_all = request.GET.get('show_all')

    if show_all:
        filtered = entries
    elif start and end:
        try:
            s = datetime.fromisoformat(start)
            e = datetime.fromisoformat(end)
            filtered = entries.filter(timestamp__range=[s,e])
        except Exception:
            filtered = entries.none()
    else:
        today = timezone.now().date()
        today_start = datetime.combine(today, time.min)
        today_end = datetime.combine(today, time.max)
        filtered = entries.filter(timestamp__range=[today_start, today_end])

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Ledger Report"
    ws.append(['Timestamp', 'Credit Particular', 'Credit Amount', 'Debit Particular', 'Debit Amount'])
    total_credit = 0
    total_debit = 0
    for entry in filtered:
        ts = entry.timestamp.isoformat() if entry.timestamp else ''
        ws.append([
            ts,
            entry.particular_credit or '',
            float(entry.credit_amount or 0),
            entry.particular_debit or '',
            float(entry.debit_amount or 0),
        ])
        total_credit += float(entry.credit_amount or 0)
        total_debit += float(entry.debit_amount or 0)
    ws.append([])
    ws.append(['','Total Credit', total_credit,'Total Debit', total_debit])
    ws.append(['','','','Balance', total_credit - total_debit])
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=ledger_report.xlsx'
    wb.save(response)
    return response

def credit_all_entry_history(request):
    entries = LedgerEntryBackups.objects.filter(flag=1).order_by('-id')
    credits = entries.filter(credit_amount__isnull=False).order_by('-id')
    context = {
        'entries': credits,
    }
    return render(request, 'ledger_app/credit_all_entry_history.html', context)
def debit_all_entry_history(request):
    entries = LedgerEntryBackups.objects.filter(flag=1).order_by('-id')
    debits = entries.filter(debit_amount__isnull=False).order_by('-id')
    context = {
        'entries': debits,
    }
    return render(request, 'ledger_app/debit_all_entry_history.html', context)


def individual_itembased_credit_entry_history(request,entry_id):
    entries = LedgerEntryBackups.objects.filter(flag=1,entry_id=entry_id).order_by('-id')
    credits = entries.filter(credit_amount__isnull=False).order_by('-id')
    context = {
        'entries': credits,
    }
    return render(request, 'ledger_app/individual_itembased_history/individual_itembased_credit_entry_history.html', context)

def individual_itembased_debit_entry_history(request,entry_id):
    entries = LedgerEntryBackups.objects.filter(flag=1,entry_id=entry_id).order_by('-id')
    debits = entries.filter(debit_amount__isnull=False).order_by('-id')
    context = {
        'entries': debits,
    }
    return render(request, 'ledger_app/individual_itembased_history/individual_itembased_debit_entry_history.html', context)



#########################################
####new server backup code start here
########################################

def view_all_LedgerEntry_entries(request):
    result = LedgerEntry.objects.all()
    context = {
        'entries': result,
    }
    return render(request, 'ledger_app/backup/view_all_LedgerEntry_entries.html', context)












import pandas as pd
from django.shortcuts import render

def upload_ledger_excel(request):
    rows = []

    if request.method == "POST" and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']

        # Read Excel
        df = pd.read_excel(excel_file)

        # Replace NaN with None
        df = df.where(pd.notnull(df), None)

        # Loop rows
        for _, row in df.iterrows():
            rows.append({
                'timestamp': row.get('Timestamp'),
                'credit_particular': row.get('Credit Particular'),
                'credit_amount': row.get('Credit Amount') or 0,
                'debit_particular': row.get('Debit Particular'),
                'debit_amount': row.get('Debit Amount') or 0,
                'entry_id': row.get('entry_id') or 0,
            })

    return render(
        request,
        'ledger_app/backup/upload_ledger.html',
        {'rows': rows}
    )





from django.shortcuts import redirect
from django.utils.dateparse import parse_datetime
from decimal import Decimal
from .models import LedgerEntry


def safe_decimal(value):
    if value in [None, '', 'nan', 'NaN']:
        return None
    try:
        return Decimal(value)
    except:
        return None


def save_ledger_entries(request):
    if request.method == "POST":

        timestamps = request.POST.getlist('timestamp[]')
        pc = request.POST.getlist('credit_particular[]')
        ca = request.POST.getlist('credit_amount[]')
        pd_ = request.POST.getlist('debit_particular[]')
        da = request.POST.getlist('debit_amount[]')
        ei = request.POST.getlist('entry_id[]')

        entries = []

        total_rows = len(timestamps)

        for i in range(total_rows):

            # Skip empty rows
            if not pc[i] and not pd_[i]:
                continue

            # Convert timestamp properly
            parsed_timestamp = parse_datetime(timestamps[i])

            entries.append(
                LedgerEntry(
                    timestamp=parsed_timestamp,
                    particular_credit=pc[i] or None,
                    credit_amount=safe_decimal(ca[i]),
                    particular_debit=pd_[i] or None,
                    debit_amount=safe_decimal(da[i]),
                    entry_id=ei[i] or None,
                    flag=1  # Default flag
                )
            )

        if entries:
            LedgerEntry.objects.bulk_create(entries)

        return redirect('upload_ledger')

#################################################
#####HISTORY BACKUP CODE START HERE ############
################################################
######CREDIT HISTORY BACKUP START HERE ###########

def all_history_entries(request):
    entries = LedgerEntryBackups.objects.filter(flag=1).order_by('-id')

    context = {
        'entries': entries,
    }
    return render(request, 'ledger_app/all_history_entries.html', context)


def view_all_CREDIT_HISTORY_entries(request):
    result = LedgerEntry.objects.all()
    context = {
        'entries': result,
    }
    return render(request, 'ledger_app/backup/history/credit/view_all_CREDIT_HISTORY_entries.html', context)




