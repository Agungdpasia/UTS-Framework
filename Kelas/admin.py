from django.contrib import admin
from .models import Barang, Jenis
# Register your models here.


class kolomBarang(admin.ModelAdmin) :
    list_display = ['kodebrg','nama','stok','harga','link_gbr','jenis_id']
    search_fields= ['kodebrg','nama']
    list_filter=('jenis_id',)
    list_per_page= 5


admin.site.register(Barang,kolomBarang)
admin.site.register(Jenis)