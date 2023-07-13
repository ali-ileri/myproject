from django.db import models
from django.urls import reverse

class Kaynak(models.Model):
    kaynak_no = models.IntegerField()
    kaynak_yontemi = models.CharField(max_length=50)
    kaynakci_adi = models.CharField(max_length=50)
    wps_no = models.IntegerField()
    ndt_yontem = models.CharField(max_length=50)
    ndt_sonucu = models.CharField(max_length=50)

   