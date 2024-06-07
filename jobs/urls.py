from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, JobViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
