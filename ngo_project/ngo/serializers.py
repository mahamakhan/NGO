from rest_framework import serializers
from .models import Donations, NgoList, BankAccount


class NgoSerializer(serializers.HyperlinkedModelSerializer):
    donations=serializers.HyperlinkedRelatedField(
        view_name='donation_detail',
        many=True,
        read_only=True
    )
    class Meta:
       model = NgoList
       fields = ('name','country','city', 'profit', 'international', 'email','id', 'donations')


class BankSerializer(serializers.HyperlinkedModelSerializer):
    # donations = serializers.HyperlinkedRelatedField(
    #     view_name='donation_detail',
    #     read_only=True
    # )
    class Meta:
       model = BankAccount
       fields = ( 'iban', 'number', 'name', 'id')


class DonationsSerializer(serializers.HyperlinkedModelSerializer):
    bank = serializers.HyperlinkedRelatedField(
        view_name='bank_detail',
        # many=True,
        read_only=True
    )
    ngo_list=serializers.HyperlinkedRelatedField(
        view_name='ngo_detail',
        # many=True,
        read_only=True
    )
    class Meta:
       model = Donations
       fields = ('name','title','typeof', 'description', 'bank','ngo_list', 'id')

