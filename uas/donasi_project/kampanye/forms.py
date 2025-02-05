from django import forms
from .models import Kampanye, PembaruanKampanye

class KampanyeForm(forms.ModelForm):
    class Meta:
        model = Kampanye
        fields = ['judul', 'deskripsi', 'target_dana', 'tanggal_berakhir', 'gambar']


class PembaruanKampanyeForm(forms.ModelForm):
    class Meta:
        model = PembaruanKampanye
        fields = ['judul', 'deskripsi']
