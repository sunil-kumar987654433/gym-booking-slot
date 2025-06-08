from django.urls import path, include
from api.book import views

from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'instructer-profile', views.InstructerProfileViewSet, basename='instructer-profile')
# router.register(r'fitness-classes', views.FitnessClassesViewSet, basename='fitness-classes')




urlpatterns = [
    path('instructer-profile/', views.InstructerProfileViewSet.as_view(), name='instructer-profile'),
    path('fitness-classes/', views.FitnessClassesViewSet.as_view(), name='fitness-classes'),

    path("book-slot/", views.CreateBookSlotApiViewSet.as_view(), name='book_slot'),
    path("bookings/<str:email>/", views.ListBookingApiViewSet.as_view(), name='bookings'),

]+ router.urls