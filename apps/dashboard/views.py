from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from apps.asets.models import (
    BendungModel,
    DanauModel,
    EmbungModel,
    CheckDamModel,
    PengamanPantaiModel,
    TanggulSungaiModel,
    SumurAirTanahModel,
    DataAbsahModel,
)


# Create your views here.
@login_required(login_url="login/")
def home(request: HttpRequest):

    absah = DataAbsahModel
    bendung = BendungModel
    danau = DanauModel
    embung = EmbungModel
    pengaman_pantai = PengamanPantaiModel
    check_dam = CheckDamModel
    sumur_air_tanah = SumurAirTanahModel
    tanggul_sungai = TanggulSungaiModel

    total_aset = (
        absah.objects.count()
        + bendung.objects.count()
        + danau.objects.count()
        + embung.objects.count()
        + pengaman_pantai.objects.count()
        + check_dam.objects.count()
        + sumur_air_tanah.objects.count()
        + tanggul_sungai.objects.count()
    )

    aset = dict(
        total_aset=total_aset,
        total_danau=danau.objects.count(),
        total_embung=embung.objects.count(),
        total_bendung=bendung.objects.count(),
        total_checkdam=check_dam.objects.count(),
        total_pengaman_pantai=pengaman_pantai.objects.count(),
        total_sumur=sumur_air_tanah.objects.count(),
        total_tanggul=tanggul_sungai.objects.count(),
        total_absah=absah.objects.count(),
    )

    context = {"filename": "home"}
    context.update(aset)
    return render(request, "home.html", context)
