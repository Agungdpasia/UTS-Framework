from django.contrib import admin
from .models import Karyawan, Jabatan

# Register your models here.
class kolomKaryawan(admin.ModelAdmin) :
    list_display = ['kodekrywn','nama','usia','gaji','tempat_lahir','jabatan_id']
    search_fields= ['kodekrywn','nama']
    list_filter=('jabatan_id',)
    list_per_page= 5


admin.site.register(Karyawan,kolomKaryawan)
admin.site.register(Jabatan)