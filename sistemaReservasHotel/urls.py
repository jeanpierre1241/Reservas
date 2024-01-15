from django.urls import path
from reservas.views import HabitacionList, ReservaListCreate, ReservaRetrieveDestroy

urlpatterns = [
    path('habitaciones/', HabitacionList.as_view()),
    path('reservas/', ReservaListCreate.as_view()),
    path('reservas/<int:pk>/', ReservaRetrieveDestroy.as_view()),
]