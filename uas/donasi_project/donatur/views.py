from django.shortcuts import render, redirect, get_object_or_404
from .forms import DonasiForm
from .models import Donatur, Donasi
from kampanye.models import Kampanye
from django.shortcuts import redirect

def redirect_to_riwayat(request, donatur):
    return redirect('riwayat_donasi', donatur_id=donatur.id)


def buat_donasi(request):
    if request.method == "POST":
        form = DonasiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_kampanye')
    else:
        form = DonasiForm()
    return render(request, 'donatur/buat_donasi.html', {'form': form})

def daftar_kampanye(request):
    kampanye_list = Kampanye.objects.all()
    return render(request, 'kampanye/daftar_kampanye.html', {'kampanye_list': kampanye_list})

def riwayat_donasi(request, donatur_id):
    donatur = get_object_or_404(Donatur, id=donatur_id)
    donasi_list = Donasi.objects.filter(donatur=donatur)
    return render(request, 'donatur/riwayat_donasi.html', {'donasi_list': donasi_list})
