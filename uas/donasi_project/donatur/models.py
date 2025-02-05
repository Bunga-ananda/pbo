from django.contrib.auth.models import User
from django.db import models
from kampanye.models import Kampanye

class Donatur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Donasi(models.Model):
    donatur = models.ForeignKey(Donatur, on_delete=models.CASCADE)
    kampanye = models.ForeignKey(Kampanye, on_delete=models.CASCADE, null=True, blank=True)

    jumlah = models.DecimalField(max_digits=12, decimal_places=2)
    tanggal_donasi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donatur.user.username} - {self.kampanye.judul}"

