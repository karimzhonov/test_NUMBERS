import time
import schedule

from project.logger import logger
from .update_database import update_database
from .send_message_about_expiration_date import send_message_about_expiration_date

schedule.every(5).seconds.do(update_database)
schedule.every().day.at("09:00").do(send_message_about_expiration_date)


def start():
    logger.info('Manager tasks started')
    while True:
        schedule.run_pending()
        time.sleep(1)
