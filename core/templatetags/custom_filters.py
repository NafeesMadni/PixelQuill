from django import template
from django.templatetags.static import static


register = template.Library()

# define custom template filters or template tags as Django does not directly allow you to use arbitrary Python functions in templates.


@register.filter(name="get_btn_col")  # Register the filter with a name
def get_btn_col(category, btn_cols):
    return btn_cols[str(category)]

@register.filter(name="get_formated_date") 
def get_formated_date(added_date):
    return added_date.strftime("%b %d, %Y · %H:%M")