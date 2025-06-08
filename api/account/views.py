from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from api.account.serializers import (
    CustomUserSerializers,
)
from account.models import CustomUser


class UserCreateListViewSet(generics.ListCreateAPIView):
    serializer_class = CustomUserSerializers
    queryset = CustomUser.objects.all()
    # http_method_names = ['post', 'get']

    def get_queryset(self):
        view_name = self.request.resolver_match.url_name.split('-')[0]
        if view_name == 'instructor':
            return self.queryset.filter(user_type='instructor')
        elif view_name == 'client':
            return self.queryset.filter(user_type='client')
        else:
            return None

    def perform_create(self, serializer):
        view_name = self.request.resolver_match.url_name.split('-')[0]
        if view_name == 'instructor':
            serializer.save(user_type="instructor")
        else:
            serializer.save(user_type="client")

# class ClientViewSet(ModelViewSet):
#     serializer_class = CustomUserSerializers
#     queryset = CustomUser.objects.all()
#     http_method_names = ['post', 'get']

#     def perform_create(self, serializer):
#         serializer.save(user_type="instructor")
        
