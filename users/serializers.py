from rest_framework import serializers
from django.contrib.auth import get_user_model
from product.models import ShoppingList, Product
User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            is_active=False
        )


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

class ProfileSerializer(serializers.ModelSerializer):
    shopping_preferences = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'shopping_preferences']

    def get_shopping_preferences(self, obj):
        return [item.product.name for item in ShoppingList.objects.filter(user=obj)]

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class PurchaseHistorySerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    purchased_at = serializers.DateTimeField(source='created_at')
    
    class Meta:
        model = ShoppingList
        fields = ['product_name', 'purchased_at', 'quantity']

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description']
