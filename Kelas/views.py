from django.shortcuts import render
from Kelas.forms import FormBarang
from Kelas.models import Barang

# Create your views here.

def tampil_brg(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs':barangs,
    }
    return render(request,'tampil_brg.html',konteks)


def tambah_barang(request):
    form=FormBarang()
    konteks={
        'form': form,
    }

    return render(request, 'tambah_barang.html',konteks)


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def contact(request):
    return render(request,'contact.html')