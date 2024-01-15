from rest_framework import generics
from .models import Habitacion, Reserva
from .serializers import HabitacionSerializer, ReservaSerializer

class HabitacionList(generics.ListAPIView):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer

class ReservaListCreate(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer