from django.urls import path
# from this folder import views.py
from . import views


urlpatterns = [
    path('', views.home),
    path('reporta/', views.reporta),
    path('mapa/', views.mapa),
]
