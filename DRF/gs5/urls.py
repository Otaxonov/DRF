from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register('stl', views.StudentModelViewSet, basename='stl')

urlpatterns = [
    path('', include(router.urls))
]
