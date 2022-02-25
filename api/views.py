from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Accommodation, Room
from .serializers import AccommodationSerializer, RoomSerializer


@api_view(['GET'])
def getAccommodate(request):
    accommodations = Accommodation.objects.all()
    serializer = AccommodationSerializer(accommodations, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addAccommodate(request):
    serializer = AccommodationSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addRoom(request):
    serializer = RoomSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)