from django.db import models

# Create your models here.
class LedgerEntry(models.Model):
    entry_id = models.CharField(max_length=200)
    timestamp = models.DateTimeField()  # auto-set on creation

    particular_credit = models.CharField(max_length=200, blank=True, null=True)
    credit_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    particular_debit = models.CharField(max_length=200, blank=True, null=True)
    debit_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    flag = models.IntegerField()

    def __str__(self):
        return f"{self.particular_credit or self.particular_debit or 'Entry ' + str(self.id)}"

class LedgerEntryBackups(models.Model):
    entry_id = models.CharField(max_length=200)
    timestamp = models.DateTimeField()  # auto-set on creation

    particular_credit = models.CharField(max_length=200, blank=True, null=True)
    credit_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    particular_debit = models.CharField(max_length=200, blank=True, null=True)
    debit_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    flag = models.IntegerField()

    def __str__(self):
        return f"{self.particular_credit or self.particular_debit or 'Entry ' + str(self.id)}"
