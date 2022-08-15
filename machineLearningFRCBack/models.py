from machineLearningFRCBack import db
from datetime import datetime

class Match(db.Model):
    match_key  = db.Column(db.String, primary_key=True)
    red_team_1 = db.Column(db.String)
    red_team_2 = db.Column(db.String)
    red_team_3 = db.Column(db.String)
    red_hang_1 = db.Column(db.Integer)
    red_hang_2 = db.Column(db.Integer)
    red_hang_3 = db.Column(db.Integer)
    red_taxi_1 = db.Column(db.Integer)
    red_taxi_2 = db.Column(db.Integer)
    red_taxi_3 = db.Column(db.Integer)
    red_auto_cargo_lower = db.Column(db.Integer)
    red_auto_cargo_upper = db.Column(db.Integer)
    red_auto_cargo_points = db.Column(db.Integer)
    red_teleop_cargo_lower = db.Column(db.Integer)
    red_teleop_cargo_upper = db.Column(db.Integer)
    red_teleop_cargo_points  = db.Column(db.Integer)
    red_foul_count  = db.Column(db.Integer)
    red_foul_points  = db.Column(db.Integer)
    red_total_score = db.Column(db.Integer)
    blue_team_1 = db.Column(db.String)
    blue_team_2 = db.Column(db.String)
    blue_team_3 = db.Column(db.String)
    blue_hang_1 = db.Column(db.Integer)
    blue_hang_2 = db.Column(db.Integer)
    blue_hang_3 = db.Column(db.Integer)
    blue_taxi_1 = db.Column(db.Integer)
    blue_taxi_2 = db.Column(db.Integer)
    blue_taxi_3 = db.Column(db.Integer)
    blue_auto_cargo_lower = db.Column(db.Integer)
    blue_auto_cargo_upper = db.Column(db.Integer)
    blue_auto_cargo_points = db.Column(db.Integer)
    blue_teleop_cargo_lower = db.Column(db.Integer)
    blue_teleop_cargo_upper = db.Column(db.Integer)
    blue_teleop_cargo_points  = db.Column(db.Integer)
    blue_foul_count  = db.Column(db.Integer)
    blue_foul_points  = db.Column(db.Integer)
    blue_total_score = db.Column(db.Integer)
    event_key = db.Column(db.String)
    event_week = db.Column(db.Integer)
    winning_alliance = db.Column(db.Integer)

    def __repr__(self):
        return f'Match({self.match_key})'

class MatchExpanded(db.Model):
    """
    Class that has all of the match data from the perpective of each team. 6x larger than Match
    """
    index = db.Column(db.Integer, primary_key=True)
    match_key  = db.Column(db.String)
    team_1 = db.Column(db.String)
    team_2 = db.Column(db.String)
    team_3 = db.Column(db.String)
    hang_1 = db.Column(db.Integer)
    hang_2 = db.Column(db.Integer)
    hang_3 = db.Column(db.Integer)
    taxi_1 = db.Column(db.Integer)
    taxi_2 = db.Column(db.Integer)
    taxi_3 = db.Column(db.Integer)
    auto_cargo_lower = db.Column(db.Integer)
    auto_cargo_upper = db.Column(db.Integer)
    auto_cargo_points = db.Column(db.Integer)
    teleop_cargo_lower = db.Column(db.Integer)
    teleop_cargo_upper = db.Column(db.Integer)
    teleop_cargo_points  = db.Column(db.Integer)
    foul_count  = db.Column(db.Integer)
    foul_points  = db.Column(db.Integer)
    total_score = db.Column(db.Integer)

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



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    auth_key = db.Column(db.String)
    is_admin = db.Column(db.Boolean)
    
    def __repr__(self):
        return f'User {self.username}, {self.email}, {self.image_file}'
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post({self.title}, {self.date_posted})"
