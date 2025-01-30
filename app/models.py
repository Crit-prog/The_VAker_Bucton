from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class CustomerDetails (models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    fullAddress = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f' {self.lastName} {self.firstName}'


class Product(models.Model):
    productName = models.CharField(max_length=50)
    productDesc = models.CharField(max_length=250, default='', blank=True, null=True)
    productPrice = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to= 'uploads/product/')


    def __str__(self):
        return self.productName

class OrderLog(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.CharField(max_length=20, choices=(
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')))








