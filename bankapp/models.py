from django.db import models

# Create your models here.

class member_details(models.Model):
    member_name = models.CharField(max_length=250)
    sum_amt = models.CharField(max_length=250)

    enter_by = models.CharField(max_length=200)
    cb_date = models.CharField(max_length=200)
    updated_by = models.CharField(max_length=200)
    ub_date = models.CharField(max_length=200)
    deleted_by = models.CharField(max_length=200)
    db_date = models.CharField(max_length=200)
    ub_flag = models.IntegerField()

    member_flag = models.IntegerField()

class bank_amount_transaction(models.Model):
    member_name = models.CharField(max_length=250)
    particulars = models.CharField(max_length=250)
    transaction_amount = models.CharField(max_length=250)
    date = models.CharField(max_length=250)

    transaction_enter_date = models.CharField(max_length=250)
    transaction_enter_time = models.CharField(max_length=250)
    month = models.CharField(max_length=20)

    transaction_updated_date = models.CharField(max_length=250)
    transaction_updated_time = models.CharField(max_length=250)

    enter_by = models.CharField(max_length=200)
    cb_date = models.CharField(max_length=200)
    updated_by = models.CharField(max_length=200)
    ub_date = models.CharField(max_length=200)
    deleted_by = models.CharField(max_length=200)
    db_date = models.CharField(max_length=200)
    ub_flag = models.IntegerField()

    flag = models.IntegerField()