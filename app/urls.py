from django.urls import path
from .views import (HomePageView, AboutPageView, ItemPageView, ContactPageView, CustomerListView, CustomerDeleteView, CustomerCreateView, CustomerUpdateView, CustomerDetailView)

urlpatterns = [
    path('', HomePageView.as_view(), name= 'home'),
    path('aboutpage/', AboutPageView.as_view(), name='about'),
    path('itempage/', ItemPageView.as_view(), name='item'),
    path('contactpage/', ContactPageView.as_view(), name='contact'),
    path('details/', CustomerListView.as_view(), name='details'),
    path('details/<int:pk>', CustomerDetailView.as_view(), name= 'Customer_Detail'),
    path('details/create', CustomerCreateView.as_view(), name='Customer_Create'),
    path('details/<int:pk>/edit', CustomerUpdateView.as_view(), name='Customer_Update'),
    path('details/<int:pk>/delete', CustomerDeleteView.as_view(), name='Customer_Delete'),

]