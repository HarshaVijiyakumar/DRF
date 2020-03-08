from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from basic_api import serializers
from basic_api import models
from basic_api import permission
# Create your views here.


class HelloApiView(APIView):
    """
    Test API View
    """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """
        Returns a list of APIview features
        """

        an_apiview = [
            'uses HTTP method as function (get, post, patch, put, delete)',
            'is similar to a traditional django view',
            'gives u the most control over you application logic',
            'is mapped manually to urls'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """
        create a hello message with our name
        """
        serializer1 = self.serializer_class(data=request.data)

        if serializer1.is_valid():
            name = serializer1.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer1.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """
        handel update an object
        """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """
        handel partial update an object
        """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """
        handel update an object
        """
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test Api viewset """
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Return a hello message"""

        a_viewset = [
            'User action (list, create , retrive, update, partial update)',
            'Automatically maps to urls using Routers',
            'provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handel getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handel updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handel updating part of  an object """
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handel delete an object """
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handel creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.user_profile.object.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = {'name', 'email'}


class UserLoginApiView(ObtainAuthToken):
    """Handel create user authentication Tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



