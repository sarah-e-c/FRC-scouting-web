# method to start the build...
import threading
import logging
import machineLearningFRCBack.logic.data_setup as data_setup
import machineLearningFRCBack.logic.match_selector as selector
import machineLearningFRCBack.logic.sql_testing as sql_testing
import requests
import time
import pandas as pd
from celery import Celery
from machineLearningFRCBack.logic.utils import Constants
import machineLearningFRCBack

current_etag = None
HEADER = {'X-TBA-Auth-Key': Constants.KEY}
YEAR = 2022
kill_build = False

# def make_celery(app):
#     celery = Celery(
#         app.import_name,
#         backend=app.config['CELERY_RESULT_BACKEND'],
#         broker=app.config['CELERY_BROKER_URL']
#     )
#     celery.conf.update(app.config)

#     class ContextTask(celery.Task):
#         def __call__(self, *args, **kwargs):
#             with app.app_context():
#                 return self.run(*args, **kwargs)

#     celery.Task = ContextTask
#     return celery


# celery = make_celery(machineLearningFRCBack.app)

def update_match_data():
    source = requests.get(f'https://www.thebluealliance.com/api/v3/events/{YEAR}/keys', HEADER)
    current_etag = source.headers['Etag']
    HEADER['If-None-Match'] = current_etag
    data_setup.get_api_data()

    print(source.headers)


def build():
    pass

if __name__ == '__main__':
    update_match_data()