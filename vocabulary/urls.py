from django.urls import path
from . import views

urlpatterns = [
    path('', views.random_vocabulary, name='random_vocabulary'),# 空文字でURLルートを設定
]
