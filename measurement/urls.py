from django.urls import path

from measurement.views import SensorDetailView, SensorListCreateView, MeasurementCreateView

urlpatterns = [
    path('sensors/<pk>/', SensorDetailView.as_view()),
    path('sensors/', SensorListCreateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
]
