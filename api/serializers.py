from rest_framework import serializers
from base.models import Accommodation, Room

class AccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Accommodation
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model= Room
        fields = '__all__'