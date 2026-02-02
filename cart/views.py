from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import ShoppingListItem
from product.models import Product
from .serializers import ShoppingListSerializer

class AddToShoppingListView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get('product')
        quantity = request.data.get('quantity', 1)

        product = Product.objects.get(id=product_id)

        item, created = ShoppingListItem.objects.get_or_create(
            user=request.user,
            product=product
        )

        if not created:
            item.quantity += int(quantity)
        else:
            item.quantity = quantity

        item.save()
        return Response(ShoppingListSerializer(item).data, status=status.HTTP_201_CREATED)


class ShoppingListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = ShoppingListItem.objects.filter(user=request.user)
        return Response(ShoppingListSerializer(items, many=True).data)


class UpdateShoppingListItemView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        item = ShoppingListItem.objects.get(pk=pk, user=request.user)
        item.quantity = request.data.get('quantity')
        item.save()
        return Response(ShoppingListSerializer(item).data)


class RemoveShoppingListItemView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        item = ShoppingListItem.objects.get(pk=pk, user=request.user)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)