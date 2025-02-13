from django.contrib import admin
from django.urls import path
from .views import GetAll,GetById,StoreData,UpdateData,UpdateDataFull,main_method,DeleteData
urlpatterns = [

    path('',main_method,name="main"),
    path('GetAll/',GetAll,name="GetAll"),
    path('GetById/<str:id>/',GetById,name="GetById"),
    path('StoreData/',StoreData,name="StoreData"),
    path('UpdateData/<str:id>/',UpdateData,name="UpdateData"),
    path('UpdateDataFull/<str:id>/',UpdateDataFull,name="StoreDataFull"),
    path('DeleteData/<str:id>/', DeleteData, name='DeleteData')
,
]
