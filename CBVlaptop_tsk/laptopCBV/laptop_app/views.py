from django.shortcuts import render

from .models import Laptop
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView


# Create your views here.

class LaptopListView(ListView):
    model = Laptop


class LaptopCreateView(CreateView):
    model = Laptop
    fields = '__all__'
    success_url = '/show/'


class LaptopUpdateView(UpdateView):
    model = Laptop
    fields = '__all__'
    success_url = '/show/'


class LaptopDeleteView(DeleteView):
    model = Laptop
    success_url = '/show/'


def homeview(request):
    template_name='Laptop_app/home.html'
    context={}
    return render(request,template_name,context)
