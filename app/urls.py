from django.urls import path
from .import views
from .views import (HomePageView, AboutPageView, ItemPageView, CustomerListView, CustomerDeleteView, CustomerCreateView, CustomerUpdateView, CustomerDetailView)

urlpatterns = [
    path('', HomePageView.as_view(), name= 'home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('product/<int:pk>', views.product, name= 'product'),
    path('aboutpage/', AboutPageView.as_view(), name='about'),
    path('itempage/', ItemPageView.as_view(), name='item'),
    path('details/', CustomerListView.as_view(), name='details'),
    path('details/<int:pk>', CustomerDetailView.as_view(), name= 'Customer_Detail'),
    path('details/create', CustomerCreateView.as_view(), name='Customer_Create'),
    path('details/<int:pk>/edit', CustomerUpdateView.as_view(), name='Customer_Update'),
    path('details/<int:pk>/delete', CustomerDeleteView.as_view(), name='Customer_Delete'),

]