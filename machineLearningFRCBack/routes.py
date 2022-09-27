from asyncore import file_dispatcher
from flask import Flask, render_template, request, jsonify
from machineLearningFRCBack import app
from machineLearningFRCBack import models
from machineLearningFRCBack import db
from machineLearningFRCBack import engine, session
from machineLearningFRCBack.logic.upload_data import handle_data
from machineLearningFRCBack.logic import data_setup
import pandas as pd
import logging
from io import StringIO

latest_version = '0.001'

logger = logging.getLogger(__name__)
def verify_key(key):
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

@app.route('/upload', methods=['GET', 'POST'])
def upload_data_page():
    key_verified = verify_key(request.headers['auth_key'])
    if request.method == 'POST':
        if key_verified:
            f = request.files['extra_data_file']
            logger.debug(f)
            df = pd.read_csv(f)
            success = handle_data(df)
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
    response = Flask.make_response(app, jsonify(list1))
    response.headers['VersionTBAData'] = models.MatchExpandedTBAVersion.query.order_by(models.MatchExpandedTBAVersion.version_num.desc()).first().version_num
    return response

@app.route('/get_user_expanded_match_data')
def give_user_expanded_data():
    def as_dict(model): # probably can make this better with postgres
       return {c.name: getattr(model, c.name) for c in model.__table__.columns}

    list_ = models.MatchExtraData.query.all()
    list1 = []
    for item in list_:
        list1.append(as_dict(item))
    return_val = jsonify(list1)
    response = Flask.make_response(app, return_val)
    response.headers['VersionUserSubmittedData'] = models.MatchExtraDataVersion.query.order_by(models.MatchExtraDataVersion.version_num.desc()).first().version_num
    return response

@app.route('/get_match_dictionary_data')
def give_match_dictionary_data():
    def as_dict(model): # probably can make this better with postgres
       return {c.name: getattr(model, c.name) for c in model.__table__.columns}

    list_ = models.MatchDictionary.query.all()
    list1 = []
    for item in list_:
        list1.append(as_dict(item))
    response = Flask.make_response(app, jsonify(list1))
    response.headers['VersionDictionaryData'] = models.MatchDictionaryVersion.query.order_by(models.MatchDictionaryVersion.version_num.desc()).first().version_num
    return response

@app.route('/get_events_data')
def give_events_data():
    def as_dict(model): # probably can make this better with postgres
       return {c.name: getattr(model, c.name) for c in model.__table__.columns}

    list_ = models.Event.query.all()
    list1 = []
    for item in list_:
        list1.append(as_dict(item))
    response = Flask.make_response(app, jsonify(list1))
    # selecting the last added version number
    response.headers['VersionEvents'] = models.EventVersion.query.order_by(models.EventVersion.version_num.desc()).first().version_num
    return response

@app.route('/ping')
def give_ping():
    response = app.make_response(rv='recieved')
    if request.headers['CurrentVersion'] != latest_version:
        response.headers['NewVersion'] = 'True'
    else:
        response.headers['NewVersion'] = 'False'

    # checking if there is a new version of TBA data
    new_version_tba_data = models.MatchExpandedTBAVersion.query.last().version_num
    if request.headers['VersionTBAData'] != new_version_tba_data:
        response.headers['NewTBAData'] = 'True'
    else:
        response.headers['NewTBAData'] = 'False' 
    
    # checking if there is a new version of dictionary data
    if request.headers['VersionDictionaryData'] != models.MatchDictionaryVersion.query.last().version_num:
        response.headers['NewDictionaryData'] = 'True'
    else:
        response.headers['NewDictionaryData'] == 'False'
    # checking if there is a new version of user submitted data
    if request.headers['VersionUserSubmittedData'] != models.MatchExtraDataVersion.query.last().version_num:
        response.headers['NewUserSubmittedData'] = 'True'
    else:
        response.headers['NewUserSubmittedData'] = 'False'
    if request.headers['VersionEvents'] != models.EventVersion().query.last().version_num:
        response.headers['NewEventsData'] = 'True'
    else:
        response.headers['NewEventsData'] = 'False'
    return response

@app.route('/submit_bug', methods=['POST'])
def submit_bug():
    new_bug = models.Bug(
        parent_user = request['User'],
        is_resolved = 0,
        content=request['BugText']
    )
    session.add(new_bug)
    session.commit()
    logger.info('bug sumbitted')
    return 'bug submitted'

    
