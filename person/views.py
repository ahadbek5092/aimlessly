from django.shortcuts import render, redirect,get_object_or_404
from django.urls import  reverse

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView, DeleteView
from .models import Person, Genral, Uprav,Otdel
from django.db.models import Count, F, Q, Sum, Max
from .filters import PersonFilter
from .forms import GenralForm
from django.db import IntegrityError
# Create your views here.
def index(request):
    return render(request, 'index.html', context={'hello': 'world'})
#///////////////////////////////////////////////////////////////////////
# def create_genral(request):
#     my_form = GenralForm()
#     if request.method =='POST':
#         my_form = GenralForm(request.POST or None)
#         if my_form.is_valid():
#             my_form.save()
#             my_form = GenralForm()
#         else:
#             print(my_form.errors)
#     context = {
#         'form': my_form,
#     }
#     return render(request, 'person/create_genral.html', context)
#///////////////////////////////////////////////////////////////////////
# def export(request):
#     plan_recourse = PlanRecources()
#     dataset = plan_recourse.export()
#     response = HttpResponse(dataset.csv, content_type='text/csv')
#     response['Content-Disposition'] = 'attachment: filename = "plan.csv"'
#     return response
# #///////////////////////////////////////////////////////////////////////
def person_list(request):
    fil = PersonFilter(request.GET, queryset=Person.objects.all())
    return render(request, 'person/rerson_filter.html', {'filter': fil})
#///////////////////////////////////////////////////////////////////////
class DepartmentListView(ListView):
    def get(self, request):
        obj = Person.objects.filter(kod__endswith='0000').distinct('kod')
        return render(request, 'pperson/department_list.html', {'object_list': obj})
#///////////////////////////////////////////////////////////////////////
class GenralList(ListView):
    model = Genral
#///////////////////////////////////////////////////////////////////////
class GenralDetailView(DetailView):
    def get(self, request, pk):
        gen = Genral.objects.filter(id=pk)
        return render(request, 'person/genral_detail.html', {"genral": gen})


    # def get_object(self, queryset=None):
    #     pk = self.kwargs.get('pk')
    #
    #     return get_object_or_404(Genral, id=pk)

#////////////////////////////////////////////////////////////////////
class GenralCreateView(CreateView):
    template_name = 'person/create_genral.html'
    form_class = GenralForm
    queryset = Genral.objects.all()
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    # model = Genral
    # fields = ['name', 'url']
    # template_name = 'person/create_genral.html'
#///////////////////////////////////////////////////////////////////////
class GenralUpdateView(UpdateView):
    template_name = 'person/genral_update.html'
    form_class = GenralForm
    queryset = Genral.objects.all()
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Genral,id= pk)
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
#///////////////////////////////////////////////////////////////////////
class GenralDeteleView(DeleteView):
    template_name = 'person/genral_delete.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Genral, id=pk)
    def get_success_url(self):
        return reverse('genral_list')
#///////////////////////////////////////////////////////////////////////
class Genral_Uprav(ListView):
    def get(self, request, pk):

        obj = Uprav.objects.filter(gend=pk)
        return render(request, 'person/uprav_list.html', {'object_list': obj})

#///////////////////////////////////////////////////////////////////////
class UpravList(ListView):
    def get(self,request):
        queryset = Uprav.objects.all()
        return render(request, 'person/uprav_list.html', {'object_list': queryset})
#///////////////////////////////////////////////////////////////////////
class UpravCreate(CreateView):
    model = Uprav
    fields = ['name', 'gend']
    template_name = 'person/uprav_form.html'
#///////////////////////////////////////////////////////////////////////
class UpravUpdate(UpdateView):
    model = Uprav
    fields = ['name', 'gend']
    template_name = 'person/uprav_update_form.html'
    success_url = "/uprav_list"
#///////////////////////////////////////////////////////////////////////
class OtdelList(ListView):
    def get(self, request, id):
        queryset = Otdel.objects.filter(uprav=id)
        return render(request, 'person/otdel_list.html', {'object_list': queryset})
#///////////////////////////////////////////////////////////////////////

