from django import template
from django.templatetags.static import static
from django.contrib.auth.models import User

register = template.Library()

# define custom template filters or template tags as Django does not directly allow you to use arbitrary Python functions in templates.


@register.filter(name="get_btn_col")  # Register the filter with a name
def get_btn_col(category, btn_cols):
    return btn_cols[str(category)]

@register.filter(name="get_formated_date") 
def get_formated_date(added_date):
    return added_date.strftime("%b %d, %Y · %H:%M")

@register.filter(name="get_user_dp")
def get_user_dp(user_id):
    user = User.objects.get(pk=user_id)
    user_data = user.profile
    return user_data.profile_img.url


@register.filter(name="get_user_full_name")
def get_user_full_name(user_id):
    user = User.objects.get(pk=user_id)
    user_data = user.profile
    return f'{user_data.f_name} {user_data.l_name}'
