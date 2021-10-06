from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from profiles_api import permission
from profiles_api import models


class HelloApiView(APIView):
    """Test API View"""

    serializer_class=serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns list of APIView features """
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})


    def post(self,request):
        """Creating Hello message with name """
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Handling updating an object"""
        return Response({'method':'PUT'})


    def patch(self, request, pk=None):
        """ Handling partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """ Handling delete method"""
        return Response({'method':'delete'})

class HelloViewSet(viewsets.ViewSet):
    """ test API view set"""

    serializer_class=serializers.HelloSerializer

    def list(self, request):
        """ Return a hello message with viewset list method"""

        an_viewset=[
        'Users actions (list,create,retrive,update,partial_update, destroy)',
        'Automatically maps Urls using routers',
        'Provide more fuctionality with lesss code'
        ]

        return Response({'message':'Hello','an_viewset':an_viewset})

    def create(self, request):
        """ Create an new hello message"""

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello,{name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )


    def retrive(self, request, pk=None):
        """ Creating new retrive method"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """ Creating new update method"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """ Creating new partial_update method"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """ Creating new destroy method"""
        return Response({'http_method':'Delete'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating user profile"""
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permission.UpdateOwnProfile,)
