from django.db import models
from django.urls import reverse

from core.apps.base_app.models import BaseModel


class Category(BaseModel):
    name = models.CharField(
        verbose_name="Название категории", max_length=100, unique=True
    )
    description = models.TextField(verbose_name="Описание категории", blank=True)
    icon = models.ImageField(
        verbose_name="Иконка категории",
        upload_to="categories/icons/",
        blank=True,
        null=True,
    )

    def get_absolute_url(self):
        return reverse("category-page", kwargs={"category_id": self.pk})

    class Meta(BaseModel.Meta):
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(verbose_name="Название товара", max_length=200)
    grade = models.IntegerField(default=0)
    country_of_origin = models.CharField(
        verbose_name="Страна происхождения", max_length=100, blank=True, null=True
    )
    production_date = models.DateField(
        verbose_name="Дата производства", blank=True, null=True
    )
    description = models.TextField(verbose_name="Описание товара", blank=True)
    price = models.FloatField(verbose_name="Цена товара", default=0.0)
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.CASCADE,
        related_name="products",
    )
    image = models.ImageField(
        verbose_name="Изображение товара",
        upload_to="products/images/",
        blank=True,
        null=True,
    )
    manufacturer = models.CharField(
        verbose_name="Производитель", max_length=200, blank=True, null=True
    )
    importer = models.CharField(
        verbose_name="Импортер", max_length=200, blank=True, null=True
    )
    net_weight = models.IntegerField(verbose_name="Нетто вес", blank=True, null=True)
    gross_weight = models.FloatField(verbose_name="Брутто вес", blank=True, null=True)
    batch_number = models.CharField(
        verbose_name="Номер партии", max_length=50, blank=True, null=True
    )
    storage_conditions = models.TextField(
        verbose_name="Условия хранения", blank=True, null=True
    )

    class Meta(BaseModel.Meta):
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


# class Banner(BaseModel):
#     title = models.CharField(verbose_name="Заголовок баннера", max_length=200)
#     image = models.ImageField(
#         verbose_name="Изображение баннера",
#         upload_to="banners/images/",
#         blank=True,
#         null=True,
#     )
#     link = models.URLField(verbose_name="Ссылка на баннер", blank=True, null=True)

#     class Meta(BaseModel.Meta):
#         verbose_name = "Баннер"
#         verbose_name_plural = "Баннеры"

#     def __str__(self):
#         return self.title
