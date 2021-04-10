from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import GameViewSet

router = routers.DefaultRouter()
router.register(r'games', GameViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls))
]