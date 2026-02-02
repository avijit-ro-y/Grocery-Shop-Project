from django.db import models
from django.conf import settings
from product.models import Product

User = settings.AUTH_USER_MODEL

class ShoppingListItem(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="shopping_cart_items"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
