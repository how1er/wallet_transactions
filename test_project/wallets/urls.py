from django.urls import path
from . import views
from transactions.views import TransactionList, TransactionDetail, transactions_of_wallet

urlpatterns = [
    path('', views.WalletList.as_view()),
    path('transactions/', TransactionList.as_view()),
    path('transactions/<int:pk>/', TransactionDetail.as_view()),
    path('transactions/<str:name>/', transactions_of_wallet),
    path('<str:name>/', views.WalletDetail.as_view()),

]
