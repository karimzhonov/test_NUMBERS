import django

django.setup()

from celery import Celery
from main import tasks

app = Celery('test_NUMBERS', namespace='CELERY')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.timezone = 'UTC'


@app.on_after_configure.connect
def setup(sender, **kwargs):
    tasks.setup(sender)


@app.task
def update_database():
    from main.tasks.update_database import update_database
    from main.requests.sheet import get_sheet
    update_database(get_sheet())


app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'project.celery.update_database',
        'schedule': 10.0,
    },
}
