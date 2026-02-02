from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order
from users.models import User

class CheckoutView(APIView):
    def post(self, request):
        user = request.user
        total = float(request.data['total'])

        if user.wallet_balance < total:
            return Response({"error": "Insufficient balance"}, status=400)

        user.wallet_balance -= total
        user.save()
        Order.objects.create(user=user, total=total)

        return Response({"message": "Order placed successfully"})