from django.shortcuts import render
from core.apps.main.models import Category


def render_home_page(request):
    return render(request, "main/index.html")


def render_category_page(request, category_id):
    category = Category.objects.filter(id=category_id).first()
    context = {
        "category": category,
    }
    return render(request, "main/category_page.html", context)
