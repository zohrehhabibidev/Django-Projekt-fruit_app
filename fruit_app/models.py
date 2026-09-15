from django.db import models


class Fruit(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    weight = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    is_available = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    origin_country = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    fruits = models.ManyToManyField(Fruit, through="OrderItem")
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.fruit.name
