import os

from django.conf import settings

from celery import Celery

# Установите модуль настроек Django по умолчанию для программы "celery".
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Использование строки здесь означает, что рабочему элементу не нужно выполнять сериализацию
# объекта конфигурации для дочерних процессов.
# - namespace="CELERY" означает, что все ключи конфигурации, связанные с celery
# должны иметь префикс `CELERY_`.
app.config_from_object(f'django.conf:settings', namespace='CELERY')

# Загружайте модули задач из всех зарегистрированных приложений Django.
app.autodiscover_tasks()