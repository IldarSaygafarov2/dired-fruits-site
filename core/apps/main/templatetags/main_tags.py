from django.template import Library

from core.apps.main.models import Category


register = Library()


@register.simple_tag()
def get_categories():
    """
    Returns all categories from the database.
    """
    return Category.objects.all()
