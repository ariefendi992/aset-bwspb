from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib import messages
from .models import SumurAirTanahModel
from .form import SumurAirTanahForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="akun:login")
def index(request):
    objects = SumurAirTanahModel.objects.order_by("-created_at").all()

    context = {
        "filename": "sumur",
        "objects": objects,
    }
    return render(request, "index_sumur.html", context)


def create(request: HttpRequest):

    if request.method == "POST":
        form = SumurAirTanahForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil disimpan.")
            return redirect("sumur:index")
        else:
            messages.error(request, "Form gagal disimpan.")
    else:
        form = SumurAirTanahForm()

    context = {
        "filename": "sumur",
        "form": form,
    }

    return render(request, "add_sumur.html", context)


def detail(request: HttpRequest, id):
    object = get_object_or_404(SumurAirTanahModel, pk=id)

    context = {"filename": "sumur", "object": object}

    return render(request, "detail_sumur.html", context)


def update(request: HttpRequest, id):
    object = get_object_or_404(SumurAirTanahModel, pk=id)
    if request.method == "POST":
        form = SumurAirTanahForm(request.POST, instance=object)

        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui.")

            return redirect("sumur:index")
        else:
            messages.error(request, "Gagal perbaharui data.")
    else:
        form = SumurAirTanahForm(instance=object)

    context = {"filename": "sumur", "form": form, "object": object}

    return render(request, "edit_sumur.html", context)


def delete(request: HttpRequest, id):
    object = get_object_or_404(SumurAirTanahModel, pk=id)
    if request.method == "POST":

        object.delete()

        messages.success(request, "Data berhasil dihapus.")

        return redirect("sumur:index")

    return redirect("sumur:index")
