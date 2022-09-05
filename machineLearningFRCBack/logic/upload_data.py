from machineLearningFRCBack import db, session
import machineLearningFRCBack.models as models
import pandas as pd
import logging

logger = logging.getLogger(__name__)
# handle data
def handle_data(data: pd.DataFrame):
    logger.debug('Recieved upload request')

    def find_index(row):
        return models.MatchExpandedTBA.query.filter_by(team_name=row['team_key']).first().index

    for row in data.iterrows():
        session.add(models.MatchExtraData(
            index= find_index(row),
            team_name = row['team_name'],
            match_number = row['match_number'],
            team_auto_lower = row['team_auto_lower'],
            team_auto_upper = row['team_auto_upper'],
            team_teleop_lower = row['team_teleop_lower'],
            team_teleop_upper  = row['team_teleop_upper']))
    session.commit()
    logger.debug('upload successful')

