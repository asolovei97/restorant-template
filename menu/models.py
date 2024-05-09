from django.db import models
from django.contrib.auth.models import AbstractUser


class DishType(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Cook(models.Model):
    photo = models.ImageField(upload_to="kitchen-service")
    full_name = models.CharField(max_length=255)
    biography = models.TextField()
    years_of_experience = models.IntegerField()

    class Meta:
        ordering = ("full_name",)

    def __str__(self):
        return f"{self.full_name} {self.biography} {self.years_of_experience}"


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="dishes")
    image = models.ImageField(upload_to="kitchen-service")

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "dishes"

    def __str__(self):
        return f"{self.name} {self.description} {self.price}"


class User(AbstractUser):
    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"
