from flask import abort
from datetime import datetime
from .nba_data_source import data as NBA

# Utility Functions

def get_timestamp(date):
    """
    Convert a date (in string format) from MMDDYYYY to MM/DD/YYYY
    
    Args:
        date (string): a date in MMDDYYYY format
    
    Returns:
        string: a date in MM/DD/YYYY format
    """
    return datetime.strptime(str(date), '%m/%d/%Y').strftime('%m%d%Y')

# Team functions

def get_teams():
    """
    This function responds to a request for /nba/teams/<int:team_id> with the
    complete list of the full names of NBA teams

    Returns:
        list: a complete list of team names
    """
    return [NBA['Teams'][key]['full_name'] for key in sorted(NBA['Teams'].keys())]

def get_team(team_id):
    """
    This function responds to a request for /nba/teams with a single team based
    on the given team ID
    
    Args:
        int: an integer representing a team ID
    
    Returns:
        dict: a dictionary containing the data for a single team
    """
    if team_id in NBA['Teams']:
        team = NBA['Teams'].get(team_id)
    else:
        abort(404, "Team with team ID {team_id} not found".format(team_id=team_id))
    return team

# Player functions

def get_players():
    """
    This function responds to a request for /nba/players with the complete list
    of the full names of NBA players

    Returns:
        list: a complete list of names of NBA players
    """
    return [NBA['Players'][key]['name'] for key in sorted(NBA['Players'].keys())]

def get_players_on_date(date):
    """
    This function responds to a request for /nba/players with a dictionary of
    the NBA players who played on a given date.
    
    Args:
        string: a date in the format MMDDYYYY

    Returns:
        dict: a dictionary of NBA players who played on a date
    """
    try:
        players = []
        games_on_date = get_games_on_date(date)
        teams_played_on_date = set()
        for game in games_on_date:
            teams_played_on_date.add(games_on_date[game]['Game']['home_team_id'])
            teams_played_on_date.add(games_on_date[game]['Game']['away_team_id'])
        for player in NBA['Players']:
            if NBA['Players'][player]['team_id'] in teams_played_on_date:
                players.append(NBA['Players'][player])
        return players
    except:
        abort(404, "No players found on date. Please ensure date is in format MMDDYYY.")

def get_player(player_id):
    """
    This function responds to a request for /nba/players/<int:player_id> with a
    single player based on the given player ID
    
    Args:
        int: an integer representing a player ID
    
    Returns:
        dict: a dictionary containing the data for a single player
    """
    if player_id in NBA['Players']:
        player = NBA['Players'].get(player_id)
    else:
        abort(404, "Player with player ID {player_id} not found".format(player_id=player_id))
    return player

def get_player_stats(player_id):
    """
    This function responds to a request for /nba/players/<int:player_id>/stats
    with a list of stats from a single player based on the given player ID
    
    Args:
        int: an integer representing a player ID
    
    Returns:
        list: a list of dictionaries containing the stats for a single player
            for the games that player played in
    """
    if player_id in NBA['Players']:
        player_stats = []
        for stat in sorted(NBA['Player Stats']):
            if NBA['Player Stats'][stat]['player_id'] == player_id:
                player_stats.append(NBA['Player Stats'][stat])  
    else:
        abort(404, "Player with player ID {player_id} not found".format(player_id=player_id))
    return player_stats

# Game Functions
    
def get_games():
    """
    This function responds to a request for /nba/games with the complete list
    of NBA games

    Returns:
        list: a complete list of games (game and game state)
    """
    return [get_game(game_id) for game_id in NBA['Games'].keys()]

def get_games_on_date(date):
    """
    This function responds to a request for /nba/games with the complete list
    of NBA games played on a given date
    
    Args:
        string: a date in the format MMDDYYYY

    Returns:
        list: a complete list of games (game and game state)
    """
    games = {}
    for game_id in NBA['Games']:
        if get_timestamp(NBA['Games'][game_id]['date']) == str(date):
            games[game_id] = get_game(game_id)
    if games:
        return games
    else:
        return {'message': "No games found on given date. Please ensure date is in format MMDDYYY."}
    return games

def get_game(game_id):
    """
    This function responds to a request for /nba/games/<int: game_id> with the
    NBA game of a given game ID
    
    Args:
        int: an integer representing a game ID

    Returns:
        dict: a dictionary representing a game object (game and game state)
    """
    if game_id in NBA['Games']:
        game_data = {
            'Game': NBA['Games'][game_id],
            'State': NBA['Game States'][game_id]
            }
    else:
        abort(404, "Game with game ID {game_id} not found".format(game_id=game_id))
    return game_data