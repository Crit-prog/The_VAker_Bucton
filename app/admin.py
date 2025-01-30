from django.contrib import admin
from .models import Category
from .models import Product
from .models import CustomerDetails
from .models import OrderLog



# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CustomerDetails)
admin.site.register(OrderLog)
