"""
URL configuration for on_road project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from on_road_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('custReg',views.custReg),
    path('mechReg',views.mechReg),
    path('login',views.login),


    path('adminHome',views.adminHome),
    path('adminCust',views.adminCust),
    path('adminMech',views.adminMech),
    path('adminBookings',views.adminBookings),
    path('adminAmbulance',views.adminAmbulance),
    path('adminFire',views.adminFire),
    path('adminApproveMech',views.adminApproveMech),
    path('adminApproveCust',views.adminApproveCust),
    path('adminReport',views.adminReport),
    path('adminFeedback',views.adminFeedback),
    




    path('custHome',views.custHome),
    path('custFindMech',views.custFindMech),
    # path('custBookMech',views.custBookMech),
    path('custBookings',views.custBookings),
    path('custAddReview',views.custAddReview),
    path('custDesc',views.custDesc),
    path('custMakePayment',views.custMakePayment),
    path('custEmergency',views.custEmergency),
    path('custAmbulanceMsg',views.custAmbulanceMsg),
    path('custFireMsg',views.custFireMsg),






    path('mechHome',views.mechHome),
    path('mechViewReq',views.mechViewReq),
    path('mechApproveReq',views.mechApproveReq),
    path('mechViewBok',views.mechViewBok),
    path('mechCompleted',views.mechCompleted),
    path('mechAddPay',views.mechAddPay),





    path('ambulanceHome',views.ambulanceHome),
    path('ambulanceNotification',views.ambulanceNotification),
    

    path('fireFighterHome',views.fireFighterHome),
    path('fireNotification',views.fireNotification),
   



]
