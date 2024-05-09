from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render, HttpResponse
from django.views import generic

from .models import Dish, DishType, Cook, User
from .forms import DishSearchForm, UserCreateForm


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "menu/index.html")


def about(request: HttpRequest) -> HttpResponse:
    num_dish = Dish.objects.count()
    num_dish_type = DishType.objects.count()
    num_cooks = Cook.objects.count()

    context = {
        "num_dish": num_dish,
        "num_dish_type": num_dish_type,
        "num_cooks": num_cooks
    }

    return render(request, "menu/about.html", context=context)


class DishListView(LoginRequiredMixin, generic.ListView):
    paginate_by = 5
    context_object_name = "dish_list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishSearchForm(
            initial={
                "name": name
            }
        )
        return context

    def get_queryset(self):
        queryset = Dish.objects.all().select_related("dish_type")
        form = DishSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5
    context_object_name = "cook_list"


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.prefetch_related("dishes__cooks")


class UserCreateView(generic.CreateView):
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy("menu:index")
