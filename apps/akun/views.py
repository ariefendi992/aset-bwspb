from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def login_view(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login berhasil.")

            next_url = request.POST.get("next") or request.GET.get("next")
            if next_url:
                messages.success(
                    request,
                    f"Selamat Datang Kembali, {user.first_name.title()} {user.last_name.title()}",
                )
                return redirect(next_url)
            return redirect("home")
        else:
            messages.error(
                request, "Login gagal, periksa kembali username atau password anda!"
            )
    return render(request, "login.html")


def logout_user(request: HttpRequest):
    logout(request)
    messages.success(request, "Anda telah keluar dari sistem.")
    return redirect("akun:login")
