from django.urls import path

from . import views


urlpatterns = [
    path("", views.render_home_page, name="home-page"),
    path("shop/", views.render_shop_page, name="shop-page"),
    path(
        "shop/category/<int:category_id>/",
        views.render_category_page,
        name="category-page",
    ),
    path(
        "shop/product/<int:product_id>/",
        views.render_product_page,
        name="product-detail",
    ),
    path("contacts/", views.render_contacts_page, name="contacts-page"),
    path("about/", views.render_about_us_page, name="about-page"),
]
