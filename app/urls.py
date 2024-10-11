from django.urls import path
from .views import HomePageView, AboutPageView, ItemPageView, ContactPageView


urlpatterns = [
    path('', HomePageView.as_view(), name= 'home'),
    path('aboutpage/', AboutPageView.as_view(), name= 'about'),
    path('itempage/', ItemPageView.as_view(), name= 'item'),
    path('contactpage/', ContactPageView.as_view(), name= 'contact'),
]