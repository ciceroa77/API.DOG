from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PetViewSet

router = DefaultRouter()
router.register(r'pets', PetViewSet)  # Define a URL para acessar os pets

urlpatterns = [
    path('', include(router.urls)),  # Inclui as URLs registradas
]
