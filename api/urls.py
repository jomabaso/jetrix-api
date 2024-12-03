# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  RegisterView, TableroViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'tableros', TableroViewSet, basename='tableros')

urlpatterns = [
    path('', include(router.urls)),
    # path("tableros/", TableroListCreate.as_view(), name="tablero-list-create"),
    # path("tableros/<int:pk>", TableroCRUD.as_view(), name="tablero-detail"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
]
