from django.urls import path
from visual.views import netflow_packets_count

urlpatterns = [
        path('', netflow_packets_count, name='netflow_packets_count'),
]

