from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, DeliveryPersonForm
from django.contrib.auth import login as my_login, logout as my_logout
from django.utils.http import is_safe_url
from django.contrib import messages
from .models import DeleveryPerson


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_superuser = True
            user.set_password(form.cleaned_data["password1"])
            user.save()
            my_login(request, user)
            return redirect("/")
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


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
                import pdb
                pdb.set_trace()
                return redirect("/")
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form, "next": request.GET.get("next", "")})


def create_delevery_person(request):
    if request.method == 'POST':
        form = DeliveryPersonForm(request.POST)
        if form.is_valid():
            delevery_man = form.save(commit=False)
            delevery_man.is_staff = True
            delevery_man.set_password(form.cleaned_data["password1"])
            delevery_man.save()
            my_login(request, delevery_man)
            messages.success(request, 'Nouveau Livreur Cree!')
            return redirect('list')
    else:
        form = DeliveryPersonForm()
    return render(request, 'registration/delevery_person_create.html', {'form': form})


def list_delevery_person(request):
    delevery_persons = DeleveryPerson.objects.select_related('customuser_ptr')
    return render(request, 'registration/delevery_person_list.html', {'delevery_persons': delevery_persons})


def logout(request):
    my_logout(request)
    return redirect("login")
