# Choose your own adventure game

# make cards
# cards have
# description, options, (events?), item conditional options

# options connect to other cards, trigger events

# are events just end cards / more description?

# player has inventory

from Player import Player
import json


# Load player
player = Player()

# Load rooms of game as an array
f = open('game.json', "r")
rooms = json.loads(f.read())['rooms']

# cool, can access the room data.
# now to make the actual game

# we have an array of room dicts,
## make this load as a list of class objects?
# each room dict can have an array of option dicts,
# each option has a key "goto" that gives the array
# index of the next room to go to after picking that option.

# options can have an "available" key that should be checked before displaying that option. 
# (null = no requirement, "item" = need that item, "!item" = won't show up if you have item.) 

# when an option is selected, 
# the "result" text should be displayed, 
# any mods should be made to player inventory,
## added a new fields to options or result to indicated if an item gets used or gained,
# the player should be moved to the next room index specified by "goto".

# when a room is accessed, 
# the "description" text should be displayed.
# if there are options, they should be listed and the player propted for a choice.
# if the "options" array is empty, this is an ending room 
# and the game should terminate or ask if player wants to play again.

# Start Game

# Find ends
ends = []
for room in rooms:
  if len(room["options"]) == 0:
    ends.append(room['id'])


# Establish start point
current_room = rooms[0]

# Game loop
while(current_room['id'] not in ends):
  # Describe room
  print('\n' + current_room['description'] + '\n')

  # list player inventory
  print('Current Inventory:')
  player.seeInventory()

  # Give options
  index = 0  # used to track option index during iterration
  valid = []  # used to keep track of valid option indices (limits valid user input)
  for option in current_room['options']:
    # increment index value for display
    index += 1
    # check available before showing option
    if option['available']:
      # absence check (prevents going back to events already done)
      if option['available'][0] == '!':
        if player.inventory[option['available'][1:]] == False:
          print(str(index) + ') ' + option['text'])
          valid.append(index)
        else:
          continue
      # presence check (option requires item)
      elif player.inventory[option['available']] == True:
        print(str(index) + ') ' + option['text'])
        valid.append(index)
      else:
        continue
    # no requirements for this option
    else:
      print(str(index) + ') ' + option['text'])
      valid.append(index)
  # Player selects from options
  selection = 0  # store user selection
  # input validation loop
  while(True):
    selection = str(input("\nWhat do you do? (enter number) "))
    if (not selection.isdigit()) or (int(selection) not in valid):
      print("\nPlease enter a number from '" + str(valid[0]) +"' to '" + str(valid[-1]) + "'")
    else:
      break

  selection = current_room['options'][int(selection) - 1]
  # show result
  if selection['result']:  # some options are straight forward, don't need a result.
    print('\n' + selection['result'] + '\n')
  # make inventory modifications
  if selection["gain"]:
    player.addItem(selection["gain"])
  if selection["lose"]:
    player.useItem(selection["lose"])
  # move to next room
  current_room = rooms[selection['goto']]


# Describe end
print('\n' + current_room['description'])


# Close the game file
f.close()