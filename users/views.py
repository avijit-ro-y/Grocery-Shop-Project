from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions,generics, permissions, status
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserCreateSerializer, PasswordResetSerializer,ProfileSerializer, ChangePasswordSerializer, PurchaseHistorySerializer, WishlistSerializer
import uuid
from django.shortcuts import get_object_or_404
from .models import EmailVerification
from product.models import ShoppingList 


User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = uuid.uuid4()
        user.emailverification_set.create(token=token)
        send_mail(
            'Verify your email',
            f'http://127.0.0.1:8000/api/users/verify-email/{token}/',
            settings.EMAIL_HOST_USER,
            [user.email]
        )
        return Response({'message': 'Verification email sent'}, status=status.HTTP_201_CREATED)

class VerifyEmailView(APIView):
    def get(self, request, token):
        verification = get_object_or_404(EmailVerification, token=token)

        user = verification.user
        user.is_active = True
        user.save()

        verification.delete()

        return Response(
            {"message": "Email verified successfully"},
            status=status.HTTP_200_OK
        )



class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh')
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({'message': 'Logged out successfully'})


class PasswordResetView(APIView):
    serializer_class = PasswordResetSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        user = User.objects.get(email=email)
        token = uuid.uuid4()
        user.emailverification_set.create(token=token)
        send_mail(
            'Password reset',
            f'http://127.0.0.1:8000/api/users/password-reset-confirm/{user.pk}/{token}/',
            settings.EMAIL_HOST_USER,
            [email]
        )
        return Response({'message': 'Password reset email sent'})


class PasswordResetConfirmView(APIView):
    def post(self, request, uid, token):
        verification = User.emailverification_set.model.objects.get(token=token)
        user = verification.user
        user.set_password(request.data['password'])
        user.save()
        verification.delete()
        return Response({'message': 'Password reset successful'})




class ProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user

class ChangePasswordView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not check_password(serializer.validated_data['old_password'], user.password):
            return Response({"old_password": "Wrong password"}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return Response({"detail": "Password updated successfully"}, status=status.HTTP_200_OK)

class PurchaseHistoryView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PurchaseHistorySerializer

    def get_queryset(self):
        return ShoppingList.objects.filter(user=self.request.user)

class WishlistView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WishlistSerializer

    def get_queryset(self):
        return
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
