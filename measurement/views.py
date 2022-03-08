from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, CreateAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, SensorListSerializer, MeasurementCreateSerializer


class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorListCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer


class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer
