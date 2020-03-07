from django.urls import path, include
from rest_framework.routers import DefaultRouter
from basic_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='Hello-viewset')


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
