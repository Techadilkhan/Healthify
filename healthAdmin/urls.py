from django.urls import path,re_path
# from django.conf.urls import include, re_path
from . import views

urlpatterns = [
    path('', views.login),
    path('logout/', views.logout),
    path('changePassword/', views.changePassword),
    path('forgotpass/', views.forgotpass),

    path('dashboard/', views.dashboard),
    path('appointment/', views.allclinic),
    re_path(r'^appointment/(\d+)/', views.paappointment),
    re_path(r'^info/(\w+)/appoint/(\d+)/', views.appointment),
    re_path(r'^info/(.+)/', views.diseaseInfo),
    re_path(r'^sendPincodeSMS/(\d+)/(\w+)/', views.sendPincodeSMS),
    re_path(r'^sendPincodeEmail/(\d+)/(\w+)/', views.sendPincodeEmail),
    path('sendSMStoAll/', views.sendSMStoAll),
    path('sendEmailtoAll/', views.sendEmailtoAll),

    path('clinic/', views.clinic),
    re_path(r'^clinic/edit/(\d+)', views.editClinic),
    re_path(r'^clinic/delete/(\d+)', views.deleteClinic),

    path('disease/', views.disease),
    re_path(r'^disease/edit/(\d+)', views.editDisease),
    re_path(r'^disease/delete/(\d+)', views.deleteDisease),

    path('adminManager/', views.adminManager),
    re_path(r'^adminManager/edit/(\d+)', views.editAdminManager),
    re_path(r'^adminManager/delete/(\d+)', views.deleteAdminManager),

    path('patients/', views.patients),
    re_path(r'^patients/edit/(\d+)', views.editPatients),
    re_path(r'^patients/delete/(\d+)', views.deletePatients),

    path('consultation/', views.consultation),
    re_path(r'^consultation/edit/(\d+)', views.editConsultation),
    re_path(r'^consultation/delete/(\d+)', views.deleteConsultation),
]