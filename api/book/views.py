from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import generics

from rest_framework.response import Response
from api.book.serializers import (
    InstructerSerializers,
    FitnessClassSerializers,
    BookingSlotSerialisers
)
from account.models import CustomUser
from book.models import Instructor, FitnessClass, BookingSlot


class InstructerProfileViewSet(generics.ListCreateAPIView):
    serializer_class = InstructerSerializers
    queryset = Instructor.objects.all()
    # http_method_names = ['post', 'get']
        
    
class FitnessClassesViewSet(generics.ListCreateAPIView):
    serializer_class = FitnessClassSerializers
    queryset = FitnessClass.objects.all()
    # http_method_names = ['post', 'get']


class CreateBookSlotApiViewSet(generics.ListCreateAPIView):
    serializer_class = BookingSlotSerialisers
    queryset = BookingSlot.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save()
    #     data = serializer.validated_data
    #     print(data)
    #     fitness_class = serializer.validated_data.get("fitness_class")

    #     print("-"*10)
    #     print(serializer.validated_data)
    #     print(serializer.data)

    #     print("-"*10)
    #     serializer.save()

    #     return super().perform_create(serializer)


class ListBookingApiViewSet(generics.ListAPIView):
    serializer_class = BookingSlotSerialisers
    # queryset = BookingSlot.objects.all()
    # lookup_field = 'client.email'

    def get_queryset(self):
        return BookingSlot.objects.filter(client__email = self.kwargs.get("email"))
