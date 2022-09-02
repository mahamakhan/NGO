# tunr/urls.py
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('ngolist', views.NgolList.as_view(), name='ngo_list'),
    path('donations/', views.DonationsList.as_view(), name='donation_list'),
    path('bank/', views.BankList.as_view(), name='bank_list'),
    path('ngolist/<int:pk>', views.NgoDetail.as_view(), name='ngo_detail'),
    path('donations/<int:pk>', views.DonationsDetail.as_view(), name="donation_detail"),
    path('bank/<int:pk>', views.BankDetail.as_view(), name="bank_detail")

]