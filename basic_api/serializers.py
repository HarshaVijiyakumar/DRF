from rest_framework import serializers
# from basic_api.models import DRFPost
from basic_api import models


class HelloSerializer(serializers.Serializer):
    """
    serializer a name field for testing for APIView
    """
    name = serializers.CharField(max_length=10)

#
# class UserProfileSerializer(serializers.ModelSerializer):
#     """ Serializer a user profile object"""
#
#     class Meta:
#         model = models.UserProfile
#         fields = ('id', 'email', 'name', 'password')
#         extra_kwards = {
#             'password': {
#                 'write_only': True,
#             }
#         }