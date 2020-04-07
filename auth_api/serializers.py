from rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from django.contrib.auth.models import User

from faculty.models import Faculty

class UserDetailsSerializer(UserDetailsSerializer):
    profile = User
    user_type = serializers.SerializerMethodField()

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('user_type',)

    def get_user_type(self, instance):
        try:
            Faculty.objects.get(user=instance)
            return 'faculty'
        except Faculty.DoesNotExist:
            return 'student'