from django.db import models
from users.models import User
from product.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order_items"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="basic_order_items" 
    )
    quantity = models.IntegerField()
