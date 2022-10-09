from django.urls import path
from . import views


urlpatterns = [
    path('', views.WalletList.as_view()),
    path('<str:name>/', views.WalletDetail.as_view()),
]


