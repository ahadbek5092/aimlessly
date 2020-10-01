import django_filters
from .models import Person


# class PlanFiler(django_filters.FilterSet):
#     CHOICES = (
#         ('ascending', 'Ascending'),
#         ('descending', 'Descending')
#     )
#     ordering = django_filters.ChoiceFilter(label='Ordering', choices = CHOICES, method='filter_by_order')
#     class Meta:
#         model = Plan
#         # fields = ('model', 'modelopt', 'plan302', 'plan278', 'name')
#         fields = {
#             'name': ['icontains'],
#             'modelopt': ['icontains'],
#         }
#
#     def filter_by_order(self, queryset, name, value):
#         expression = 'created' if value == 'ascending' else '-created'
#         return queryset.order_by(expression)


class PersonFilter(django_filters.FilterSet):
    # kat = django_filters.CharFilter()
    kod = django_filters.NumberFilter()
    class Meta:
        model = Person
        fields = {
            'kat': ['lte', 'gte'],
            'kod': ['lte', 'gte'],
        }
