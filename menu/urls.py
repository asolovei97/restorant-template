from django.urls import path
from .views import (
    index,
    about,
    DishListView,
    DishDetailView,
    CookListView,
    CookDetailView,
    UserCreateView
)


urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("cook/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("user/create", UserCreateView.as_view(), name="user-create")
]

app_name = "menu"

