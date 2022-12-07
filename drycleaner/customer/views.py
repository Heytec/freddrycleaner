from django.shortcuts import render
from .models import  Customer
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class Customerlist(LoginRequiredMixin,ListView):
    model = Customer
    context_object_name = 'customers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['customers'] = context['customers'].filter(
                name__contains=search_input)

        context['search_input'] = search_input

        return context




class CustomerDetail(LoginRequiredMixin,DetailView):
    model = Customer
    context_object_name = 'customer'


class CustomerCreate(LoginRequiredMixin,CreateView):
    model = Customer
    fields = [
        "name",
        "phone_number",
        "description",
        "quantity",
        "price",
        "collection_date",
        "collected",
        "paid"

    ]
    success_url = reverse_lazy('customers')



class CustomerUpdate(LoginRequiredMixin,UpdateView):
    model = Customer
    fields = [
        "name",
        "phone_number",
        "description",
        "quantity",
        "price",
        "collection_date",
        "collected",
        "paid"

    ]
    success_url = reverse_lazy('customers')

class CustomerDeleteview(LoginRequiredMixin,DeleteView):
    model = Customer
    context_object_name = 'customer'
    success_url = reverse_lazy('customers')


