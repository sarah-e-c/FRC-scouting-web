from machineLearningFRCBack import app
from machineLearningFRCBack import models
from machineLearningFRCBack import db
import pandas as pd

@app.route('/')
@app.route('/home')
def home():
    return '<h1>WRONG PAGE</h1>'

@app.route('/admin')
def start_build_page():
    pass

@app.route('/upload', methods=['GET', 'POST'])
def upload_data_page():
    pass

@app.route('/get_match_data')
def give_match_data():
    #df = pd.read_sql(models.Match.query.all())
    #return df.to_json()
    return models.Match.query.all()
    