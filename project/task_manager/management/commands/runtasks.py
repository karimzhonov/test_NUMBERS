"""python manage.py runtasks - Run schedules"""
from django.core.management.base import BaseCommand
from task_manager import tasks


class Command(BaseCommand):
    def handle(self, *args, **options):
        tasks.start()
