from django import template

register = template.Library()


@register.filter('multiplechoice')
def multiplechoice(field):
    return field.field.widget.__class__.__name__ == 'SelectMultiple'
