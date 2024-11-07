# api/urls.py

from django.urls import path
from .views import TableroListCreate, TableroCRUD

urlpatterns = [
    path("tableros/", TableroListCreate.as_view(), name="tablero-list-create"),
    path("tableros/<int:pk>", TableroCRUD.as_view(), name="tablero-detail"),
]
