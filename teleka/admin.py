from django.contrib import admin
from .models import *

admin.site.register(Member)
admin.site.register(Deposit)
admin.site.register(Withdraw)
admin.site.register(Loan)
admin.site.register(RepayLoan)
