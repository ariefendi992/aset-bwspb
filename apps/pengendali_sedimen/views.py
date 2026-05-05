from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse, Http404, HttpRequest
from django.contrib import messages
from .models import CheckDamModel, FotoCheckDamModel
from .forms import CheckDamForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="akun:login")
def index(request):

    obj = CheckDamModel.objects.all().prefetch_related("dokumentasi")

    context = {"filename": "checkdam", "objects": obj}

    return render(request, "index_checkdam.html", context)


@login_required(login_url="akun:login")
def create(request: HttpRequest):

    if request.method == "POST":
        form = CheckDamForm(request.POST, request.FILES)

        if form.is_valid():
            checkdam = form.save()
            image_list = request.FILES.getlist("images")

            for image in image_list:
                FotoCheckDamModel.objects.create(checkdam=checkdam, image=image)

            messages.success(request, "Data berhasil disimpan.")

            return redirect("checkdam:index")
        else:
            messages.error(request, "Form gagal disimpan.")
    else:
        form = CheckDamForm()

    context = {"filename": "checkdam", "form": form}

    return render(request, "add_checkdam.html", context)


@login_required(login_url="akun:login")
def detail(request: HttpRequest, obj_id):
    object = get_object_or_404(CheckDamModel, pk=obj_id)

    context = {"filename": "checkdam", "object": object}

    return render(request, "detail_checkdam.html", context)


@login_required(login_url="akun:login")
def update(request: HttpRequest, obj_id):

    checkdam = get_object_or_404(CheckDamModel, pk=obj_id)

    if request.method == "POST":
        form = CheckDamForm(request.POST, request.FILES, instance=checkdam)
        if form.is_valid():
            checkdam_ = form.save()

            # ambil multiple file
            files = request.FILES.getlist("images")

            for file in files:
                FotoCheckDamModel.objects.create(checkdam=checkdam_, image=file)

            messages.success(request, "Data berhasil diperbaharui.")
            return redirect("checkdam:index")
        else:
            messages.error(request, "Gagal perbaharui data.")
    else:
        form = CheckDamForm(instance=checkdam)

    fotos = checkdam.dokumentasi.all()

    context = {"filename": "checkdam", "form": form, "fotos": fotos}
    return render(request, "edit_checkdam.html", context)


@login_required(login_url="akun:login")
def delete(request: HttpRequest, obj_id):
    checkdam = get_object_or_404(CheckDamModel, pk=obj_id)

    if request.method == "POST":
        checkdam.delete()
        messages.success(request, "Data berhasil dihapus.")
        return redirect("checkdam:index")

    return redirect("checkdam:index")


@login_required(login_url="akun:login")
def download_foto(request, foto_id):
    try:
        foto = FotoCheckDamModel.objects.get(id=foto_id)
        return FileResponse(foto.image.open(), as_attachment=True)
    except:
        raise Http404("File tidak ditemukan")
