from multiprocessing import cpu_count
from os import environ

bind = '0.0.0.0:' + environ.get('PORT', '8000')
max_requests = 1000
workers = cpu_count()

env = {
    'DJANGO_SETTINGS_MODULE': 'project.settings'
}

reload = True
name = 'test_NUMBERS'