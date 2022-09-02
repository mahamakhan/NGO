from django.db import models


class NgoList(models.Model):
    name=models.CharField(max_length=100)
    country=models.CharField(max_length=120)
    zakat_eligible=models.BooleanField()
    

    def __str__(self):
            return self.name

class Donations(models.Model):
    ngo_list=models.ForeignKey(NgoList, on_delete=models.CASCADE, related_name='donations')
    name=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    typeof=models.CharField(max_length=100)
    description=models.CharField(max_length=400)
    

    def __str__(self):
        return self.name

class BankAccount(models.Model):
    donation=models.ForeignKey(Donations, on_delete=models.CASCADE, related_name='bank_account')
    name=models.CharField(max_length=100)
    number=models.IntegerField()
    iban=models.IntegerField()
    

    def __str__(self):
         return self.name