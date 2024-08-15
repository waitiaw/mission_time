from django.template.loader import get_template
from django.template import TemplateDoesNotExist
from django.conf import settings
from pathlib import Path
import django
import os

# Django 설정 모듈을 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websoket_time.settings')
django.setup()

def check_template_paths():
    # 템플릿 경로 확인
    template_dirs = settings.TEMPLATES[0]['DIRS']
    print(f"Template directories: {template_dirs}")

    # 템플릿 검색 경로 확인
    for directory in template_dirs:
        print(f"Checking directory: {directory}")
        if os.path.exists(directory):
            files = os.listdir(directory)
            print(f"Files in {directory}: {files}")
        else:
            print(f"Directory does not exist: {directory}")

    # 템플릿 로드 시도
    try:
        get_template('time.html')
        print("Template 'time.html' found and loaded successfully.")
    except TemplateDoesNotExist as e:
        print(f"Error: {e}")
    # 템플릿 디렉토리 경로 확인
    print(f"BASE_DIR: {settings.BASE_DIR}")
    print(f"Template directories: {settings.TEMPLATES[0]['DIRS']}")
    for directory in settings.TEMPLATES[0]['DIRS']:
        if not os.path.exists(directory):
            print(f"Directory does not exist: {directory}")
        else:
            print(f"Directory exists: {directory}")

check_template_paths()