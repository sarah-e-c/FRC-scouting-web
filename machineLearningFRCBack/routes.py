from flask import Flask, render_template, request, jsonify
from machineLearningFRCBack import app
from machineLearningFRCBack import models
from machineLearningFRCBack import db
from machineLearningFRCBack import engine
from machineLearningFRCBack.logic.upload_data import handle_data
import pandas as pd
import logging
from io import StringIO

logger = logging.getLogger(__name__)
def verify_key():
    return True

def handle_files(f):
    pass

@app.route('/')
@app.route('/home')
def home():
    return '<h1>WRONG PAGE</h1>'

@app.route('/admin')
def start_build_page(methods=['GET', 'POST']):
    pass

@app.route('/upload', methods=['POST'])
def upload_data_page():
    #key_verify = verify_key(request.headers['auth_key'])
    if request.method == 'POST':
        if True:
            f = request.files['extra_data_file']
            logger.debug(f)
            success = handle_data(pd.read_csv(f))
            if success:
                return 'Uploaded successfully'
            else: 
                return 'Upload failed'
        else:
            return 'please use a valid key.'
        
        


@app.route('/get_match_data')
def give_match_data():
    def as_dict(model):
       return {c.name: getattr(model, c.name) for c in model.__table__.columns}
    list_ = models.MatchExpandedTBA.query.all()
    list1 = []
    for item in list_:
        list1.append(as_dict(item))
    return jsonify(list1)
    
