from django.db import models

# Create your models here.
class Jabatan(models.Model): 
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self) :
        return self.nama

class Karyawan(models.Model):
    kodekrywn = models.CharField(max_length=8)
    nama = models.CharField(max_length=50)
    usia = models.IntegerField()
    gaji = models.BigIntegerField()
    tempat_lahir = models.CharField(max_length=150, blank=True)
    waktu_posting=models.DateTimeField(auto_now_add=True)
    jabatan_id=models.ForeignKey(Jabatan,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return "{}. {}".format(self.kodekrywn,self.nama)