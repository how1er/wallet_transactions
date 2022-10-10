from django.urls import path
from . import views
from transactions.views import TransactionList

urlpatterns = [
    path('', views.WalletList.as_view()),
    path('transactions/', TransactionList.as_view()),
    path('<str:name>/', views.WalletDetail.as_view()),

]
