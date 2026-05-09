from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Tym, Hrac, Zapas, StatistikaHrace


def seznam_tymu(request):
    tymy = Tym.objects.all()
    return render(request, 'seznamHracu/seznam_tymu.html', {'tymy': tymy})

def detail_tymu(request, pk):
    tym = get_object_or_404(Tym, pk=pk)
    return render(request, 'seznamHracu/detail_tymu.html', {'tym': tym})


def seznam_hracu(request):
    hraci = Hrac.objects.all()
    return render(request, 'seznamHracu/seznam_hracu.html', {'hraci': hraci})

def detail_hrace(request, pk):
    hrac = get_object_or_404(Hrac, pk=pk)
    return render(request, 'seznamHracu/detail_hrace.html', {'hrac': hrac})


def seznam_zapasu(request):
    zapasy = Zapas.objects.all()
    return render(request, 'seznamHracu/seznam_zapasu.html', {'zapasy': zapasy})

def detail_zapasu(request, pk):
    zapas = get_object_or_404(Zapas, pk=pk)
    statistiky = StatistikaHrace.objects.filter(zapas=zapas)
    return render(request, 'seznamHracu/detail_zapasu.html', {'zapas': zapas, 'statistiky': statistiky})