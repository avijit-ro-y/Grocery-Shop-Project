from django.urls import path
from .views import RegisterView, VerifyEmailView, LogoutView, PasswordResetView, PasswordResetConfirmView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import ProfileView, ChangePasswordView, PurchaseHistoryView, WishlistView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('verify-email/<uuid:token>/', VerifyEmailView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset-confirm/<int:uid>/<uuid:token>/', PasswordResetConfirmView.as_view()),
    
    path('profile/', ProfileView.as_view(), name='profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('purchase-history/', PurchaseHistoryView.as_view(), name='purchase-history'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
]