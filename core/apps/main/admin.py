from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "icon")
    list_display_links = ("name",)
    search_fields = ("name",)
    list_filter = ("created_at", "updated_at")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
        "manufacturer",
        "importer",
        "net_weight",
        "gross_weight",
        "status"
    )
    list_display_links = ("name",)
    search_fields = ("name", "category__name", "manufacturer", "importer")
    list_filter = ("category", "status", "created_at")
