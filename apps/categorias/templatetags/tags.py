from django import template
from ..models import Categoria

register = template.Library()

@register.inclusion_tag('templatetags/menu_categorias.html')
def menu_categorias():
	return {
		'categorias': Categoria.objects.all(),
	}
