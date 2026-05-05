from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import FileResponse, Http404, HttpRequest
from .models import DataAbsahModel, FotoDataAbsahModel
from .forms import AbsahForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="akun:login")
def index(request: HttpRequest):
    objects = DataAbsahModel.objects.order_by("-created_at").all()

    context = {
        "filename": "absah",
        "objects": objects,
    }

    return render(request, "index_absah.html", context)


@login_required(login_url="akun:login")
def create(request: HttpRequest):

    if request.method == "POST":
        form = AbsahForm(request.POST, request.FILES)

        if form.is_valid():
            object = form.save()

            files = request.FILES.getlist("images")

            for image in files:
                foto = FotoDataAbsahModel.objects.create(absah=object, image=image)
                foto.save()
            messages.success(request, "Data berhasil disimpan.")

            return redirect("absah:index")
        else:
            messages.error(request, "Form gagal disimpan.")

    else:
        form = AbsahForm()

    context = {"filename": "absah", "form": form}

    return render(request, "add_absah.html", context)


@login_required(login_url="akun:login")
def update(request: HttpRequest, id):
    object = get_object_or_404(DataAbsahModel, pk=id)

    if request.method == "POST":
        form = AbsahForm(request.POST, request.FILES, instance=object)

        if form.is_valid():
            absah = form.save()

            files = request.FILES.getlist("images")

            for image in files:
                foto = FotoDataAbsahModel.objects.create(absah=absah, image=image)
                foto.save()

            messages.success(request, "Data berhasil disimpan.")

            return redirect("absah:index")
        else:
            messages.error(request, "Form gagal disimpan.")

    else:
        form = AbsahForm(instance=object)

    context = {"filename": "absah", "form": form, "object": object}

    return render(request, "edit_absah.html", context)


@login_required(login_url="akun:login")
def detail(request: HttpRequest, id):
    object = get_object_or_404(DataAbsahModel, pk=id)

    context = {"filename": "absah", "object": object}

    return render(request, "detail_absah.html", context)


@login_required(login_url="akun:login")
def delete(request: HttpRequest, id):
    object = get_object_or_404(DataAbsahModel, pk=id)

    if request.method == "POST":
        object.delete()
        messages.success(request, "Data berhasil dihapus.")

        return redirect("absah:index")

    return redirect("absah:index")


@login_required(login_url="akun:login")
def download_foto(request, id):
    try:
        foto = FotoDataAbsahModel.objects.get(pk=id)
        return FileResponse(foto.image.open(), as_attachment=True)
    except:
        raise Http404("File tidak ditemukan")
