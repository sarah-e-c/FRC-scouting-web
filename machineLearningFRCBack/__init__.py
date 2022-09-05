from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_sqlalchemy_session import flask_scoped_session



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/sarahcrowder/Desktop/codingStuff/machineLearningFRCWeb/data.db'
app.config['CELERY_BROKER_URL'] = 'amqp:///localhost//'
app.config['CELERY_BACKEND'] = 'db+sqlite:///data.db'
db = SQLAlchemy(app)
engine = db.create_engine('sqlite:////Users/sarahcrowder/Desktop/codingStuff/machineLearningFRCWeb/data.db', app.config['SQLALCHEMY_ENGINE_OPTIONS'])
print(db.engine)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:////Users/sarahcrowder/Desktop/codingStuff/machineLearningFRCWeb/data.db")
session_factory = sessionmaker(bind=engine)

session = flask_scoped_session(session_factory, app)



import machineLearningFRCBack.logic.build
import machineLearningFRCBack.logic.data_setup
import machineLearningFRCBack.logic.match_selector
import machineLearningFRCBack.logic.sql_testing
import machineLearningFRCBack.logic.utils


from machineLearningFRCBack import routes
from machineLearningFRCBack import models

