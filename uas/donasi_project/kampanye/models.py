from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Kampanye(models.Model):
    STATUS_CHOICES = [
        ('aktif', 'Aktif'),
        ('selesai', 'Selesai'),
        ('dibatalkan', 'Dibatalkan'),
    ]

    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()
    target_dana = models.DecimalField(max_digits=12, decimal_places=2)
    dana_terkumpul = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    tanggal_mulai = models.DateField(default=timezone.now)
    tanggal_berakhir = models.DateField()
    pengelola = models.ForeignKey(User, on_delete=models.CASCADE, related_name="kampanye_dikelola", blank=True, null=True)
    gambar = models.ImageField(upload_to='kampanye_images/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='aktif')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.judul

    def simpan_donasi(self, jumlah):
        """Menambahkan dana yang didonasikan ke kampanye."""
        if self.dana_terkumpul + jumlah > self.target_dana:
            raise ValueError("Dana terkumpul tidak boleh melebihi target dana")
        self.dana_terkumpul += jumlah
        self.save()

class PembaruanKampanye(models.Model):
    kampanye = models.ForeignKey(Kampanye, on_delete=models.CASCADE, related_name="pembaruan_kampanye")
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pembaruan: {self.judul} - {self.kampanye.judul}"
        
