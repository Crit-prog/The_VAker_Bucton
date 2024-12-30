from django.views.generic import TemplateView,ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CustomerDetails
from django.urls import reverse_lazy



class HomePageView(TemplateView):
    template_name = 'app/homepage.html'

class AboutPageView(TemplateView):
    template_name = 'app/aboutpage.html'

class ItemPageView(TemplateView):
    template_name = 'app/itemspage.html'

class ContactPageView(TemplateView):
        template_name = 'app/contactpage.html'

class CustomerListView (ListView):
    model = CustomerDetails
    context_object_name = 'detail_list'
    template_name = 'app/Customer_List.html'

class CustomerDetailView(DetailView):
    model = CustomerDetails
    context_object_name = 'detail'
    template_name = 'app/Customer_Detail.html'

class CustomerCreateView(CreateView):
    model = CustomerDetails
    fields = ['lastName', 'firstName', 'email', 'password', 'fullAddress', 'phone']
    template_name = 'app/Customer_Create.html'
    success_url = reverse_lazy('details')


class CustomerUpdateView(UpdateView):
    model = CustomerDetails
    fields = ['lastName', 'firstName', 'email', 'password', 'fullAddress', 'phone']
    template_name = 'app/Customer_Update.html'
    success_url = reverse_lazy('details')

class CustomerDeleteView(DeleteView):
    model = CustomerDetails
    template_name = 'app/Customer_Delete.html'
    success_url = reverse_lazy('details')

