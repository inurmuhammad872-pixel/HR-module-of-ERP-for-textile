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
    ism = models.CharField(max_length=100, null=True, blank=True)
    sharif = models.CharField(max_length=200, null=True, blank=True)
    familiya = models.CharField(max_length=200, null=True, blank=True)
    tugilgan_sana = models.DateField(null=True, blank=True)
    jins = models.CharField(max_length=10, choices=Jins.choices, null=True, blank=True)
    tugilgan_joyi = models.CharField(max_length=100, null=True, blank=True)
    fuqarolik = models.CharField(max_length=100, null=True, blank=True)

    pasport_berilgan_joy = models.CharField(max_length=200, null=True, blank=True)
    pasport_berilgan_sana = models.DateField(null=True, blank=True)
    soliq_raqami = models.CharField(max_length=20, null=True, blank=True)

    yashash_manzili = models.CharField(max_length=200, null=True, blank=True)
    telefon = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    ijtimoiy_tarmoq = models.CharField(max_length=100, null=True, blank=True)
    aloqa_usuli = models.CharField(max_length=50, null=True, blank=True)

    # -----------------------------
    # OILA
    # -----------------------------
    oilaviy_holat = models.CharField(max_length=50, null=True, blank=True)
    farzandlar_soni = models.IntegerField(
        default=0,
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(8)]
    )

    # -----------------------------
    # TA’LIM VA KONIKMALAR
    # -----------------------------
    diplom_malumotlari = models.CharField(max_length=200, null=True, blank=True)
    til_bilish_darajasi = models.CharField(max_length=200, null=True, blank=True)
    kasbiy_konikalari = models.CharField(max_length=200, null=True, blank=True)

    # -----------------------------
    # ISH MA’LUMOTLARI
    # -----------------------------
    lavozim = models.CharField(max_length=100, null=True, blank=True)
    bolim = models.CharField(max_length=100, null=True, blank=True)
    rahbar = models.CharField(max_length=100, null=True, blank=True)
    shartnoma_turi = models.CharField(
        max_length=100,
        choices=ShartnomaTuri.choices,
        null=True,
        blank=True
    )
    davomat = models.CharField(max_length=200, null=True, blank=True)
    tarif_razryad = models.CharField(max_length=100, null=True, blank=True)
    oylik = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    ish_holati = models.CharField(
        max_length=50,
        choices=IshHolati.choices,
        null=True,
        blank=True
    )

    # -----------------------------
    # ISH GRAFIGI
    # -----------------------------
    ish_soatlari = models.CharField(max_length=100, null=True, blank=True)
    smena_raqami = models.IntegerField(null=True, blank=True)
    time_tracker_holati = models.CharField(max_length=100, null=True, blank=True)
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
