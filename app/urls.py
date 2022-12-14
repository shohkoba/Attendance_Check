from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('guardian/', views.guardian, name='guardian'),
    path('guardian/resister/', views.resister, name='resister'),
    path('list/', views.list, name='list'),
    path('respon/<int:pk>/', views.respon, name='respon'),
    path('guardian/cfm_hist_list/', views.cfm_hist_list, name='cfm_hist_list'),
    path('guardian/cfm_hist/<int:pk>/', views.cfm_hist, name='cfm_hist'),
]