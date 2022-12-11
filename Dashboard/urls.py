"""Dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Kelas.views import *
from Karyawan.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("service/", service, name="service"),
    path("contact/", contact, name="contact"),
    path("Vbrg/",tambah_barang),
    path("tampil_barang/",tampil_brg, name="tampil_brg"),
    path("tampil_karyawan/",tampil_krywn, name="tampil_krywn"),
]
