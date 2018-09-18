from django import template
from info.models import LandingTabExtra

register = template.Library()


@register.inclusion_tag('main/extra_menu_header.html')
def extra_menu_header():
    extra_menu = LandingTabExtra.objects.actual().select_related('content')
    return {'extra_menu': extra_menu}
