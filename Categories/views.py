from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Category
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


# Create your views here.
class CategoryList(LoginRequiredMixin, ListView):
    model = Category
    template_name = "category_list.html"
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_nb'] = Category.objects.all().count()
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff, login_url='/forbidden/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CategoryCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    fields = ["name", "slug", "image"]
    template_name = "category_add.html"
    success_url = reverse_lazy('categories:list')
    success_message = "Categorie %(name)s Creee !"

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CategoryUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    fields = ["name", "slug", "image"]
    template_name = "category_update.html"
    success_url = reverse_lazy('categories:list')
    success_message = "Categorie %(name)s Modifiee !"

    @method_decorator(user_passes_test(lambda u: u.is_staff, lambda v: v.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = "category_confirm_delete.html"
    success_url = reverse_lazy('categories:list')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)