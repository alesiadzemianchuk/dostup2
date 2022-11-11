import logging
from time import sleep
from dostup2.celery import app


@app.task
def send_message(employee: str):
    sleep(5)
    email = 'alesik1410@yandex.ru'
    logging.info(f'email to {email}  for {employee} send successfully')


@app.task
def schedule_task():
    logging.info('SCHEDULE TASK')