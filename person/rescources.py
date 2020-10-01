from import_export import  resources
from person.models import  Person

class PersonRescources(resources.ModelResource):
    class Meta:
        model = Person