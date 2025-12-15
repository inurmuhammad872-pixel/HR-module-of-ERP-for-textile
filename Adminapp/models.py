from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


class Jins(models.TextChoices):
    ERKAK = "male", "Erkak"
    AYOL = "female", "Ayol"


class ShartnomaTuri(models.TextChoices):
    TOLIQ_STAVKA = "full_time", "Toliq stavka"
    QISMIY_STAVKA = "part_time", "Qisman stavka"
    TEMPORARY = "temporary", "Vaqtinchalik"
    SOATBAY = "hourly", "Soatbay"


class IshHolati(models.TextChoices):
    ISHDA = "active", "Ishda"
    ISHDAN_BOSHAGAN = "inactive", "Faol emas"
    BOSHATILGAN = "fired", "Ishdan boshatilgan"
    TATILDA = "vacation", "Ta’tilda"


class Xodimlar(models.Model):
    # -----------------------------
    # ASOSIY MA’LUMOTLAR
    # -----------------------------

    ism = models.CharField(max_length=100)
    sharif = models.CharField(max_length=200)
    familiya = models.CharField(max_length=200)
    tugilgan_sana = models.DateField()
    jins = models.CharField(max_length=10, choices=Jins.choices)
    tugilgan_joyi = models.CharField(max_length=100)
    fuqarolik = models.CharField(max_length=100)

    pasport_seriya = models.CharField(
        max_length=2,
        validators=[RegexValidator(r'^[A-Z]{2}$', message="Pasport seriyasi 2 ta bosh harf bolishi kerak.")],
        null=True
    )
    pasport_raqam = models.IntegerField(
        validators=[MinValueValidator(1000000), MaxValueValidator(9999999)],
        null=True
    )
    pasport_berilgan_joy = models.CharField(max_length=200)
    pasport_berilgan_sana = models.DateField()
    soliq_raqami = models.CharField(max_length=20)

    yashash_manzili = models.CharField(max_length=200)
    telefon = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    ijtimoiy_tarmoq = models.CharField(max_length=100)
    aloqa_usuli = models.CharField(max_length=50)

    # -----------------------------
    # OILA MA’LUMOTLARI
    # -----------------------------
    oilaviy_holat = models.CharField(max_length=50)
    turmush_ortogi_haqida = models.CharField(max_length=200, null=True, blank=True)
    farzandlar_soni = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(8)]
    )
    farzandlar_haqida = models.CharField(max_length=200, null=True, blank=True)
    nogironlik_holati = models.CharField(max_length=100, null=True, blank=True)
    imtiyozlar = models.CharField(max_length=200, null=True, blank=True)

    # -----------------------------
    # TA’LIM VA KONIKMALAR
    # -----------------------------
    diplom_malumotlari = models.CharField(max_length=200)
    maxsus_kurslar = models.CharField(max_length=200, null=True, blank=True)
    sertifikatlar = models.FileField(upload_to='certificates/', null=True, blank=True)
    til_bilish_darajasi = models.CharField(max_length=200)
    kompyuter_konikalari = models.CharField(max_length=255, null=True, blank=True)
    kasbiy_konikalari = models.CharField(max_length=200)
    haydovchilik_guvohnomasi = models.CharField(max_length=100, null=True, blank=True)

    # -----------------------------
    # ISH MA’LUMOTLARI
    # -----------------------------
    lavozim = models.CharField(max_length=100)
    bolim = models.CharField(max_length=100)
    rahbar = models.CharField(max_length=100)
    shartnoma_turi = models.CharField(max_length=100, choices=ShartnomaTuri.choices)
    davomat = models.CharField(max_length=200)
    tarif_razryad = models.CharField(max_length=100)
    oylik = models.DecimalField(max_digits=10, decimal_places=2)
    ish_holati = models.CharField(max_length=50, choices=IshHolati.choices)

    # -----------------------------
    # ISH GRAFIGI
    # -----------------------------
    ish_soatlari = models.CharField(max_length=100)
    smena_raqami = models.IntegerField()
    time_tracker_holati = models.CharField(max_length=100) 
    tatil_holati = models.BooleanField(default=False)  
    tatil_boshlanish_sana = models.DateField(null=True, blank=True)
    tatil_tugash_sana = models.DateField(null=True, blank=True)
    kasallik_kunlari = models.IntegerField(null=True, blank=True)

    # -----------------------------
    # HUJJATLAR
    # -----------------------------
    mehnat_shartnomasi = models.FileField(upload_to='documents/contracts/', null=True, blank=True)
    lavozim_instruksiyasi = models.FileField(upload_to='documents/job_instructions/', null=True, blank=True)
    pasport_nusxasi = models.FileField(upload_to='documents/passports/', null=True, blank=True)
    diploma_nusxasi = models.FileField(upload_to='documents/diplomas/', null=True, blank=True)
    tibbiy_kitobcha = models.FileField(upload_to='documents/medical_books/', null=True, blank=True)
    arizalar_tarixi = models.TextField(null=True, blank=True)
    intizomiy_protokollar = models.FileField(upload_to='documents/disciplinary/', null=True, blank=True)

    # -----------------------------
    # ISH TARIXI
    # -----------------------------
    oldingi_ish_joylari = models.TextField(null=True, blank=True)
    stajirovka_tajriba = models.TextField(null=True, blank=True)
    lavozimlar_tarixi = models.TextField(null=True, blank=True)
    rotatsiyalar_va_otkazmalar = models.TextField(null=True, blank=True)

    # -----------------------------
    # KPI VA SAMARADORLIK
    # -----------------------------
    kpi_korsatkichlari = models.TextField(null=True, blank=True)
    oylik_natijalar = models.TextField(null=True, blank=True)
    samaradorlik_indeksi = models.FloatField(null=True, blank=True)
    bonuslar_va_motivatsiya = models.TextField(null=True, blank=True)

    # -----------------------------
    # TIBBIY MA’LUMOTLAR
    # -----------------------------
    oxirgi_tibbiy_korik_sana = models.DateField(null=True, blank=True)
    zararli_ishga_ruxsat = models.BooleanField(default=False)
    emlash_holati = models.CharField(max_length=255, null=True, blank=True)

    # -----------------------------
    # XAVFSIZLIK VA RUXSATLAR
    # -----------------------------
    kirish_karta_id = models.CharField(max_length=100, null=True, blank=True)
    avtotransport_ruhsatnomasi = models.CharField(max_length=100, null=True, blank=True)
    bino_kirish_huquqlari = models.CharField(max_length=255, null=True, blank=True)
    it_tizim_loginlari = models.TextField(null=True, blank=True)

    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        if self.pasport_seriya:
            self.pasport_seriya = self.pasport_seriya.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.familya_ism_sharif


class User(AbstractUser):
    ROLE_CHOICES = (
        ('director', 'Direktor'),
        ('teacher', 'Oqituvchi'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='admin')
