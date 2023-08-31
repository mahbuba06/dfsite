from django.urls import path, include
from women.views import *
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r"women-list", WomenViewSet, basename='women-list')

urlpatterns = [
    path("drf-auth/", include("rest_framework.urls")),
    path("women-list/", WomenListCreateAPIVIew.as_view(), name="women-list"),
    path("women-list/<int:pk>", WomenUpdateDestroyAPIView.as_view(), name="women-list"),
]
