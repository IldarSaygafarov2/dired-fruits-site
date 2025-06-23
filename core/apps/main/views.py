from django.shortcuts import render
from core.apps.main.models import Category, Product


def render_home_page(request):
    return render(request, "main/index.html")


def render_shop_page(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "main/category_page.html", context)


def render_category_page(request, category_id):
    category = Category.objects.filter(id=category_id).first()
    products = Product.objects.filter(category=category)

    context = {
        "category": category,
        "category_id": category_id,
        "products": products,
    }
    return render(request, "main/category_page.html", context)


def render_product_page(request, product_id):
    return render(request, "main/product_page.html")


def render_contacts_page(request):
    return render(request, "main/contacts.html")


def render_about_us_page(request):
    return render(request, "main/about-us.html")
