from django.http import JsonResponse
from .models import LogNetflow
import time
from collections import Counter

def netflow_packets_count(request):
    aggregate_by = request.GET.get('aggregate_by', 'minute')
    packets = LogNetflow.objects.all().order_by('-time_start')[:80000]  # 示例：获取最近的800条记录

    aggregated_data = Counter()
    for packet in packets:
        timestamp_time = time.localtime(packet.time_start)

        if aggregate_by == 'minute':
            key = time.strftime('%Y-%m-%d %H:%M', timestamp_time)
        elif aggregate_by == 'hour':
            key = time.strftime('%Y-%m-%d %H', timestamp_time)
        else:  # day
            key = time.strftime('%Y-%m-%d', timestamp_time)

        aggregated_data[key] += 1

    labels, data = zip(*sorted(aggregated_data.items(), key=lambda x: x[0])[-12:])

    return JsonResponse({'labels': labels, 'data': data})

