from rest_framework import serializers
from .models import Donations, NgoList, BankAccount


class NgoSerializer(serializers.HyperlinkedModelSerializer):
    donations = serializers.HyperlinkedRelatedField(
        view_name='donation_detail',
        many=True,
        read_only=True
    )
    class Meta:
       model = NgoList
       fields = ('name','country','zakat_eligible',)


class DonationsSerializer(serializers.HyperlinkedModelSerializer):
    bank = serializers.HyperlinkedRelatedField(
        view_name='bank_detail',
        many=True,
        read_only=True
    )
    class Meta:
       model = Donations
       fields = ('name', 'ngo_list','title','typeof', 'description')

class BankSerializer(serializers.HyperlinkedModelSerializer):
    donations = serializers.HyperlinkedRelatedField(
        view_name='donation_detail',
        many=True,
        read_only=True
    )
    class Meta:
       model = BankAccount
       fields = ( 'iban', 'number', 'name', 'donation',)