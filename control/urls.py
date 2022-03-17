from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'division', views.DivisionViewSet)
router.register(r'grouppolicy', views.GroupPolicyViewSet)
router.register(r'users', views.DomenUserViewSet)
router.register(r'computers', views.ComputersViewSet)


urlpatterns = [
    path('', include(router.urls)),
]