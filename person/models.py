from django.db import models
from django.urls import reverse
# Create your models here.
#***************************************************************************************************
class Genral(models.Model):
        name = models.CharField(max_length=200)
        url = models.IntegerField()
        class Meta:
                ordering = ['url',]
        def __str__(self):
                return self.name
        def get_absolute_url(self):
                return reverse('genral_detail', kwargs={'pk': self.id})
#***************************************************************************************************
class Uprav(models.Model):
        name = models.CharField(max_length=200)
        gend = models.ForeignKey(Genral, on_delete=models.CASCADE)
        class Meta:
                ordering = ['id',]
        def __str__(self):
                return self.name

        def get_absolute_url(self):
                return reverse('otdel_list', kwargs={'id': self.id})
#***************************************************************************************************
class Otdel(models.Model):
        name = models.CharField(max_length=200)
        uprav = models.ForeignKey(Uprav, on_delete=models.CASCADE)
        class Meta:
                ordering = ['id']
        def __str__(self):
                return self.name

#***************************************************************************************************
class Person(models.Model):
        pod = models.CharField(max_length=200, null=True)
        kod = models.CharField(max_length=200, null=True)
        kodd = models.IntegerField(null=True)
        aa = models.IntegerField(null=True)
        bb = models.IntegerField(null=True)
        cc = models.IntegerField(null=True)
        kodp = models.IntegerField(null=True)
        dd = models.IntegerField(null=True)
        ee = models.IntegerField(null=True)
        proff = models.CharField(max_length=200, null=True)
        smena = models.CharField(max_length=200, null=True)
        kofl = models.CharField(max_length=200, null=True)
        bp = models.DecimalField(max_digits=8, decimal_places=2, null=True)
        fact = models.IntegerField(null=True)
        facte = models.IntegerField(null=True)
        factlf = models.IntegerField(null=True)
        factb = models.IntegerField(null=True)
        vak = models.IntegerField(null=True)
        vake = models.IntegerField(null=True)
        lpen = models.IntegerField(null=True)
        planch = models.IntegerField(null=True)
        kor = models.IntegerField(null=True)
        kore = models.IntegerField(null=True)
        korlf = models.IntegerField(null=True)
        plane = models.IntegerField(null=True)
        plaf = models.IntegerField(null=True)
        planl4 = models.IntegerField(null=True)
        plan3 = models.IntegerField(null=True)
        vik = models.IntegerField(null=True)
        svsh = models.IntegerField(null=True)
        svbp = models.IntegerField(null=True)
        diap = models.CharField(max_length=200, null=True)
        kat = models.CharField(max_length=200, null=True)
        katr = models.IntegerField(null=True)
        katt = models.IntegerField(null=True)
        katd = models.IntegerField(null=True)
        ist = models.CharField(max_length=200, null=True)
        tabel = models.CharField(max_length=200, null=True)
        perev = models.CharField(max_length=200, null=True)
        ppn = models.IntegerField(null=True)
        fio = models.CharField(max_length=200, null=True)
        prikas = models.CharField(max_length=200, null=True)
        prik = models.CharField(max_length=200, null=True)
        staj = models.IntegerField(null=True)
        datap = models.IntegerField(null=True)
        godr = models.IntegerField(null=True)
        oklad = models.IntegerField(null=True)
        kodh = models.CharField(max_length=200, null=True)
        kodph = models.IntegerField(null=True)