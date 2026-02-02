from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=0)

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="products"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class ShoppingList(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="shopping_lists"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ["user", "product"]


class CartItem(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="product_cart_items"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)



class Deposit(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="deposits"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders"
    )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="priced_order_items"  
    )
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class ProductReview(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="product_reviews"
    )
    rating = models.PositiveIntegerField() 
    review = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["product", "user"]

    def __str__(self):
        return f"{self.product.name} - {self.rating}"

