from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.template.context_processors import request
from .models import Product
from django.views.generic import TemplateView,ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CustomerDetails
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'app/product.html', {'product': product})

def item(request):
    products = Product.objects.all()
    return render(request, 'app/itemspage.html', {'products':products})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.success(request, 'There was an error, Please try again...')
            return redirect('login')

    else:
         return render(request, 'app/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')

def register_user(request):
        form = SignUpForm()
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']

                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, ("You have successfully registered! Welcome!"))
                return redirect('home')
            else:
                messages.success(request, 'There was a problem Registering, please try again later...')
                return redirect('login')
        else:

            return render(request, "app/register.html", {'form': form})


class HomePageView(TemplateView):
    template_name = 'app/homepage.html'

class AboutPageView(TemplateView):
    template_name = 'app/aboutpage.html'

class ItemPageView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'app/itemspage.html'

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

