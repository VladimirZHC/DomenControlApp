from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'divisions', views.DivisionViewSet)
router.register(r'grouppolicies', views.GroupPolicyViewSet)
router.register(r'users', views.DomenUserViewSet)
router.register(r'computers', views.ComputersViewSet)
router.register(r'schemas', views.SchemaParamsViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('test/', views.ApiView.as_view()),
]


