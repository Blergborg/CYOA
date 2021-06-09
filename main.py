from Player import Player
from Room import Room
import json
import os

# Object-Oriented Main

# Choose a game from the games folder
## get list of files
games = (os.listdir('games'))

print('\n=== Welcome to Choose Your Own Adventure ===\n')
## get a valid pick
while(True):
  ## display list
  print('\nHere are the games we found:')
  for game in games:
    print(game[:-5])
  ## prompt user input
  game_pick = str(input("\nEnter the name of the game you want to play: "))
  ## clean & validate input
  if len(game_pick) < 5:
    game_pick = game_pick + '.json'
  if game_pick[-5:] != ".json":
    game_pick = game_pick + '.json'
  if game_pick not in games:
    print('Please pick one of the listed games.')
  else:
    break

## format path to game and open file
game_pick = 'games/' + game_pick
with open(f'{game_pick}', "r") as data:
  ## parse file & load as dict
  allData = json.loads(data.read())
  ## separate into player_data and game_data
  player_data = allData['player']
  game_data = allData['rooms']


# Load player inventory
player = Player(player_data)
# Load rooms of game as an array of room objects
rooms = []
for room in game_data:
  rooms.append(Room(room['id'], room['description'], room['options']))

# set start point
current_room = rooms[0]

# Show title
if (allData['title']):
  print('\n' + allData['title'])

# game loop
while(True):
  current_room.describe(player)
  choice = current_room.choose(player)
  current_room = rooms[choice]
  
  # check if end has been reached
  if len(current_room.options) == 0:
    break

# describe the end
current_room.describe(player)