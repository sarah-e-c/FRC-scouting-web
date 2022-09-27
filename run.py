import machineLearningFRCBack.logic.data_setup as data_setup
import machineLearningFRCBack.logic.sql_testing as t
from machineLearningFRCBack import session, app
import logging
import pandas as pd
import requests
import threading


logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    #machineLearningFRCBack.process_data.process()
    # database = r"data.db"
    # connection = t.create_connection(database)
    # data_setup.get_api_data(connection, data_loaded=True, event_keys='all')


    #df = pd.read_csv('backup_to_sql_file.csv')
    #df.drop(['Unnamed: 0', 'Unnamed: 1', 'level_0', 'team_keys', 'winning_alliance', 'team_alliance', 'set_number'], axis=1, inplace=True)

    #df.to_sql('match_expanded_TBA', connection, if_exists='replace')
    # t.create_matches_data_table(connection)
    # t.fill_matches_data_table(connection)
    
    app.run(debug=True)
    
