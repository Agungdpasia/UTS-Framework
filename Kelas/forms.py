from django.forms import ModelForm
from Kelas.models import Barang
from django import forms

class FormBarang(ModelForm):
    class Meta :
        model = Barang
        fields='__all__'

        Widget = {
            'kodebrg' : forms.TextInput({'class':'form-control'}),
            'nama': forms.TextInput({'class':'form-control'}),
            'stok': forms.TextInput({'class':'form-control'}),
            'harga': forms.TextInput({'class':'form-control'}),
            'link_gbr': forms.TextInput({'class':'form-control'}),
            'waktu_posting': forms.TextInput({'class':'form-control'}),
            'jenis_id': forms.TextInput({'class':'form-control'}),
        }
