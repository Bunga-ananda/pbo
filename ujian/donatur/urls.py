from django.urls import path
from . import views

urlpatterns = [
    # path('donasi/', buat_donasi, name='buat_donasi'),
    path('riwayat/<int:donatur_id>/', views.riwayat_donasi, name='riwayat_donasi'),
    path('riwayat-donasi/', views.riwayat_donasi, name='riwayat_donasi'), 
    
]

