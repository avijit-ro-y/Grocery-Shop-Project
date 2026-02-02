from rest_framework.permissions import BasePermission
from order.models import OrderItem

class IsAdminOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.created_by == request.user

class HasPurchasedProduct(BasePermission):
    message = "You must purchase this product before reviewing it."

    def has_permission(self, request, view):
        product_id = request.data.get("product")
        if not product_id:
            return False

        return OrderItem.objects.filter(
            order__user=request.user,
            product_id=product_id
        ).exists()
