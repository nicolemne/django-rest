from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from profiles.models import Profile
from profiles.serializers import ProfileSerializer

class ProfileList(generics.ListAPIView):
    '''
    Lists all profiles.
    No create view as profile creation is handled by Django signals
    '''
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateAPIView):
    '''
    Retrieve or update a profile if you're the owner
    '''
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
