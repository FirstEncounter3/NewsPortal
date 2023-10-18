from django_filters import (
    FilterSet,
    DateTimeFilter,
    ModelChoiceFilter,
    CharFilter,
)

from django.forms import DateTimeInput

from .models import (
    Category,
    Author,
)


class PostFilter(FilterSet):
    name = CharFilter(
        field_name='heading',
        lookup_expr='icontains',
        label='Название',

    )

    category = ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        empty_label='Любая',
        label='Категория',
    )

    created_at = DateTimeFilter(
        field_name='created_at',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
        label='ОТ даты',
    )

    author = ModelChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        empty_label='Любой',
        label='Автор',
    )
