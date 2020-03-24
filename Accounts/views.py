from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login as my_login, logout as my_logout
from django.utils.http import is_safe_url


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            login(request, user)
            return redirect("/")
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            my_login(request, user)
            redirect_to = request.POST.get("next", "")
            url_is_safe = is_safe_url(redirect_to, "")
            if redirect_to and url_is_safe:
                return redirect(redirect_to)
            else:
                return redirect("/")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form, "next": request.GET.get("next", "")})


def logout(request):
    my_logout(request)
    return redirect("login")
