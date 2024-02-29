from django.http import JsonResponse
from .models import LogNetflow
from collections import defaultdict

def netflow_packets_count(request):
    print("netflow_packets_count running")

    logs = LogNetflow.objects.all().order_by('-time_start')[:30]

    packets_per_minute = defaultdict(int)
    for log in logs:
        # 使用rts方法获取datetime对象
        minute_key = log.group_time_start()
        packets_per_minute[minute_key] += 1

    # 准备响应数据
    labels = list(packets_per_minute.keys())
    data = list(packets_per_minute.values())

    response_data = {
        'labels': labels[::-1],  # 反转列表以确保时间顺序（最早到最新）
        'data': data[::-1],  # 同样反转以匹配标签的顺序
    }

    return JsonResponse(response_data)
