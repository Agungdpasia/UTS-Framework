from django.shortcuts import render
from .models import Karyawan
# Create your views here.


def tampil_krywn(request):
    karyawans = Karyawan.objects.all()

    konteks = {
        'karyawans': karyawans,
    }
    return render(request, 'tampil_karyawan.html', konteks)
