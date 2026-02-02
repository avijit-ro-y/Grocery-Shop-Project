from django.urls import path
from .views import (
    AddToShoppingListView,
    ShoppingListView,
    UpdateShoppingListItemView,
    RemoveShoppingListItemView
)

urlpatterns = [
    path('add/', AddToShoppingListView.as_view()),
    path('', ShoppingListView.as_view()),
    path('update/<int:pk>/', UpdateShoppingListItemView.as_view()),
    path('remove/<int:pk>/', RemoveShoppingListItemView.as_view()),
]