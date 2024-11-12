# api/urls.py

from django.urls import path
from .views import TableroListCreate, TableroCRUD, RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("tableros/", TableroListCreate.as_view(), name="tablero-list-create"),
    path("tableros/<int:pk>", TableroCRUD.as_view(), name="tablero-detail"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
]
