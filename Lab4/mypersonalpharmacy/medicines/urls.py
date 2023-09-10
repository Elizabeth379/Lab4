from django.urls import path, re_path

from .views import *
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('medhome/', views.test, name='medhome'),  # http://127.0.0.1:8000/medicines/
    path('about/', views.about, name='about'),  # http://127.0.0.1:8000/medicines/about/
    path('medlist/', views.MedList.as_view(), name='medlist'),  # http://127.0.0.1:8000/medicines/medlist/
    path('pharms/', views.Pharmacies.as_view(), name='pharms'),
    path('bying/<int:bying_id>/', views.bying, name='bying'),
    path('thanks/<int:thanks_id>/', views.thanks, name='thanks'),
    path('no_avail/', views.NoAvailable.as_view(), name='no_avail'),
    path('w_registr/', views.w_registr, name='w_registr'),
    path('medhomew/', views.MedWithoutHome.as_view(), name='medhomew'),
    path('main/', views.Main.as_view(), name='main' )
]
