# days/templatetags/rating_colors.py

from django import template

register = template.Library()

@register.filter
def rating_color(rating):
    colors = {
        'F': 'black',
        'E': 'gray',
        'D': 'white',
        'C': 'green',
        'B': 'blue',
        'A': 'purple',
        'S': 'red'
    }
    return colors.get(rating, 'black')