from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_kampanye, name='daftar_kampanye'),
    path('detail_kampanye', views.detail_kampanye, name='detail_kampanye'),
    path('tambah_kampanye/', views.tambah_kampanye, name='tambah_kampanye'),
    path('tambah_pembaruan/<int:kampanye_id>/', views.tambah_pembaruan, name='tambah_pembaruan'),
]
