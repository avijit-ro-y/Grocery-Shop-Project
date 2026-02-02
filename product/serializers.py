from rest_framework import serializers
from .models import ProductReview


from .models import (
    Product, Category, ShoppingList,
    CartItem, Deposit, Order, OrderItem
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = "__all__"
        read_only_fields = ["user"]


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"
        read_only_fields = ["user"]


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = "__all__"
        read_only_fields = ["user"]


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"

class ProductReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProductReview
        fields = [
            "id",
            "product",
            "user",
            "rating",
            "review",
            "created_at",
            "updated_at"
        ]
        read_only_fields = ["user"]


class ProductSerializer(serializers.ModelSerializer):
    reviews = ProductReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if not reviews.exists():
            return 0
        return round(sum(r.rating for r in reviews) / reviews.count(), 1)
