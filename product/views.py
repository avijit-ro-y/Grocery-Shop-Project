from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from .models import (Product,ProductReview, ShoppingList,CartItem, OrderItem)
from .serializers import (ProductSerializer,ProductReviewSerializer,ShoppingListSerializer, CartItemSerializer,DepositSerializer, OrderItemSerializer)
from .permissions import IsAdminOrOwner,HasPurchasedProduct


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Product.objects.all()      
        return Product.objects.filter(created_by=user) 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProductFilterView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        qs = Product.objects.filter(available=True)
        category = self.request.query_params.get("category")
        if category:
            qs = qs.filter(category_id=category)
        return qs

class ShoppingListViewSet(viewsets.ModelViewSet):
    serializer_class = ShoppingListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ShoppingList.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DepositView(generics.CreateAPIView):
    serializer_class = DepositSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SellerSalesView(generics.ListAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return OrderItem.objects.filter(
            product__created_by=self.request.user
        )

class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ProductReviewSerializer
    permission_classes = [permissions.IsAuthenticated, HasPurchasedProduct]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ProductReview.objects.filter(user=self.request.user)


class ProductReviewListView(generics.ListAPIView):
    serializer_class = ProductReviewSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        product_id = self.kwargs["product_id"]
        return ProductReview.objects.filter(product_id=product_id)

