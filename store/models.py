from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    apellido = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    whatsapp = models.CharField(max_length=9, null=True)

    def __str__(self):
        mensaje = f'{self.name}'
        return mensaje


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    slug = models.CharField(max_length=150, null=True, blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    price_false = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    digital = models.BooleanField(default=False, null=True, blank=False)
    nuevo = models.BooleanField(default=False, null=True, blank=False)
    tendencia = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=False)
    quantity = models.IntegerField(null=True, blank=False)


    def __str__(self):
        mensaje = f'{self.name}'
        return mensaje

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def image2URL(self):
        try:
            url = self.image2.url
        except:
            url = ''
        return url

    @property
    def image3URL(self):
        try:
            url = self.image3.url
        except:
            url = ''
        return url

    @property
    def image4URL(self):
        try:
            url = self.image4.url
        except:
            url = ''
        return url


class Order(models.Model):
    # Antiguo 1
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    #
    # Nuevo 1
    #customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    #
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        mensaje = f'{self.id} - {self.customer.name}'
        return mensaje

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        mensaje = f'{self.product.name}'
        return mensaje



class ShippingAddres(models.Model):
    # Antiguo 1
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    #
    # Nuevo 1
    #customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    #
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.CharField(max_length=200, null=True)

    def __str__(self):
        mensaje = f'{self.address}'
        return mensaje
