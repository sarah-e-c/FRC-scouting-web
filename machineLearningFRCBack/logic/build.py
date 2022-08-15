# method to start the build...
import threading
import logging
import data_setup
import match_selector
import sql_testing
import requests
import time
import pandas as pd
from celery import Celery
from utils import Constants
import machineLearningFRCBack

HEADER = {'X-TBA-Auth-Key': Constants.KEY}
YEAR = 2022
kill_build = False

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


celery = make_celery(machineLearningFRCBack.app)

@celery.task()
def thread_short_term():
    while True:
        all_events = list(pd.read_json(requests.get(f'https://www.thebluealliance.com/api/v3/events/{YEAR}/keys', HEADER).text)[0])
        time.sleep(1)
        if kill_build:
            break


def build():
    pass