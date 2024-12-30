from django.db import models


class CustomerDetails (models.Model):
    lastName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    fullAddress = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.lastName


class Cookies(models.Model):
    productName = models.CharField(max_length=20)
    productDesc = models.CharField(max_length=100)
    productPrice = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.productName

class OrderLog(models.Model):
    customer = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
    cookieOrder = models.ManyToManyField(Cookies)
    status = models.CharField(max_length=20, choices=(
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')))

    def __str__(self):
        return f"{self.customer.lastName if self.customer else 'No Customer'}"








