from django.urls import path, include
from api.account import views

from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'instructor', views.UserCreateListViewSet, basename='instructor')
# router.register(r'client', views.UserCreateListViewSet, basename='client')


urlpatterns = [
    path('instructor', views.UserCreateListViewSet.as_view(), name='instructor'),
    path('client', views.UserCreateListViewSet.as_view(), name='client')

]+ router.urls