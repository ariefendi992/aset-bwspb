from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, Http404
from django.contrib import messages
from .models import PengamanPantaiModel
from .forms import PengamanPantaiForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="akun:login")
def index(request: HttpRequest):

    objects = PengamanPantaiModel.objects.order_by("-created_at").all()

    context = {"filename": "ppantai", "objects": objects}

    return render(request, "index_ppantai.html", context)


@login_required(login_url="akun:login")
def create(request: HttpRequest):

    if request.method == "POST":
        form = PengamanPantaiForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil disimpan.")

            return redirect("ppantai:index")
        else:
            messages.error(request, "Form gagal disimpan.")
    else:
        form = PengamanPantaiForm()

    context = {"filename": "ppantai", "form": form}
    return render(request, "add_ppantai.html", context)


@login_required(login_url="akun:login")
def detail(request: HttpRequest, obj_id):

    object = get_object_or_404(PengamanPantaiModel, pk=obj_id)

    context = {"filename": "ppantai", "object": object}
    return render(request, "detail_ppantai.html", context)


@login_required(login_url="akun:login")
def update(request: HttpRequest, obj_id):
    object = get_object_or_404(PengamanPantaiModel, pk=obj_id)

    if request.method == "POST":
        form = PengamanPantaiForm(request.POST, instance=object)
        if form.is_valid():
            form.save()

            messages.success(request, "Data berhasil diperbaharui.")

            return redirect("ppantai:index")

        else:
            messages.error(request, "Gagal perbaharui data.")

    else:
        form = PengamanPantaiForm(instance=object)

    context = {"filename": "ppantai", "form": form, "obj": object}

    return render(request, "edit_ppantai.html", context)


@login_required(login_url="akun:login")
def delete(request: HttpRequest, obj_id):
    object = get_object_or_404(PengamanPantaiModel, pk=obj_id)

    if request.method == "POST":
        object.delete()
        messages.success(request, "Data berhasil dihapus.")

        return redirect("ppantai:index")
    return redirect("ppantai:index")
