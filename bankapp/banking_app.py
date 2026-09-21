from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum

from myapp.models import *
from bankapp.models import *
import datetime

# Create your views here.

def member_creation(request):
    if 'username' in request.session:
        return render(request,'banking_app/members_details/member_creation.html')
    return render(request, 'index.html')


def member_regi(request):
    itname = request.POST.get('name')
    chkitemname = member_details.objects.filter(member_name=itname).exists()
    print('this is m y test uname',chkitemname)

    if chkitemname == True:
        messages.info(request, 'Member name is already exists!. please try another one')
        return render(request, 'banking_app/members_details/member_creation.html', )
    else:
        if request.method == 'POST':
            mem_name = request.POST.get('name')
            uc=member_details()
            uc.member_name = mem_name

            uc.enter_by = 'CB ' + request.session['username']
            import datetime
            uc.cb_date = datetime.datetime.now()
            uc.ub_flag = 0

            uc.member_flag = 1
            uc.save()

    messages.info(request,'Member created sucessfully')
    context = {
        'member': member_details.objects.filter(member_flag=1),
    }
    return render(request,'banking_app/members_details/view_all_members.html',context)

def view_all_members(request):
    if 'username' in request.session:
        context={
            'member': member_details.objects.filter(member_flag=1),
        }
        return render(request,'banking_app/members_details/view_all_members.html',context)
    return render(request,'index.html')

def delete_member(request,id):
    if 'username' in request.session:
        r = member_details.objects.all().filter(id=id, member_flag=1).exists()
        if r == True:
            d = member_details.objects.get(id=id)
            d.deleted_by = 'DB ' + request.session['username']
            import datetime
            d.db_date = datetime.datetime.now()
            d.member_flag = 2
            d.save()
            messages.info(request, 'Member deleted sucessfully')
            context = {
                'member': member_details.objects.filter(member_flag=1),
            }
            return render(request, 'banking_app/members_details/view_all_members.html', context)
        else:
            messages.info(request, 'Member already  Deleted')
            context = {
                'member': member_details.objects.filter(member_flag=1),
            }
            return render(request, 'banking_app/members_details/view_all_members.html', context)
        return render(request, 'index.html')
    return render(request, 'index.html')

def update_member(request,id):
    mem_name = request.POST.get('name')
    #chkitemname = member_details.objects.filter(member_name=mem_name).exists()
    #print('this is m y test uname',chkitemname)

    # Check whether another member already has this name
    chkitemname = member_details.objects.filter(member_name=mem_name).exclude(id=id).exists()

    if chkitemname == True:
        messages.info(request, 'Member name is already exists!. please try another one')
        context = {
            'sd': member_details.objects.get(member_flag=1, id=id),
        }
        return render(request, 'banking_app/members_details/update_member.html', context)
    else:
        if request.method == 'POST':
            mem_name = request.POST.get('name')

            uc=member_details.objects.get(id=id)
            uc.member_name = mem_name

            uc.updated_by = 'UB ' + request.session['username']
            import datetime
            uc.ub_date = datetime.datetime.now()
            uc.ub_flag = 1

            uc.member_flag = 1
            uc.save()

            messages.info(request,'Member Updated sucessfully')
            return redirect('view_all_members')
    context = {
        'member': member_details.objects.filter(member_flag=1),
        'sd': member_details.objects.get(member_flag=1,id=id),
    }
    return render(request,'banking_app/members_details/update_member.html',context)

def view_all_deleted_members(request):
    if 'username' in request.session:
        context={
            'member': member_details.objects.filter(member_flag=2),
        }
        return render(request,'banking_app/members_details/view_all_deleted_members.html',context)
    return render(request,'index.html')

#####################################################################
def choose_months(request,id):
    if 'username' in request.session:
        context = {
            'member': member_details.objects.filter(member_flag=1),
            'id': id,
        }
        return render(request,'banking_app/amount_transaction/choose_months.html',context)
    return render(request, 'index.html')
def enter_amount(request,id):
    if 'username' in request.session:
        context = {
            'member': member_details.objects.filter(member_flag=1),
            'id': id,
        }
        return render(request,'banking_app/amount_transaction/enter_amount.html',context)
    return render(request, 'index.html')


def amount_regi(request):
    if 'username' in request.session:
        if request.method == 'POST':

            from datetime import datetime
            now = datetime.now()
            #print("Date:", now.date())
            #print("Time:", now.time())
            formatted = now.strftime("%H:%M:%S")
            #print('formatted', formatted)

            #month_number = datetime.now().month



            mem_name = request.POST.get('name')
            particular = request.POST.get('particular')
            transaction_amt = request.POST.get('amount')
            date = request.POST.get('date')
            print('my date date', date)
            month = int(date.split('-')[1])

            print('my date:', date)
            print('my month:', month)

            uc=bank_amount_transaction()
            uc.member_name = mem_name
            uc.particulars = particular
            uc.transaction_amount = transaction_amt
            uc.date = date

            uc.transaction_enter_date = now.date()
            uc.transaction_enter_time = formatted
            uc.month = month

            uc.enter_by = 'CB ' + request.session['username']
            import datetime
            uc.cb_date = datetime.datetime.now()
            uc.ub_flag = 0

            uc.flag = 1

            uc.save()

            messages.info(request,'Bank transaction successfully completed')
            return redirect('memberwise_transaction_details')

def view_all_transaction_byid_OLD(request,id,mth):
    if 'username' in request.session:
        sum = sum(bank_amount_transaction.objects.all().filter(member_name=id,month=mth).order_by('-id'))
        context={
            'transactions': bank_amount_transaction.objects.all().filter(member_name=id,month=mth).order_by('-id'),
            'res_sum': sum,
        }
        return render(request,'banking_app/amount_transaction/view_all_transaction.html', context)
    return render(request,'index.html')

