from django.contrib import admin
from .models import Kampanye, PembaruanKampanye

class PembaruanKampanyeInline(admin.TabularInline):
    model = PembaruanKampanye
    extra = 1

class KampanyeAdmin(admin.ModelAdmin):
    list_display = ('judul', 'pengelola', 'target_dana', 'dana_terkumpul', 'status')
    list_filter = ('status', 'tanggal_mulai')
    search_fields = ('judul', 'deskripsi')
    inlines = [PembaruanKampanyeInline]

admin.site.register(Kampanye, KampanyeAdmin)
admin.site.register(PembaruanKampanye)
