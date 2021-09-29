from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ Serializers a name field to test our API Views"""
    name =serializers.CharField(max_length=10)