def view_all_transaction_byid(request, id, mth):
    if 'username' in request.session:

        transactions = bank_amount_transaction.objects.filter(
            member_name=id,
            month=mth,
            flag = 1
        ).order_by('-id')

        result = transactions.aggregate(
            total=Sum('transaction_amount')
        )

        context = {
            'transactions': transactions,
            'res_sum': result['total'] or 0,
            'id': id,
        }
        return render(request,'banking_app/amount_transaction/view_all_transaction.html', context)
    return render(request, 'index.html')

def view_all_transaction(request):
    if 'username' in request.session:
        context={
            'transactions': bank_amount_transaction.objects.all().order_by('-id'),
        }
        return render(request,'banking_app/amount_transaction/view_all_transaction.html', context)
    return render(request,'index.html')

def memberwise_transaction_details_OLD(request):
    if 'username' in request.session:
        mem_l = []
        mem = member_details.objects.filter(member_flag=1)
        for i in mem:
            mem_l.append(i.member_name)

        tran_details = bank_amount_transaction.objects.all().order_by('-id')
        sum_ml=mem_l
        final_sum_ml = []
        for i in len(mem_l):
            for j in tran_details:
                if j.member_name == mem_l[i]:
                    sum_ml[i]=j.transaction_amount
            final_sum_ml.append(sum(sum_ml))

        res = member_details.objects.filter(member_flag=1)
        for i in res:
            i.sum_amt = final_sum_ml[i]

        context={
            #'member': member_details.objects.filter(member_flag=1),
            'member': res,
        }
        return render(request,'banking_app/amount_transaction/memberwise_transaction_details.html',context)
    return render(request,'index.html')

def memberwise_transaction_details_OLD1(request):
    if 'username' in request.session:

        members = member_details.objects.filter(member_flag=1)
        transactions = bank_amount_transaction.objects.all()

        for member in members:
            total = 0

            for transaction in transactions:
                if transaction.member_name == member.member_name:
                    total += transaction.transaction_amount

            member.sum_amt = total

        context = {
            'member': members,
        }

        return render(
            request,
            'banking_app/amount_transaction/memberwise_transaction_details.html',
            context
        )

    return render(request, 'index.html')

def memberwise_transaction_details(request):
    if 'username' in request.session:

        members = member_details.objects.filter(member_flag=1)
        transactions = bank_amount_transaction.objects.filter(flag=1)

        for member in members:
            total = 0

            for transaction in transactions:
                if transaction.member_name == member.member_name:

                    try:
                        total += float(transaction.transaction_amount)
                    except (ValueError, TypeError):
                        continue

            member.sum_amt = total

        context = {
            'member': members,
        }

        return render(
            request,
            'banking_app/amount_transaction/memberwise_transaction_details.html',
            context
        )

    return render(request, 'index.html')



def update_amount_transaction(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            from datetime import datetime
            now = datetime.now()
            formatted = now.strftime("%H:%M:%S")

            particular = request.POST.get('particular')
            transaction_amt = request.POST.get('amount')
            date = request.POST.get('date')
            print('my date date', date)
            month = int(date.split('-')[1])

            print('my date:', date)
            print('my month:', month)

            uc = bank_amount_transaction.objects.get(id=id)
            uc.particulars = particular
            uc.transaction_amount = transaction_amt
            uc.date = date

            uc.transaction_updated_date = now.date()
            uc.transaction_updated_time = formatted
            uc.month = month

            uc.updated_by = 'UB ' + request.session['username']
            import datetime
            uc.ub_date = datetime.datetime.now()
            uc.ub_flag = 1

            uc.flag = 1
            uc.save()

            messages.info(request,'Transaction Updated sucessfully')
            #return redirect('view_all_members')
            return redirect('memberwise_transaction_details')
        context = {
            'member': member_details.objects.filter(member_flag=1),
            'sd': bank_amount_transaction.objects.get(flag=1, id=id),
        }
        return render(request,'banking_app/amount_transaction/update_amount_transaction.html',context)
    return render(request, 'index.html')


def delete_amount_transaction(request,id):
    if 'username' in request.session:
        r = bank_amount_transaction.objects.all().filter(id=id, flag=1).exists()
        if r == True:
            d = bank_amount_transaction.objects.get(id=id)
            d.deleted_by = 'DB ' + request.session['username']
            import datetime
            d.db_date = datetime.datetime.now()
            d.flag = 2
            d.save()
            messages.info(request, 'Amount Transaction Deleted Sucessfully')
            return redirect('memberwise_transaction_details')
            #context = {
            #    'member': bank_amount_transaction.objects.filter(flag=1),
            #}
            #return render(request, 'banking_app/amount_transaction/memberwise_transaction_details.html', context)
        else:
            messages.info(request, 'Amount Transaction already  Deleted')
            return redirect('memberwise_transaction_details')
            #context = {
            #    'member': bank_amount_transaction.objects.filter(flag=1),
            #}
            #return render(request, 'banking_app/amount_transaction/memberwise_transaction_details.html', context)
        return render(request, 'index.html')
    return render(request, 'index.html')


def view_all_deleted_transaction(request, id):
    if 'username' in request.session:
        context={
            'transactions': bank_amount_transaction.objects.filter(member_name=id).order_by('-id'),
            'id': id,
        }
        return render(request,'banking_app/amount_transaction/view_all_deleted_transaction.html', context)
    return render(request,'index.html')