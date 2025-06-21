from django.urls import path

from . import views


urlpatterns = [
    path(
        "",
        views.render_home_page,
        name="home-page",
    ),
    path(
        "category/<int:category_id>/",
        views.render_category_page,
        name="category-page",
    ),
]
