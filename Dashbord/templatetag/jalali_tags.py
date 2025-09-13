import jdatetime
from django import template
from django.utils import timezone

register = template.Library()

@register.simple_tag
def jalali_now(format_string="Y-m-d"):
    now = timezone.now()
    return jdatetime.datetime.fromgregorian(datetime=now).strftime(format_string)