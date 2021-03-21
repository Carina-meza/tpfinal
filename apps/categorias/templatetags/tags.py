from django import template
from ..models import Categoria

register = template.Library()

@register.inclusion_tag('templatetags/menu_categorias.html')
def menu_categorias():
    return {
        'categorias': Categoria.objects.all(),
    }

@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()
