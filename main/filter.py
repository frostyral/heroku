import django_filters
from .models import *
from django_filters import CharFilter

class StudentFilter(django_filters.FilterSet):
    search_bar = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = StudentList
        fields = ('search_bar', 'college', 'course')