from machineLearningFRCBack import db
from datetime import datetime

# class Match(db.Model):
#     match_key  = db.Column(db.String, primary_key=True)
#     red_team_1 = db.Column(db.String)
#     red_team_2 = db.Column(db.String)
#     red_team_3 = db.Column(db.String)
#     red_hang_1 = db.Column(db.Integer)
#     red_hang_2 = db.Column(db.Integer)
#     red_hang_3 = db.Column(db.Integer)
#     red_taxi_1 = db.Column(db.Integer)
#     red_taxi_2 = db.Column(db.Integer)
#     red_taxi_3 = db.Column(db.Integer)
#     red_auto_cargo_lower = db.Column(db.Integer)
#     red_auto_cargo_upper = db.Column(db.Integer)
#     red_auto_cargo_points = db.Column(db.Integer)
#     red_teleop_cargo_lower = db.Column(db.Integer)
#     red_teleop_cargo_upper = db.Column(db.Integer)
#     red_teleop_cargo_points  = db.Column(db.Integer)
#     red_foul_count  = db.Column(db.Integer)
#     red_foul_points  = db.Column(db.Integer)
#     red_total_score = db.Column(db.Integer)
#     blue_team_1 = db.Column(db.String)
#     blue_team_2 = db.Column(db.String)
#     blue_team_3 = db.Column(db.String)
#     blue_hang_1 = db.Column(db.Integer)
#     blue_hang_2 = db.Column(db.Integer)
#     blue_hang_3 = db.Column(db.Integer)
#     blue_taxi_1 = db.Column(db.Integer)
#     blue_taxi_2 = db.Column(db.Integer)
#     blue_taxi_3 = db.Column(db.Integer)
#     blue_auto_cargo_lower = db.Column(db.Integer)
#     blue_auto_cargo_upper = db.Column(db.Integer)
#     blue_auto_cargo_points = db.Column(db.Integer)
#     blue_teleop_cargo_lower = db.Column(db.Integer)
#     blue_teleop_cargo_upper = db.Column(db.Integer)
#     blue_teleop_cargo_points  = db.Column(db.Integer)
#     blue_foul_count  = db.Column(db.Integer)
#     blue_foul_points  = db.Column(db.Integer)
#     blue_total_score = db.Column(db.Integer)
#     event_key = db.Column(db.String)
#     event_week = db.Column(db.Integer)
#     winning_alliance = db.Column(db.Integer)

#     def __repr__(self):
#         return f'Match({self.match_key})'

class MatchExpandedTBA(db.Model):
    """
    Class that has all of the match data from the perpective of each team. 6x larger than Match
    """

    __tablename__ = 'match_expanded_tba'
    index = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String)
    comp_level = db.Column(db.String)
    event_key = db.Column(db.String)
    key  = db.Column(db.String)
    match_number = db.Column(db.Integer)
    set_number = db.Column(db.Integer)
    winning_alliance = db.Column(db.String)
    team_alliance = db.Column(db.String)
    teammate_1 = db.Column(db.String)
    teammate_2 = db.Column(db.String)
    teammate_3 = db.Column(db.String)
    opponent_1 = db.Column(db.String)
    opponent_2 = db.Column(db.String)
    opponent_3 = db.Column(db.String)
    taxied = db.Column(db.Integer)
    hang = db.Column(db.Integer)
    alliance_auto_cargo_lower = db.Column(db.Integer)
    alliance_auto_cargo_upper = db.Column(db.Integer)
    alliance_teleop__cargo_lower = db.Column(db.Integer)
    alliance_teleop__cargo_upper = db.Column(db.Integer)
    # team_auto_cargo_lower = db.Column(db.Integer, nullable=True)
    # team_auto_cargo_upper = db.Column(db.Integer, nullable=True)
    # team_teleop_cargo_lower = db.Column(db.Integer, nullable=True)
    # team_teleop_cargo_upper = db.Column(db.Integer, nullable=True)
    won_game = db.Column(db.Integer)
    week = db.Column(db.Integer)

class MatchExtraData(db.Model):
    __tablename__ = 'match_extra_data'
    index = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String)
    match_number = db.Column(db.Integer)
    team_auto_lower = db.Column(db.Integer)
    team_auto_upper = db.Column(db.Integer)
    team_teleop_lower = db.Column(db.Integer)
    team_teleop_upper = db.Column(db.Integer)


# class MatchStats(db.Model):
#     """
#     Table that uses the training data.
#     """
    
#     pass



# class TeamStatistics(db.Model):
#     """
#     Class that stores team statistics per
#     """
#     pass

# class TeamGeneral(db.Model):
#     """
#     Class that stores general information about teams. Currently unused.
#     """
#     pass

# class Event(db.Model):
#     """
#     Class that stores information about events. Used to query data from specific events.
#     """
#     pass
