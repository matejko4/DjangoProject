from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


POZICE_VOLBY = [
    ('brankár', 'Brankář'),
    ('obránce', 'Obránce'),
    ('záložník', 'Záložník'),
    ('útočník', 'Útočník'),
]

NOHA_VOLBY = [
    ('pravá', 'Pravá'),
    ('levá', 'Levá'),
    ('obě', 'Obě'),
]


class Tym(models.Model):
    nazev = models.CharField(max_length=100, verbose_name='Název týmu', help_text='Zadejte název týmu',
                             error_messages={'blank': 'Název týmu musí být vyplněn'})
    mesto = models.CharField(max_length=100, verbose_name='Město', help_text='Zadejte město týmu',
                             error_messages={'blank': 'Město musí být vyplněno'})
    zalozen = models.IntegerField(validators=[MinValueValidator(1800), MaxValueValidator(2100)],
                                  verbose_name='Rok založení', help_text='Zadejte rok založení (1800 - 2100)')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Tým'
        verbose_name_plural = 'Týmy'

    def __str__(self):
        return self.nazev


class Hrac(models.Model):
    jmeno = models.CharField(max_length=50, verbose_name='Jméno', help_text='Zadejte jméno hráče',
                             error_messages={'blank': 'Jméno hráče musí být vyplněno'})
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení', help_text='Zadejte příjmení hráče',
                                error_messages={'blank': 'Příjmení hráče musí být vyplněno'})
    datum_narozeni = models.DateField(verbose_name='Datum narození', help_text='Zadejte datum narození')
    narodnost = models.CharField(max_length=50, verbose_name='Národnost', help_text='Zadejte národnost hráče',
                                 error_messages={'blank': 'Národnost musí být vyplněna'})
    pozice = models.CharField(max_length=20, choices=POZICE_VOLBY, verbose_name='Pozice', help_text='Vyberte pozici hráče')
    cislo_dresu = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)],
                                              verbose_name='Číslo dresu', help_text='Zadejte číslo dresu (1 - 99)')
    preferovana_noha = models.CharField(max_length=10, choices=NOHA_VOLBY, default='pravá',
                                        verbose_name='Preferovaná noha')
    tym = models.ForeignKey(Tym, on_delete=models.SET_NULL, null=True, blank=True,
                            related_name='hraci', verbose_name='Tým')
    datum_pristupu = models.DateField(blank=True, null=True, verbose_name='Datum přístupu do týmu')

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name = 'Hráč'
        verbose_name_plural = 'Hráči'

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'


class Zapas(models.Model):
    domaci = models.ForeignKey(Tym, on_delete=models.CASCADE, related_name='domaci_zapasy', verbose_name='Domácí tým')
    hoste = models.ForeignKey(Tym, on_delete=models.CASCADE, related_name='hostujici_zapasy', verbose_name='Hostující tým')
    datum = models.DateField(verbose_name='Datum zápasu', help_text='Zadejte datum zápasu')
    goly_domaci = models.PositiveIntegerField(default=0, verbose_name='Góly domácích')
    goly_hoste = models.PositiveIntegerField(default=0, verbose_name='Góly hostů')

    class Meta:
        ordering = ['-datum']
        verbose_name = 'Zápas'
        verbose_name_plural = 'Zápasy'

    def __str__(self):
        return f'{self.domaci} vs {self.hoste} ({self.datum})'


class StatistikaHrace(models.Model):
    hrac = models.ForeignKey(Hrac, on_delete=models.CASCADE, related_name='statistiky', verbose_name='Hráč')
    zapas = models.ForeignKey(Zapas, on_delete=models.CASCADE, related_name='statistiky', verbose_name='Zápas')
    goly = models.PositiveIntegerField(default=0, verbose_name='Góly')
    asistence = models.PositiveIntegerField(default=0, verbose_name='Asistence')
    minuty = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(120)],
                                         verbose_name='Odehrané minuty', help_text='Zadejte počet odehraných minut (0 - 120)')

    class Meta:
        verbose_name = 'Statistika hráče'
        verbose_name_plural = 'Statistiky hráčů'
        unique_together = ('hrac', 'zapas')

    def __str__(self):
        return f'{self.hrac} – {self.zapas}'