from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Kampanye, PembaruanKampanye
from .forms import KampanyeForm, PembaruanKampanyeForm

def daftar_kampanye(request):
    kampanye_list = Kampanye.objects.all()
    return render(request, 'daftar_kampanye.html', {'kampanye_list': kampanye_list})

def detail_kampanye(request, id):
    kampanye = get_object_or_404(Kampanye, id=id)
    pembaruan_list = kampanye.pembaruan_kampanye.all()
    return render(request, 'detail_kampanye.html', {'kampanye': kampanye, 'pembaruan_list': pembaruan_list})

def tambah_kampanye(request):
    if request.method == "POST":
        form = KampanyeForm(request.POST)
        if form.is_valid():
            kampanye = form.save()  # Simpan ke database
            return redirect('tambah_pembaruan', kampanye.id)  # Sekarang id sudah ada
    else:
        form = KampanyeForm()
    return render(request, 'tambah_kampanye.html', {'form': form})


@login_required
def tambah_pembaruan(request, kampanye_id):
    kampanye = get_object_or_404(Kampanye, id=kampanye_id)
    if request.method == "POST":
        form = PembaruanKampanyeForm(request.POST)
        if form.is_valid():
            pembaruan = form.save(commit=False)
            pembaruan.kampanye = kampanye
            pembaruan.save()
            return redirect('detail_kampanye', id=kampanye_id)
    else:
        form = PembaruanKampanyeForm()
    return render(request, 'tambah_pembaruan.html', {'kampanye_id': kampanye_id})

def homepage(request):
    kampanye_list = Kampanye.objects.order_by('-id')[:3]  # Ambil 3 kampanye terbaru
    return render(request, 'homepage.html', {'kampanye_list': kampanye_list})

