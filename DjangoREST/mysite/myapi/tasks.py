import time

from celery import shared_task
from django.db.models import Sum, F
from django.db.models.functions import Length


@shared_task
def common_shared_task(var1: str, var2: str):
    time.sleep(3)
    print("Hello from celery shared_task", var1, var2)
    return f"shared_task {var1}, {var2}".upper()

