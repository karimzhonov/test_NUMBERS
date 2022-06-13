from django.core.management.base import BaseCommand
from main import tasks


class Command(BaseCommand):
    def handle(self, *args, **options):
        tasks.start()
