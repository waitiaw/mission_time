# timeapp/views.py

from django.shortcuts import render
from datetime import datetime

def current_time(request):
    now = datetime.now()  # 현재 시간 가져오기
    return render(request, 'time.html', {'current_time': now})  # 템플릿에 현재 시간 전달