from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import FileResponse, HttpRequest, Http404
from .models import TanggulSungaiModel, FotoTanggulSungaiModel
from .forms import FotoTanggulSungaiForm, TanggulSungaiForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="akun:login")
def index(request):
    objects = TanggulSungaiModel.objects.order_by("-created_at").all()

    context = {"filename": "tsungai", "objects": objects}

    return render(request, "index_tsungai.html", context)


@login_required(login_url="akun:login")
def create(request: HttpRequest):

    if request.method == "POST":
        form = TanggulSungaiForm(request.POST, request.FILES)

        if form.is_valid():
            tsungai = form.save()

            image_list = request.FILES.getlist("images")

            for image in image_list:
                FotoTanggulSungaiModel.objects.create(tanggul=tsungai, image=image)

            messages.success(request, "Data berhasil disimpan.")

            return redirect("tsungai:index")
        else:
            messages.error(request, "Form gagal disimpan.")
    else:
        form = TanggulSungaiForm()

    context = {"filename": "tsungai", "form": form}

    return render(request, "add_tsungai.html", context)


@login_required(login_url="akun:login")
def detail(request: HttpRequest, id):

    object = get_object_or_404(TanggulSungaiModel, pk=id)

    context = {"filename": "tsungai", "object": object}

    return render(request, "detail_tsungai.html", context)


@login_required(login_url="akun:login")
def update(request: HttpRequest, id):
    object = get_object_or_404(TanggulSungaiModel, pk=id)

    if request.method == "POST":
        form = TanggulSungaiForm(request.POST, request.FILES, instance=object)

        if form.is_valid():
            tsungai = form.save()
            files = request.FILES.getlist("images")

            for image in files:
                files_images = FotoTanggulSungaiModel.objects.create(
                    tanggul=tsungai, image=image
                )
                files_images.save()

            messages.success(request, "Data berhasil diperbaharui.")
            return redirect("tsungai:index")
        else:
            messages.error(request, "Gagal perbaharui data.")
    else:
        form = TanggulSungaiForm(instance=object)

    context = {"filename": "tsungai", "form": form}
    return render(request, "edit_tsungai.html", context)


@login_required(login_url="akun:login")
def delete(request: HttpRequest, id):
    object = get_object_or_404(TanggulSungaiModel, pk=id)

    if request.method == "POST":
        object.delete()

        messages.success(request, "Data berhasil dihapus.")
        return redirect("tsungai:index")

    return redirect("tsungai:index")


@login_required(login_url="akun:login")
def donwload(request, id):
    try:
        foto = FotoTanggulSungaiModel.objects.get(pk=id)
        return FileResponse(foto.image.open(), as_attachment=True)
    except:
        raise Http404("File tidak ditemukan")
