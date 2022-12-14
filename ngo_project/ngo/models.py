from django.db import models


class NgoList(models.Model):
    name=models.CharField(max_length=100)
    country=models.CharField(max_length=120)
    founded=models.CharField(max_length=120, null=True)
    profit=models.CharField(max_length=1020, null=True)
    international=models.CharField(max_length=120, null=True)
    email=models.CharField(max_length=120, null=True)

    def __str__(self):
            return self.name

class BankAccount(models.Model):
    name=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    iban=models.CharField(max_length=100)
    

    def __str__(self):
         return self.name

class Donations(models.Model):
    ngo_list=models.ForeignKey(NgoList, on_delete=models.CASCADE, related_name='donations')
    bank=models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='donations', null=True)
    name=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    typeof=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    

    def __str__(self):
        return self.name

