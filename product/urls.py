from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ProductViewSet, ShoppingListViewSet,CartItemViewSet, ProductFilterView,DepositView, SellerSalesView,ReviewCreateView,ReviewUpdateDeleteView,ProductReviewListView)

router = DefaultRouter()
router.register("products", ProductViewSet, basename="products")
router.register("shopping-list", ShoppingListViewSet, basename="shopping-list")
router.register("cart", CartItemViewSet, basename="cart")

urlpatterns = [
    path("", include(router.urls)),
    path("products/filter/", ProductFilterView.as_view()),
    path("deposit/", DepositView.as_view()),
    path("dashboard/sales/", SellerSalesView.as_view()),
    path("reviews/", ReviewCreateView.as_view(), name="create-review"),
    path("reviews/<int:pk>/", ReviewUpdateDeleteView.as_view(), name="update-delete-review"),
    path("products/<int:product_id>/reviews/", ProductReviewListView.as_view(), name="product-reviews"),
]