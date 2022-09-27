#data_setup.create_event_table(machineLearningFRCBack.session)
import logging
import psycopg2
logger = logging.getLogger(__name__)

# run this if setting up for first time. commented out for protection

def first_time_setup():
    conn = psycopg2.connect(
        database='postgres',
        user='postgres',
        password='password',
        host='localhost',
        port= '5432'
    )
    conn.autocommit = True
    sql_1 = """DROP DATABASE IF EXISTS ml_frc_api"""
    sql_2 = """CREATE DATABASE ml_frc_api"""
    cursor = conn.cursor()
    cursor.execute(sql_1)
    logger.info('database deleted if existed.')
    cursor.execute(sql_2)
    logger.info('database created successfully!')
    conn.close()

    from machineLearningFRCBack import engine, db
    from machineLearningFRCBack import models
    from machineLearningFRCBack.logic import data_setup
    # i know that this is cursed
    
    db.create_all() # creating tables
    data_setup.fill_event_table(db.session)
    logger.debug('event data gotten')
    data_setup.get_match_dictionary_data(db.session)
    logger.debug('match dictionary data gotten')
    data_setup.get_api_data(engine=engine, event_keys='all')
    logger.debug('api data gotten')

    v1_tba = models.MatchExpandedTBAVersion(version_num=0,
    major_change=0)
    v1_dict = models.MatchDictionaryVersion(version_num=0,
    major_change=0)
    v1_user_data = models.MatchExtraDataVersion(version_num=0,
    major_change=0)
    v1_events_data = models.EventVersion(version_num = 0, major_change = 0)
    db.session.add(v1_tba)
    db.session.add(v1_dict)
    db.session.add(v1_user_data)
    db.session.add(v1_events_data)
    db.session.commit()
    logger.debug('all done!')

if __name__ == '__main__':
    first_time_setup()