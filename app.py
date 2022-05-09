from datetime import datetime
from sys import api_version
import berserk
import os

API_TOKEN = os.getenv("TOKEN")


session = berserk.TokenSession(API_TOKEN)
client = berserk.Client(session=session)

start = berserk.utils.to_millis(datetime(2017, 12, 8))
end = berserk.utils.to_millis(datetime(2022, 1, 9))
d = client.games.export_by_player('Mseserovich', since=start, until=end, max=300)
games = list(d)
# print(games[-1]['moves'].split(" "))
# # print(games[-2]['moves'])
# print([f"{index}.{i}" for index, i in enumerate(games[-2]['moves'].split(" "))])
# print(games[0])

username = []
for i in range(20):
    colour = 'white'
    player_id = games[i]['players'][colour]['user']['id']
    moves = games[i]['moves']
    game_id = games[i]['id']
    if player_id == 'mseserovich':     #pull data from lichess
        colour = 'black'
        player_id = games[i]['players'][colour]['user']['id']
    username.append(player_id)
    print(games[i]['id'])
    print(games[i]['moves'])
# game_id = games[0]['id']
# username
# rating
# date_pullled
# current_date