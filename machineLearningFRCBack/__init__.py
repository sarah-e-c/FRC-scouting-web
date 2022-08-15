from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['CELERY_BROKER_URL'] = 'amqp:///localhost//'
app.config['CELERY_BACKEND'] = 'db+sqlite:///data.db'
db = SQLAlchemy(app)


from machineLearningFRCBack import routes
from machineLearningFRCBack import models

