from django import template

register = template.Library()

@register.filter(name='add_class')
def addclass(field, class_attr):
    return field.as_widget(attrs={'class': class_attr})
