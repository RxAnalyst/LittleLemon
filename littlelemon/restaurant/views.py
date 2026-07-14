#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view,  permission_classes

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, MenuSerializer
from .models import Menu, Booking
from .serializers import BookingSerializer
from rest_framework.response import Response

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

# Menu API - GET all menu items and POST new item
class MenuView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuView(
    generics.RetrieveUpdateAPIView,
    generics.DestroyAPIView
):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})