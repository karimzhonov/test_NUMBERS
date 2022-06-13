import time
import schedule

from project.logger import logger
from .update_database import update_database

schedule.every(5).seconds.do(update_database)


def start():
    logger.info('Manager tasks started')
    while True:
        schedule.run_pending()
        time.sleep(0.1)
