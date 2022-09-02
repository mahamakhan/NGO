from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Donations, NgoList, BankAccount
admin.site.register(Donations)
admin.site.register(NgoList)
admin.site.register(BankAccount)