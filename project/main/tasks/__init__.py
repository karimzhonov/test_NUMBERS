from celery import Celery
from celery.schedules import schedule
from .update_database import update_database


def setup(app: Celery):
    app.add_periodic_task(schedule(5), app.task(update_database).s(), name='Update Database')
