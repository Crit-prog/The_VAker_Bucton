from django.contrib import admin
from .models import CustomerDetails
from .models import OrderLog
from .models import Cookies

# Register your models here.

admin.site.register(CustomerDetails)
admin.site.register(OrderLog)
admin.site.register(Cookies)