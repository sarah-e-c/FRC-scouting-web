from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
import logging
from machineLearningFRCBack.logic.utils import Constants
import os
from flask_migrate import Migrate

logger = logging.getLogger(__name__)

YEAR = 2022
HEADER = {'X-TBA-Auth-Key': Constants.KEY}
import pandas as pd



app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/sarahcrowder/Desktop/codingStuff/machineLearningFRCWeb/data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1148@localhost:5432/ml_frc_api"
app.config['CELERY_BROKER_URL'] = 'amqp:///localhost//'
app.config['CELERY_BACKEND'] = 'db+sqlite:///data.db'

db = SQLAlchemy(app)
engine = db.engine.execution_options(isolation_level='AUTOCOMMIT')


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



db.init_app(app)
migrate = Migrate(app, db)

engine = db.get_engine()
session = db.session


import machineLearningFRCBack.logic.build
import machineLearningFRCBack.logic.data_setup
import machineLearningFRCBack.logic.match_selector
import machineLearningFRCBack.logic.sql_testing
import machineLearningFRCBack.logic.utils


from machineLearningFRCBack import routes
from machineLearningFRCBack import models

