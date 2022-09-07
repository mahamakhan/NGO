from django.shortcuts import render
from .models import Donations, BankAccount, NgoList
from rest_framework import generics
from .serializers import DonationsSerializer, BankSerializer, NgoSerializer
# Create your views here.




class NgolList(generics.ListCreateAPIView):
    queryset = NgoList.objects.all()
    serializer_class = NgoSerializer

class NgoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NgoList.objects.all()
    serializer_class = NgoSerializer


class DonationsList(generics.ListCreateAPIView):
    queryset = Donations.objects.all()
    serializer_class = DonationsSerializer

class DonationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donations.objects.all()
    serializer_class = DonationsSerializer
    

class BankList(generics.ListCreateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankSerializer

class BankDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankSerializer