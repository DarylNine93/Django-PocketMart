from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, DeliveryPersonForm
from django.contrib.auth import login as my_login, logout as my_logout
from django.utils.http import is_safe_url
from django.contrib import messages
from .models import DeliveryPerson
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test


# Create your views here.

@user_passes_test(lambda u: u.is_staff, login_url='/forbidden/')
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_superuser = True
            user.set_password(form.cleaned_data["password1"])
            user.save()
            my_login(request, user)
            request.session.set_expiry(300)
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
            request.session.set_expiry(300)
            redirect_to = request.POST.get("next", "")
            url_is_safe = is_safe_url(redirect_to, "")
            if redirect_to and url_is_safe:
                return redirect(redirect_to)
            else:
                return redirect("/")
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form, "next": request.GET.get("next", "")})


@user_passes_test(lambda u: u.is_staff, login_url='/forbidden/')
def create_delivery_person(request):
    if request.method == 'POST':
        form = DeliveryPersonForm(request.POST)
        if form.is_valid():
            delivery_man = form.save(commit=False)
            delivery_man.set_password(form.cleaned_data["password1"])
            delivery_man.save()
            group = Group.objects.get(name='DeliveryPersons')
            delivery_man.groups.add(group)
            my_login(request, delivery_man)
            messages.success(request, 'Nouveau Livreur Cree!')
            return redirect('list')
    else:
        form = DeliveryPersonForm()
    return render(request, 'registration/delivery_person_create.html', {'form': form})


@user_passes_test(lambda u: u.is_staff, login_url='/forbidden/')
def list_delivery_person(request):
    delivery_persons = DeliveryPerson.objects.select_related('customuser_ptr')
    return render(request, 'registration/delivery_person_list.html', {'delivery_persons': delivery_persons})


def delivery_person_profile(request):
    user = request.user
    data = {'id': user.id, 'username': user.username, 'email': user.email, 'phone': user.phone}
    form = SignUpForm(initial=data)
    return render(request, "registration/delivery_person_profile.html", {"user": user, "form": form})


def delivery_person_profile_edit(request):
    user = request.user
    if request.method == "POST":
        form = SignUpForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    return 0


def logout(request):
    my_logout(request)
    return redirect("login")
