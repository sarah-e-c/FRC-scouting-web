import sqlite3
import logging
import pandas as pd
import machineLearningFRCBack.logic.match_selector as selector
from machineLearningFRCBack.logic.utils import Constants
from machineLearningFRCBack import db
import requests
import time
HEADER = {'X-TBA-Auth-Key': Constants.KEY}
import numpy as np
YEAR = 2022
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
# first method
def get_api_data(conn: sqlite3.Connection, data_loaded=False, verbose=True, event_keys='default', match_data_filepath='all_matches_uncleaned.json'):
    """
    Method to grab all of the data needed for the program from the Blue Alliance api.
    data_loaded -- signify if data is loaded already. (mostly for testing, usually you wouldn't have to run this method at all)
    verbose -- signify if print statements/logs are wanted
    event_keys -- pass 'default' for default list of events, pass 'all' for all good events for year, or pass in custom list of event keys
    match_data_filepath -- filepath where the wanted matches will be saved in a json
    """
    if verbose:
        logger.debug('getting data from api...')
    def get_score_data(df, team_name):

        taxied_list = []
        endgames_list = []

        auto_lower_points_list = []
        auto_upper_points_list = []
        tele_lower_points_list = []
        tele_upper_points_list = []

        total_team_points_list = []
        won_game_list = []
        week_list = []


        # iterating through all:
        for i in range(df.shape[0]):
            team_alliance = df.iloc[i]['team_alliance']
            try:
                data_list = df.iloc[i]['score_breakdown'][team_alliance]
                # which robot were they ?
                if df.iloc[i]['Teammate1'] == team_name:
                    taxied_list.append(data_list['taxiRobot1'])
                    endgames_list.append(data_list['endgameRobot1'])
                if df.iloc[i]['Teammate2'] == team_name:
                    taxied_list.append(data_list['taxiRobot2'])
                    endgames_list.append(data_list['endgameRobot2'])
                if df.iloc[i]['Teammate3'] == team_name:
                    taxied_list.append(data_list['taxiRobot3'])
                    endgames_list.append(data_list['endgameRobot3'])
            except:
                taxied_list.append(None)
                endgames_list.append(None)
            
            try:
                # auto lower
                total_auto_lower_points = (data_list['autoCargoLowerBlue'] +  data_list['autoCargoLowerFar']
                                            + data_list['autoCargoLowerNear'] + data_list['autoCargoLowerRed'])
                auto_lower_points_list.append(total_auto_lower_points)
            except:
                auto_lower_points_list.append(None)
            
            try:
                # auto upper
                total_auto_upper_points = (data_list['autoCargoUpperBlue'] +  data_list['autoCargoUpperFar']
                                            + data_list['autoCargoUpperNear'] + data_list['autoCargoUpperRed'])
                auto_upper_points_list.append(total_auto_upper_points)
            
            except:
                auto_upper_points_list.append(None)
            
            try:
                # teleop lower
                total_teleop_lower_points = (data_list['teleopCargoLowerBlue'] +  data_list['teleopCargoLowerFar']
                                            + data_list['teleopCargoLowerNear'] + data_list['teleopCargoLowerRed'])    
                tele_lower_points_list.append(total_teleop_lower_points)
            
            except:
                tele_lower_points_list.append(None)
            
            try:
                # teleop upper
                total_teleop_upper_points = (data_list['teleopCargoUpperBlue'] +  data_list['teleopCargoUpperFar']
                                            + data_list['teleopCargoUpperNear'] + data_list['teleopCargoUpperRed'])    
                tele_upper_points_list.append(total_teleop_upper_points)
            
            except:
                tele_upper_points_list.append(None)
            
            # won game ?
            total_team_points_list.append(data_list['totalPoints'])
            if df.iloc[i]['team_alliance'] == df.iloc[i]['winning_alliance']:
                won_game_list.append('Yes')
            elif df.iloc[i]['winning_alliance'] == '': # checking if its nan
                won_game_list.append('Tie')
            else:
                won_game_list.append('No')
            
        # week
        week_list = [-1] * len(taxied_list)
        for i in range(5):
            current_week_indexes = selector.select_by_event_week([i], df)
            for index in current_week_indexes:
                week_list[index] = i
        


        return pd.DataFrame({'taxied': taxied_list,
                            'hang': endgames_list,
                            'alliance_auto_cargo_lower': auto_lower_points_list,
                            'alliance_auto_cargo_upper': auto_upper_points_list,
                            'alliance_teleop__cargo_lower': tele_lower_points_list,
                            'alliance_teleop__cargo_upper': tele_upper_points_list,
                            'alliance_total_points': total_team_points_list,
                            'won_game': won_game_list,
                            'week': week_list
        }) 


    def get_team(df, team_name):
        team_list = []
        for i in range(df.shape[0]):
            #team_split_string = df.iloc[i]['alliances'].split('red')
            try:
                if team_name in df.iloc[i]['alliances']['blue']['team_keys']:
                    team_list.append('blue')
                elif team_name in df.iloc[i]['alliances']['red']['team_keys']:
                    team_list.append('red')
                
            except:
                team_list.append('red')
        return pd.Series(team_list, name='team_alliance')


    # returns dataframe of opponents and teammates
    def get_opponents(df):
        teammate_1_list = []
        teammate_2_list = []
        teammate_3_list = []

        opponent_1_list = []
        opponent_2_list = []
        opponent_3_list = []

        for i in range(df.shape[0]):
            if df.iloc[i]['team_alliance'] == 'red':
                teammate_list = df.iloc[i]['alliances']['red']['team_keys']
                teammate_1_list.append(teammate_list[0])
                teammate_2_list.append(teammate_list[1])
                teammate_3_list.append(teammate_list[2])
                opponent_list = df.iloc[i]['alliances']['blue']['team_keys']
                opponent_1_list.append(opponent_list[0])
                opponent_2_list.append(opponent_list[1])
                opponent_3_list.append(opponent_list[2])
            else:
                teammate_list = df.iloc[i]['alliances']['blue']['team_keys']
                teammate_1_list.append(teammate_list[0])
                teammate_2_list.append(teammate_list[1])
                teammate_3_list.append(teammate_list[2])
                opponent_list = df.iloc[i]['alliances']['red']['team_keys']
                opponent_1_list.append(opponent_list[0])
                opponent_2_list.append(opponent_list[1])
                opponent_3_list.append(opponent_list[2])
        
        return pd.DataFrame({'teammate_1': teammate_1_list,
                            'teammate_2': teammate_2_list, 
                            'teammate_3': teammate_3_list,
                            'opponent_1': opponent_1_list,
                            'opponent_2': opponent_2_list,
                            'opponent_3': opponent_3_list
                            })
    
    
    def load_data(good_event_list, data_preloaded=True):
        all_matches = []
        all_teams = [] # getting all teams
        all_teams_matches = []

        # if the data is not already loaded into file, get data
        if not data_preloaded:
            for event in good_event_list:
                event_matches = pd.read_json(requests.get(f'https://www.thebluealliance.com/api/v3//event/{event}/matches', HEADER).text)
                all_matches.append(event_matches)
                time.sleep(0.2) # being nice
            
            # writing this to a csv so less requests
            all_matches = pd.concat(all_matches).reset_index()

            all_matches.to_json(match_data_filepath)

        all_matches = pd.read_json(match_data_filepath)
        all_matches = all_matches.loc[all_matches['event_key'].apply(lambda x: x in good_event_list)]


        # print('written to csv!!!')
        for match in all_matches['alliances']:

            # getting a list of teams
            all_teams.append(match['red']['team_keys'][0])
            all_teams.append(match['red']['team_keys'][1])
            all_teams.append(match['red']['team_keys'][2])
            all_teams.append(match['blue']['team_keys'][0])
            all_teams.append(match['blue']['team_keys'][1])
            all_teams.append(match['blue']['team_keys'][2])
            
        # getting rid of duplicates
        all_teams = np.unique(all_teams)

        # mapper to extract team keys out
        def map_team_keys(dict):
            team_names = []
            team_names.append(dict['red']['team_keys'][0])
            team_names.append(dict['red']['team_keys'][1])
            team_names.append(dict['red']['team_keys'][2])
            team_names.append(dict['blue']['team_keys'][0])
            team_names.append(dict['blue']['team_keys'][1])
            team_names.append(dict['blue']['team_keys'][2])
            return team_names

        all_matches['team_keys'] = all_matches['alliances'].map(map_team_keys)

        def clean_data(df, team_name):
            new_data = df.copy()
            new_data = new_data.join(get_team(df, team_name))
            new_data = new_data.join(get_opponents(new_data))
            new_data = new_data.join(get_score_data(new_data, team_name))
            new_data.drop(['actual_time', 'alliances', 'post_result_time', 'predicted_time', 'score_breakdown', 'videos', 'time'], axis=1, inplace=True)
            new_data.sort_values(by='match_number', inplace=True)
            new_data.reset_index(inplace=True)
            new_data.drop('index', axis=1, inplace=True)

            return new_data

        for index, team in enumerate(all_teams):
            all_teams_matches.append(all_matches.loc[all_matches['team_keys'].apply(lambda x: team in x)])
            all_teams_matches.append(clean_data(all_teams_matches[index].reset_index().drop('index', axis=1), team))
        return all_teams_matches

        # none_list = None * all_teams_matches.shape[0]
        # all_teams_matches['team_auto_cargo_lower'] = none_list
        # all_teams_matches['team_auto_cargo_upper'] = none_list
        # all_teams_matches['team_teleop_cargo_lower'] = none_list
        # all_teams_matches['team_teleop_cargo_upper'] = none_list
    def get_good_events(bad_events_filepath='bad_events.csv'):
        """
        method to separate the valid events from the invalid events. Assumes that bad events
        (unique not a requirement) are preloaded into a csv file.
        bad_events_filepath -- filepath where the bad events are loaded.
        **Future updates will have False as an option and will generate the bad events.
        """
        bad_events = pd.read_csv(bad_events_filepath)
        all_events = list(pd.read_json(requests.get(f'https://www.thebluealliance.com/api/v3/events/{YEAR}/keys', HEADER).text)[0])
        bad_events_actual = np.unique(list(bad_events['BadEvents']))
        for event in bad_events_actual:
            all_events.remove(event)
        return all_events

    if event_keys =='all':
        fin_df = load_data(get_good_events(), data_preloaded=data_loaded)
    elif event_keys == 'default':
        default_events = [
        "2022va305",
        '2022va306',
        '2022va319',
        "2022va320",
        '2022dc305',
        '2022dc306',
        '2022dc312',
        '2022dc313',
        '2022dc326'
        ]
        fin_df = load_data(default_events, data_preloaded=data_loaded)
    else:
        try:
            fin_df = load_data(event_keys, data_preloaded=data_loaded)
        except:
            pass
    fin_df = pd.concat(fin_df)
    fin_df.to_sql('match_expanded_tba', conn, if_exists='replace')

def process_expanded_match_data():
    source = requests.get(f'https://www.thebluealliance.com/api/v3/events/{YEAR}/keys', HEADER)
    current_etag = source.headers['ETag']
    HEADER['If-None-Match'] = current_etag
    get_api_data(db.make_connector())
    print('all done!')

def process_event_data():
    pass