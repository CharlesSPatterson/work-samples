from flask import Flask, request
from flask_restful import Resource, Api
from resources import nba

app = Flask(__name__)
api = Api(app)

# Team Resources

class GetTeams(Resource):
    def get(self):
        return nba.get_teams()
    
class GetTeam(Resource):
    def get(self, team_id):
        return nba.get_team(team_id)
    
api.add_resource(GetTeams, '/nba/teams')
api.add_resource(GetTeam, '/nba/teams/<int:team_id>')
    
# Player Resources
    
class GetPlayers(Resource):
    def get(self):
        date = request.args.get('date')
        if date == None:
            return nba.get_players()
        else:
            return nba.get_players_on_date(date)
    
class GetPlayer(Resource):
    def get(self, player_id):
        return nba.get_player(player_id)

class GetPlayerStats(Resource):
    def get(self, player_id):
        return nba.get_player_stats(player_id)

api.add_resource(GetPlayers, '/nba/players')
api.add_resource(GetPlayer, '/nba/players/<int:player_id>')
api.add_resource(GetPlayerStats, '/nba/players/<int:player_id>/stats')

# Game Resources
    
class GetGames(Resource):
    def get(self):
        date = request.args.get('date')
        if date == None:
            return nba.get_games()
        else:
            return nba.get_games_on_date(date)
    
class GetGame(Resource):
    def get(self, game_id):
        return nba.get_game(game_id)

api.add_resource(GetGames, '/nba/games')
api.add_resource(GetGame, '/nba/games/<int:game_id>')

if __name__ == '__main__':
    app.run(debug=True)